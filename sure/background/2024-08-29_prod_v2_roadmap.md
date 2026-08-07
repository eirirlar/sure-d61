# Prod v2 Roadmap — Sunlit Sea

_Sunlit Sea AS. Prosjekttittel: «Product B development». Prosjektleder: Eirik Larsen. Datert 29.08.2024._

_Konvertert fra `Prod v2 roadmap (1).xlsx` med openpyxl. Regnearket har 27 ark; de mest tekst-tunge arkene er konvertert til Markdown-tabeller under. Gantt-oriented ark (`Roadmap`, `Roadmap_old`) og fritekst-orienterte design-ark (`Design`, `Design considerations`, `Design Per/Guillaume/Eirik`, `Tasks`) er best lest fra XLSX-fila direkte._

Ark i regnearket: Summary, Function - criteria - Solution, Roadmap, Design, Design considerations, Design Per, Design Guillaume, Design - Eirik, Tasks, FP1, FP2, FC1, FC2, FC3, FC4, FC5, FC6, FC7, FC8, FC9, FC10, FC11, FC12, FS1, FS2, FS3, Roadmap_old

## Summary

| Feature | Priority | Status | Owner | Time period | Notes |
| --- | --- | --- | --- | --- | --- |
| FP1: Produces power | Prio 3 | Not started |  |  |  |
| FP2: is certified | Prio 2 | Not started |  |  |  |
| FC1: Floats on water | Prio 1 | Not started |  |  |  |
| FC2: Is water tight | Prio 2 | Not started |  |  |  |
| FC3: Mechanically attached | Prio 1 | Not started |  |  |  |
| FC4: Does not go submarining under stream exposure, 3 m/s | Prio 3 | Not started |  |  |  |
| FC5: Feasible to change panel type, i.e from Chinese to US | Prio 2 | Not started |  |  |  |
| FC6: Resists high wind | Prio 3 | Not started |  |  |  |
| FC7: Resists waves up to 1.5 Hs | Prio 3 | Not started |  |  |  |
| FC8: Cheap to produce, cheaper total cost to install than competitors | Prio 1 | Not started |  |  |  |
| FC9: Grounding of the FPV unit | Prio 2 | Not started |  |  |  |
| FS1: Can walk on it | Prio 2 | Not started |  |  |  |
| FS2: Fast to produce, not necessarily mass producible | Prio 2 | Not started |  |  |  |
| FS3: Fast to install | Prio 3 | Not started |  |  |  |

## FP1

| Function | Criteria | HOW |
| --- | --- | --- |
| Produces power | Performance ratio (how much kWh per kWp), power density (kWp/sqm), soiling degree, cooling effect | Sourcing a high kW output PV panel |
|  |  | Sourcing a glass/glass PV panel for easy cleaning |
|  |  | Sourcing a PV panel with high quality level |
|  |  | Decide of an angle towards the sun |

## FP2

| Function | Criteria | How  |
| --- | --- | --- |
| Certiication | Certification not broken by modification/assembly | Clear out with supplier what is posible to touch before breaking certification |
|  |  | Supply a PV panel that is certified |
|  |  | Investagate the certification specification (IEC, and UL) to see if there are voiding conditions |

## FC1

| Function | Criteria | How |
| --- | --- | --- |
| Floats on water | Sufficient Buoyancy of the float / panel / hinges | Single unit buoyancy |
|  |  | Float |
|  |  | floating hinge  |
|  |  | Using the PV+frame as a float  |
|  |  | 1 hydroformed trofe, 2 HF trofes, with different infils,  |
|  |  | Multiple unit buoyancy |
|  |  | Strucutral integraity of the assembled matrix |
|  |  | Saussage on the matrix edge |

## FC2

| Function | Criteria | How |
| --- | --- | --- |
| Is water tight | Float must be water tight. minimize the degradation ratio and fault probability PV & electronics must be protected | Marine PU foam inside the float it self |
|  |  | Heighten the PV above the water line |
|  |  | Protect the backside of the PV and the junction box with Foam |
|  |  | Extra protecting box with PM  |
|  |  | Enhance the protection of the PV edge |
|  |  | Protect the Cables going in and out of the float |
|  |  | MC4 connectors must be protected |

## FC3

| Function | Criteria | How  |  |
| --- | --- | --- | --- |
| Is mechanically attached | Tensile strength, shear strength, compression strength, fatigue strength safety value pass. | Sketch |  |
|  |  | 3D design |  |
|  |  | LS dyna simu |  |
|  |  | optimze parameters |  |
|  |  | Model scale test |  |
|  |  | Fatigue |  |
|  |  | Tensile str | Lab testing by SINTEF |
|  |  | Shear str |  |
|  |  | compression str |  |
|  |  | Full scale prototype testing |  |
|  |  | Source a new hinge |  |

## FC4

| Function | Criteria | How |
| --- | --- | --- |
| Submarining | resist 3m/s stream | Design a stream breaking bow potentially buoyant |
|  |  | Simulate " |
|  |  | Parameter optimization |
|  |  | Scale model test |
|  |  | Source a product out of the shelve |

## FC5

| Function | Criteria | How  |
| --- | --- | --- |
| Interchangeability | Keep design open to different standard size | Every 3D design should be done with regards to standard size |
|  |  | Assess the PV on the market (EU, CN and US) |
|  |  | Find a common denominator to work with |

## FC6

| Function | Criteria | How / Sub fonction |
| --- | --- | --- |
| Resists high wind | profile low and no wind traps | Avoid lift |
|  |  | Safety factor for wind induced load |
|  |  | CFD wind software |

## FC7

