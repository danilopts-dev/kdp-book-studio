"""Métricas do human-voice-writing (seção 5.4): o que dá para contar sem LLM.

Não substitui a leitura do revisor; aponta onde olhar.
"""
from __future__ import annotations

import re

BANNED_EN = ["delve", "tapestry", "navigate", "landscape", "journey", "realm", "robust", "leverage",
             "seamless", "empower", "unlock", "elevate", "foster", "testament", "crucial", "pivotal",
             "nuanced", "it's worth noting", "in today's fast-paced world", "ignite", "comprehensive",
             "ultimate", "here's the thing", "the point is", "let's be clear", "in other words",
             "ultimately", "at its core", "this distinction matters", "notice what"]
BANNED_PT = ["no cenário atual", "mergulhar", "jornada", "desbloquear", "potencializar", "vale ressaltar",
             "em suma"]
AI_NAMES = ["Priya", "Nadia", "Maya", "Elena", "Sarah Chen", "Marcus", "Ethan"]
NEG_CORR = re.compile(
    r"\b(isn't|is not|aren't|are not|wasn't|not about|não é|não se trata)\b[^.!?]{0,80}[.!?]\s+"
    r"(It's|It is|They're|This is|É|Trata-se)\b|\bnot (just |only )?\w+[^.!?]{0,30}, but\b", re.I)
TRIAD = re.compile(r"\b\w+(?:\s\w+)?, \w+(?:\s\w+)?,? (?:and|e|or|ou) \w+", re.I)


def sentences(text: str) -> list[str]:
    text = re.sub(r"^#.*$", "", text, flags=re.M)
    parts = re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", text))
    return [p for p in parts if re.search(r"\w", p)]


def analyze(text: str) -> dict:
    words = re.findall(r"\b[\w'’]+\b", text)
    n_words = max(len(words), 1)
    sents = sentences(text)
    lens = [len(re.findall(r"\b[\w'’]+\b", s)) for s in sents]
    short = sum(1 for n in lens if n <= 6)
    run, max_run = 0, 0
    for n in lens:
        run = run + 1 if n <= 8 else 0
        max_run = max(max_run, run)
    low = text.lower()
    banned = {w: low.count(w) for w in BANNED_EN + BANNED_PT if re.search(r"\b" + re.escape(w) + r"\b", low)}
    dashes = text.count("—") + len(re.findall(r"\s--\s", text))
    paras = [p for p in text.split("\n\n") if p.strip() and not p.strip().startswith("#")]
    endings = [sentences(p)[-1] for p in paras if sentences(p)]
    punchy_endings = sum(1 for e in endings if len(e.split()) <= 6)
    return {
        "words": len(words),
        "sentences": len(sents),
        "short_sentence_pct": round(100 * short / max(len(sents), 1), 1),
        "max_short_run": max_run,
        "em_dashes_per_400w": round(dashes * 400 / n_words, 2),
        "negation_correction": len(NEG_CORR.findall(text)),
        "triads": len(TRIAD.findall(text)),
        "punchy_paragraph_endings": punchy_endings,
        "banned_words": banned,
        "ai_names": [n for n in AI_NAMES if n in text],
    }


def verdict(m: dict) -> list[str]:
    """Violações das metas do human-voice-writing."""
    v = []
    if m["short_sentence_pct"] >= 15:
        v.append(f"frases ≤6 palavras = {m['short_sentence_pct']}% (meta < 15%)")
    if m["max_short_run"] > 3:
        v.append(f"{m['max_short_run']} frases curtas seguidas (máx. 3)")
    if m["em_dashes_per_400w"] > 1:
        v.append(f"travessões: {m['em_dashes_per_400w']} por 400 palavras (máx. ~1)")
    if m["negation_correction"] > 1:
        v.append(f"negação-correção: {m['negation_correction']}x (máx. 1 por capítulo)")
    limit_punchy = max(1, m["words"] // 500)
    if m["punchy_paragraph_endings"] > limit_punchy:
        v.append(f"parágrafos fechando em frase de efeito curta: {m['punchy_paragraph_endings']} (máx. ~{limit_punchy})")
    if m["triads"] > max(2, m["words"] // 400):
        v.append(f"possíveis tríades automáticas: {m['triads']}")
    if m["banned_words"]:
        v.append(f"vocabulário proibido: {m['banned_words']}")
    if m["ai_names"]:
        v.append(f"nomes-padrão de IA: {m['ai_names']}")
    return v
