# T150 round 5: editor and confidentiality review of d84_merged.md

Persona: editor and confidentiality reviewer, sentence by sentence, annexes included. d84_merged.md has 1,592 lines and was read end to end. Confidentiality was checked against the financial plan (surewave/deliverables/2026-11-22_surewave_hrb_financial_plan_ker1.md, "FP"), docs/project_facts.md, D7.4 (public, with its cost model on Zenodo) and the EIC Transition and EUPI-PV budgets that SINTEF, Clement Germany and EDP know. Decisions D1–D65 and owner_questions.md are taken as given, and only errors inside them are reported. Line numbers refer to d84_merged.md.

## Mechanical and rendering checks

- `pandoc d84_merged.md -t html` returns rc 0 with no warnings. The 84 heading lines render as 1 h1, 19 h2, 56 h3 and 8 h4, in order, and every heading has a blank line before and after it. No "---" rules remain.
- The draft has 51 Markdown tables, and the HTML has 51 `<table>` elements. In both, every row has the same column count, and every separator row is valid and followed by data with no blank line.
- The rendered text has no literal `**`, `|`, `](` or `&lt;`. The nested list in the executive summary (l.23–26) renders as a nested `<ul>`. The source has no `**`.
- Every "Section x.y" and "Annex A.n" reference resolves to a heading. None of "precisely", "crucially", "clearly", "therefore", "thus", "which is why", "it follows", "well beyond" or "importantly" appears. "Already" appears once, as a fact (l.759, "capacity already installed"). "Very" appears only in the Booster expert's quoted ratings (l.143) and in D4.1's requirement (l.343).
- Named customers, sites and vendors were checked and none appears: Skien, Gunneklev, Storavatnet, Leipzig/Hainer, Gotland, Aaltvedt, Rixen, Magdeburg, Herøya, Enova, Lithuania, China, Swedish reference plant. No kit price, EPC price or cost per watt appears.
- Counts re-checked and correct:
  - first table: 16 targets, 11 met, 5 exceptions;
  - reach table: 22 rows, 3 / 1 / 3 / 5 / 7 / 1 / 2;
  - 27 results (3+6+1+3+6+2+6), 23 in KERs, 4 as impact;
  - A.4: 14 rows (4+4+3+2+1; 7+2+2+3);
  - A.5: 15 rows;
  - Zenodo: 18 records = 12 + 6, by registrant 6+4+2+2+2+1+1;
  - OpenAIRE: 13 deliverables;
  - 4.6: €9.75M / 10,375 kWp = €940/kWp; 1.22/9.75 ≈ 13 %; 212/940 < 25 %;
  - 4.10: −40 % and −31 %;
  - hinge: 37 × 1.08 ≈ 40 kN; 5 × 2.04 = 10.2 kN and 10.2/3.69 ≈ 2.8; 5 × 8.36 ≈ 42 kN; 10.2/33 < 1/3;
  - mooring ratio: 1/(1 − 0.56) to 1/(1 − 0.59) = 2.3–2.4;
  - NOK conversion at 11.7;
  - Wood Mackenzie: 4.4 GW over 10 years ≈ 0.44 GW, and 16 MWp ≈ 3.6 %;
  - D8.3's 170,000 t / 25 years ≈ 7,000 t a year;
  - EIC months 22 + 12 = 34;
  - 4.7 figures against FP l.40–44, 112–116, 427–432 and 446–480.

## Round-5 check against d84_merged_r3int.md (before the round-4 fixes and the de-duplication pass)

- I compared the two versions sentence by sentence and figure by figure (scripted: every number with a unit, DOI, deliverable, task, preprint and journal citation, and the person and partner names). The only figures removed are the share table of 4.6.2 (67/80 %, 30/46 %, 15/25 %, 6/11 %, 2/4 %) and the "45° sector … straight at 30 MWp" basis sentence. Both were removed on purpose under D60a. All other numbers, DOIs, preprints and journal citations are still present.
- The new qualitative statement in 4.6.2 (l.715) matches the removed table and FP l.318–327:
  - 50–300 kWp: "about as much as the PV plant to several times as much", against shares of 46–80 % without other uses;
  - about 5 MWp: "around a tenth", against 11 % (FP: €0.11 against €0.94 per watt);
  - a few tens of MWp: "a few per cent", against 2–4 %.
