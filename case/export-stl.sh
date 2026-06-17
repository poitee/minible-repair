#!/bin/bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo "Generating STLs with tools/generate_stl.py"
python3 "$ROOT/tools/generate_stl.py"
