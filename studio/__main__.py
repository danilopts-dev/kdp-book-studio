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

from . import onedrive
from .book import BOOKS, ROOT, Book, next_task, replan, set_status

IMPRINT_NAMES = {
    "golden-chapter": "Golden Chapter Press",
    "silvia-press": "Silvia Press",
    "emily-harper": "Emily P. Harper",
    "jonah-feldman": "Jonah Feldman",
}

ICON = {"pending": "·", "in_progress": "▶", "done": "✓", "blocked": "⛔", "skipped": "–"}


def _book(slug: str) -> Book:
    """Aceita o apelido exato da pasta ou um pedaço do apelido/título ("hanukkah", "planner")."""
    b = Book(slug)
    if b.path("book.yaml").exists():
        return b
    term = slug.lower()
    found = []
    for d in sorted(BOOKS.glob("*/book.yaml")):
        name = d.parent.name
        if name.startswith("_"):
            continue
        title = str((yaml.safe_load(d.read_text(encoding="utf-8")) or {}).get("title", "")).lower()
        if term in name.lower() or term in title:
            found.append(name)
    if len(found) == 1:
        return Book(found[0])
    if found:
        sys.exit(f"'{slug}' combina com mais de um livro: {', '.join(found)}")
    sys.exit(f"Livro '{slug}' não existe em books/. Use: python -m studio new {slug} --type ...")


STAGE_LABELS = {
    "intake": "Ficha técnica (TOC → plano do livro)",
    "matter": "Páginas de abertura e fechamento",
    "bonus": "Bônus (PDF, e-mail no Brevo, QR)",
    "build": "Montagem do PDF",
    "editorial": "Revisão final do livro",
    "listing": "Página da Amazon (título, keywords, descrição, A+)",
    "cover": "Capa",
    "finalize": "Entrega",
}


def label(book: Book, t: dict) -> str:
    """Nome legível da tarefa, para falar com o Danilo."""
    if t.get("unit"):
        u = next((u for u in book.units if u["id"] == t["unit"]), {})
        return u.get("title") or t["unit"]
    return STAGE_LABELS.get(t["id"], t["id"])


def open_questions(book: Book) -> tuple[int, int]:
    """(preciso de você, decidi sozinho) abertas em questions.md."""
    q = book.path("questions.md")
    if not q.exists():
        return 0, 0
    need = mine = 0
    for line in q.read_text(encoding="utf-8").splitlines():
        if not line.startswith("- [ ]"):
            continue
        if "BLOQUEANTE" in line or "PRECISO" in line.upper():
            need += 1
        else:
            mine += 1
    return need, mine


def cmd_new(a):
    b = Book(a.slug)
    if b.dir.exists():
        sys.exit(f"books/{a.slug} já existe.")
    shutil.copytree(ROOT / "templates" / "book", b.dir)
    meta = yaml.safe_load((b.dir / "book.yaml").read_text(encoding="utf-8"))
    meta.update(slug=a.slug, type=a.type, imprint=a.imprint or meta.get("imprint"), title=a.title or meta.get("title"))
    if a.imprint:
        meta["imprint_name"] = IMPRINT_NAMES.get(a.imprint, a.imprint)
    if a.onedrive:
        meta["onedrive_folder"] = a.onedrive
    b.save_meta(meta)
    replan(b)
    if a.onedrive:
        onedrive.link(b)
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
        print(f"  {ICON[t['status']]} {label(b, t)} [{t['id']}]{note}")
    nt = next_task(b)
    need, mine = open_questions(b)
    print(f"Próxima: {label(b, nt) + ' [' + nt['id'] + ']' if nt else '— livro concluído'} | "
          f"preciso do Danilo: {need} | decidi sozinho (conferir): {mine}")


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


def cmd_link(a):
    onedrive.link(_book(a.slug))


def cmd_publish(a):
    onedrive.publish(_book(a.slug), quiet=a.quiet)


def cmd_list(a):
    for d in sorted(BOOKS.glob("*/book.yaml")):
        b = Book(d.parent.name)
        if b.slug.startswith("_") and not a.all:
            continue
        tasks = b.load_state()["tasks"]
        done = sum(t["status"] in ("done", "skipped") for t in tasks)
        need, _ = open_questions(b)
        state = "pronto" if tasks and done == len(tasks) else f"{done}/{len(tasks)} etapas"
        wait = f" | preciso do Danilo: {need}" if need else ""
        print(f"{b.slug:30} {state:14} {b.meta.get('title', '')}{wait}")


def cmd_qr(a):
    from . import extras
    b = _book(a.slug)
    if not (a.url or a.placeholder):
        sys.exit("Passe a URL do formulário do Brevo, ou --placeholder.")
    print(extras.make_qr(b, None if a.placeholder else a.url))


def cmd_bonus(a):
    from . import extras
    r = extras.build_bonus(_book(a.slug), preview=a.preview)
    for name, n in r.items():
        print(f"{name}: {n} páginas")


def cmd_estimate(a):
    from . import extras
    print(json.dumps(extras.estimate_pages(_book(a.slug)), ensure_ascii=False, indent=1))


def cmd_keywords(a):
    from . import extras
    p, msg = extras.keyword_research(_book(a.slug), a.seeds)
    print(f"{msg} -> {p.relative_to(ROOT)}")


def main():
    p = argparse.ArgumentParser(prog="studio")
    s = p.add_subparsers(dest="cmd", required=True)
    n = s.add_parser("new"); n.add_argument("slug"); n.add_argument("--type", required=True,
        choices=["prose", "activity", "calendar", "planner", "children"])
    n.add_argument("--imprint"); n.add_argument("--title")
    n.add_argument("--onedrive", help='nome da pasta no OneDrive, ex.: "15 - Meu Livro"'); n.set_defaults(f=cmd_new)
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
    lk = s.add_parser("link"); lk.add_argument("slug"); lk.set_defaults(f=cmd_link)
    pb = s.add_parser("publish"); pb.add_argument("slug"); pb.add_argument("--quiet", action="store_true")
    pb.set_defaults(f=cmd_publish)
    ls = s.add_parser("list"); ls.add_argument("--all", action="store_true", help="inclui os livros _demo")
    ls.set_defaults(f=cmd_list)
    q = s.add_parser("qr", help="QR do bônus em inputs/bonus-qr.png")
    q.add_argument("slug"); q.add_argument("url", nargs="?")
    q.add_argument("--placeholder", action="store_true", help="quadrado provisório até o formulário existir")
    q.set_defaults(f=cmd_qr)
    bo = s.add_parser("bonus", help="compila bonus/*.typ em build/<livro>-bonus.pdf")
    bo.add_argument("slug"); bo.add_argument("--preview", action="store_true"); bo.set_defaults(f=cmd_bonus)
    es = s.add_parser("estimate", help="projeta o total de páginas com as unidades prontas")
    es.add_argument("slug"); es.set_defaults(f=cmd_estimate)
    kw = s.add_parser("keywords", help="termos reais do autocomplete de Livros da Amazon.com")
    kw.add_argument("slug"); kw.add_argument("seeds", nargs="+", help='ex.: "hanukkah activity book" "hanukkah gifts for kids"')
    kw.set_defaults(f=cmd_keywords)
    a = p.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
