# T150 condensation brief: D8.4 from about 200 to at most 60 pages

Start a fresh session with: "Read surewave/deliverables/2026-11-24_d8.4_t150_work/2026-11-24_condensation_brief.md and do it."

## Status of the documents (read first)

- The full version (about 51,000 words, about 200 pages in the docx) is the verified master: `surewave/deliverables/2026-09-28_surewave_d8.4_exploitation_pathways_business_plan.md` as of 2026-11-24. Before condensing, copy it to this folder as `d84_master_200p_2026-11-24.md`. From then on it is a frozen reference: it is not maintained.
- The condensed version (at most 60 pages) replaces the D8.4 file in `surewave/deliverables/` and becomes the only live D8.4.
- Eirik gives his feedback only on the condensed version, after it lands. His feedback is applied to the condensed version only and is never back-ported to the 200-page master. If a fact changes in his feedback, update `docs/project_facts.md` and the companion files, not the master.
- The master stays useful as the evidence base: when the condensed text needs a source, a figure or a fuller statement, take it from the master (already verified), not from fresh research.

## Target

At most 60 pages in the SUREWAVE docx (about 15,000 words including tables). Check the page count of the built docx (`scripts/md_to_surewave_docx_from_delivered.py`, then count pages, e.g. by converting a copy to PDF only if Eirik asks for LibreOffice; otherwise estimate from words and tables at about 250 words per page).

Page budget:

| Part | Pages |
|---|---|
| Cover, front matter, executive summary | 5 |
| 1–2 Purpose, method, partner input; 2.5 KPI table with status and the exceptions only | 4 |
| 3 KERs: identification (3.1, short), KER table (3.2), depth of treatment (3.3), proposal-to-result table (3.4, one line per result) | 7 |
| 4 KER1 business plan | 22 |
| 5 Roles, agreements, fair price | 3 |
| 6 Partner pathways, about one page each | 8 |
| 7–11 IP (incl. 7.4 remaining IPR actions), standards, agreements, projects, Horizon Europe support | 6 |
| 12–15 Risks, obligations, timeline, conclusions | 4 |
| Annex B, deliverables cited | 1–2 |

Annex A (the item-by-item dissemination record) leaves D8.4. Its content is already in the KPI record (`surewave/background/2026-11-19_surewave_wp8_kpi_verification.md`), which feeds the final technical report. D8.4 keeps the KPI table with status, the reach-target summary, the open-access status and one paragraph on how the reach serves exploitation. D8.4 must stand alone, so do not refer the reader to the KPI record.

## What must survive the cut

The decisions in `decisions.md` (D1–D72) stay in force. The statements that went wrong before and must be checked explicitly in the condensed text:

1. TRL: integrated concept TRL 5 from SINTEF's D7.2 (summarised in D7.6); the EIC proposal sets TRL 4 as its starting point; the plan uses TRL 4–5; proposal target TRL 4–5.
2. Hinge figures like for like (D4r): 3.69 kN complete first-generation hinges; 8.36 kN a one-fifth segment of the full-edge connection with a steel rod; 37 kN the design ULS of the third generation (D7.2); North Sea loads still above; full-edge hinge tested only as a SINTEF segment.
3. Basin tests: a 1:10 3 × 5 array behind one breakwater section; the ring only simulated; second campaign with paired second-generation connectors.
4. Stadt Towing Tank tests were outside SUREWAVE; MARIN validated DIFFRAC motions against them.
5. SUREWAVE array used the Generation 1 aluminium float; Sunlit Sea started the Generation 2 redesign in SUREWAVE and continues it in SuRE (parallel project).
6. D7.4 reference plant: 10 MWp layout, 10,375 kWp installed, €9.75M, €940/kWp; "the D7.4 reference plant" vs "the Norwegian reference plants".
7. Mooring: D5.1 reductions per site; fairlead tensions rise in three of six optimised designs; no "anchor loads".
8. Project: 51 months after extensions of 12 and 3 months, end 31 December 2026; D8.4 due 30 September 2026 (month 48); coordinator "SINTEF".
9. Partner credit by deliverable and work package (Clement WP3 lead and breakwater, mooring and anchoring design; ACCIONA D4.x and the Gijón prototype; Ceit WP5; IFEU WP7 and D7.1; SINTEF D7.2 and tests; MARIN D5.1); Sunlit Sea's own technical work (WP2, D3.1, D3.4, D7.4).
10. Confidentiality: no Sunlit Sea price or cost per watt, named customer, named site or host, and no combination of figures from which a price or cost per watt can be derived (volumes with euro revenue, EBITDA or sensitivity effects; breakwater geometry, unit masses or shares with D7.4 costs; EIC or EUPI-PV plant sizes with euro effects).
11. No statement that anyone agreed, approved or decided something without a source; the Q1 2027 confirmation of contributions is Sunlit Sea's request and the WP8 lead's proposal.
12. No citations of the final technical report; KPI headline with the exceptions stated; five of seven peer-reviewed papers deposited late, one meets the deposit-at-publication rule.

Writing rules: CLAUDE.md "Language and tone" (no bold in body, no emphasis-by-assertion, no "therefore/thus/which is why", positive claim first, plain sentences, abbreviations defined at first use, tables with constant column counts, no "---" rules, blank lines around headings).

## Process — aim for speed (Eirik is short of time; target about 40 minutes)

Work for speed: start at once, ask nothing during the work, run steps in parallel, and keep checks focused. The content is already verified, so this is editing, not research: take every fact from the master and do not re-check sources unless the condensed wording changes a meaning.

1. Copy the master (above) and split it into the five section groups of the page budget (front matter to 2; 3; 4; 5–6; 7–15 and Annex B). Drop Annex A.
2. Five Opus agents in parallel, one per group, all launched in the same message. Each condenses its group to its page budget from the master only, keeps every decision and the twelve checks, and checks its own text against the twelve checks and the confidentiality rule before returning. Tell each to prefer cutting whole subsections, table rows and repetition over rewording sentence by sentence, and to return a short log of what it cut.
3. Merge; renumber and fix cross-references (script check that every "Section x.y" exists); pandoc to HTML (no error, no "<p>|", no "**").
4. One focused Opus check of the merged text: the twelve checks, confidentiality, and meaning against the master for the passages that were rewritten (not those only cut). Fix what it finds directly.
5. Install the condensed D8.4, build the docx, estimate the page count (words and tables), check no shell text is left; update T150 and hand over: page count, what moved out, the open owner questions, and that Eirik's feedback round comes next.

Estimated cost: about 0.5–0.7 million tokens; about 40 minutes if the parallel steps run smoothly.
