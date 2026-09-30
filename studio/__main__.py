"""CLI do estúdio. Uso: python -m studio <comando> ...

Tudo aqui é determinístico e não gasta tokens: o Claude chama estes comandos e lê só o resumo.
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

import yaml

from .book import BOOKS, ROOT, Book, next_task, replan, set_status

ICON = {"pending": "·", "in_progress": "▶", "done": "✓", "blocked": "⛔", "skipped": "–"}


def _book(slug: str) -> Book:
    b = Book(slug)
    if not b.path("book.yaml").exists():
        sys.exit(f"Livro '{slug}' não existe em books/. Use: python -m studio new {slug} --type ...")
    return b


def cmd_new(a):
    b = Book(a.slug)
    if b.dir.exists():
        sys.exit(f"books/{a.slug} já existe.")
    shutil.copytree(ROOT / "templates" / "book", b.dir)
    meta = yaml.safe_load((b.dir / "book.yaml").read_text(encoding="utf-8"))
    meta.update(slug=a.slug, type=a.type, imprint=a.imprint or meta.get("imprint"), title=a.title or meta.get("title"))
    names = {"golden-chapter": "Golden Chapter Press", "silvia-press": "Silvia Press",
             "emily-harper": "Emily P. Harper", "jonah-feldman": "Jonah Feldman"}
    meta["imprint_name"] = names.get(meta["imprint"], meta.get("imprint_name"))
    b.save_meta(meta)
    replan(b)
    print(f"Criado books/{a.slug}/ — cole o TOC aprovado em books/{a.slug}/toc.md e rode /proximo {a.slug}")


def cmd_plan(a):
    st = replan(_book(a.slug))
    print(f"{len(st['tasks'])} tarefas planejadas.")
    cmd_status(a)


def cmd_status(a):
    b = _book(a.slug)
    tasks = b.load_state()["tasks"]
    done = sum(t["status"] in ("done", "skipped") for t in tasks)
    print(f"{b.meta.get('title', a.slug)} — {done}/{len(tasks)} etapas concluídas")
    for t in tasks:
        note = f"  ({t['note']})" if t.get("note") else ""
        print(f"  {ICON[t['status']]} {t['id']}{note}")
    nt = next_task(b)
    q = b.path("questions.md")
    open_q = sum(l.startswith("- [ ]") for l in q.read_text(encoding="utf-8").splitlines()) if q.exists() else 0
    print(f"Próxima: {nt['id'] if nt else '— livro concluído'} | perguntas abertas: {open_q}")


def cmd_next(a):
    b = _book(a.slug)
    t = next_task(b, runnable=a.runnable)
    if t:
        print(json.dumps(t, ensure_ascii=False, indent=1))
        return
    blocked = [x["id"] for x in b.load_state()["tasks"] if x["status"] == "blocked"]
    print(json.dumps({"id": None, "blocked": blocked,
                      "reason": "livro concluído" if not blocked else "restante depende de tarefas bloqueadas"},
                     ensure_ascii=False))


def cmd_mark(a):
    t = set_status(_book(a.slug), a.task, a.status, a.note or "")
    print(f"{t['id']} -> {t['status']}")


def cmd_build(a):
    from .render.build import build
    r = build(_book(a.slug), preview=a.preview, ppi=a.ppi)
    st = r["style"]
    print(f"PDF: {Path(r['pdf']).relative_to(ROOT)} | {r['pages']} páginas | trim {st['trim']} "
          f"| corpo {st['size']}pt (fonte preferida: {st['body_font'][0]}) | margem interna {st['inside']:.3f}in")
    for p in r.get("previews", []):
        print("preview:", Path(p).relative_to(ROOT))


def cmd_preview(a):
    """Renderiza páginas escolhidas e junta numa contact sheet (1 imagem = poucos tokens)."""
    import subprocess
    from .render.build import build
    b = _book(a.slug)
    r = build(b, preview=a.pages, ppi=a.ppi)
    out = b.build_dir / "sheet.png"
    subprocess.run([sys.executable, str(ROOT / "scripts" / "contact_sheet.py"), str(b.build_dir / "preview"),
                    str(out), str(a.cols)], check=True, capture_output=True)
    print(f"{r['pages']} páginas | folha: {out.relative_to(ROOT)} ({len(r.get('previews', []))} páginas)")


def cmd_check(a):
    from .validators import checks
    b = _book(a.slug)
    findings = checks.check_content(b, a.unit)
    if a.pdf:
        findings += checks.check_pdf(b)
    name = f"checks-{a.unit}.md" if a.unit else "checks.md"
    p = checks.write_report(b, findings, name, f"Checagem automática — {a.unit or 'livro inteiro'}")
    crit = sum(f["sev"] == checks.CRIT for f in findings)
    maj = sum(f["sev"] == checks.MAJ for f in findings)
    print(f"{len(findings)} achados ({crit} críticos, {maj} major) -> {p.relative_to(ROOT)}")
    for f in findings:
        if f["sev"] in (checks.CRIT, checks.MAJ):
            print(f"  {f['sev']} {f['where']}: {f['msg']}")
    sys.exit(1 if crit else 0)


def cmd_voice(a):
    from .validators import voice
    b = _book(a.slug)
    files = [b.unit_file(u) for u in b.units if u.get("kind", "prose") == "prose" and a.unit in (None, u["id"])]
    bad = 0
    for f in files:
        if not f.exists():
            continue
        m = voice.analyze(f.read_text(encoding="utf-8"))
        v = voice.verdict(m)
        bad += bool(v)
        print(f"{f.name}: {m['words']} palavras | curtas {m['short_sentence_pct']}% | "
              f"travessões/400w {m['em_dashes_per_400w']} | " + ("OK" if not v else "; ".join(v)))
    sys.exit(1 if bad else 0)


def cmd_cover(a):
    from pypdf import PdfReader
    from .render.cover import build_cover
    b = _book(a.slug)
    pdf = b.build_dir / f"{a.slug}-interior.pdf"
    pages = a.pages or (len(PdfReader(str(pdf)).pages) if pdf.exists() else None)
    if not pages:
        sys.exit("Sem PDF do miolo; rode build antes ou passe --pages.")
    r = build_cover(b, pages)
    print(json.dumps(r, ensure_ascii=False, indent=1))


def cmd_gen(a):
    """Gera puzzles/grids faltantes de uma unidade sem compilar o livro."""
    from .render.build import _ensure_generated
    b = _book(a.slug)
    u = next((u for u in b.units if u["id"] == a.unit), None)
    if not u:
        sys.exit(f"Unidade {a.unit} não existe.")
    d = _ensure_generated(b, u)
    print(f"{a.unit}: {len(d.get('puzzles', []))} puzzles prontos.")


def cmd_list(a):
    for d in sorted(BOOKS.glob("*/book.yaml")):
        b = Book(d.parent.name)
        tasks = b.load_state()["tasks"]
        done = sum(t["status"] in ("done", "skipped") for t in tasks)
        print(f"{b.slug:30} {done:>3}/{len(tasks):<3} {b.meta.get('title', '')}")


def main():
    p = argparse.ArgumentParser(prog="studio")
    s = p.add_subparsers(dest="cmd", required=True)
    n = s.add_parser("new"); n.add_argument("slug"); n.add_argument("--type", required=True,
        choices=["prose", "activity", "calendar", "planner", "children"])
    n.add_argument("--imprint"); n.add_argument("--title"); n.set_defaults(f=cmd_new)
    for name, f in (("plan", cmd_plan), ("status", cmd_status)):
        x = s.add_parser(name); x.add_argument("slug"); x.set_defaults(f=f)
    nx = s.add_parser("next"); nx.add_argument("slug")
    nx.add_argument("--runnable", action="store_true", help="pula bloqueadas e respeita dependências")
    nx.set_defaults(f=cmd_next)
    m = s.add_parser("mark"); m.add_argument("slug"); m.add_argument("task"); m.add_argument("status")
    m.add_argument("--note"); m.set_defaults(f=cmd_mark)
    bl = s.add_parser("build"); bl.add_argument("slug"); bl.add_argument("--preview", help='ex.: "1-4,12,last"')
    bl.add_argument("--ppi", type=int, default=50); bl.set_defaults(f=cmd_build)
    pv = s.add_parser("preview"); pv.add_argument("slug"); pv.add_argument("pages", help='ex.: "1-6,12,last"')
    pv.add_argument("--ppi", type=int, default=45); pv.add_argument("--cols", type=int, default=6)
    pv.set_defaults(f=cmd_preview)
    c = s.add_parser("check"); c.add_argument("slug"); c.add_argument("--unit"); c.add_argument("--pdf", action="store_true")
    c.set_defaults(f=cmd_check)
    v = s.add_parser("voice"); v.add_argument("slug"); v.add_argument("--unit"); v.set_defaults(f=cmd_voice)
    cv = s.add_parser("cover"); cv.add_argument("slug"); cv.add_argument("--pages", type=int); cv.set_defaults(f=cmd_cover)
    g = s.add_parser("gen"); g.add_argument("slug"); g.add_argument("unit"); g.set_defaults(f=cmd_gen)
    ls = s.add_parser("list"); ls.set_defaults(f=cmd_list)
    a = p.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
