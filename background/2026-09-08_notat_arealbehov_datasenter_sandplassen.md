# Foreløpig vurdering av arealbehov og bygningspotensiale for datasenter, Sandplassen/Thamshavn

**Fra:** Ikon Arkitekt & Ingeniør AS (v/ MHI)
**Til:** Ami-Consulting AS, v/ Robert Mitani
**Kopi:** Dag Alexander Olsen, Jon Mikal Solberg
**Dato:** 08.09.2026
**Vår ref.:** 1520-MHI

## 1. Bakgrunn og formål

Som del av fase 1-arbeidet med å avklare om Sandplassen/Thamshavn kan være en egnet lokalisering for et datasenter, har vi gjort en overordnet vurdering av hvor mye areal et datasenter av ulik effektstørrelse normalt krever, hvilken betydning valg av kjøleteknologi har for både arealbehov og muligheten for å levere overskuddsvarme til fjernvarmenettet, og hvor stort anlegg som trolig kan bygges innenfor det regulerte arealet på Sandplassen.

Vurderingen er basert på offentlig tilgjengelig informasjon om sammenlignbare datasenterprosjekter i Norge og internasjonalt, samt egne beregninger opp mot gjeldende reguleringsplan for Sandplassen. Dette er et tidlig og overordnet grunnlag – ikke en detaljprosjektering – og tallene bør verifiseres direkte med en aktuell datasenteroperatør før prosjektet går videre til neste fase.

## 2. Arealbehov for datasenter – generelt grunnlag

Det finnes ingen entydig fasit for hvor mange kvadratmeter bygg som kreves per MW installert effekt. Forholdstallet varierer betydelig med valgt kjøleteknologi, redundansnivå og om anlegget er en enkeltstående, arealeffektiv løsning eller et anlegg med romslige marginer og faseutbygging. For å etablere et realistisk spenn har vi sett på følgende sammenlignbare anlegg:

| Referanseanlegg | Bygningsareal (BRA) | Effekt | Areal / MW |
|---|---|---|---|
| Green Mountain, Enebakk (NO) | ca. 12 300 m² | 26,8 MW | ≈ 460 m²/MW |
| Facebook/Meta, Luleå (SE) | ca. 28 000 m² | 114 MW | ≈ 250 m²/MW |
| Generelle colocation-anlegg | 1 300–10 000 m² | 10 MW | 130–1 000 m²/MW |
| Molandsmoen, Fyresdal (NO) | ca. 108 000 m² | inntil 365 MW | ≈ 300 m²/MW |
| Aker Nscale, Narvik (NO) – ett byggetrinn | ca. 7 200 m² | 75 MW | ≈ 100 m²/MW |

Basert på dette legger vi til grunn en praktisk planleggingsramme på ca. 250–1 000 m² bygningsareal (BRA) per MW for et konvensjonelt, luftkjølt anlegg, med et typisk nivå rundt 450–500 m²/MW. De mest arealeffektive anleggene i tabellen (Molandsmoen og Aker Nscale) er store, moderne anlegg med tett, delvis væskekjølt teknologi – se punkt 3.

## 3. Betydningen av moderne kjøleteknologi

Valg av kjøleteknologi påvirker prosjektet på to måter som begge er relevante for Sandplassen: hvor mye areal anlegget krever, og hvilken temperatur overskuddsvarmen kan leveres ved til fjernvarmenettet.

### 3.1 Arealbehov

Arealbehovet henger tett sammen med hvor mye effekt som kan pakkes inn per serverskap (kW/skap), siden selve datahallen og mye av det tekniske støttearealet i praksis dimensjoneres etter antall skap, ikke direkte etter MW:

- Konvensjonell luftkjøling: typisk 3–10 kW per skap, forsterkede løsninger opptil 20–40 kW/skap.
- Moderne væskekjøling (direct-to-chip): typisk 80–250+ kW per skap. Dagens ledende AI-maskinvare (Nvidias GB200 NVL72-skap) leverer 120–132 kW i ett og samme skap – en størrelsesorden tettere enn et konvensjonelt skap.

Dette gir en effekttetthet som er grovt sett 5–10 ganger høyere med væskekjøling, noe som forklarer hvorfor de mest arealeffektive anleggene i tabellen over (Molandsmoen, Aker Nscale) benytter denne teknologien. Gevinsten er ikke helt lineær – væskekjøling krever egne tekniske rom for kjølefordeling, og en del areal (adkomst, kontor, sikkerhetssoner) følger uansett hele anleggets størrelse – men den underliggende effekten er betydelig.

### 3.2 Overskuddsvarme til fjernvarme

Samme teknologivalg påvirker også hvilken temperatur overskuddsvarmen kan leveres ved:

- Luftkjøling gir avtrekksvarme typisk i området 30–50 °C – for lavt til å mates direkte inn på fjernvarmenettet. Det kreves da en varmepumpe som løfter temperaturen opp mot 80–85 °C. Dette er en velprøvd løsning i stor skala (bl.a. Microsofts datasenterregion i Espoo/Helsingfors-området, hvor Fortum henter ut overskuddsvarme til fjernvarmenettet), men varmepumpen er en betydelig ekstra investerings- og driftskostnad.
- Væskekjøling fanger varmen mer konsentrert og kan levere brukbar temperatur (eksempelvis 60 °C, jf. et illustrerende prosjekt fra Asetek) direkte inn på fjernvarmenettet uten varmepumpe.