| Function | Criteria | How |
| --- | --- | --- |
| Resists waves | linked to the hinges and the strucutral integrity of the float | Work with MARIN (From Surewave) to evaluate the new loads on a matrix of different sizes |
|  | safety factor for the hinge performances | Apply those loads to a simulation and check that our hinge system validates the safety factor |
|  | Resist wave up to 1.5 Hs | Possibly an external consultancy |

## FC8

| Function | Criteria | How  |
| --- | --- | --- |
| Cost efficiency | As cheap or cheaper than competitors CAPEX wise (now 250€/kWp) | Cheap PV compared to kWp output |
|  |  | Cheap float |
|  |  | Simplest assembly  |
|  |  | Number of components should be low |
|  |  | Number of assembly steps should be low |
|  |  | Cost of extra component should be low |
|  |  | Keep frakt lowest |
|  |  | Cheap infrastructure for prod |

## FC9

| Function | Criteria | How |
| --- | --- | --- |
| Grounding system | Must resist corrosion and constant movement (fatigue) | develop and reinforce the mainnheim system |
|  |  | Attachment  |
|  |  | Guide over the FPV |

## FC10

| Function  | Criteria | How |
| --- | --- | --- |
| PV attachment | Ease of operation | Investigate glue |
|  | Infrastrucutre costs | Investigate weld |
|  | Components costs | Investigate roller hemming/seaming |
|  | Durability | Investigate clinching |
|  | water protection | Investigate bolting |

## FC11

| Function | Criteria | How |
| --- | --- | --- |
| Mooring | System must remain in place safely | Design a mooring system for stream water |
|  |  | Design a mooring system for nearshore/offshore water |
|  |  | Design a mooring system for still water |

## FC12

| Function | Criteria | How |
| --- | --- | --- |
| Internal pressure control | No overpressure  | Exhaust hole in float |
|  | No cavity | QA on production |

## FS1

| Function | Criteria | How |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Can walk on it | Avoid microcrack when walking on it and float matrix must be stable | Chose a glass/glass PV |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Ensure the PV is supported on its backside |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Study/test the buoyancy balance of a float |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

## FS2

| Function | Criteria | How / Sub fonction |
| --- | --- | --- |
| Manufacturability | Must be possible to assemble in Askim | Processes compatible with mass production |
|  | should be exportable to the US. Objective: 90 to 900 floats per weeks for 2 people | Processes compatible with organic production |

## FS3

| Function | Criteria | How |
| --- | --- | --- |
| Fast to install | Plug and play electrically,   | Use standard connectors |
|  | Objective: 20 kW installed per Man/hour, | Ensure ease of handling |
|  | Light FPV carried by 2 ppl | Ensure personnel safety |
|  | No tools | Ensure equipment safety |

## Function - criteria - Solution

| Column 1 | Names | Functions | Prio | Criteria | Solutions | Comment |
| --- | --- | --- | --- | --- | --- | --- |
| FP1 | Power production | Produces power | 3.0 | Performance ratio (how much kWh per kWp), power density (kWp/sqm), soiling degree, cooling effect | PV panel |  |
| FP2 | Certification | is certified | 2.0 | Certification not broken by modification/assembly | Supplied certified | Check certification void conditions |
| FC1 | Buoyancy | Floats on water | 1.0 | Sufficient Buoyancy of the float / panel / hinges |  |  |
| FC2 | Water protection | Is water tight | 2.0 | Float must be water tight. minimize the degradation ratio and fault probability PV & electronics must be protected |  |  |
| FC3 | Mechnical performance | Mechanically attached | 1.0 | Tensile strength, shear strength, compression strength, fatigue strength safety value pass. is about the interconnection between floats |  |  |
| FC4 | Submarining | Does not go submarining under stream exposure, 3 m/s | 3.0 | resist 3m/s stream | Outsource the study |  |
| FC5 | Interchageability | Feasible to change panel type, i.e from Chinese to US | 2.0 | Keep design open to different standard size |  |  |
| FC6 | Wind resistance | Resists high wind | 3.0 | we keep the profile low and no wind traps |  |  |
| FC7 | Wave resistance | Resists waves up to 1.5 Hs | 3.0 | linked to the hinges and the strucutral integrity of the float |  | Long term goal |
| FC8 | Cost efficiency | Cheap to produce, cheaper total cost to install than competitors | 1.0 | As cheap or cheaper than competitors CAPEX wise (now 250€/kWp) |  |  |
| FC9 | Grounding system | Grounding of the FPV unit | 2.0 | maintainable grouding system of the floating matrix |  |  |
| FC10 | PV attachment | The PV needs to stick to the float | 1.0 | Must remained attached to the float, must allow for hinge to be attached to the FPV |  |  |
| FC11 | Mooring  | Should be moored safely | 3.0 |  |  |  |
| FC12 | Internal pressure control | Internal pressure control | 3.0 |  No buldging, continious bonding of components |  |  |
| FS1 | Walkability | Can walk on it | 2.0 | Avoid microcrack when walking on it and float matrix must be stable |  |  |
| FS2 | Manufacturability | Fast to produce, not necessarily mass producible | 2.0 | Must be possible to assemble in Askim and should be exportable to the US. Objective: 90 to 900 floats per weeks for 2 people |  |  |
| FS3 | Deployability | Fast to install | 3.0 | plug and play electrically, objective: 20 kW installed per Man/hour, light FPV carried by 2 ppl, no tools |  |  |

---

## Ark ikke konvertert til Markdown

Følgende ark er best lest fra XLSX-fila direkte:

- `Roadmap` og `Roadmap_old` — Gantt-strukturert timeline med x-avmerking per uke, egner seg ikke godt som Markdown-tabell.
- `Design`, `Design considerations`, `Design Per`, `Design Guillaume`, `Design - Eirik` — fritekst-orienterte design-notater med varierende struktur.
- `Tasks` — lang liste med enkelt-oppgaver.