9/17/26, 4:47 PM                                       Simuleringsrapport

PRODUKSJONSSIMULERING · REV. 1.1

Flytende solkraftverk -- Mulighetsstudie

Blekinge/Kronoberg, Sverige · 56,63°N / 14,65°Ø · Sunlit Sea-teknologi

Utarbeidet: September 2026 Utarbeidet av: Sunlit Sea AS Status: Innledende estimat

Irradiasjonsdata: Estimert (GHI, ingen TMY-verifisering)

ANTALL PANELER                INSTALLERT EFFEKT        POA-INNSTRÅLING (2°           PERFORMANCE RATIO
                                                       SØR)
8 608                         6,456                                                  90
                                                       1 088
stk                           MWp DC                                                 %
                                                       kWh/m²/år

ESTIMERT PRODUKSJON           SPESIFIKK YIELD

6 320                         979

MWh/år                        kWh/kWp/år

1. PANELKONFIGURASJON OG AREAL

Sunlit Sea-teknologien monterer panelene med 2° helning mot sør på pontongkonstruksjoner. Mellomrom på 100 mm i
begge akser sørger for overflateavrenning og pontongfeste.

PARAMETER                                                               VERDI ENHET  MERKNAD
Panelmål (B × H)                                       2 384 × 1 303 mm              Oppgitt paneldimensjon
Mellomrom (gap)                                                                      Begge akser
Slot-areal per panel (B × H)                                             100 mm      Panel + gap
Slot-areal per panel                                   2 484 × 1 403 mm              2,484 × 1,403
Paneleffekt (nominell)                                                               Per panel, STC
Effekttetthet                                                      3,485 m²          750 ÷ 3,485
Dekkgrad (packing factor)                                                            (2,384 × 1,303) ÷ (2,484 × 1,403)
Tilgjengelig vannflate                                                   750 Wp      30 mål = 30 000 m²

                                                                   215,2 Wp/m²

                                                                       89,1 %
                                                                   30 000 m²

file:///C:/Users/eirirlar/Downloads/solrapport_1.html                                                                   1/4
9/17/26, 4:47 PM                                                            Simuleringsrapport

        PARAMETER                                                         VERDI ENHET           MERKNAD
        Antall paneler
        Installert DC-effekt                           8 608 stk                                30 000 ÷ 3,485
        Installert DC-effekt
                                                       6 456 kWp                                8 608 × 750 W

                                                       6,456 MWp                                Avrundet arbeidsverdi

2. SOLINNSTRÅLING OG POA-ANALYSE

Med 2° helning mot sør fanges en større andel direkte normalinnstråling (DNI) og himmeldiffus (DHI) enn for en ren
horisontal flate. POA er beregnet med pvlib / Perez-modellen, scaled mot GHI = 1 050 kWh/m²/år for 56,6°N.

PARAMETER                                               VERDI ENHET                             MERKNAD
GHI (horisontal referanse)                             1 050 kWh/m²/år                          Regional statistikk, 56,6°N
POA ved 2° sørvendt (Sunlit Sea)                                                                pvlib / Perez; +3,6 % vs. flat
                                                       1 088 kWh/m²/år

Helningsvinkel                                                              2°                  Mot sør (azimut 180°)

Gain vs. horisontal flate                                                 +38 kWh/m²/år         +3,6 %

Merknad: POA-beregning er utført med clear-sky-modell (Ineichen) skalert til regional GHI. TMY-verifisering mot PVGIS anbefales i
neste fase. Gain fra 2° er robust og lite sensitiv for skymodell.

3. TAPSBUDSJETT -- PR-DEKOMPONERING

TAPSKOMPONENT                 TAP (%) MERKNAD

Temperaturkoeffisient         3,0 %                    Kjøleeffekt av vann      TAPSBUDSJETTET VISUALISERT
                                                       reduserer dette vs.
                                                       bakkebasert              Innstråling (POA)                                100 %
                                                                                ­ Temperatur                                    ­3,0 %
Inverter-                     2,0 % Euro-  97,5­98 %                            ­ Inverter                                      ­2,0 %
virkningsgrad                                                                   ­ Kabling DC+AC                                 ­1,5 %
                                                                                ­ Soiling / mismatch                            ­1,0 %
DC-kabeltap                   1,0 %                    String-kabling på        ­ LID + tilgjengelighet                         ­1,5 %
                                                       pontong                  ­ Transformator                                 ­1,0 %

AC-kabeltap                   0,5 % Til nettilkobling

Mismatch                      0,5 % Produksjonstoleranse                        PR netto                                        90,0 %

Soiling / smuss               0,5 %                    Lavt pga. regn og        Merk: Flytende installasjon har typisk lavere
                                                       tilgjengelighet          temperaturtap (~1­2 % lavere enn bakkebasert) pga.
                                                                                kjøleeffekten av vann. PR på 90 % anses som konservativt
LID (lysindusertes            0,5 % Initialår                                   for Sunlit Sea.
degradering)

