# Palette group: Food Plant Conveyors

Create 10 tabs. After DesignCenter build, add **Separators** and **Text** labels inside each tab.

Block pattern: `FP-CONV-{FAMILY}-{VIEW}-{WIDTH}[-OPT]`
Insertion: infeed tail at origin, centerline on Y=0, product flow +X.

## Tab 01 Belt
- FP-CONV-BELT-PLN-06/08/12/18/24/36/48
- FP-CONV-BELT-ELV-06/08/12/18/24/36/48
- FP-CONV-BELT-CLT-PLN / ELV (cleated)
- FP-CONV-BELT-PDU-PLN / ELV (positive-drive homogeneous TPU)
- FP-CONV-BELT-INC-15 / 30 / 45
- FP-CONV-BELT-ZFR-PLN / ELV (Z / LPZ / gooseneck)
- FP-CONV-BELT-CUR-90 / 180
- FP-CONV-BELT-VBT-PLN / ELV (vertical belt)
Command: `FPBELT` `FPBELTE`

## Tab 02 Modular plastic
- FP-CONV-MOD-PLN-12/18/24/36/48
- FP-CONV-MOD-ELV-...
- FP-CONV-MOD-CLT-PLN (cleated / scoop)
- FP-CONV-MOD-OPN-PLN (open-hinge hygienic)
- FP-CONV-MOD-CUR-90 / 180
- FP-CONV-MOD-ZFR
Command: `FPMOD`

## Tab 03 Wire mesh / metal belt
- FP-CONV-MESH-PLN-12/18/24/36
- FP-CONV-MESH-ELV
- FP-CONV-MESH-BAL / FLT / CLN
Command: draw with `FPMOD` then set BELT=WM, or insert DXF and rename.

## Tab 04 Tabletop / flexible chain
- FP-CONV-TT-PLN-3.25 / 4.5 / 7.5 / 12
- FP-CONV-TT-CUR-30 / 45 / 90
- FP-CONV-TT-WET

## Tab 05 Roller (L1–L2 only)
- FP-CONV-ROL-GRV-PLN-12/18/24/36
- FP-CONV-ROL-CDL-PLN
- FP-CONV-ROL-ACC-PLN
- FP-CONV-ROL-PLT-PLN
Command: `FPROLL`

## Tab 06 Bulk + special
- FP-CONV-SCRW-PLN-04/06/09/12/16
- FP-CONV-SCRW-ELV + hopper
- FP-CONV-BKT-PLN / ELV
- FP-CONV-VIB-PLN-12/18/24/36
- FP-CONV-SPR-PLN / ELV (spiral footprint)
Command: `FPSCRW`

## Tab 07 Transfers
- FP-CONV-XFR-NOSE-06..48
- FP-CONV-XFR-PWR / DED / 90 / CHU / POP / LAN
Command: `FPXFR`

## Tab 08 Structure
- FP-CONV-STD-H-22/30/36/42/48
- FP-CONV-STD-ADJ / CAS
- FP-CONV-HNG-CLG
- FP-CONV-PAN-DRP-12..48
- FP-CONV-GD-FIX / HNG / ADJ
- FP-CONV-HOP
Command: `FPSTD` `FPDPAN`

## Tab 09 Sanitation + QC
- FP-CONV-SAN-CIP / SCR / LFT / CUT
- FP-CONV-QC-MD-12/18/24
- FP-CONV-QC-CW / XR / REJ / INS
Command: `FPMD`

## Tab 10 Annotation
- FP-CONV-ANNO-FLOW / TOB / HYG-L1..L5
- FP-CONV-ANNO-MAT-304 / 316
- FP-CONV-ANNO-ZONE / WASH / LOCK / ID / CLER
- FP-CONV-LGND-HYG
Command: `FPFLOW`

## Tool properties to set after Create Tool Palette
- Prompt for rotation: Yes
- Explode: No
- Scale: 1
- Layer: as listed in Standards/LAYERS.md
- Aux scale: none (blocks are 1:1 inches)
