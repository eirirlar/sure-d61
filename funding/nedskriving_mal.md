---
title: "Nedskrivingstest — mal"
scope: Foretaksuavhengig mal for gjennomføring av nedskrivingstest av anleggsmidler (varige driftsmidler og immaterielle eiendeler) etter norsk regnskapslovgivning
malversjon: 1.0
utarbeidet: 2026-07-08
---

# Nedskrivingstest — mal

Denne malen strukturerer gjennomføring og dokumentasjon av nedskrivingstest for anleggsmidler etter norsk regnskapslovgivning. Den er primært rettet mot små foretak (NRS 8), med korte notater der mellomstore og store foretak avviker. Bruk den ved å kopiere til en ny fil (feks `funding/nedskriving_YYYY.md`), fylle inn plassholdere merket `[…]` og fjerne de veilednings-notatene som er markert med `> Veiledning:` når teksten er endelig.

Full ordlyd av siterte bestemmelser ligger i [`background/lover/`](../background/lover/).

---

## 0. Om malen

**Når trengs testen.** Nedskrivning skal vurderes ved hver regnskapsavleggelse (rskl § 5-3 tredje ledd). Er det ingen indikatorer på verdifall, og eiendelen ikke inngår i vurderingsenhet med andre eiendeler som har indikatorutslag, kan videre vurdering unnlates — men indikator-vurderingen skal likevel dokumenteres.

**Hvem malen er skrevet for.** Regnskapspliktige små foretak etter rskl § 1-5 annet ledd, som anvender NRS 8 God regnskapsskikk for små foretak. NRS(F) Nedskrivning av anleggsmidler brukes utfyllende der NRS 8 er tynn (særlig kap. 5 om gjenvinnbart beløp). For mellomstore og store foretak gjelder full NRS med skjerpede noteopplysningskrav — merknader er lagt inn der relevant.

**Rekkefølge på arbeidet.** (1) Fastsett vurderingsenhet. (2) Vurder indikatorer (Trinn 1). (3) Beregn eventuelt gjenvinnbart beløp (Trinn 2). (4) Konkludér og eventuelt gjennomfør nedskrivning (Trinn 3). (5) Vurder reversering av tidligere nedskrivninger. (6) Utarbeid noteopplysninger.

---

## 1. Formål og omfang

*[Sett inn foretaksnavn]* gjennomfører nedskrivingstest for balanseførte anleggsmidler pr. balansedag *[dato, feks 31.12.YYYY]* som del av årsregnskapet for *[regnskapsår]*. Testen dekker følgende eiendelsgrupper:

- *[Fyll inn eiendelsgrupper som testes, feks: balanseførte utviklingsutgifter, kjøpt goodwill, varige driftsmidler i produksjon, o.l.]*

> **Veiledning:** Ta med både tidligere års aktiveringer med gjenværende bokført verdi og eventuelle årets aktiveringer. Utsatt skattefordel er unntatt fra nedskrivningsstandarden (jf. NRS(F) pkt. 1). Andre finansielle anleggsmidler enn investering i datterselskap, tilknyttet selskap og felles kontrollert virksomhet er også unntatt.

Formålet er å oppfylle nedskrivningsplikten etter regnskapsloven § 5-3 tredje ledd og dokumentere metodikk, vurderinger og konklusjon.

---

## 2. Foretakskategori og valgt regnskapsstandard

**Foretakskategori:** *[Mikroforetak / Lite foretak / Mellomstort foretak / Stort foretak]*, jf. regnskapsloven § 1-5.

