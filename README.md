# Food Plant Conveyor Tool Palette for AutoCAD

Sanitary / food-processing conveyor CAD library for plant layout.
Generic hygiene classes only — not a copy of any OEM catalog.

**Units:** 1 drawing unit = 1 inch. Insert at 1:1.
**Prefix:** `FP-CONV-`
**Commands:** `FPSETUP` `FPBELT` `FPBELTE` `FPMOD` `FPROLL` `FPSCRW` `FPXFR` `FPSTD` `FPDPAN` `FPMD` `FPFLOW` `FPLIB`

## What you get

| Folder | Contents |
|---|---|
| `Lisp/` | AutoLISP that creates layers and draws parametric plan/elevation blocks |
| `Python/` | R12 DXF generator (no extra packages) |
| `Dxf/` | Ready-to-import 2D symbols |
| `Palettes/` | Tab inventory and tool list for DesignCenter |
| `Standards/` | NCS-style layers, hygiene levels, drawing conventions |

## Install in AutoCAD (fastest path)

1. Copy this folder to a stable path, preferably UNC:
   `\\Server\\CAD\\FoodPlant_Conveyor_ToolPalette\\`
   or `C:\\CAD\\FoodPlant_Conveyor_ToolPalette\\`
2. `APPLOAD` → load `Lisp/FP-FoodPlant-Conveyors.lsp`.
   Check *Startup Suite* so it loads every session.
3. Type **FPSETUP** then **FPLIB**.
   FPLIB builds standard-width blocks in the current drawing.
4. Save as `Blocks/FP-CONV-LIBRARY.dwg`.
5. `ADCENTER` (Ctrl+2) → browse to that DWG → **Blocks** → right-click → **Create Tool Palette**.
6. Repeat per family DWG if you split libraries, or keep one master palette and add separators.
7. `CUSTOMIZE` → drag palettes into a group named **Food Plant Conveyors** → right-click group → **Export** `.xpg`.
8. Right-click each palette → **Export** `.xtp` into `Palettes/`.
9. OPTIONS → Files → add the folder to **Support File Search Path** and **Tool Palettes File Locations**.

### Import DXF symbols without LISP

`INSERT` or `IMPORTHFB` each file in `Dxf/`, or drag from DesignCenter.
Then Create Tool Palette from those blocks.

### AutoCAD Architecture / MEP

Those products cannot Import `.xtp`. Use Content Browser and an `.atc` catalog, or drag blocks from DesignCenter onto an existing palette.

## Important XTP facts

- An `.xtp` does **not** contain geometry. It stores labels, layer/scale/rotation properties, and a **Source File** path to the DWG.
- Icons live in a sibling `Images\\` folder created on Export. Keep XTP + Images together.
- If tools go blank after a move: right-click tool → Properties → Source File → repath to the library DWG.
- Do not hand-author XTP XML. GUIDs and stock-tool refs break easily.

## Hygiene levels (put on every conveyor)

| Tag | Zone | Construction |
|---|---|---|
| L1 | Dry / packaged | Bolted or painted 304, IP54–IP65 |
| L2 | Light wash / bakery pack | Bolted 304 #4, standoff bearings, IP65–IP66 |
| L3 | Washdown | Welded 304 open frame, tip-up tail, IP66 |
| L4 | Sanitary / CIP | TIG 304/316, 32 µin Ra, sloped, H1 lube, IP69K |
| L5 | 3-A / USDA | Continuous welds, min radii, tool-less COP |

304 default. 316/316L for salt, brine, hypochlorite, aggressive CIP.

## Standard sizes

- Belt widths (in): 6, 8, 12, 18, 24, 36, 48
- Length modules (in): 36, 48, 60, 72, 96, 120
- Work height / TOB: 30–36 in process/pack; 18–24 in dumpers
- H-stand spacing: 12 in from ends, then 60–72 in c/c
- Frame overhang: 2 in each side of belt (24 in belt → 28 in overall)

## Legal / use

Layout symbols only. Verify dimensions against the selected OEM and plant sanitary design review (FDA, USDA, 3-A SSI, NSF, BISSC, AMI/NAMI, FSMA, EHEDG as applicable).