- Fewer mentions of some names and deliverables (Stadt 10→7, D6.3 28→22, Energies 19(7) 1609 13→10, Task 6.5 5→3, Task 7.1 4→2, FLOW-3D 3→2). I checked each against its home, and no credit is lost:
  - the Gijón Task 6.5 credit: 6.2 l.931 and 3.4 R3/R4;
  - FLOW-3D: 3.4 R2 and 6.3;
  - Stadt and DIFFRAC: 6.5 l.1026, 4.1 l.386 and l.412, Section 10 MariSol row;
  - D6.3 figures: 4.1 l.407–411;
  - Task 7.1: 6.4 l.989, 6.7 l.1080;
  - the MARIN/Ceit/Clement/Sunlit Sea co-authors of Energies 17(9): 6.5 l.1032 and A.1/A.23;
  - the Ceit market line was reworded, not lost (6.6 l.1049).
- I checked every pointer the de-duplication added against the statement it claims. All lead to the right statement:
  - 4.1.1 heavy row "unit mass in Section 6.3" → l.958;
  - 4.1.1 l.432 "Section 6.3 gives the transmission" → l.958;
  - 4.6.1 "breakwater share is in Section 4.6" → l.689;
  - 3.2 KER4 "Section 3.4, R5" → l.345;
  - 3.2 KER2 and 6.2 "Section 4.6.1" → l.699;
  - 6.1 "Section 2.5" → l.258–260;
  - 6.5 "(Section 10)" and "(Section 4.1)" → l.1197, l.412;
  - 4.6.2 "(Section 4.4.1)" → l.618;
  - 4.8 "largest single risk … (Section 4.7)" → l.768;
  - 4.1 l.410 "(Section 4.8)" → l.792;
  - 7.2 KER6 "(Section 7.4)" → l.1150;
  - 7.4 "proposed below" → l.1157;
  - 2.1 "Section 4.1, which also explains how hinge generations are numbered" → l.404.

## A. Major

None.

## B. Minor

1. Minor (consistency, stand-alone reading). In several places "after the project" means after the EIC Transition project, while everywhere else in D8.4 "the project" is SUREWAVE, which ends on 31 December 2026. In 4.6.2 the reading gives a wrong statement.
   - l.711: "The financial plan models it in 2031, the first full year after the project (Section 4.7)." The first full year after SUREWAVE is 2027. 2031 is the first full year after the EIC project (36 months, decision December 2026 – January 2027).
   - The same ambiguity appears in:
     - exec l.25: "targets the first commercial site with a breakwater class after the project, from about 2030";
     - 4.1 table l.421: "a first commercial site with a breakwater class after the project";
     - 4.6.2 l.711: "a first commercial installation of 1–5 MWp after the project";
     - 4.7 l.745 and l.754: "at the demonstrator site after the project";
     - Section 14 l.1299: "targeted after the project in the EIC Transition proposal";
     - Section 15 l.1307: "after the project, about 2030".
   - Source: EIC proposal (36 months; first commercial installation "immediately after completion" and "within 12–24 months after completion"), as quoted in l.711. The FP models the plant in 2031.
   - Fix l.711: "The EIC Transition proposal targets a first commercial installation of 1–5 MWp after the EIC Transition project: immediately after its completion in the proposal's summary, about 2030, and within 12–24 months after completion in its exploitation plan, subject to the site owner, permits and finance. The financial plan models it in 2031, the first full year after the EIC Transition project would end (Section 4.7)."
   - Fix elsewhere: replace "after the project" with "after the EIC Transition project" in l.25, l.421, l.745, l.754, l.1299 and l.1307.