> **Veiledning kategori.** Sett inn den kategorien foretaket faller i etter to påfølgende år (rskl § 1-5 åttende ledd — to-år-regelen). Terskler:
>
> - Mikroforetak: balansesum ≤ 5 MNOK, salgsinntekter ≤ 10 MNOK, ≤ 10 årsverk (overskrider én eller ingen).
> - Lite foretak: balansesum ≤ 84 MNOK, salgsinntekter ≤ 168 MNOK, ≤ 50 årsverk (overskrider én eller ingen).
> - Stort foretak: overskrider minst to av tersklene 290 MNOK / 580 MNOK / 250 årsverk.
> - Mellomstort foretak: alt som ikke er mikro, lite eller stort.
>
> Foretak av allmenn interesse (rskl § 1-6 — noterte foretak, banker, kredittforetak, forsikringsforetak) følger reglene for store foretak uavhengig av terskeltall.

**Valgt regnskapsstandard:**

- For små foretak: NRS 8 God regnskapsskikk for små foretak som primær ramme, NRS(F) Nedskrivning av anleggsmidler utfyllende for gjenvinnbart beløp og reversering.
- For mellomstore og store foretak: NRS(F) Nedskrivning av anleggsmidler er den ordinære standarden, komplettert med NRS 19 Immaterielle eiendeler for balanseføring og avskrivning.

*[Beskriv kort hvilken standard foretaket faktisk følger og hvorfor.]*

---

## 3. Hjemmelsgrunnlag

Nedskrivingstesten forankres i følgende bestemmelser. Utdrag av lovtekst ligger i `background/lover/`.

### 3.1 Regnskapsloven

| Bestemmelse | Innhold | Utdrag |
|---|---|---|
| § 1-5 | Kategorier av foretak og konsern (mikro/små/mellomstore/store) | [`2024-11-01_regnskapsloven_1-5_kategorier_av_foretak.md`](../background/lover/2024-11-01_regnskapsloven_1-5_kategorier_av_foretak.md) |
| § 5-1 | Klassifisering av eiendeler (anleggsmidler vs. omløpsmidler) | [`2024-11-01_regnskapsloven_5-1_klassifisering_av_eiendeler.md`](../background/lover/2024-11-01_regnskapsloven_5-1_klassifisering_av_eiendeler.md) |
| § 5-3 tredje ledd | Nedskrivningsplikten: "Anleggsmidler skal nedskrives til virkelig verdi ved verdifall som forventes ikke å være forbigående. Nedskrivningen skal reverseres i den utstrekning grunnlaget for nedskrivningen ikke lenger er til stede." | [`2024-11-01_regnskapsloven_5-3_anleggsmidler.md`](../background/lover/2024-11-01_regnskapsloven_5-3_anleggsmidler.md) |
| § 5-6 | Forskning og utvikling — aktiveringsvilkår og små foretaks valgrett | [`2024-11-01_regnskapsloven_5-6_forskning_og_utvikling.md`](../background/lover/2024-11-01_regnskapsloven_5-6_forskning_og_utvikling.md) |
| § 5-7 | Goodwill — nedskrivning skal ikke reverseres | *(ikke gjengitt separat; nevnt i NRS(F) pkt. 7)* |
| § 7-13 annet ledd | Notekrav om forutsetninger for nedskrivning og reversering av varige driftsmidler | *(nevnt i NRS(F) pkt. 2 og pkt. 10)* |
| § 7-39 | Notekrav for anleggsmidler: anskaffelseskost, tilgang, avgang, samlede av- og nedskrivninger, periodens av- og nedskrivninger | *(nevnt i NRS 8 pkt. 4.3.1.1.4)* |

### 3.2 Norsk regnskapsstandarder

