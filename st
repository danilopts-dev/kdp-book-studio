#!/usr/bin/env bash
# Atalho para a CLI do estúdio: ./st status meu-livro
cd "$(dirname "$0")"
if [ -x .venv/bin/python ]; then PY=.venv/bin/python
elif [ -x .venv/Scripts/python.exe ]; then PY=.venv/Scripts/python.exe
else PY=python; fi
export PYTHONIOENCODING=utf-8
exec "$PY" -m studio "$@"
