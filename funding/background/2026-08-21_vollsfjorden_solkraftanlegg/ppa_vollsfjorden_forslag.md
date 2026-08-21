# PPA-prisforslag: Vollsfjorden solkraftanlegg bak Havnevegen 72

| | |
|---|---|
| **Dokumentdato** | ukjent |
| **Avsender / opphav** | Sunlit Sea (internt forslag) |
| **Kildefil** | `funding/background/nye/Vollsfjorden Solkraftanlegg/PPA/vollsfjorden_ppa_forslag.pdf` |
| **Konvertert** | 2026-08-21 med `pdftotext -layout` + `scripts/extract_pdf_images.py` + `scripts/insert_pdf_page_images.py` |

> Automatisk konvertert fra PDF. Layout fra `-layout` er beholdt. Bilder ligger i `images/ppa_vollsfjorden_forslag/` og er lenket inn nederst på hver side.

---

PPA-prisforslag: Vollsfjorden solkraftanlegg bak Havnevegen 72

Grunnlag: analysen i havnevegen_solar.md, malstrukturen i ppa_template.md (2-årig PPA per para-
graf 2.4), og leverandørens oppgitte kostnad EUR 600/kWp installert. Forslaget skal være rettferdig
mellom kjøper (Aaltvedt Betong) og leverandør, og gi begge parter bedre økonomi enn 0-caset – “ingen
PPA, alt fortsetter som i dag”.
Alle tall er ex mva. Aaltvedt er mva-registrert bedrift og kan trekke fra inngående mva, så økonomiske
sammenligninger gjøres på ex mva-nivå. Nettleie-tall fra hovedrapporten (inc mva) er konvertert ved å
dele på 1.25.


Aaltvedts 0-case

Uten solkraft betaler Aaltvedt full nettleie og full spotpris for hele forbruket på Havnevegen 72.

             Post                                                     Årlig verdi (ex mva)
             Nettleie Havnevegen 72                                             287 850 kr
             Spotkostnad (979 MWh x ~0.966 kr/kWh tidsvektet)                  ~945 000 kr
             Sum årlig strømkostnad Havnevegen 72                            ~1 233 000 kr


Dette er referansen Aaltvedt sammenligner PPA-tilbudet mot.


Verdien anlegget skaper for Aaltvedt

Fra analysen (bak Havnevegen 72, ex mva):

Post                                                                                          Årlig verdi
Redusert nettleie                                                                              23 280 kr
Unngått spotkostnad ved egenforbruk (257                                                      215 100 kr
MWh, tidsvektet)
Innmatingsinntekt ved eksport (80 MWh,                                                          45 500 kr
tidsvektet)
Sum brutto verdi                                                                              283 900 kr


Denne verdien er potten partene forhandler over via PPA-prisen.


Aaltvedts betalingsvillighet per solkraft-kWh

PPA-malen paragraf 5.2 (take-or-pay) forplikter kjøper å betale for all produsert solkraft, uavhengig av
egenforbruk eller eksport. Vektet snitt over 337 MWh/år er 283 900 / 337 000 = 0.843 kr/kWh ex mva
som Aaltvedts break-even mot 0-caset. Over denne prisen kommer Aaltvedt dårligere ut med PPA enn
uten.
Marginalverdien varierer mellom strømningene: egenforbruks-kWh (~0.95 kr/kWh via unngått spot +
unngått marginal nettleie) er mer verdt for Aaltvedt enn eksport-kWh (~0.57 kr/kWh via innmatingstariff
+ spot ved eksporttime, som er lavere pga solkraft-cannibalization i spotmarkedet).




                                                    1
Leverandørens kostside med 2-årig PPA

Med oppgitt kostnad EUR 600/kWp installert og 378 kW anlegg:

    • Capex: 378 kW x EUR 600 x 11.5 NOK/EUR ~ 2.61 MNOK
    • Opex: ~2.5%/år av capex ~ 65 000 kr/år
    • PPA-varighet per mal paragraf 2.4: 2 år, uten garantert forlengelse
    • Årsproduksjon: 337 MWh

Sentral ligning for at prosjektet skal være selvfinansierende innenfor PPA-perioden:

2 x PPA‐pris x 337 000 kWh + offentlig støtte >= Capex 2.61 MNOK + 2 x Opex 65 000 kr


Uten støtte krever leverandøren PPA-pris ~4.10 kr/kWh over 2 år for full tilbakebetaling – 5x Aaltvedts
break-even. Prosjektet er da helt uviable som ren 2-årig PPA.
Konsekvens: Uten forlengelses-forpliktelse må enten offentlig støtte dekke mesteparten av capex, eller
leverandøren må akseptere pilot-investering (bevisst tap på 2-årsperioden i bytte mot senere forlengelse
eller kunde-referanse).