Konklusjon: en operatør som velger moderne, væskekjølt teknologi vil trolig oppnå både et mindre arealbehov og en bedre fjernvarmeøkonomi (høyere temperatur gir høyere betalingsvillighet hos Orkland Energi Varme, og sparer investeringen i varmepumpe). Væskekjøling bør derfor fremheves som en klar fordel overfor en fremtidig operatør, uten at det stilles som et absolutt krav – begge teknologier er tekniske fullgode løsninger for lokalisering på Sandplassen.

## 4. Bygningspotensiale ved Sandplassen

Det regulerte arealet som er aktuelt for datasenterformål utgjør totalt 22,4 daa (22 400 m²). Gjeldende reguleringsplan åpner for bygninger med gesims-/mønehøyde inntil 16 meter over gjennomsnittlig planert terreng, og tanker inntil 26 meter (sistnevnte bestemmelse stammer fra planens opprinnelige forutsetning om et biogassanlegg på tomten, men gir en frihetsgrad som fortsatt kan være aktuell å utnytte).

Vi har sett på en skisse med et bygg på 50 × 100 meter i 3 etasjer, som vurderes som løselig å plassere på tomten:

| Parameter | Verdi |
|---|---|
| Tomteareal | 22 400 m² (22,4 daa) |
| Bebygd areal (fotavtrykk) | 5 000 m² (≈ 22 % av tomten) |
| Antall etasjer | 3 (≈ 5 m fri høyde per etasje innenfor 16 m-grensen) |
| Totalt bygningsareal (BRA) | 15 000 m² |
| Restareal til støttefunksjoner | ≈ 17 400 m² (≈ 78 % av tomten) |

En etasjehøyde på ca. 5 meter er realistisk for datahaller (opphøyd gulv, kabelbroer, kanalføringer), og et bygg i tre etasjer er ikke uvanlig på arealbegrensede tomter – både Molandsmoen (3 etasjer) og Aker Nscale i Narvik (4 etasjer) er bygget etter samme prinsipp. Det gjenværende restarealet på ca. 17 400 m² vurderes som tilstrekkelig til nødaggregat, kjøletårn/dry coolers, trafo- og koblingsanlegg, adkomst, parkering og sikkerhetssone.

## 5. Konklusjon: hvor stort anlegg kan bygges innenfor regulert areal

Ved å sette bygningsarealet på 15 000 m² BRA opp mot arealrammene fra punkt 2 og 3, får vi følgende bilde av hvor stort datasenter Sandplassen-tomten trolig kan romme, avhengig av hvilken generasjon brikketeknologi/kjøleløsning en fremtidig operatør velger:

| Teknologi | Typisk arealeffektivitet | Implisert effekt i 15 000 m² BRA |
|---|---|---|
| Tradisjonell luftkjøling | 450–1 000 m²/MW | ca. 15–33 MW |
| Moderne væskekjøling (dagens AI/GPU-maskinvare) | 100–300 m²/MW | ca. 50–150 MW |

Selv med en konservativ, romslig luftkjølt løsning dekker bygningsmassen godt over det «småskala» 2–3 MW-scenariet som ble diskutert med Nettselskapet AS, og med en typisk luftkjølt løsning lander man rundt 30 MW – over «storskala» 20 MW-scenariet. Velges moderne, væskekjølt teknologi, kan det samme bygget i prinsippet romme et vesentlig større anlegg.

Vår foreløpige vurdering er derfor at arealet på Sandplassen ikke fremstår som den begrensende faktoren for et anlegg i størrelsesordenen 2–50 MW. Det er trolig krafttilgangen som blir styrende for hvor stort anlegget faktisk kan bli.

## 6. Forbehold og videre arbeid

- Tallene i dette notatet er foreløpige anslag basert på offentlig tilgjengelig informasjon om sammenlignbare prosjekter, og på en enkel massestudie – ikke en detaljprosjektering.
- Faktisk arealbehov og oppnåelig effekt bør verifiseres direkte med en konkret datasenteroperatør så snart et operatørkonsept er identifisert, ettersom kjøleteknologi og redundanskrav varierer mye mellom aktører.
- Den endelige rammen for anleggets størrelse avhenger av utfallet av den pågående dialogen med Tensio AS og Nettselskapet AS om tilgjengelig nettkapasitet, samt av videre avklaring med Orkland Energi Varme om avtalestruktur for overskuddsvarme.
- Vi anbefaler at disse temaene følges opp videre i en eventuell fase 2, sammen med konkret utbyggingskapasitet og bygningsplassering, fiber, kjøleløsning og behov for endring av gjeldende reguleringsplan.

*Ikon Arkitekt & Ingeniør AS, Hauggata 12, 6509 Kristiansund. Org.nr. 992 869 631.*
