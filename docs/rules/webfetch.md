# WebFetch — når det er trygt, når det ikke er

Utdyping av kjerneregelen fra `CLAUDE.md`: WebFetch er tillatt for hverdagsoppslag, men forbudt for verbatim-tekst til leveranser og under brukerens override.

## Hvorfor det er en risiko

WebFetch returnerer AI-prosessert innhold: en liten modell oppsummerer, parafraserer eller kutter lange sider i stedet for å gi rå tekst. Dette er katastrofalt for juridisk arbeid, der parafraserte lovsitater eller forvaltningsuttalelser kan ødelegge en sak eller tilføre faktafeil til et sakspapir som skal signeres.

Nabo-repoet `../fjordgata30` kjørte en audit 6. oktober 2026 (fjordgata30 T157) og fant at WebFetch systematisk ga sammendrag for lange paragrafer *selv når prompten eksplisitt bad om verbatim* — og at parafrasene hadde glidd inn i leveranser sendt til forvaltningsorganer. Dette er en strukturell svakhet ved verktøyet, ikke noe som kan prompt-fikses.

## Default-regel

For lovsitater, forskriftssitater, formelle uttalelser fra forvaltningsorganer (Skatteetaten, Brønnøysund, Finanstilsynet, DSB, Sivilombudet), og all annen tekst der verbatim ordlyd skal inn i en leveranse eller et sakspapir — bruk `curl` via Bash-verktøyet, ikke WebFetch. Kombiner med egen HTML-parsing (regex eller BeautifulSoup via `uv run --with beautifulsoup4 python`) for ekstraksjon.

For hverdagsoppslag der et sammendrag holder (selskapsinfo, generelle nettsider, bakgrunnslesing, kart-oppslag) er WebFetch greit og ofte raskere.

Terskel: hvis det du henter kan ende opp som sitat i en leveranse, bruk curl. Hvis det bare er bakgrunn for din egen forståelse som du uansett omformulerer selv, er WebFetch greit.

## Brukerens override

Når brukeren sier "bruk curl", "ikke bruk webfetch", "curl bare" eller lignende i en samtale eller prompt, er WebFetch forbudt for hele den samtalen — ingen unntak — inntil brukeren eksplisitt opphever det.

## Grunnregelen

Parafrase er aldri verdt risikoen når brukeren har bedt om rå tekst eller når leveransen skal til forvaltningsorgan, revisor, auditor eller generalforsamling.

## Praktisk mønster for Lovdata

Se `.claude/skills/last-ned-paragraf/SKILL.md` for den operative oppskriften. Kort form:

```bash
curl -s -A "Mozilla/5.0" "https://lovdata.no/lov/<yyyy-mm-dd>-<nr>/§<n>" -o /tmp/paragraf.html
uv run --with beautifulsoup4 python -c "
from bs4 import BeautifulSoup
html = open('/tmp/paragraf.html').read()
soup = BeautifulSoup(html, 'html.parser')
# Lovdata bruker <section class='paragraf'> eller lignende — inspiser og ekstraher verbatim
"
```

Resultatet lagres i `generic/background/lover/` med dato-prefikset filnavn og metadata-header, jf. `docs/rules/lovparagrafer.md`.