| Standard | Innhold relevant for nedskrivingstest | Utdrag |
|---|---|---|
| NRS 8 (desember 2025) | Kap. 4.3.1.1 om FoU og immaterielle eiendeler; 4.3.1.1.2 om avskrivning og nedskrivning av immaterielle eiendeler; 4.3.2.2 om nedskrivningsindikatorer for varige driftsmidler; 7.1.1.3 om offentlige tilskudd; 7.1.1.3.5 om Skattefunn | [`2025-12-01_nrs_8_immaterielle_eiendeler_og_nedskrivning.md`](../background/lover/2025-12-01_nrs_8_immaterielle_eiendeler_og_nedskrivning.md) |
| NRS(F) Nedskrivning av anleggsmidler (desember 2022) | Pkt. 3 indikatorer, pkt. 4 vurderingsenhet, pkt. 5 gjenvinnbart beløp (bruksverdi/salgsverdi/diskonteringsrente), pkt. 6 gjennomføring, pkt. 7 reversering, pkt. 10 tilleggsopplysninger | [`2022-12-01_nrsf_nedskrivning_av_anleggsmidler.md`](../background/lover/2022-12-01_nrsf_nedskrivning_av_anleggsmidler.md) |
| NRS 4 Offentlige tilskudd (revidert juni 2008) | Bruttoføring vs. nettoføring av investeringstilskudd, resultatføring i takt med avskrivning, notekrav. Gjelder tilsvarende for små foretak (NRS 8 pkt. 7.1.1.3.3) | [`2020-02-01_nrs_4_offentlige_tilskudd.md`](../background/lover/2020-02-01_nrs_4_offentlige_tilskudd.md) |

> **Veiledning IFRS.** Foretak som avlegger regnskap etter IFRS anvender IAS 36 *Impairment of Assets* i stedet. Malen dekker ikke IFRS. Metodikken er tilsvarende (indikatorvurdering → gjenvinnbart beløp → nedskrivning), men reversering av goodwill er ikke tillatt heller ikke etter IAS 36, og noteopplysningskravene er vesentlig mer omfattende.

---

## 4. Vurderingsenhet

Etter NRS(F) Nedskrivning pkt. 4.1 bestemmes vurderingsenheten av det laveste nivået hvor det er mulig å identifisere inngående kontantstrømmer som er uavhengige av inngående kontantstrømmer fra andre grupperinger av anleggsmidler.

> **Veiledning.** For mindre foretak med ett enkelt forretningsområde vil ofte foretaket som helhet være den naturlige vurderingsenheten (NRS(F) pkt. 4.1). Faktorer å avveie:
>
> - Kan inntektene fra en gitt eiendel eller eiendelsgruppe identifiseres uavhengig av andre eiendeler? Hvis nei — inngår i en større vurderingsenhet.
> - Er eiendelene organisatorisk styrt sammen? Hvis ja — peker mot samme vurderingsenhet.
> - Finnes felleseiendeler (bygg for sentraladministrasjon, IT-avdeling e.l.) som brukes av flere avdelinger? Disse skal fordeles på vurderingsenheter (NRS(F) pkt. 4.1).
> - Eiendeler som ikke lenger er i bruk skal alltid vurderes individuelt (NRS(F) pkt. 4.1).
> - Er goodwill henført til vurderingsenheten? Da skal nedskrivningen først gjennomføres på goodwill før den fordeles på øvrige eiendeler (NRS(F) pkt. 6).

**Vurderingsenhet i denne testen:** *[beskriv]*

**Begrunnelse:** *[begrunn hvorfor denne enheten er valgt — henvis til om det er én uavhengig kontantstrøm, om felleseiendeler er fordelt, og om goodwill er inkludert]*

---

## 5. Metodikk

Fremgangsmåten følger NRS 8 pkt. 4.3.1.1.2 og NRS(F) Nedskrivning pkt. 3–6 i tre trinn:

**Trinn 1 — Indikatorvurdering.** Ved regnskapsavleggelse skal foretaket vurdere om det finnes indikatorer på verdifall (NRS(F) pkt. 3, NRS 8 pkt. 4.3.2.2). Hvis ingen indikatorer slår ut, og eiendelen ikke inngår i en vurderingsenhet der andre eiendeler har indikatorutslag, kan ytterligere vurdering unnlates.

