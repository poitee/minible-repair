#!/usr/bin/env python3
"""Generate Mini BLE service shell STLs (no OpenSCAD required)."""

from __future__ import annotations

import sys
from pathlib import Path

import trimesh
import trimesh.boolean

# Mirrors case/minible-shell.scad
CASE_L = 89.0
CASE_W = 35.5
CASE_H = 12.5
WALL = 1.8
CLEARANCE = 0.4
PCB_L = 74.8
PCB_W = 31.2
PCB_H = 6.0
MARGIN_X = (CASE_L - PCB_L) / 2
MARGIN_Y = (CASE_W - PCB_W) / 2
SPLIT_GAP = 0.25
SPLIT_Z = CASE_H / 2 - SPLIT_GAP

USB_X = 72.9
USB_Y = 5.35
USB_OPEN_W = 9.5
USB_OPEN_H = 3.5

WHEEL_Y = 17.75
WHEEL_BORE = 20.0

OLED_CX = 41.4
OLED_CY = 17.75
OLED_W = 52.0
OLED_H = 14.0

CARD_X = 4.0
CARD_Y = 29.3
CARD_SLOT_W = 24.0
CARD_SLOT_H = 1.4

BATTERY_CX = 7.4
BATTERY_CY = 17.75
BATTERY_DOOR_W = 22.0
BATTERY_DOOR_H = 34.0

MOUNT_J1 = (9.6, 3.75)
MOUNT_J2 = (9.6, 31.75)
MOUNT_D = 1.6
SCREW_POST = 4.8

LIP_DEPTH = 2.0
LIP_INSET = 1.2

INNER_L = PCB_L + 2 * CLEARANCE
INNER_W = PCB_W + 2 * CLEARANCE
INNER_H = PCB_H + CLEARANCE


def box_at(x0: float, y0: float, z0: float, x1: float, y1: float, z1: float) -> trimesh.Trimesh:
    extents = (x1 - x0, y1 - y0, z1 - z0)
    center = ((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2)
    return trimesh.creation.box(
        extents,
        transform=trimesh.transformations.translation_matrix(center),
    )


def difference(base: trimesh.Trimesh, *cuts: trimesh.Trimesh) -> trimesh.Trimesh:
    result = base.copy()
    for cut in cuts:
        result = trimesh.boolean.difference([result, cut], engine="manifold")
    return result


def union(*parts: trimesh.Trimesh) -> trimesh.Trimesh:
    mesh = parts[0].copy()
    for part in parts[1:]:
        mesh = trimesh.boolean.union([mesh, part], engine="manifold")
    return mesh


def pcb_cavity() -> trimesh.Trimesh:
    return box_at(
        MARGIN_X,
        MARGIN_Y,
        WALL,
        MARGIN_X + INNER_L,
        MARGIN_Y + INNER_W,
        WALL + INNER_H,
    )


def mount_holes() -> list[trimesh.Trimesh]:
    holes = []
    for x, y in (MOUNT_J1, MOUNT_J2):
        holes.append(
            box_at(
                x - MOUNT_D / 2,
                y - MOUNT_D / 2,
                -0.1,
                x + MOUNT_D / 2,
                y + MOUNT_D / 2,
                CASE_H + 0.2,
            )
        )
    return holes


def mount_posts() -> list[trimesh.Trimesh]:
    posts = []
    for x, y in (MOUNT_J1, MOUNT_J2):
        posts.append(
            box_at(
                x - SCREW_POST / 2,
                y - SCREW_POST / 2,
                0,
                x + SCREW_POST / 2,
                y + SCREW_POST / 2,
                CASE_H,
            )
        )
    return posts


def mating_lip(top: bool) -> trimesh.Trimesh:
    x0 = MARGIN_X - LIP_INSET
    y0 = MARGIN_Y - LIP_INSET
    x1 = MARGIN_X + INNER_L + LIP_INSET
    y1 = MARGIN_Y + INNER_W + LIP_INSET
    if top:
        z0 = SPLIT_Z + SPLIT_GAP
        z1 = z0 + LIP_DEPTH
    else:
        z1 = SPLIT_Z + SPLIT_GAP
        z0 = z1 - LIP_DEPTH
    outer = box_at(x0, y0, z0, x1, y1, z1)
    inner = box_at(
        x0 + LIP_INSET,
        y0 + LIP_INSET,
        z0 - 0.1,
        x1 - LIP_INSET,
        y1 - LIP_INSET,
        z1 + 0.1,
    )
    return difference(outer, inner)


def top_shell() -> trimesh.Trimesh:
    body = box_at(0, 0, SPLIT_Z, CASE_L, CASE_W, CASE_H)
    cuts = [
        pcb_cavity(),
        box_at(
            OLED_CX - OLED_W / 2,
            OLED_CY - OLED_H / 2,
            CASE_H - WALL - 0.1,
            OLED_CX + OLED_W / 2,
            OLED_CY + OLED_H / 2,
            CASE_H + 0.2,
        ),
        box_at(
            CASE_L - WALL - 0.1,
            WHEEL_Y - WHEEL_BORE / 2,
            CASE_H / 2 - WHEEL_BORE / 2,
            CASE_L + 0.2,
            WHEEL_Y + WHEEL_BORE / 2,
            CASE_H / 2 + WHEEL_BORE / 2,
        ),
        *mount_holes(),
    ]
    shell = difference(body, *cuts)
    return union(shell, mating_lip(True), *mount_posts())


def bottom_shell() -> trimesh.Trimesh:
    body = box_at(0, 0, 0, CASE_L, CASE_W, SPLIT_Z + SPLIT_GAP)
    cuts = [
        pcb_cavity(),
        box_at(
            USB_X,
            USB_Y - USB_OPEN_H / 2,
            -0.1,
            USB_X + USB_OPEN_W,
            USB_Y + USB_OPEN_H / 2,
            WALL + 0.2,
        ),
        box_at(
            CARD_X,
            CARD_Y - CARD_SLOT_W / 2,
            CASE_H / 2 - CARD_SLOT_H / 2,
            CARD_X + WALL + 2,
            CARD_Y + CARD_SLOT_W / 2,
            CASE_H / 2 + CARD_SLOT_H / 2,
        ),
        box_at(
            BATTERY_CX - BATTERY_DOOR_W / 2,
            BATTERY_CY - BATTERY_DOOR_H / 2,
            -0.1,
            BATTERY_CX + BATTERY_DOOR_W / 2,
            BATTERY_CY + BATTERY_DOOR_H / 2,
            WALL + INNER_H + 0.5,
        ),
        *mount_holes(),
    ]
    shell = difference(body, *cuts)
    return union(shell, mating_lip(False), *mount_posts())


def battery_door() -> trimesh.Trimesh:
    t = 1.4
    return box_at(
        BATTERY_CX - BATTERY_DOOR_W / 2,
        BATTERY_CY - BATTERY_DOOR_H / 2,
        WALL - 0.05,
        BATTERY_CX + BATTERY_DOOR_W / 2,
        BATTERY_CY + BATTERY_DOOR_H / 2,
        WALL - 0.05 + t,
    )


def main() -> int:
    out_dir = Path(__file__).resolve().parents[1] / "case" / "stl"
    out_dir.mkdir(parents=True, exist_ok=True)

    parts = {
        "minible-shell-top.stl": top_shell(),
        "minible-shell-bottom.stl": bottom_shell(),
        "minible-battery-door.stl": battery_door(),
    }

    for name, mesh in parts.items():
        path = out_dir / name
        mesh.export(path)
        print(f"Wrote {path} ({path.stat().st_size // 1024} KiB)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
