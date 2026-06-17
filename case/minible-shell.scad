// Mooltipass Mini BLE — service shell (two-part clam shell)
// Coordinate system: origin at bottom-left-back corner of the case.
//   +X = toward scroll wheel end (89 mm)
//   +Y = toward smartcard edge (35.5 mm)
//   +Z = toward display face (12.5 mm)
//
// Dimensions derived from minible_hw KiCad (see docs/dimensions.md).
// Run: ./case/export-stl.sh

part = "both";          // "front" | "back" | "both" | "battery_door"

// --- case envelope ---
case_l = 89.0;
case_w = 35.5;
case_h = 12.5;
wall = 1.8;
clearance = 0.4;
corner_r = 3.0;

// --- PCB pocket ---
pcb_l = 74.8;
pcb_w = 31.2;
pcb_h = 6.0;            // verify stack height on hardware
margin_x = (case_l - pcb_l) / 2;   // 7.1
margin_y = (case_w - pcb_w) / 2;   // 2.15

// --- feature positions (case coords, mm) ---
usb_x = 72.9;
usb_y = 5.35;
usb_open_w = 9.5;
usb_open_h = 3.5;

wheel_x = 78.4;
wheel_y = 17.75;
wheel_bore_d = 20.0;

oled_cx = 41.4;         // approx. center of 52 mm active area
oled_cy = 17.75;
oled_w = 52.0;
oled_h = 14.0;

card_x = 4.0;
card_y = 29.3;
card_slot_w = 24.0;
card_slot_h = 1.4;

battery_cx = 7.4;
battery_cy = 17.75;
battery_door_w = 22.0;
battery_door_h = 34.0;

mount_j1 = [9.6, 3.75];
mount_j2 = [9.6, 31.75];
mount_d = 1.6;          // M1.4 screw clearance

lip_depth = 2.0;
lip_inset = 1.2;
split_gap = 0.25;
screw_post_d = 4.8;

inner_l = pcb_l + 2 * clearance;
inner_w = pcb_w + 2 * clearance;
inner_h = pcb_h + clearance;

module rounded_box(l, w, h, r) {
    // Simple chamfered box — avoids heavy minkowski() in headless export.
    cube([l, w, h]);
}

module pcb_cavity() {
    translate([margin_x, margin_y, wall])
        cube([inner_l, inner_w, inner_h]);
}

module usb_port() {
    translate([usb_x, usb_y - usb_open_h / 2, -0.1])
        cube([usb_open_w, usb_open_h, wall + 0.2]);
}

module wheel_bore() {
    translate([case_l, wheel_y, case_h / 2])
        rotate([0, 90, 0])
            cylinder(h = wall + 0.2, d = wheel_bore_d, center = true, $fn = 72);
}

module display_window() {
    translate([oled_cx - oled_w / 2, oled_cy - oled_h / 2, case_h - wall - 0.1])
        cube([oled_w, oled_h, wall + 0.2]);
}

module card_slot() {
    translate([card_x, card_y - card_slot_w / 2, case_h / 2 - card_slot_h / 2])
        cube([wall + 2, card_slot_w, card_slot_h + 0.2]);
}

module mount_posts() {
    for (p = [mount_j1, mount_j2])
        translate([p[0], p[1], 0])
            cylinder(h = case_h, d = screw_post_d, $fn = 32);
}

module mount_holes() {
    for (p = [mount_j1, mount_j2])
        translate([p[0], p[1], -0.1])
            cylinder(h = case_h + 0.2, d = mount_d, $fn = 24);
}

module mating_lip(top = true) {
    z0 = top ? case_h / 2 : case_h / 2 - lip_depth;
    translate([margin_x - lip_inset, margin_y - lip_inset, z0])
        difference() {
            cube([inner_l + 2 * lip_inset, inner_w + 2 * lip_inset, lip_depth]);
            translate([lip_inset, lip_inset, -0.1])
                cube([inner_l, inner_w, lip_depth + 0.2]);
        }
}

module top_shell() {
    intersection() {
        difference() {
            rounded_box(case_l, case_w, case_h, corner_r);
            pcb_cavity();
            display_window();
            wheel_bore();
            mount_holes();
        }
        translate([-0.1, -0.1, case_h / 2 - split_gap])
            cube([case_l + 0.2, case_w + 0.2, case_h / 2 + split_gap]);
    }
    mating_lip(true);
    mount_posts();
}

module bottom_shell() {
    intersection() {
        difference() {
            rounded_box(case_l, case_w, case_h, corner_r);
            pcb_cavity();
            usb_port();
            card_slot();
            mount_holes();
            battery_access_cut();
        }
        translate([-0.1, -0.1, -0.1])
            cube([case_l + 0.2, case_w + 0.2, case_h / 2 + split_gap]);
    }
    mating_lip(false);
    mount_posts();
}

module battery_access_cut() {
    // Pocket under BT1 for future swaps without splitting the whole shell.
    translate([battery_cx - battery_door_w / 2, battery_cy - battery_door_h / 2, -0.1])
        cube([battery_door_w, battery_door_h, wall + inner_h + 0.5]);
}

module battery_door() {
  t = 1.4;
  translate([battery_cx - battery_door_w / 2, battery_cy - battery_door_h / 2, wall - 0.05])
    cube([battery_door_w, battery_door_h, t]);
}

if (part == "front" || part == "top") {
    top_shell();
} else if (part == "back" || part == "bottom") {
    bottom_shell();
} else if (part == "battery_door") {
    battery_door();
} else {
    color("Gainsboro") top_shell();
    translate([0, case_w + 6, 0]) color("DimGray") bottom_shell();
    translate([0, 2 * (case_w + 6), 0]) color("Silver") battery_door();
}
