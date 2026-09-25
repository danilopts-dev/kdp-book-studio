#!/usr/bin/env bash
# Prepara o ambiente (venv + dependências). Idempotente e rápido quando já está pronto.
# Roda sozinho no início de cada sessão do Claude Code (hook SessionStart em .claude/settings.json).
set -e
cd "$(dirname "$0")/.."
if [ -x .venv/bin/python ]; then PY=.venv/bin/python
elif [ -x .venv/Scripts/python.exe ]; then PY=.venv/Scripts/python.exe
else
  (python3 -m venv .venv || python -m venv .venv) >/dev/null
  if [ -x .venv/bin/python ]; then PY=.venv/bin/python; else PY=.venv/Scripts/python.exe; fi
fi
STAMP=.venv/.req-stamp
if [ ! -f "$STAMP" ] || ! cmp -s requirements.txt "$STAMP"; then
  "$PY" -m pip install -q --disable-pip-version-check -r requirements.txt
  cp requirements.txt "$STAMP"
fi
