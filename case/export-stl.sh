#!/bin/bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$ROOT/case/stl"
SCAD="$ROOT/case/minible-shell.scad"

mkdir -p "$OUT"

OPENSCAD=""
for candidate in \
    "$(command -v openscad 2>/dev/null || true)" \
    "/opt/homebrew/bin/openscad" \
    "/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD" \
    "/Applications/OpenSCAD-2021.01.app/Contents/MacOS/OpenSCAD"
do
    if [ -n "$candidate" ] && [ -x "$candidate" ]; then
        OPENSCAD="$candidate"
        break
    fi
done

if [ -z "$OPENSCAD" ]; then
    echo "OpenSCAD not found. Install with: brew install --cask openscad"
    echo "Or export STLs manually from the OpenSCAD GUI using minible-shell.scad"
    exit 1
fi

export_part() {
    local part="$1"
    local file="$2"
    echo "Exporting $file"
    "$OPENSCAD" -o "$OUT/$file" -D "part=\"$part\"" "$SCAD"
}

export_part top minible-shell-top.stl
export_part bottom minible-shell-bottom.stl
export_part battery_door minible-battery-door.stl

echo "STLs written to $OUT"
