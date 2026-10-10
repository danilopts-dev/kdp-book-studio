"""Modelo do livro (book.yaml) e estado do pipeline (state.json)."""
from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
BOOKS = ROOT / "books"
PIPELINE = ROOT / "pipelines" / "pipeline.yaml"

STATUSES = ("pending", "in_progress", "done", "blocked", "skipped")


@dataclass
class Book:
    slug: str

    @property
    def dir(self) -> Path:
        return BOOKS / self.slug

    @property
    def build_dir(self) -> Path:
        return self.dir / "build"

    def path(self, *parts: str) -> Path:
        return self.dir.joinpath(*parts)

    @property
    def meta(self) -> dict:
        return yaml.safe_load(self.path("book.yaml").read_text(encoding="utf-8")) or {}

    def save_meta(self, meta: dict) -> None:
        self.path("book.yaml").write_text(
            yaml.safe_dump(meta, allow_unicode=True, sort_keys=False, width=100), encoding="utf-8"
        )

    @property
    def units(self) -> list[dict]:
        return self.meta.get("units") or []

    def unit_file(self, unit: dict) -> Path:
        kind = unit.get("kind", "prose")
        ext = {"prose": "md", "typst": "typ"}.get(kind, "yaml")
        return self.path("content", f"{unit['id']}.{ext}")

    # --- estado -------------------------------------------------------------
    @property
    def state_path(self) -> Path:
        return self.path("state.json")

    def load_state(self) -> dict:
        if not self.state_path.exists():
            return {"tasks": []}
        return json.loads(self.state_path.read_text(encoding="utf-8"))

    def save_state(self, state: dict) -> None:
        self.state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


def load_pipeline() -> dict:
    return yaml.safe_load(PIPELINE.read_text(encoding="utf-8"))


def plan_tasks(book: Book) -> list[dict]:
    """Expande o pipeline em tarefas concretas. Etapas per_unit viram uma tarefa por unidade."""
    pipe = load_pipeline()
    tasks = []
    for stage in pipe["stages"]:
        if stage.get("per_unit"):
            for u in book.units:
                kind = u.get("kind", "prose")
                spec = pipe["unit_kinds"].get(kind)
                if spec is None:
                    raise ValueError(f"Unidade '{u['id']}' com kind '{kind}' sem definição em pipeline.yaml")
                tasks.append({
                    "id": f"unit:{u['id']}",
                    "stage": stage["id"],
                    "unit": u["id"],
                    "kind": kind,
                    "agent": spec["agent"],
                    "instructions": spec["instructions"],
                })
        else:
            tasks.append({
                "id": stage["id"],
                "stage": stage["id"],
                "agent": stage["agent"],
                "instructions": stage["instructions"],
            })
    return tasks


def replan(book: Book) -> dict:
    """Recria a lista de tarefas preservando o status das que já existiam."""
    old = {t["id"]: t for t in book.load_state()["tasks"]}
    tasks = []
    for t in plan_tasks(book):
        prev = old.get(t["id"], {})
        t["status"] = prev.get("status", "pending")
        t["note"] = prev.get("note", "")
        t["updated"] = prev.get("updated", "")
        tasks.append(t)
    state = {"tasks": tasks}
    book.save_state(state)
    return state


def set_status(book: Book, task_id: str, status: str, note: str = "") -> dict:
    if status not in STATUSES:
        raise ValueError(f"Status inválido: {status}")
    state = book.load_state()
    for t in state["tasks"]:
        if t["id"] == task_id:
            t["status"] = status
            if note:
                t["note"] = note
            t["updated"] = datetime.now().isoformat(timespec="minutes")
            book.save_state(state)
            return t
    raise KeyError(f"Tarefa '{task_id}' não existe. Rode `python -m studio plan {book.slug}`.")


# Etapas que só rodam com tudo o que vem antes concluído (o livro inteiro precisa existir).
NEEDS_ALL_PREVIOUS = {"build", "editorial", "listing", "cover", "finalize"}
# Etapas que correm em paralelo: não seguram build/editorial/listing/capa, só a entrega (finalize).
# O bônus depende de ações do Danilo (link do PDF, formulário no Brevo); enquanto isso o livro segue.
PARALLEL = {"bonus"}


def next_task(book: Book, runnable: bool = False) -> dict | None:
    """Próxima tarefa. Com runnable=True pula as bloqueadas e respeita dependências:
    unidades, matter e bonus só dependem do intake; build em diante dependem de tudo antes
    (menos do bonus, que só segura o finalize)."""
    tasks = book.load_state()["tasks"]
    ok = ("done", "skipped")
    for i, t in enumerate(tasks):
        if t["status"] in ok:
            continue
        if not runnable:
            return t
        if t["status"] == "blocked":
            continue
        if t["id"] != "intake" and any(x["id"] == "intake" and x["status"] not in ok for x in tasks):
            return None
        if t["stage"] in NEEDS_ALL_PREVIOUS and any(
            x["status"] not in ok and (t["stage"] == "finalize" or x["stage"] not in PARALLEL) for x in tasks[:i]
        ):
            return None
        return t
    return None