**Trinn 2 — Beregning av gjenvinnbart beløp.** Hvis indikatorer utløser vurderingsplikt: beregn gjenvinnbart beløp for vurderingsenheten, definert som det høyeste av (a) netto salgsverdi og (b) bruksverdi (NRS(F) pkt. 5).

- Netto salgsverdi er hva vurderingsenheten kan selges for i en armlengdes transaksjon, fratrukket salgskostnader. Beregnes med utgangspunkt i observert markedspris hvis det finnes et fungerende marked; ellers skjønnsmessig.
- Bruksverdi er nåverdien av forventede kontantstrømmer fra fortsatt bruk over gjenværende økonomisk levetid (NRS(F) pkt. 5.3). Prognoseperioden er høyst fem år, deretter fremskriving med konstant eller avtakende vekstrate. Finansieringsutgifter tas ikke med. Skatt tas med bare hvis diskonteringsrenten er etter-skatt.

**Trinn 3 — Nedskrivningsvurdering.** Hvis gjenvinnbart beløp er lavere enn balanseført verdi for vurderingsenheten, gjennomføres nedskrivning ned til gjenvinnbart beløp (NRS(F) pkt. 6). For vurderingsenhet med goodwill fordeles nedskrivningen først på goodwill; deretter forholdsmessig på øvrige eiendeler basert på balanseført verdi.

---

## 6. Trinn 1 — Indikatorvurdering

NRS(F) pkt. 3 og NRS 8 pkt. 4.3.2.2 lister syv minimumsindikatorer som skal vurderes ved hver regnskapsavleggelse.

### 6.1 Eksterne indikatorer

| # | Indikator | Vurdering | Slår ut? |
|---|---|---|---|
| 1 | Anleggsmidlets markedsverdi har i perioden falt vesentlig mer enn det som kunne forventes som følge av elde eller slit ved normal bruk | *[begrunnelse — spesielt relevant for eiendeler med observerbar markedspris]* | Ja / Nei / Ikke relevant |
| 2 | Vesentlig negativ endring i teknologiske, markedsmessige, økonomiske eller juridiske rammebetingelser | *[begrunnelse — vurder både bransje-, produkt- og reguleringsendringer]* | Ja / Nei |
| 3 | Markedsrenter eller andre markedsbaserte avkastningskrav har økt i perioden, og økningen antas å påvirke diskonteringsrenten som anvendes til å beregne anleggsmidlets bruksverdi og vesentlig redusere anleggsmidlets gjenvinnbare beløp | *[begrunnelse — sammenlign rentesituasjon nå med tidspunkt for opprinnelig anskaffelse eller siste vurdering]* | Ja / Nei |
| 4 | Markedsverdien av egenkapitalen er mindre enn foretakets balanseførte egenkapital | *[for foretak som ikke er børsnotert er dette bare relevant hvis markedsverdien er kjent — feks fra nylig emisjon eller due-diligence-prosess]* | Ja / Nei / Ikke kjent |

### 6.2 Interne indikatorer

| # | Indikator | Vurdering | Slår ut? |
|---|---|---|---|
| 5 | Observert ukurans eller fysisk skade av anleggsmidlet | *[begrunnelse — for immaterielle eiendeler tolkes "ukurans" som at teknologien eller kunnskapen ikke lenger har økonomisk verdi]* | Ja / Nei |
| 6 | Vesentlige endringer i perioden som har negative konsekvenser for bruk eller forventet bruk av anleggsmidlet, inkludert planer om avvikling og restrukturering | *[begrunnelse]* | Ja / Nei |
| 7 | Intern rapportering som tilsier at avkastningen fra anleggsmidlet blir dårligere enn forventet — vesentlig overskridelse av investeringsutgift vs. budsjett, eller vesentlig nedjustering av forventede fremtidige kontantstrømmer eller resultater | *[begrunnelse — sammenlign faktisk vs. budsjett; vurder om det ligger vesentlige nedjusteringer i siste ledelsesgodkjente prognose]* | Ja / Nei |

