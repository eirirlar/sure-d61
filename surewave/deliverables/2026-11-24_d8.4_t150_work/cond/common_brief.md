# Common brief for the five condensation agents (T150, D8.4 to at most 60 pages)

Folder: C:\dev\src\sure-d61\surewave\deliverables\2026-11-24_d8.4_t150_work\ (call it W).

Read first: W\2026-11-24_condensation_brief.md (the task), W\decisions.md (D1–D72, all stay in force; later rounds win over earlier ones), then your input group file W\cond\gN_in.md. The master (verified, about 51,000 words) is W\d84_master_200p_2026-11-24.md; use it only if your group needs context from another section. Do not do fresh research: the content is verified. Take every fact from the master.

Your job: condense your group to its word budget (words counted with `wc -w`, tables included). Write the result to W\cond\gN_out.md and a short log (what you cut, merged or moved; any subsection removed or renumbered; any cross-reference you could not resolve) to W\cond\gN_log.md. Write only those two files, at those absolute paths (not inside any worktree). Do not touch any other file. Do not run git.

How to cut:
- Prefer cutting whole subsections, table rows, repetition and secondary detail over rewording sentence by sentence. Where you keep a sentence, keep its wording; reword only to join or shorten, and never change a meaning, a number, an attribution or a hedge ("planned", "indicative", "Sunlit Sea's estimate", "the WP8 lead's proposal").
- Keep the top-level section numbers and headings. Keep the numbers of retained subsections as in the master; if you remove a subsection, do not renumber the others unless a gap would look odd, and log every change.
- Cross-references to "Section x.y" in other groups: keep them as they are (the merge step fixes them). Remove every reference to Annex A (the dissemination record leaves D8.4) and to the KPI record or final technical report as a document the reader should consult. The deliverables annex stays "Annex B" in your text; the merge renames it.
- One home per evidence item (D54): if a fact is stated in full in another group, a short mention suffices.

The twelve checks (verify your own text against each before returning; say in the log that you did):
1. TRL: integrated concept TRL 5 from SINTEF's D7.2 (summarised in D7.6); the EIC proposal sets TRL 4 as its starting point; the plan uses TRL 4–5; proposal target TRL 4–5.
2. Hinge figures like for like: 3.69 kN complete first-generation hinges; 8.36 kN a one-fifth segment of the full-edge connection with a steel rod; 37 kN the design ULS of the third generation (D7.2); North Sea loads still above; full-edge hinge tested only as a SINTEF segment.
3. Basin tests: a 1:10 3 × 5 array behind one breakwater section; the ring only simulated; second campaign with paired second-generation connectors.
4. Stadt Towing Tank tests were outside SUREWAVE; MARIN validated DIFFRAC motions against them.
5. The SUREWAVE array used the Generation 1 aluminium float; Sunlit Sea started the Generation 2 redesign in SUREWAVE and continues it in SuRE (parallel project).
6. D7.4 reference plant: 10 MWp layout, 10,375 kWp installed, €9.75M, €940/kWp; "the D7.4 reference plant" vs "the Norwegian reference plants".
7. Mooring: D5.1 reductions per site; fairlead tensions rise in three of six optimised designs; no "anchor loads".
8. Project: 51 months after extensions of 12 and 3 months, end 31 December 2026; D8.4 due 30 September 2026 (month 48); coordinator "SINTEF".
9. Partner credit by deliverable and work package (Clement WP3 lead and breakwater, mooring and anchoring design; ACCIONA D4.x and the Gijón prototype; Ceit WP5; IFEU WP7 and D7.1; SINTEF D7.2 and tests; MARIN D5.1); Sunlit Sea's own technical work (WP2, D3.1, D3.4, D7.4).
10. Confidentiality: no Sunlit Sea price or cost per watt, named customer, named site or host, and no combination of figures from which a price or cost per watt can be derived (volumes with euro revenue, EBITDA or sensitivity effects; breakwater geometry, unit masses or shares with D7.4 costs; EIC or EUPI-PV plant sizes with euro effects). If the master contains such a combination in your group, break it and log it.
11. No statement that anyone agreed, approved or decided something without a source; the Q1 2027 confirmation of contributions is Sunlit Sea's request and the WP8 lead's proposal.
12. No citations of the final technical report; KPI headline with the exceptions stated; five of seven peer-reviewed papers deposited late, one meets the deposit-at-publication rule.

If the master text contradicts a check, the check wins; log the fix.

Writing rules (CLAUDE.md "Language and tone"): English; no bold (`**`) anywhere in body text; no emphasis-by-assertion (precisely, exactly, crucially, importantly, it is worth noting, not merely); no "therefore", "thus", "which is why"; positive claim first; plain sentences; define abbreviations at first use within your group if the term first appears there; tables with a constant number of columns in every row; no "---" rules; a blank line before and after every heading; no repo file paths, task numbers or internal framing ("draft", "condensed", "master").
