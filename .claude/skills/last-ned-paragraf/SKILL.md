---
name: last-ned-paragraf
description: Last ned en norsk lovparagraf verbatim fra Lovdata via curl, parse HTML og lagre som .md med metadata-header i generic/background/lover/. Bruk ALLTID før en leveranse eller et chat-utkast refererer til en konkret paragraf, ledd eller punktum (eks. "aksjeloven § 9-2 annet ledd", "regnskapsloven § 5-3 tredje ledd"). Forbudt å bruke WebFetch — den returnerer AI-prosessert parafrase. Trigger-fraser: "last ned paragraf", "verifisér lovteksten", "hent § X fra lovdata", "sjekk at paragrafen stemmer".
---

# Last ned lovparagraf verbatim fra Lovdata

## Når skill-en skal brukes

**Alltid** før du navngir en konkret paragraf, ledd eller punktum (eks. "aksjeloven § 9-2 annet ledd", "regnskapsloven § 5-3 tredje ledd", "skatteforvaltningsloven § 14-1 første ledd") i:

- Leveranser (brev til myndighet, revisorpakke, auditor-notat, grant-søknad, styrepapir, sakspapir til generalforsamling)
- Utkast og forslag
- Chat-svar

**Unntak:** Hvis paragrafen allerede finnes som verifisert `.md`-fil i `generic/background/lover/` med metadata-header og hentedato, kan den brukes som kilde direkte. Re-verifisér sitatet mot filen før utsending.

## Trinn-for-trinn

### 1. Identifisér paragrafen

- Lov: full tittel og vanlig kortnavn (aksjeloven, regnskapsloven, skatteforvaltningsloven, forvaltningsloven, osv.)
- Paragrafnummer (og evt. ledd/punktum)
- Hva paragrafen regulerer (brukes i filnavn-beskrivelsen)
- Dato for gjeldende versjon av paragrafen (brukes i filnavn-prefikset — se trinn 5)

### 2. Konstruér Lovdata-URL

Grunnmønster for en paragraf:

```
https://lovdata.no/lov/<yyyy-mm-dd>-<nr>/§<n>
```

For forskrifter:

```
https://lovdata.no/dokument/SF/forskrift/<yyyy-mm-dd>-<nr>/§<n>
```

Eksempler på gjeldende base-URL for lover som er mye brukt i dette repoet:

- Aksjeloven: `https://lovdata.no/lov/1997-06-13-44/`
- Regnskapsloven: `https://lovdata.no/lov/1998-07-17-56/`
- Skatteforvaltningsloven: `https://lovdata.no/lov/2016-05-27-14/`
- Forvaltningsloven: `https://lovdata.no/lov/1967-02-10/`

### 3. Last ned med curl via Bash — ALDRI WebFetch

Lovdata serverer `/lov/<lovnr>/§<n>` som en 303-redirect til `/dokument/NL/lov/<lovnr>/§<n>` (`/forskrift/<nr>/§<n>` → `/dokument/SF/forskrift/<nr>/§<n>`). Bruk `-L` for å følge redirecten. Lagre i en prosjekt-lokal `.tmp_verify/`-mappe, ikke `/tmp/` — Python i uv-miljøet på Windows mapper ikke git-bashs `/tmp/`.

```bash
mkdir -p .tmp_verify
curl -sL -A "Mozilla/5.0" "<lovdata-url>" -o .tmp_verify/paragraf.html
```

**Hvorfor curl, ikke WebFetch:** WebFetch returnerer AI-prosessert innhold (parafrase/sammendrag). Nabo-repoets audit (fjordgata30 T157, 2026-10-06) avdekket at parafrase systematisk gled inn i leveranser til forvaltningsorganer selv når prompten eksplisitt bad om verbatim. Dette er en strukturell svakhet som ikke kan prompt-fikses. Bruk alltid curl.

### 4. Parse HTML og ekstrahér §-tekst verbatim

Lovdatas gjeldende HTML-struktur (bekreftet 2026-10-19 under T130):

- Paragraf-container: `<div id="PARAGRAF_<n>" class="paragraf morTag_p">`
- Overskrift: `<h3|h4|h5|h6 class="paragrafHeader">` — nivået varierer per lov og dybde
- Innhold: ett eller flere søsken-elementer med `class="avsnitt"`:
  - Multi-ledd paragrafer: `<table class="numeral morTag_an avsnitt">` per ledd, med `(1)`, `(2)` osv. i første `<td>`
  - Single-ledd paragrafer: `<p class="morTag_a avsnitt">` med ren tekst (ingen `(1)`-prefiks)