### 6.3 Sammendrag

*[Konklusjon: X av 7 indikatorer utløser vurderingsplikt / Ingen indikatorer utløser vurderingsplikt.]*

> **Veiledning ved sammendraget.** Er utfallet at ingen indikatorer utløser vurderingsplikt, kan trinn 2 og 3 utelates. Dokumenter likevel at vurderingen er gjennomført, og gjør en kortfattet konklusjonsnote (feks "Ingen indikatorer på verdifall utløste vurderingsplikt for balanseførte anleggsmidler pr. balansedag. Nedskrivning gjennomføres ikke.") direkte til pkt. 8.
>
> Er utfallet at én eller flere indikatorer utløser vurderingsplikt, går man videre til trinn 2 og beregner gjenvinnbart beløp for hele vurderingsenheten (ikke bare den enkelte eiendel), jf. NRS(F) pkt. 3 siste avsnitt.

---

## 7. Trinn 2 — Beregning av gjenvinnbart beløp

Utføres bare dersom trinn 1 har utløst vurderingsplikt.

### 7.1 Balanseført verdi pr. balansedag

Balanseført verdi for vurderingsenheten er summen av enkeltposter etter planmessig avskrivning og eventuelle tidligere nedskrivninger.

| Eiendel / eiendelsgruppe | Aktiveringsår(er) | Opprinnelig aktivert (NOK) | Akk. avskrivning + tidligere nedskrivning (NOK) | Bokført restverdi (NOK) | Kommentar |
|---|---|---|---|---|---|
| *[navn]* | *[år]* | *[beløp]* | *[beløp]* | *[beløp]* | *[merknad, feks kilde til aktivering / tilknyttet støtteordning]* |
| *[navn]* | *[år]* | *[beløp]* | *[beløp]* | *[beløp]* | *[merknad]* |
| **Sum vurderingsenhet** | — | *[sum]* | *[sum]* | ***[sum]*** | — |

> **Veiledning tilskudd-behandling.** Er investeringstilskudd (Skattefunn, Enova, Innovasjon Norge, EU-tilskudd o.l.) knyttet til aktiveringen ført brutto der grunnlaget for bruttoføring er til stede (NRS 4 pkt. 3.4 og NRS 8 pkt. 7.1.1.3.2), med tilhørende utsatt inntekt periodisert over avskrivningsplanen? Tilskudd ment å redusere selve investeringens virkelige verdi er ført netto. Kolonnen for "bokført restverdi" viser verdien slik den fremkommer på balansen. Hold separat oversikt over utsatt inntekt der bruttoføring er anvendt.

### 7.2 Bruksverdi

Beregnes som nåverdi av forventede kontantstrømmer fra fortsatt bruk av vurderingsenheten, jf. NRS(F) pkt. 5.3. Prosedyre:

1. **Prognoseperiode.** Kontantstrømsestimater dekker høyst fem år, med fremskriving basert på konstant eller avtakende vekstrate deretter (NRS(F) pkt. 5.3.2). Sist godkjente budsjett/prognose fra ledelsen legges til grunn.
2. **Kontantstrøm-estimat.** Netto for hver periode: forventet positiv kontantstrøm minus forventet fremtidig negativ kontantstrøm som er nødvendig for å skape de positive. Vedlikeholdsutgifter inkluderes. Eventuell kontantstrøm ved fremtidig utrangering tas med. Finansieringsutgifter tas ikke med. Skatt tas bare med hvis diskonteringen er etter-skatt.
3. **Diskonteringsrente.** Markedsmessig avkastningskrav for investering i tilsvarende type virksomhet. For foretak som ikke er børsnotert kan alternativ lånerente anvendes (NRS(F) pkt. 5.3.3), forutsatt at det ikke gir åpenbart misvisende resultat. Alternativ lånerente = den renten foretaket måtte ha betalt til en långiver for å fullfinansiere investeringen frem til slutten av økonomisk levetid.
4. **Nåverdi.** Diskonter forventet kontantstrøm for hver periode med diskonteringsrenten. Summer, legg til nåverdi av eventuell utrangeringsverdi.