Støttebehov for viabilitet

Ved Aaltvedts maksimale betaling over 2 år (max PPA-pris = 0.843 kr/kWh x 337 000 kWh x 2 år = 568
400 kr), kan leverandøren dekke:

                    Post                                                         Beløp
                    Total PPA-inntekt over 2 år (ved 0.843 kr/kWh)         568 400 kr
                    Opex over 2 år                                         130 000 kr
                    Netto tilgjengelig for capex-dekning                   438 400 kr
                    Capex som må dekkes                                  2 610 000 kr
                    Støttebehov for full 2-års viabilitet               ~2.17 MNOK


Uansett hvor mye Aaltvedt betaler innenfor sin betalingsvillighet, må prosjektet ha minst ~2.2 MNOK i
støtte for at leverandøren skal få dekket capex over 2 år uten forlengelses-forpliktelse.


Scenarier med støtte

Tre nivåer, basert på støttebeløp leverandøren kan realistisk sikte mot.           PPA-pris settes slik at
leverandørens 2-års inntekt + støtte dekker capex + opex.


Scenario A: 1.2 MNOK støtte – ikke viable som 2-årig PPA alene

    • Leverandøren må dekke fra PPA: 2.61 - 1.2 + 0.13 opex = 1.54 MNOK
    • Nødvendig PPA-pris: 1 540 000 / (2 x 337 000) = 2.28 kr/kWh
    • Over Aaltvedts break-even (0.843) -> prosjektet ikke viable som 2-årig kontrakt uten mer

Ved dette støttenivået trengs enten forlengelses-forpliktelse (se “Ved forlengelse”), ytterligere støtte fra
andre kilder, eller at leverandøren aksepterer pilot-tap.




                                                     2
Scenario B: 2.2 MNOK støtte – akkurat viable

    • Leverandøren må dekke fra PPA: 2.61 - 2.2 + 0.13 = 0.54 MNOK
    • Nødvendig PPA-pris: 540 000 / (2 x 337 000) = 0.80 kr/kWh
    • Under Aaltvedts break-even (0.843) -> viable, men Aaltvedt får minimal besparelse

                   Størrelse                                                 2-års total
                   PPA-betaling (2 x 337 MWh x 0.80)                     539 200 kr
                   Aaltvedts brutto verdi over 2 år                      567 800 kr
                   Aaltvedts netto besparelse over 2 år                  ~28 600 kr
                   Leverandørens 2-års inntekt                           539 200 kr
                   Leverandøren kost (capex - støtte + opex)             540 000 kr
                   Leverandørens 2-års resultat                  ~0 kr (break-even)


Leverandøren får akkurat dekket kostnadene, ingen avkastning på 2-årsperioden. Aaltvedt får ~14 300
kr/år netto besparelse – marginal, men positiv.


Scenario C: 2.5 MNOK støtte – komfortabelt viable

    • Leverandøren må dekke fra PPA: 2.61 - 2.5 + 0.13 = 0.24 MNOK
    • Leverandørens break-even PPA-pris: 240 000 / (2 x 337 000) = 0.36 kr/kWh
    • Godt under Aaltvedts break-even -> begge parter får meningsfullt utbytte

Ved fair midtpunkt mellom leverandørens break-even (0.36) og Aaltvedts (0.843) blir PPA-prisen ~0.60
kr/kWh:

                       Størrelse                                          2-års total
                       PPA-betaling (2 x 337 MWh x 0.60)              404 400 kr
                       Aaltvedts brutto verdi over 2 år               567 800 kr
                       Aaltvedts netto besparelse over 2 år          ~163 400 kr
                       Leverandørens 2-års inntekt                    404 400 kr
                       Leverandøren kost (capex - støtte + opex)      240 000 kr
                       Leverandørens 2-års resultat                  ~164 400 kr


Fordeling ~50/50 av overskuddet. Aaltvedt får ~82 000 kr/år netto besparelse (7% av 0-case).


Ved forlengelse

Prosjektets langsiktige verdi realiseres først ved forlengelse. Om leverandøren og Aaltvedt forlenger
PPA-en etter 2 år, kan capex amortiseres over lengre periode. Illustrasjon (uten støtte, 8% IRR):

                 Total driftstid   Annuitisert capex   Total årlig kost             LCOE
                           5 år          654 000 kr        719 000 kr        2.13 kr/kWh
                          10 år          389 000 kr        454 000 kr        1.35 kr/kWh
                          15 år          305 000 kr        370 000 kr        1.10 kr/kWh
                          25 år          244 400 kr        309 400 kr       0.918 kr/kWh
                          30 år          232 000 kr        297 000 kr       0.881 kr/kWh



                                                   3
