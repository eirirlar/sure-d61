# D8.4 round-1 integration log (2026-11-23)

Input: d84_merged.md (concatenation of r1part1–8), r1disp_A–E cross-part lists, decisions D1–D34 with the round-1 revisions. Backups before editing: d84_merged_pre_r1int.md, erreport_pre_r1int.md, kpi_pre_r1int.md, bp_pre_r1int.md. Edit script: r1_integrate.py (edits E01–E30), plus the follow-up edits F1–F6 below. Line endings kept (CRLF for d84_merged.md, the KPI record and the business plan; LF for the exploitable results report and the financial section). Nothing in C:\dev\src\sure-d61 was edited; no git.

## 1. Cross-part items

Applied by the fix agents already (checked in the merged draft, no change needed): r1disp_A 1, 2, 3 (Lean Canvas in 4.4, value chain in 4.4.1), 4, 5, 6, 7, 9, 10, 11, 12; r1disp_B 2, 3, 4 (Section 13), 5, 7; r1disp_C 1, 2, 3, 6, 8, 9, 11, 12, 15 (no "350 kWp" or "3.2 MWp" left); r1disp_D 1, 2 (Section 12 has no first use), 4, 8, 9, 10, 11, 12, 13; r1disp_E 1, 3, 4, 5, 6, 7, 10, 11.

Applied in this integration:

| Item | Change |
|---|---|
| r1disp_B 1 | Not applied: the executive summary already uses r1disp_A 2 wording, which matches D10r and Section 2.5; the two versions say the same |
| r1disp_B 6, r1disp_C 6 | Not applicable without the owner's answer (owner question 39) |
| r1disp_C 4 | 4.8 durability row: "control of the casting process (see the prototype 4 row)" added (E19); shortened to avoid repeating the D6.3 shrinkage detail of the prototype 4 row |
| r1disp_C 5 | 4.8 key-person row: "IFE for structural simulation" (E18) |
| r1disp_C 7 | 2.5.20: "D8.3 uses the 7 MWp plant of D3.4 and the D7.4 version 1.0 economics; Section 4.1 gives the basis this plan uses." The old sentence also listed the readiness level, which 4.1 says is the same in both (E06) |
| r1disp_C 10, r1disp_D 5 | 4.9 2030 bullet shortened to a pointer to 4.6.2, which holds the full EIC wording (E22); Section 14 2030 row points to 4.6.2 (E29) |
| r1disp_C 13, r1disp_D 2 | 4.4.1, first use: "the extension of Sunlit Sea's scope in SuRE (CINEA decision pending)" (E14) |
| r1disp_D 3 | Section 14 2027 row: "business plan adopted by the board (M2)" (E28) |
| r1disp_D 7, r1disp_E 2, r1disp_A 8 (D33) | Mooring per site and farm size, verified in D5.1 Table 9 (10 MWp: Mediterranean −34 %, North Sea −42 %, Baltic ×3.16; 2 MWp: −56 %, −59 %, ×2.05). Full figures in 6.5 (MARIN's pathway) and 3.2 KER5 (E26, E08); 3.1 conflict bullet, 3.4 R6 and 4.10 CAPEX row give 34–59 % and 2–3 times heavier with a pointer to 6.5 (E07, E11, E23). "Factor 2–3 reduction" removed everywhere (D3); MARIN's figure is now described as "a larger reduction in mooring chains than D5.1 gives" |
| r1disp_E 8 | 4.3.1 last sentence: pointer to Section 6; the sentence "They were not tested in the project; each owner tests them in its own market" stays only in the Section 6 introduction, to remove the duplicate (E13) |
| r1disp_E 9 | 4.9 2027: "test-service agreements with both sought" (E20); journal article "is submitted", matching the Section 13 target (E21). 4.7 already says "second business-planning workshop" |
| r1disp_E 12 | Reach table, 300 social actors row: "the communication after the project is set out in Section 6.9" (E05) |
| r1disp_E 13 | 3.4 R1 evidence: "(D6.2 and D8.3; the first also in Energies 17(9) 2059 ...; results of the second also used in D5.7)" (E09). D5.7 uses the second campaign's slamming results; D8.3 describes both campaigns; D6.2 is not in the repo (owner question 23) |
| r1disp_A 13 | Annex of cited deliverables not added (optional; owner question 40) |

## 2. End-to-end consistency pass

| Id | Section | Change | Reason |
|---|---|---|---|
| E01, E02, E03 | 2.4/2.5, 3, 4, 6, 10, 12, 4.6.2/4.7 | Blank line added before headings that followed text or "---" directly (7 places) | Markdown renders "---" followed by a heading as a setext heading; headings need a blank line |
| E04 | 2.5 own share | "it wrote the dissemination, exploitation and communication master plan D8.1 and its update D8.5" | GA deliverable table: D8.1 lead beneficiary Sunlit Sea; 6.1 already said so |
| E09 | 3.4 R1 | Hinge evidence shortened to a pointer to 4.1 | Duplicate of the full hinge record in 4.1 (D4r wording kept there) |
| E10 | 3.4 R3 | D34 wording exactly: "D4.1's mix uses 400 kg/m³ of cement instead of 500, with fly ash and slag (ACCIONA); the proposal's target was 350 kg/m³" | D34 |
| E12 | 4.1.1 | Breakwater cost per kWp (€117, €58, €550) replaced by a qualitative statement ("close to ten times the value at 10 MWp") | D21: with the 4.6.2 shares, the euro figures let a reader back out the plant cost per watt; owner question 35 |
| E15 | 4.6.1 supply row | ACCIONA mixes: "lighter or thinner sections" in place of "a thinner shell" | D24 wording |
| E16, E17 | 2.3, 4.7 | 4.7 no longer repeats "the definitive business plan" (2.3 states it for Section 4); the review and update of the plan stand in 4.7 only, 2.3 points to it | Duplication |
| E24 | 4.10 partner-results row | Shortened; points to 3.4 for UHPFRC, ReFRESCO and SHMS detail | Duplication with 3.4 R3–R10 |
| E25 | 6.1 Generation 2 result | Hinge figures and the D1.8/Ceit sentence replaced by pointers to 4.1 (hinge record) and 3.1 (redesign inputs) | Duplication; D4 (Ceit not named in hinge statements outside the 3.1 source-conflict note) |
| E27 | 13 | "final periodic report" in place of "final report" | Avoids reading as the final technical report (D22) |
| E30 | 4.1 | "the 10 MWp layout of Clement Germany's material quantities" | D31: say once why the plan's basis differs from D8.3 |
| F1 | 4.6, 4.10 | "(D7.4, Section 2.5)" → "(section 2.5 of D7.4)"; same for 7.4 | Section references must point to D8.4 sections; these pointed to D7.4's own sections |
| F2 | 4.4 Lean Canvas | "design break load of the full-width hinge 37 kN, against 14 kN for the earlier corner hinge, D7.6" | D4r: like for like, not "from 14 to 37" |
| F3 | 4.7 | "Most floating PV in Europe is on man-made inland water (Section 4.3)" in place of "Most of that forecast is calm inland water" | The Wood Mackenzie report as cited gives no split; IEA PVPS Task 13 (4.3) supports the new wording |
| F4 | 4.1 maturity, executive summary | Gijón dates (September 2025 – June 2026) removed; "about nine months"; results "reported in November 2026 (Preprints 202611.1592), after D7.6, and are not part of D7.6's assessment" | No citable source in the repo for the dates (D8.3 does not give them; D22); D2r evidence order; owner question 19 |

Checks run after all edits (script): every "Section x.y" reference exists as a heading; no "**"; every table has a constant column count and no blank line after the separator row; no "factor 2–3", "milder", "therefore", "thus", "which is why", "it follows", "passed on at cost", "first breakwater site", "final technical report", "planning platform"; KER names match Section 3.2 everywhere. Checked and left as they are: TRL wording (D2r) in the executive summary, 3.2, 3.3, 3.4, 4.1, 4.10, 15; hinge figures (D4r) in 4.1, 4.8, 3.2 KER4; HPC wording in 3.1, 3.2, 6.2; SHMS inputs (D13r) in 3.1 and 6.6; Clement credit (D29) in the executive summary, 3.1, 3.2, 4.1, 5, 6.1, 15; access rights Q1 2027 and the Horizon Results Platform rule (D23) in 4.5, 4.8, 4.9, 5, 6.8, 9, 11, 12, 13, 14; KPI headline and exceptions (D10r) in the executive summary and 2.5; project names and relations (D14) in the executive summary, 3.1, 6.4, 10, 15; equity, volume and break-even figures identical in the executive summary, 3.3, 4.7, 4.10 and 15.

## 3. Companions

| File | Change |
|---|---|
| companions\2026-11-22_surewave_d8.4_ker1_financial_section.md | Body below the YAML header replaced by D8.4 Section 4.7 exactly (verified identical by script after the last edit F3) |
| companions\2026-09-30_surewave_exploitable_results_report.md | Template sequence (D27); "site-planning tool" (3 places); KER1: Clement Germany components (D29) and D2r TRL wording; LWAC conflict as in D8.4 3.1; HPC per D34, without the final technical report figure (D22); ACCIONA licence route per D8.4 Section 5 and value per D24, with D7.3's no-saving finding; SINTEF reuse per D13/D14 (finite element methods being reused, hydrodynamics planned); mooring per site (D33); Ceit sensor status (D13); SHMS inputs (D13r); sources dated November 2025 to October 2026 |
| companions\2026-11-19_surewave_wp8_kpi_verification.md | Reporting-period line per D10r (second period to project end; "after RP2" means after 30 September 2026); summary statuses for publications (Not met for the GA), videos and press releases (Partly met), conference workshops (Met for D8.5, not for the GA); row 24 and §1 note on the submitted manuscripts as in D8.4 2.5.3; "Not met" line replaced by the D10r exceptions and a pointer to the reach table; counting rules extended with the ACCIONA announcement, the CINEA and own-event rules, the written-counts rule and the own-record items |
| companions\2026-11-14_surewave_hrb_business_plan_ker1.md | Hinge claim per D4r (37 kN full-width third generation against 14 kN second-generation corner hinge, not fully validated); "site-planning tool" (4 places) |
| companions\2026-11-22_surewave_hrb_financial_plan_ker1.md | No change: no conflict found with the new draft (figures, scenarios, downside cases and breakwater wording match 4.7; the round-0 corrections are in place) |
| companions\project_facts.md | No change (already holds SFI BLUES and FlexiShape) |

## 4. Owner questions

owner_questions.md: 41 numbered questions, deduplicated from r1disp_A–E (45 items) and disp_A–E, plus two from this integration (Q35 breakwater cost per kWp, Q36 €0.10/kWh). Q14 (lead of D8.1) is answered from the Grant Agreement.

## 5. Not done

- No .docx or PDF generated.
- docs/project_facts.md in the repo not edited (owner question 41).
- Annex of cited deliverables not added (owner question 40).