**Forutsetninger som er lagt til grunn:**

- Prognoseperiode: *[antall år, feks 5 år 2027-2031]*
- Vekstrate etter prognoseperiode: *[feks konstant 2% eller avtakende]*
- Diskonteringsrente (før-/etter-skatt): *[feks 8% før-skatt]*
- Kilde til rentesats: *[feks alternativ lånerente, WACC-estimat, tilsvarende]*
- Andre vesentlige forutsetninger: *[feks kapasitetsutnyttelse, prisutvikling, kostnadsutvikling]*

**Beregning:**

*[Sett inn kontantstrømoppstilling og nåverdi-beregning. Skal fremstå transparent slik at en revisor kan følge tallgangen.]*

**Bruksverdi:** *[NOK-beløp]*

### 7.3 Netto salgsverdi

Netto salgsverdi = det beløpet vurderingsenheten kan selges for i en armlengdes transaksjon, fratrukket salgskostnader.

> **Veiledning når netto salgsverdi er meningsfull.** Ved etablert annenhåndsmarked (varige driftsmidler, maskiner, kjøretøy) kan netto salgsverdi estimeres ut fra observert markedspris. For egenutviklede immaterielle verdier under utvikling finnes normalt ikke et fungerende marked, og skjønnsmessig verdsettelse blir i praksis en verdivurdering av virksomheten som helhet. I slike tilfeller settes ofte netto salgsverdi til null eller til en nedre grense av rimelig verdsettelsesintervall, og bruksverdi blir det relevante mål.

**Netto salgsverdi:** *[NOK-beløp, eventuelt "ikke meningsfullt estimerbart"]*

### 7.4 Gjenvinnbart beløp

Gjenvinnbart beløp = maks(netto salgsverdi, bruksverdi) = *[NOK-beløp fra pkt. 7.2 eller 7.3]*

---

## 8. Trinn 3 — Nedskrivningsvurdering

Sammenligning av gjenvinnbart beløp med balanseført verdi:

| Post | Beløp (NOK) |
|---|---|
| Bokført samlet verdi vurderingsenhet (pkt. 7.1) | *[sum]* |
| Gjenvinnbart beløp (pkt. 7.4) | *[beløp]* |
| **Nedskrivningsbehov (positivt tall = nedskrivning kreves)** | ***[differanse]*** |

### 8.1 Konklusjon

*[Velg ett av alternativene og bygg ut med de spesifikke tallene.]*

**Alternativ A — Ingen nedskrivning:** Gjenvinnbart beløp overstiger balanseført verdi. Ingen nedskrivning gjennomføres pr. balansedag. Vurderingen dokumenteres i note til årsregnskapet med kort begrunnelse.

**Alternativ B — Nedskrivning gjennomføres:** Gjenvinnbart beløp er lavere enn balanseført verdi med *[X]* NOK. Nedskrivning på *[X]* NOK gjennomføres. Fordeling på de enkelte balansepostene innenfor vurderingsenheten skjer først på goodwill (hvis inkludert i vurderingsenheten), deretter forholdsmessig basert på balanseført verdi før nedskrivning (NRS(F) pkt. 6):

| Eiendel / gruppe | Balanseført før (NOK) | Andel av total | Nedskrivning (NOK) | Balanseført etter (NOK) |
|---|---|---|---|---|
| *[navn]* | *[a]* | *[a/sum]* | *[nedskrivning × andel]* | *[a − nedskrivning × andel]* |
| *[navn]* | *[b]* | *[b/sum]* | *[…]* | *[…]* |
| **Sum** | *[sum]* | 100% | ***[X]*** | *[sum − X]* |

