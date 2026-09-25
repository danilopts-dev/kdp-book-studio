#!/usr/bin/env bash
# Teste rápido do engine com os livros de demonstração (books/_demo*). Rode depois de mexer em studio/.
set -e
cd "$(dirname "$0")/.."
./st build _demo && ./st build _demo-prose
./st check _demo --pdf >/dev/null || true
./st cover _demo-prose --pages 120 >/dev/null
echo "selftest OK"