- Fotnoter/endringshistorikk: `<table class="textList fotnote avsnitt liste">` — her ligger "Endret ved lov DD mnd YYYY (i kraft D mnd YYYY)" eller "(ikr. D mnd YYYY)"

Standard ekstraksjon som dekker begge innhold-strukturer og rydder vekk inline-anchor artefakter:

```bash
uv run --with beautifulsoup4 python - <<'PY'
from bs4 import BeautifulSoup
import re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

PARA_NUM = "9-2"  # juster per paragraf

html = open('.tmp_verify/paragraf.html', encoding='utf-8').read()
soup = BeautifulSoup(html, 'html.parser')
para = soup.select_one(f'div#PARAGRAF_{PARA_NUM}')
assert para, "fant ikke paragraf-container — sjekk HTML-strukturen"

# Strip UI-noise som ellers forurenser teksten
for a in para.find_all('a', class_='anchor'): a.decompose()
for a in para.find_all('a', class_='namedAnchor'): a.decompose()
for a in para.find_all('a', class_='share-paragraf'): a.decompose()
for el in para.find_all(class_='icon'): el.decompose()

def clean(elem):
    s = elem.get_text(" ", strip=True)
    s = re.sub(r'\s+', ' ', s).strip()
    # Fjern spøkelses-mellomrom før komma/punktum som oppstår fra inline-§-anchors
    # (get_text(" ") inserter " " rundt hver inline-anchor; må samles opp)
    s = re.sub(r'\s+([,.;:)])', r'\1', s)
    return s

h = para.find(['h3','h4','h5','h6'], class_='paragrafHeader')
heading = clean(h)

content, footer = [], []
for c in para.children:
    if not getattr(c, 'name', None): continue
    classes = c.get('class') or []
    if 'avsnitt' not in classes: continue
    if 'fotnote' in classes or 'textList' in classes:
        footer.append(clean(c))
    else:
        content.append(clean(c))

print(f"# {heading}\n")
print("\n\n".join(content))
print(f"\n# footer: {' '.join(footer)}")
PY
```

Verifisér visuelt at parsingen fanget hele paragrafen inkludert alle ledd og bokstavpunkter. Hvis siste ledd eller en liste er kuttet, juster parsing-logikken.

### 4b. Finn ikrafttredelses-dato for filnavn-prefiks

Fotnote-rekken inneholder "Endret ved lov …" med enten `(ikr. D mnd YYYY …)` eller `(i kraft D mnd YYYY …)` — begge varianter forekommer avhengig av lovens alder. For forskrifter kan dato stå nakent uten "ikr./i kraft"-prefiks.

```python
IKR_PAT = re.compile(r'(?:ikr\.|i\s*kraft|fra)\s+(\d{1,2})\.?\s+([A-Za-zæøåÆØÅ]+)\.?\s+(\d{4})', re.IGNORECASE)
# Finn alle datoer og plukk den kronologisk seneste (ikke første!)
candidates = [parse_date(*m.groups()) for m in IKR_PAT.finditer(footer_text)]
ikr_date = max(c for c in candidates if c) if candidates else None
# Fallback for forskrifter uten "i kraft"-prefiks: senere DD mnd YYYY i footer
# Fallback for paragrafer som aldri er endret: lovens hoveddato
# (aksjeloven: 1999-01-01, regnskapsloven: 1999-01-01, skatteforvaltningsloven: 2017-01-01)
```

Månedsnavn kan være fulle (`januar`) eller forkortede (`jan`, `sep`/`sept`, `okt`, `des`). Håndter begge.

### 5. Lagre som `.md` med metadata-header

**Målmappe:** `generic/background/lover/` (eneste målmappe i sure-d61).

**Filnavn:** `YYYY-MM-DD_<lov>_<para>_<beskrivelse>.md`

Dato er ikrafttredelses- eller publiseringsdato for *gjeldende versjon av paragrafen* (slik Lovdata viser den), ikke dagen filen ble opprettet. Dette er samme dato-prefikskonvensjon som T75 brukte for regnskapsloven og skatteforvaltningsloven.

Eksempler:

- `2024-11-01_regnskapsloven_5-3_anleggsmidler.md`
- `2026-01-01_skatteforvaltningsloven_14-1_tvangsmulkt.md`
- `2024-07-01_aksjeloven_9-2_erverv_egne_aksjer.md`

**Metadata-header + verbatim tekst:**

```markdown
---
kilde: "<Lovens fulle tittel, slik Lovdata presenterer den>"
lovnr: "YYYY-MM-DD nr. X"
url: https://lovdata.no/lov/YYYY-MM-DD-X/§<n>
hentet: YYYY-MM-DD
---

# § <n>. <paragrafens overskrift>

<Verbatim paragraftekst, inkludert alle ledd og bokstavpunkter, slik det står på Lovdata.>
```

Ingen `source:`-felt som peker på det nedlastede HTML-fragmentet — den slettes etter konvertering, slik konvensjonen i CLAUDE.md om *Converted .md files must be self-contained* krever. `url` + `hentet` er den livevarige kilden.

### 6. Verifisering før bruk som kilde

Når en leveranse refererer paragrafen:

- Re-les filen og bekreft at sitatet som brukes i leveransen er ordrett.
- Sjekk at paragrafnummer, ledd og evt. punktum stemmer.
- Oppdater `hentet`-feltet (eller last ned på nytt) hvis det er lenge siden sist og paragrafen er sentral for leveransen.

### 7. Rydding

Slett `/tmp/paragraf.html` etter at `.md`-filen er lagret. Dette er en fil jeg genererte i samtalen, så ingen bruker-godkjenning nødvendig per *destructive-ops*-regelen.

## Regler som gjelder

- **WebFetch er forbudt** for lovsitater — bruk kun curl. Se `docs/rules/webfetch.md`.
- Hvis brukeren sier "bruk curl", "ikke bruk webfetch" e.l. i samtalen, er WebFetch forbudt for ALT i resten av samtalen (ikke bare paragrafer).
- Ved tvil om paragraf-nummer eller ledd: omformulér uten paragrafnavn ("etter aksjeloven", ikke "etter asl. § 9-2"). Se `docs/rules/lovparagrafer.md`.
- Filnavnkonvensjon følger sure-d61s dato-prefikskonvensjon fra T75, ikke fjordgata30s lov-kortnavn-prefiks.

## Allerede verifiserte lovfiler

Sjekk alltid om paragrafen allerede finnes før du laster ned på nytt:

```bash
ls generic/background/lover/
```

Per T75 (juli 2026) lagret: regnskapsloven §§ 1-5, 5-1, 5-3, 5-6; skatteforvaltningsloven §§ 8-1, 8-2, 14-1, 14-2; skatteforvaltningsforskriften § 14-1-1; NRS 4, NRS 8, NRS(F) Nedskrivning av anleggsmidler.

Per T130 (oktober 2026) lagret: aksjeloven §§ 3-1, 3-4, 4-1, 9-2, 9-3, 9-4 (backfill etter T123-feilen).

## Kjente feil å unngå

- Bruk av WebFetch — gir parafrase, ikke verbatim. Oppdaget i fjordgata30-audit T157.
- Å sitere lovparagrafer fra hukommelsen uten verifikasjon — ledd og punktum feiles oftest. Oppdaget konkret i T123 (feil versjon av `aksjeloven § 9-2`).
- Lagring uten `hentet`-dato — fil kan bli stale uten at det oppdages ved re-bruk.
- Dato-prefikset er dagens dato — det skal være paragrafens ikrafttredelses- eller publiseringsdato for *gjeldende* versjon.
- Ekstrahering som kutter paragrafens siste ledd eller bokstavpunkt — sjekk alltid at hele teksten er med.
- Å lagre `.md`-filen med `source: /tmp/paragraf.html` — brudd på selvstendighets-regelen; bare `url` + `hentet` er livevarige.

## Historisk referanse

- **T75** (ARCHIVE) — opprinnelsen til `generic/background/lover/`-konvensjonen; lagret regnskapsloven og NRS-standardene for prinsippendrings-arbeidet.
- **T123** (TASKS) — sakspapir om erverv av egne aksjer; siterte foreldet `aksjeloven § 9-2` fra hukommelsen fordi denne skillen ikke eksisterte ennå. Den direkte årsaken til T130 og denne skillen.
- **fjordgata30 T157** (nabo-repo, 2026-10-06) — audit som avdekket at WebFetch returnerte systematisk parafrase av lovsitater. Skill-mønsteret er adoptert derfra.