Nedskrivning føres på linjen «Nedskrivning av varige driftsmidler og immaterielle eiendeler» i resultatregnskapet (NRS 8 pkt. 4.3.1.1.3, jf. rskl § 6-1 nr. 8).

> **Veiledning ved goodwill i vurderingsenheten.** Nedskrivning skal alltid fordeles først på goodwill inntil goodwill er satt til null (NRS(F) pkt. 6). Deretter fordeles resten forholdsmessig på øvrige eiendeler. Nedskrivning av goodwill kan aldri reverseres (rskl § 5-7).

---

## 9. Behandling av tilhørende offentlige tilskudd

Nedskrivning av selve eiendelsverdien påvirker ikke den regnskapsmessige behandlingen av tilhørende offentlige tilskudd direkte, men periodiseringen må vurderes:

- **Tilskudd ført brutto (utsatt inntekt).** Periodisering av utsatt inntekt følger opprinnelig avskrivningsplan. Endres avskrivningsplanen som følge av nedskrivningen (kortere gjenværende levetid eller endret verdi), skal periodiseringen justeres tilsvarende (NRS 4 pkt. 3.4, NRS 8 pkt. 7.1.1.3.2).
- **Tilskudd ført netto.** Ingen særskilt behandling — nettobeløpet er allerede reflektert i den reduserte anskaffelseskosten som nedskrives.
- **Skattefunn.** Skattefunn-tilskudd er ført som reduksjon av skyldig skatt eller som fordring på skattemyndighetene (NRS 8 pkt. 7.1.1.3.5). Nedskrivning av tilknyttede utviklingsverdier utløser ikke tilbakebetalingsforpliktelse så lenge de opprinnelige Skattefunn-vilkårene er oppfylt.
- **Tilbakebetalingsforpliktelser.** Vurder om nedskrivningen indikerer at støttebetingelser (Skattefunn, Enova, IN, EU eller andre) ikke lenger vil kunne bli oppfylt (feks hvis prosjektet reelt sett er avviklet). I så fall må tilbakebetalingsforpliktelse regnskapsføres etter NRS 13 Usikre forpliktelser.

> **Veiledning bruttoføring vs. nettoføring.** Hovedregelen er bruttoføring (NRS 4 pkt. 3.4). Nettoføring brukes bare når tilskuddet er ment å bringe eiendelens virkelige verdi ned til det som er nødvendig for å oppnå overensstemmelse med fremtidige kontantstrømmer. Endring fra bruttoføring til nettoføring eller omvendt behandles som endring av regnskapsprinsipp (NRS 4 pkt. 3.6) og krever omarbeidet sammenligningstall.

---

## 10. Noteopplysninger

### 10.1 For alle foretak (rskl § 7-39)

For sum immaterielle eiendeler og sum varige driftsmidler oppgis:

1. Anskaffelseskost med spesifikasjon av balanseførte lånekostnader (finansieringsutgifter) knyttet til egentilvirkede anleggsmidler.
2. Tilgang og avgang i løpet av regnskapsåret.
3. Samlede avskrivninger, nedskrivninger og reverseringer av nedskrivninger.
4. Avskrivninger, nedskrivninger og reverseringer av nedskrivninger i regnskapsåret.

I tillegg opplyses om økonomisk levetid og valg av avskrivningsplan (NRS 8 pkt. 4.3.1.1.4).

### 10.2 For mellomstore og store foretak (NRS(F) pkt. 10)

Ut over kravene i pkt. 10.1 skal det gis følgende tilleggsopplysninger:

- Størrelsen på nedskrivning i perioden, fordelt på ulike klasser av anleggsmidler, dersom dette ikke fremgår av resultatregnskapet.
- Forutsetninger som er lagt til grunn for nedskrivningen, herunder hvordan vurderingsenhet og gjenvinnbart beløp er fastsatt.
- Størrelsen på eventuell reversering i perioden, fordelt på ulike klasser av anleggsmidler.
- Forutsetninger som er lagt til grunn for reversering.