Selv med 25 års driftstid er LCOE uten støtte over Aaltvedts break-even (0.843). Prosjektet er strukturelt
avhengig av offentlig støtte for å være lønnsomt bak måler, uavhengig av tidshorisont.
Om støtte er sikret for pilot-fasen, kan forlengelses-PPA settes betydelig lavere (marginalt over opex
65k/år ~ 0.19 kr/kWh) fordi capex er nedbetalt. Det er dette som gjør prosjektet strategisk interessant
for leverandøren: 2-års pilot med støtte, som muliggjør 20+ års lønnsomt salg etterpå.


Anbefaling

Rangert etter realiserbarhet:

   1. Sikre 2.5 MNOK+ støtte før PPA signeres. Ved dette støttenivået kan PPA settes til ~0.60 kr/kWh
      og begge parter får meningsfullt utbytte allerede i 2-årsperioden.
   2. Ved 2.2 MNOK støtte: PPA på 0.80 kr/kWh gir leverandøren break-even og Aaltvedt marginal
      (~14k/år) besparelse. Fungerer, men uten “pilotens” reelle attraktivitet – hele oppsiden ligger i
      eventuell forlengelse.
   3. Ved lavere støtte: krev forlengelses-forpliktelse (kjøpsopsjon eller PPA-forlengelse til 10+ år) som
      del av signering. Uten det er prosjektet ikke viable som 2-årig kontrakt.

Modell for prisstruktur: fastpris KPI-indeksert per PPA-malen paragraf 5.3. Spot-koblet modell er ikke
aktuell i 2-årig pilot der prisen må matches presist til kostdekning.


Forbehold

    • Anleggsbidrag (se havnevegen_solar.md): et engangsbidrag fra Lede rammer 2-årig pilot spe-
      sielt hardt – det må dekkes i sin helhet innenfor perioden om det ikke kan overføres til en forlenget
      avtale. Et bidrag på 500 000 kr utgjør 0.74 kr/kWh over 2 år, som alene vil ta hele Aaltvedts
      betalingsvillighet.
    • Plusskunde vs prosument-klassifisering: hvis Lede krever prosument-status uten toleranse (~10
      100 kr/år Fastledd (produksjon)), reduseres Aaltvedts brutto verdi fra 283 900 til ~273 800 kr,
      break-even faller til 0.813 kr/kWh og støttebehovet vokser.
    • Kostnadsomfang for EUR 600/kWp: anslaget forutsetter at dette er totalt levert-og-installert-
      kost inkludert forankring, kabling, inverter, tilrettelegging og igangkjøring. Om det er komponent-
      kost alene, må ekstra kostnader (typisk 20-40% for installasjonssystemer og prosjektledelse)
      legges til, som ytterligere skjerper støttebehovet.
    • NOK/EUR-kurs 11.5 brukt i konverteringen. Ved kurs 11.0 blir capex 2.50 MNOK, ved 12.0 blir
      det 2.72 MNOK. PPA-prisen bør avtales i NOK for å skjerme Aaltvedt fra valutaeksponering.
    • Ingen forlengelses-forpliktelse i mal paragraf 2.4: PPA-malen paragraf 8 legger opp til reforhan-
      dling eller kjøpsopsjon, men uten juridisk binding. For at leverandøren skal akseptere pilot-tap i
      scenarier med lav støtte, bør en formell intensjonsavtale om forlengelses-vurdering inngå ved kon-
      traktsigneringen.


Datagrunnlag

Alle tall over kan verifiseres mot vedleggene til havnevegen_solar.md:

    • havnevegen_solar_and_meter_2026.csv – time-vis solkraft, forbruk og spot
    • havnevegen_nettleie_meter_2026.csv – baseline nettleie
    • havnevegen_nettleie_solar_and_meter.csv – med-solkraft nettleie
    • havnevegen_solar.md – samlet analyse og verditabell




                                                    4
    • ppa_template.md – leverandørens PPA-malstruktur

Leverandørens capex på EUR 600/kWp er oppgitt av leverandøren og brukes som gitt. Endelig prisinter-
vall må valideres når leverandøren bekrefter (a) at kostnaden er totalt-levert-og-installert, og (b) hvilket
støttenivå som er realistisk å sikre for prosjektet.




                                                     5