2. Minor (confidentiality, a remaining route after D60a). D60a removed the geometry, unit mass and distances from the 4.6.2 basis. Section 4.1.1, to which 4.6.2 points for the classes, still gives the light-class unit mass ("about 30 t per 20 m unit", l.437; "A light unit of about 30 t", l.441), the medium unit ("about 73 t per 20 m unit", l.438), the stand-off ("15 m from the array", l.445) and the sector widening ("widened by 10° on each side", l.445). 4.6.2 l.715 says the breakwater is "around a tenth of the plant cost" at about 5 MWp, for "a light breakwater on the exposed side of a plant built by a kit buyer".
   - The route: Clement Germany (which knows the EIC lake's exposure) or any partner who assumes a sector could cost the light breakwater from D7.4's public cost model (material per tonne or per metre, pontoon installation). It could then read the kit-buyer plant cost as about nine times that figure. FP l.316–323 gives the real value as €0.83/W.
   - Without Sunlit Sea's markups (FP: fabrication, fittings, transport, supplier factor 1.25, mobilisation) and without a sector, the estimate is coarse, roughly ±40 %. The unit masses are the input that makes it tighter.
   - Fix (low cost, no loss of argument):
     - l.437: "About 2.5 m wide, 1 m draft";
     - l.438: "About 4 m wide, 1.5 m draft";
     - l.441: "The draft is measured to the bottom of the keels, so a unit weighs less than a solid block of the stated width and draft. A light unit can be cast, trucked and lifted with ordinary harbour equipment."
     - Keep the 15 m and the 10° widening, which describe the method, or drop "the distance in D7.4's cost model for its 2 MWp ring" if the owner wants to close the route further.
   - Owner question Q36/Q74 should name this as the last remaining input.

3. Minor (confidentiality). l.770: "Kit volume 30 % lower in 2030–2031, a kit price about 6–7 % lower, or a kit cost higher by the same amount per watt …".
   - The FP case behind it is a fixed step of €0.03/W on the 2030 and 2031 kit prices (FP l.452–453; 0.03/0.47 = 6.4 % and 0.03/0.45 = 6.7 %). A reader who guesses that the sensitivity step is a round amount per watt gets the kit price back from the percentage: €0.03 / 6.5 % ≈ €0.46/W. That is the price D8.4 withholds (FP l.130–132).
   - "By the same amount per watt" tells the reader that the step was set in euro per watt.
   - Fix: "Kit volume 30 % lower in 2030–2031, a kit price a few per cent lower, or a kit cost higher by the same amount, each lowers 2031 EBITDA, which stays positive in every case; cash stays positive."

4. Minor (self-contradiction, A.23 l.1546).
   - The text says: "The partners deposit these five in the SUREWAVE community on Zenodo before this plan is submitted, so they are deposited after publication." The next sentence makes the fifth (MARINE 2025) conditional: "MARIN deposits the accepted manuscript under CC BY if its publishing agreement with CIMNE allows it; otherwise the paper stays open under CC BY-NC-SA 3.0". Owner action 1 also says MARIN is only "asked".
   - Fix: "The partners deposit the four papers published under CC BY 4.0 in the SUREWAVE community on Zenodo before this plan is submitted, so they are deposited after publication. For the MARINE 2025 paper, whose published licence excludes commercial use, MARIN deposits the accepted manuscript under CC BY if its publishing agreement with CIMNE allows it; otherwise …" (rest unchanged).
   - 2.5 l.256 can stay as it is.

5. Minor (requirement 1, exec l.13). "This plan uses TRL 4–5 for the integrated system and for Sunlit Sea's CONNECT platform:" is followed only by the evidence for the integrated system (D7.2 TRL 5, EIC TRL 4). The source for CONNECT's TRL 4–5 is Sunlit Sea's own rating in its Booster business plan (4.1 l.397; 3.4 l.353), and the summary does not give it.
   - Fix: after "… starts from TRL 4 (Section 4.1)", add "; Sunlit Sea rates CONNECT at TRL 4–5 in its Horizon Results Booster business plan (Section 4.1)". Alternatively, split the sentence: "This plan uses TRL 4–5 for the integrated system: … starts from TRL 4. Sunlit Sea rates its CONNECT platform at TRL 4–5 (Section 4.1)."

## C. Wording

6. Wording. l.141: "In the November outputs the first market became sheltered coastal sites, and the product the CONNECT platform (Generation 2) described in Section 4.1." Fix: "… and the product became the CONNECT platform (Generation 2) described in Section 4.1."

7. Wording. l.726: "… and delivers the other two, both multi-megawatt plants (Section 4.4), as EPC contractor to the hosts' plant companies: the first in 2028, the second in 2030–2031." Here "the first" can be read as the first reference plant, which is delivered in 2027. Fix: "… : one in 2028 and the other in 2030–2031."

8. Wording. A.8 l.1409: "Joint webinar with NaturSea-PV, coordinated by Tecnalia, 2 February 2026, co-hosted by NaturSea-PV, …" reads as if Tecnalia coordinated the webinar, and it names NaturSea-PV twice. Fix: "Joint webinar of SUREWAVE and NaturSea-PV (the EU project coordinated by Tecnalia), 2 February 2026, co-hosted by the two projects, with speakers from …"

9. Wording (requirement 7, define at first use). "doi" is used at l.225 ("doi 10.3390/s25196234") before the definition "digital object identifier (DOI)" at l.231. Fix: at l.225 write "(digital object identifier, doi 10.3390/s25196234)", and at l.231 shorten to "with a DOI".

10. Wording (repetition). l.754: "The EIC and EU-upside cases also include the first commercial plant at the demonstrator site after the project." This repeats the EIC bullet at l.745 ("and a first commercial plant from the kit at the demonstrator site after the project"). Fix: delete the l.754 sentence, keeping "Grant income is not counted as revenue."

11. Wording (one home, D54). The statement that the first breakwater-class sites are lakes or inner waters exposed to wind waves appears six times: exec l.25, 4.3 l.478, 4.4 l.557, 4.6.2 l.709, the 4.8 breakwater-cost row l.796 and Section 15 l.1307. Home: 4.6.2. Fix: l.478 "For the breakwater classes, the first sites are lakes (Section 4.6.2)."; l.557 "None of the three needs a breakwater class on current site data (first sites with a class: Section 4.6.2)." Keep exec and Section 15 as the summary mentions.

12. Wording (D63 phrase). The identical KER1 clause "developed in the parallel project SuRE on the results of the Generation 1 aluminium-float SUREWAVE array" (l.301, l.341, l.907, l.1117) stacks four modifiers before "array", which a non-native reader parses with difficulty. The fix keeps the same wording in all four places, as D63 asks: "developed in the parallel project SuRE on the results of the SUREWAVE array, which used Sunlit Sea's Generation 1 aluminium floats".

13. Wording (r4 #23, still partly open). These paragraphs and table rows are over 1,500 characters:
    - l.32 (1,517). Split after "(Section 4.7)." and after "(Section 4.8).".
    - l.341, R1 row (1,944). Move the evidence cell's last sentence ("The campaigns and the hinge record are in Section 4.1, MARIN's validation of DIFFRAC in Section 6.5") to the text below the table, or cut it, since both pointers are in 4.1.
    - l.343, R3 row (1,697). Cut "The LWAC used in the prototype is set out in Section 3.1, step 4." Its pointer is already given in the KER2 row.
    - l.1157 (1,529). Split after "(Section 3.1, step 4)." and after "joint-ownership arrangement."

## D. Earlier rejections in my area: does each rejection hold?

- r4disp, r4_writing 5 (Generation 1 named before Q28): holds. D63 and Sunlit Sea's input (l.37) give the Generation 1 float, and Q28 is now only the patent question.
- r4disp, r4_writing 15 (D8.3 revised version in the portal): holds as owner action 5. A.20 and Annex B describe the facts without a placeholder.
- r3disp_C, r3_writing 4 (site-type column in 4.4): holds as owner question Q75. The table still reads "Port / Industrial basin / Lake" (l.553–555).
- r3disp_C, r3_writing 5 (EIC lake, dual use): holds as Q36/Q74. The price figure is gone (l.719, "well above the average award"). See item 2 for the last input.
- r3disp_C, r3_writing 30, 31: hold.
- r2disp_D, r2_writing 2, 3, 7; r2disp_A, r2_cold 6; r2disp_E, r2_cold 5: hold.
- r1disp_A, r1_cold 59 (glossary): holds, apart from item 9 (DOI).
- r1disp_D, r1_writing 3, 6; disp_D writing 22, 24, 25: hold.

## E. Earlier findings in my area still not fixed

- r4 #1–3 (major): fixed. The share table and its basis are gone, 4.6.2 is qualitative, the EIC and EU-upside rows and the €0.7M/€0.9M deltas are removed, and no plant size is linked to the EIC scenario (l.745, 754, 758). One input remains in 4.1.1 (item 2).
- r4 #4 (Q68, two margin lines): the text is unchanged pending the owner (l.731 "41–44 %", l.765 "40–50 %"). Q68 now names both lines, so it is not reported again.
- r4 #6–11, #13, #14, #16–22: fixed.
- r4 #12 (second campaign repeated): fixed by the de-duplication pass. The campaign is in full at l.409 only, with pointers at l.903 and l.1032.
- r4 #23 (long paragraphs): partly fixed (item 13).

Findings: 0 major, 5 minor, 8 wording.