file:///C:/Users/eirirlar/Downloads/solrapport_1.html                                                                                     2/4
9/17/26, 4:47 PM                                                           Simuleringsrapport

        TAPSKOMPONENT      TAP (%) MERKNAD
        Tilgjengelighet /
        nedetid            1,0 %                       Vedlikeholdsstans,
                                                       feil
        Transformatortap
                           1,0 % MV-transformator
        Sum tap
                            10,0
        Performance Ratio        %
        (PR)
                            90,0 Antatt
                                 %

4. ENERGIPRODUKSJON                                     VERDI ENHET                    BEREGNING
                                                       6 456 kWp                       8 608 paneler × 750 Wp
   PARAMETER                                           1 088 kWh/m²/år                 pvlib/Perez, 56,6°N -- +3,6 % vs. flat
  Installert DC-effekt (Ppeak)                                                         Antatt (se tapsbudsjett)
  POA-innstråling (2° sørvendt, H)                      0,90 --                        P × H × PR = 6 456 × 1 088 × 0,90
  Performance Ratio (PR)                                                               6 320 000 ÷ 6 456
  Estimert produksjon (E)                              6 320 MWh/år                    Tilsvarer ~2,7 h/dag i snitt
  Spesifikk yield                                                                      979 ÷ 8 760 h/år
  Ekvivalente driftstimer                                 979 kWh/kWp/år
  Kapasitetsfaktor                                        979 h/år
                                                        11,2 %

E = 6 456 kWp × 1 088 kWh/m²/år × 0,90 = 6 320 MWh/år

5. SENSITIVITETSANALYSE

SCENARIO      GHI              PR                      PROD. MWH/ÅR        PRODUKSJONSINTERVALL
Lav       1 034            87 %                                 5 810
Basis                                                                      Lav (­8 %)            5 810 MWh
          1 088            90 %                               6 320

                                                                           Basis                 6 320 MWh

Høy       1 142 92 %                                   6 780               Høy (+7 %)            6 780 MWh

GHI-variasjon ±5 % · PR-variasjon ­3/+2 prosentpoeng                       Spenn: 5 810 ­ 6 780 MWh/år (±7­8 % rundt basisverdien)

file:///C:/Users/eirirlar/Downloads/solrapport_1.html                                                                               3/4
9/17/26, 4:47 PM                                       Simuleringsrapport

     6. NØKKELANTAKELSER OG BEGRENSNINGER

TEMA                ANTAKELSE / BEGRENSNING                                      ANBEFALT NESTE STEG
Solinnstråling
                    GHI = 1 050 kWh/m²/år estimert basert på regional            Hent PVGIS TMY-data for eksakte
POA / tilt          statistikk for sørsverige (56°N). Ingen site-spesifikk TMY-  koordinater. Sjekk horisontskygge fra
                    analyse er gjennomført.                                      skog/terreng.
Areal
                    Paneler er modellert med 2° helning mot sør. POA = 1 088     Bekreft faktisk helningsvinkel i Sunlit
Panelspesifikasjon  kWh/m²/år (pvlib/Perez). Eksakt konstruksjonsvinkel bør      Seas pontongkonstruksjon med
Performance Ratio   bekreftes mot Sunlit Seas dokumentasjon.                     leverandør.

Albedo              Hele 30 mål antas tilgjengelig for paneler. Ingen arealtap   Netto tilgjengelig areal bør fastsettes.
Nettkapasitet /     til gangbaner, ankerfeste, transformatorstasjon eller        Typisk 80­90 % av brutto.
inverter            buffersoner.
Regulering
                    750 Wp per panel antatt. Eksakt modell og effekt fra Sunlit  Innhent oppdatert
                    Sea må bekreftes.                                            produktspesifikasjon fra Sunlit Sea.

                    PR = 90 % antatt. Temperaturledd er sannsynligvis            Vurder justert temperaturmodell for
                    konservativt for flytende anlegg (kjøleeffekt).              flytende solkraft (Twater vs.
                                                                                 Tambient).

                    Vannalbedo (~6 %) ikke inkludert. Bidrag til flate paneler   Kan inkluderes i PVGIS-simuleringen
                    er minimalt.                                                 som sensitivitetsparameter.

                    AC-kapasitet (MWac) ikke fastsatt. DC/AC-ratio ikke          Fastsett DC/AC-ratio (typisk 1,10­
                    definert.                                                    1,20 for flytende solkraft).

                    Kommunalt og nasjonalt regelverk for flytende solkraft i     Igangsett regulatorisk screening for
                    Sverige ikke vurdert. Miljøpåvirkning/permitting ikke        flytende solkraft i
                    analysert.                                                   Blekinge/Kronoberg.

Rapport: Simuleringsrapport ­ Flytende solkraftverk, Rev. 1.1 · September 2026 · Sunlit Sea AS
Beregningsmetode: E = Ppeak [kWp] × H [kWh/m²/år] × PR -- standardmetode iht. IEC 61724.
Irradiasjonsgrunnlag: POA = 1 088 kWh/m²/år, beregnet med pvlib/Perez for 2° sørvendt helning, skalert mot GHI 1 050 kWh/m²/år (PVGIS
regional statistikk, 56,6°N). TMY-verifisering utestående.
Dette er et innledende estimat. Resultatene bør ikke benyttes til investeringsbeslutninger uten videre teknisk due diligence.

file:///C:/Users/eirirlar/Downloads/solrapport_1.html                                                                                  4/4
