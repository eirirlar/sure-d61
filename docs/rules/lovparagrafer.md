# Lovparagrafer — verifisering før sitering

Utdyping av kjerneregelen fra `CLAUDE.md`: lovparagrafer skal verifiseres mot nedlastet verbatim kilde før de siteres, både i leveranser og i chat/utkast.

## Grunnregel for leveranser

Når en leveranse (brev til myndighet, revisorpakke, auditor-notat, grant-søknad, styrepapir, sakspapir til generalforsamling) refererer til en konkret lovparagraf, skal paragrafens ordlyd lastes ned verbatim fra Lovdata og lagres som egen `.md`-fil i `generic/background/lover/`. Lagre bare refererte paragrafer, ikke hele loven.

Filnavn følger sure-d61s dato-prefikskonvensjon:

```
YYYY-MM-DD_<lov>_<para>_<beskrivelse>.md
```

Dato er ikrafttredelses- eller publiseringsdato for gjeldende versjon av *paragrafen* (ikke dagen filen ble laget). Eksempler:

- `2024-11-01_regnskapsloven_5-3_anleggsmidler.md`
- `2026-01-01_skatteforvaltningsloven_14-1_tvangsmulkt.md`
- `2026-10-19_aksjeloven_9-2_erverv_egne_aksjer.md`

Hver fil skal ha metadata-header med lovens fulle tittel, dato/lovnr., lovdata-URL og hentedato, deretter paragraftekst verbatim.

- Finnes paragrafen allerede som fil: re-verifisér at leveransens sitater og paragrafhenvisning stemmer mot filen før utsending.
- Finnes den ikke: last ned først via `last-ned-paragraf`-skillen.

**Grunn:** Feil paragrafreferanse eller unøyaktig sitat kan gjøre et dokument juridisk uriktig — særlig kritisk når sakspapiret skal på generalforsamling, inn i en revisorpakke, eller sendes til forvaltningsorgan (Skatteetaten, Brønnøysund, Finanstilsynet). Modellens treningsdata har kutoff; norske lover endres kontinuerlig og konkrete endringer treffer sjelden hukommelsen i tide.

## Hele-loven-filer

Hvis en hele-loven-fil (eller flere-paragraf-fil fra en tidligere kontekst, som NRS- og NRS(F)-filene fra T75) allerede ligger i `generic/background/lover/`, kan den brukes som kilde — men den konkrete paragrafens tekst skal fortsatt ekstraheres til egen paragraf-fil ved første *leveransereferanse*, slik at `url` og `hentet` entydig knytter sitatet til Lovdata-posten.

## Verifisering av lagrede filer mot Lovdata-kilde

Når brukeren sier "sjekk/verifisér/audit lovene vi har" eller lignende, betyr det én ting: curl mot Lovdata, ekstrahér paragraftekst verbatim, og sammenlign tegn-for-tegn mot lagret `.md`-fil. En header-audit (å kun inspisere YAML-feltene i de lagrede filene) er IKKE verifisering — det tester at vi har skrevet en header, ikke at innholdet matcher gjeldende Lovdata-tekst.

Prosedyren som skal følges:

1. For hver fil i `generic/background/lover/` som peker på en Lovdata-URL (via `url:` eller `kilde:`-felt):
   - Curl den aktuelle URL-en (`-sL` for å følge Lovdatas 303-redirect).
   - Parse `div#PARAGRAF_<n>` og ekstrahér paragraftekst som beskrevet i `.claude/skills/last-ned-paragraf/SKILL.md` (begge innhold-strukturer, med whitespace-opprydding rundt inline-anchors).
   - Normaliser whitespace, så sammenlign med lagret body (etter at YAML og `# § X.`-overskrift er strippet).
2. For hver fil som har reell innholds-forskjell: erstatt den lagrede filen med gjeldende Lovdata-versjon. Oppdater filnavn-prefikset til gjeldende ikrafttredelses-dato for paragrafen (plukket fra fotnote-rekken i Lovdata-HTML, kronologisk seneste match av `(ikr\.|i kraft|fra) D mnd YYYY`).
3. Rapportér hver konstaterte endring eksplisitt — hvilket felt/sitat endret seg, og hvilke leveranser i repoet som siterer paragrafen (grep på paragrafnummer) og derfor kan være påvirket.
4. Hvis Lovdata-paragrafen har fått en ny ikrafttredelses-dato: oppdater filnavnet og legg merke til at eventuelle tidligere leveranser som siterer den eldre versjonen må vurderes for revisjon.

