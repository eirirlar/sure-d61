# Deprecated wording (SUREWAVE and Sunlit Sea documents)

Phrases that were correct once, or never, and must not appear in current documents. Each line: the pattern (a Python regular expression, case-insensitive), the replacement, and the decision behind it. `scripts/check_deprecated_wording.py` reads the table below and reports every hit in `surewave/deliverables/` and `docs/`, skipping `background/`, `archive/`, work folders (`*_work/`) and this file.

Delivered documents (D8.3, D7.4) and partner sources keep their own wording; they are not edited to match this list, and the script skips files whose names contain `d8.3_technical_brochure` or `d7.4`. Lines that quote a rule (containing "Do not use") are skipped too. Published posts in the archive section of `surewave/deliverables/linkedin_posts.md` are history and are not edited either.

Canonical facts: `docs/project_facts.md`. When a fact there changes, add the old phrasing here.

| Pattern | Use instead | Decision |
|---|---|---|
| `(first\|second\|third\|fourth)[- ]generation (hinge\|connector)` | the corner hinges of the Generation 1 floats; the full-edge hinge of CONNECT | Hinges have no versions or generations (Eirik 2026-11-24) |
| `hinge v[123]\b\|generation v[123]\b\|hinges? \(v[23]\)` | describe the hinge by its form | as above; v2/v3 are SINTEF's and IFEU's labels, cited only as theirs |
| `prototypes? 4 and 5 are made\|no prototype 5` | three CONNECT prototypes made, a fourth under construction, a fifth planned | Eirik 2026-11-24 |
| `TRL 4[–-]5 for the integrated system` | TRL 5 for the integrated system; CONNECT TRL 4–5 | Eirik 2026-11-24 |
| `\b(11\|12\|13\|14\|15) of (the )?16\b` | all 21 output targets met | KPI readings, Eirik 2026-11-24 |
| `Not met \(GA\)` | Met | conference workshops read as 3 or more |
| `none at the start` | 2 press releases: SINTEF 1 November 2022 and ACCIONA 11 October 2024 | Eirik 2026-11-24 |
| `no final summary video` | the seven videos together are the final summary | Eirik 2026-11-24 |
| `life-cycle assessment has not been made` | the CONNECT float LCA is made in SuRE by TNO | Eirik 2026-11-24 |
| `for Clement Germany to confirm\|to be confirmed by Clement Germany` | Clement Germany and SINTEF size each project's breakwater with the SUREWAVE tools | Eirik 2026-11-24 |
| `pending at CINEA\|CINEA decision on the extension is pending` | CINEA confirmed the extension verbally early in 2026; the formal process is still running | Eirik 2026-11-24 |
| `at least 34 (LinkedIn )?posts` | 40 posts by 31 December 2026 | Eirik 2026-11-24 |
| `about 3\.5\s?kN` | a mean of 3.69 kN (D6.1) | D6.1 |
| `could not be (fully )?validated` | state the result and its basis (CLAUDE.md "No defensive caveats") | Eirik 2026-11-24 |
