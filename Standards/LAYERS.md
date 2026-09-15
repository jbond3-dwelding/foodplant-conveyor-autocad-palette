# Layer standard — Food Plant Conveyors

NCS-aligned. Discipline **Q** = Equipment. Major group **CONV** = conveying.

| Layer | Color | Linetype | Plot | Use |
|---|---|---|---|---|
| Q-CONV-BELT | 4 cyan | CONTINUOUS | 0.35 | Belt / carrying surface |
| Q-CONV-FRAM | 7 white | CONTINUOUS | 0.50 | Stainless frame |
| Q-CONV-SUPP | 8 grey | CONTINUOUS | 0.35 | H-stands, hangers, feet |
| Q-CONV-DRIV | 1 red | CONTINUOUS | 0.50 | Motor, gearbox, drum |
| Q-CONV-XFER | 6 magenta | CONTINUOUS | 0.35 | Transfers, chutes, rejects |
| Q-CONV-SANI | 3 green | HIDDEN2 | 0.25 | Drip pans, CIP, scrapers |
| Q-CONV-GUID | 2 yellow | CONTINUOUS | 0.18 | Side guides / UHMW |
| Q-CONV-CNTR | 2 yellow | CENTER2 | 0.18 | Belt centerline |
| Q-CONV-FLOW | 1 red | CONTINUOUS | 0.25 | Flow arrows |
| Q-CONV-ANNO | 7 white | CONTINUOUS | 0.25 | Tags, IDs, notes |
| Q-CONV-HIDD | 8 grey | HIDDEN2 | 0.18 | Return belt, hidden frame |
| Q-CONV-CLR | 8 grey | PHANTOM2 | 0.13 | 36 in wash aisle / service |
| Q-CONV-ZONE | 30 | CONTINUOUS | 0.13 | Hygiene zone hatch |
| Q-EQPM-INSP | 5 blue | CONTINUOUS | 0.50 | MD / checkweigher / X-ray |
| Defpoints | 7 | CONTINUOUS | off | Construction inside blocks |

Text style: **FP-ANNO** — romans.shx, height 0.125 in model (use annotative 1/8 in if preferred).
Dim style: decimal inches, 0.00, closed filled arrow.

Block attributes (every conveyor):
`TAG WIDTH LENGTH TOB MATL HYG BELT DRIVE FLOW ZONE NOTES`