Forbudt snarveier:

- Kun lese YAML-feltene og sjekke at `url:`/`kilde:`/`hentet:` er tilstede — det tester form, ikke sannhet.
- Stole på at `hentet:`-datoen er fersk nok — tre måneder er nok tid til at en lov kan ha fått flere endringer.
- Spot-sjekke "noen få representative paragrafer" uten å kjøre alle — bruker bad eksplisitt om *alle*.

Presedens: T130 (sjekk 2026-10-19) avdekket at `regnskapsloven § 5-6` lå med 586 tegn fra T75-nedlasting (juli 2026), men gjeldende Lovdata-versjon er 355 tegn — en kortere og delvis endret ordlyd som trådte i kraft 1. juli 2021. T75-filen var altså feil ved nedlasting, og en header-audit alene ville ha godkjent den.

## Også for utkast, forslag og chat

Dette gjelder også for utkast, forslag og tekst i chat — ikke bare for ferdige leveranser.

Før du navngir en konkret paragraf, ledd eller punktum (eks. "aksjeloven § 9-2 annet ledd", "regnskapsloven § 5-3 tredje ledd", "skatteforvaltningsloven § 14-1 første ledd") i *noe* du produserer — chat-svar, utkast, forslag, plan, oppsummering — må du først bekrefte at paragrafen finnes som verifisert `.md`-fil i `generic/background/lover/` med metadata-header og verbatim tekst.

Finnes den ikke, enten:

- (a) last ned først via `last-ned-paragraf`-skillen, eller
- (b) omformulér til generelt språk uten paragrafnavn ("etter aksjeloven", ikke "etter asl. § 9-2"; "etter regnskapsloven", ikke "etter rskl. § 5-3 tredje ledd").

Særlig kritisk for ledd-, bokstav- og punktumhenvisninger — disse er påstander om tekstens strukturering som brukeren ikke rimelig kan dobbeltsjekke uten å gå til Lovdata selv.

**Grunn:** Brukere limer regelmessig chat-utkast rett inn i e-post eller inn i en kommende leveranse, så en feil paragrafhenvisning i chat går like gjerne ut til mottaker som en feil i en ferdig fil. Verbatim-reglen for leveranser blir da for sent utløst — feilen er allerede inkorporert i det brukeren jobber med. Paragraf-, ledd- og punktumhenvisninger fra hukommelsen går jevnlig galt (feil paragraf, feil ledd, hallusinert regel, foreldet versjon), så minimumsterskelen må være en faktisk filverifisering i samme samtale.

**Symptom å se etter i egne svar før du sender:** naken "§ X", "jf. § Y annet ledd", "hjemmel i § Z" uten at Glob/Grep/Read av `generic/background/lover/` er gjennomført tidligere i samme samtale.

Ved tvil: omformulér uten paragrafnavn, eller stopp og last ned.

## Historisk referanse

- **T75** (ARCHIVE, juli 2026) — etablerte mønsteret for `generic/background/lover/` med dato-prefikserte paragraf-filer for regnskapsloven, i forbindelse med prinsippendring og nedskrivingstest 2025. Lagret 7 paragrafutdrag fra regnskapsloven og NRS/NRS(F)-standarder.
- **T123** (TASKS, oktober 2026) — sakspapir om ny styrefullmakt til erverv av egne aksjer. Siterte `aksjeloven § 9-2` 10 %-ramme fra hukommelsen; regelen var endret til minste-aksjekapital-basert tak før ikrafttredelse 31.12.2025. Feilen ble oppdaget av regnskapsfører etter at genforsprotokollen var signert. Direkte årsak: T75-konvensjonen ble ikke anvendt for aksjeloven, og `check-deliverable` pkt. 5 ble ikke kjørt. Denne regelen og `last-ned-paragraf`-skillen eksisterer som direkte konsekvens.
- **fjordgata30 T157** (6. oktober 2026, nabo-repo) — audit som avdekket at WebFetch systematisk returnerte parafraserte lovsitater selv når prompten eksplisitt bad om verbatim. Opphav til curl-only-regelen og `last-ned-paragraf`-skillen som sure-d61 nå adopterer.
