# Teardown notes

## Factory enclosure

The retail Mini BLE uses a **brushed aluminum** shell approximately **89 × 35.5 × 12.5 mm**. The factory assembly is not designed for end-user service. Expect:

- Adhesive or tight snap fits
- Risk of cosmetic damage when opening
- No standard screws on most units

Community contributors should document their opening method here once validated. If you succeed with a repeatable technique, add photos via pull request.

## Internal layout (from open hardware files)

Reference repository: [mooltipass/minible_hw](https://github.com/mooltipass/minible_hw)

| Item | Notes |
|------|-------|
| Main PCB outline | 74.8 × 31.2 mm (Edge.Cuts bounding box) |
| Battery `BT1` | 2/3 AAA NiMH, soldered (`BAT_TWOTHIRD_AAA`) |
| Display | OLED module with fragile flex cable |
| USB-C | Board edge connector |
| Scroll wheel | Mechanical assembly on front face |
| Smartcard slot | End of device |

## FCC internal photos

Stephan Electronics filed internal photos for model **MBLE1**:

https://fccid.io/2AYPT-MBLE1/Internal-Photos/Internal-Photos-5088688

Use these photos together with the KiCad PCB to confirm component keep-out zones before printing a service shell.

## Recommended service approach

1. Open or sacrifice the factory shell once.
2. Take **caliper measurements** of:
   - PCB-to-shell clearance (top/bottom/sides)
   - Display active area and bezel overlap
   - USB-C port centerline and panel thickness
   - Scroll wheel bore diameter and exposed height
3. Compare against [dimensions.md](dimensions.md) and tune [minible-shell.scad](../case/minible-shell.scad).
4. Install the PCB in the printed **service shell** for future battery access.

## Opening techniques (community draft)

The stock shell is aluminum and not designed for user service. Approaches reported in similar devices:

| Method | Risk | Notes |
|--------|------|-------|
| Plastic spudger along seam | Cosmetic scratches | Work slowly around the perimeter |
| Heat gun + isopropyl on adhesive | Warping / burn risk | Low heat only; keep away from battery |
| Sacrifice rear panel | Lose waterproofing | Acceptable if moving to printed shell |

> **We need community validation.** If you successfully open a unit, please document your method with photos in a pull request.

## Assembly orientation

When viewing the device with the **display facing up** and the **scroll wheel to your right**:

- USB-C is on the bottom edge near the wheel end
- Smartcard slot is on the top edge near the battery end
- Battery cell sits under the left end of the PCB

## Battery service constraint

The stock design routes battery replacement through **desoldering** because there is no inline disconnect switch ([minible_hw#4](https://github.com/mooltipass/minible_hw/issues/4)). Plan for full PCB removal or a shell that allows bottom access.

## ESD and cleanliness

The secure MCU and smartcard interface are ESD-sensitive. Avoid metal tools near powered flex cables.