### 10.3 For små foretak

NRS 4 og NRS 19 sine noteopplysningskrav gjelder ikke automatisk for små foretak. De skal likevel gis dersom de er nødvendige for å bedømme foretakets stilling og resultat, jf. rskl § 7-1 annet ledd. Vurder særlig behovet for slike opplysninger hvis (a) nedskrivningen er vesentlig i forhold til balansesum eller resultat, eller (b) det er vesentlige balanseførte utviklingsverdier eller offentlige tilskudd på balansen.

---

## 11. Reversering av tidligere nedskrivning

Regnskapsloven § 5-3 tredje ledd annet punktum fastsetter at nedskrivning skal reverseres i den utstrekning grunnlaget ikke lenger er til stede. Dette vurderes ved hver regnskapsavleggelse (NRS(F) pkt. 7).

**Reverseringsindikatorer** (minimum-vurdering per NRS(F) pkt. 7):

1. Vesentlig økning av anleggsmidlets markedsverdi i perioden.
2. Vesentlig positiv endring i teknologiske, markedsmessige, økonomiske eller juridiske rammebetingelser.
3. Markedsrenter eller andre markedsbaserte avkastningskrav har falt i perioden, og fallet antas å påvirke diskonteringsrenten og vesentlig øke eiendelens gjenvinnbare beløp.
4. Vesentlige endringer i perioden som har positive konsekvenser for bruk eller forventet bruk av anleggsmidlet.
5. Intern rapportering som tilsier at avkastningen fra anleggsmidlet blir bedre enn forventet.

**Vurdering i denne testen:** *[dokumenter om noen av reverseringsindikatorene slår ut, og eventuelt beregn nytt gjenvinnbart beløp]*

**Balanseført verdi etter reversering** begrenses oppad til den verdien eiendelen ville hatt om nedskrivning ikke var foretatt (NRS(F) pkt. 7). Goodwill skal aldri reverseres (rskl § 5-7).

---

## 12. Konklusjon

*[Fyll inn kortfattet oppsummering. Anbefalt struktur:]*

- Testomfang og vurderingsenhet: *[gjenta i én setning hva som er testet og hvordan]*.
- Utfall indikatorvurdering: *[antall indikatorer som slo ut, og hvilke]*.
- Utfall gjenvinnbart-beløp-beregning (hvis gjennomført): *[bruksverdi vs. balanseført verdi]*.
- Beslutning: *[Ingen nedskrivning / Nedskrivning på X NOK gjennomføres / Reversering på Y NOK gjennomføres]*.
- Vesentlige forutsetninger som er lagt til grunn: *[stikkord]*.

---

## Vedlegg: sjekkliste

- [ ] Foretakskategori fastsatt (pkt. 2) og valgt regnskapsstandard angitt
- [ ] Vurderingsenhet argumentert (pkt. 4)
- [ ] Alle 7 indikatorer eksplisitt vurdert (pkt. 6)
- [ ] Balanseført verdi pr. balansedag oppført per post (pkt. 7.1)
- [ ] Diskonteringsrente og prognoseforutsetninger dokumentert (pkt. 7.2)
- [ ] Bruksverdi vs. netto salgsverdi vurdert (pkt. 7.4)
- [ ] Gjenvinnbart beløp sammenlignet mot balanseført verdi (pkt. 8)
- [ ] Eventuell fordeling av nedskrivning på enkeltposter dokumentert (pkt. 8.1)
- [ ] Behandling av tilhørende offentlige tilskudd vurdert (pkt. 9)
- [ ] Noteopplysninger utarbeidet i tråd med foretakskategori (pkt. 10)
- [ ] Reversering av tidligere nedskrivning vurdert (pkt. 11)
- [ ] Konklusjon oppsummerer test, utfall og beslutning (pkt. 12)
