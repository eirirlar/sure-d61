---
source: 2020.06.29 Løypemelding.pdf
date: 2020-06-29
type: investor progress update (løypemelding)
---

  Her kommer en oppdatering på aktiviteter i Sunlit Sea siden sist.

Vi er i god gang med utviklingen av vår egen modulnivå kraftelektronikk. Dette innebærer at vi legger til rette for:

              · Inkorporering av maximum-power-point-tracking (MPPT) i kraftelektronikken. Dette er en teknologi som
              finnes og er brukt i noen løsninger på land/tak i dag, som feks hos SolarEdge, og som anslagsvis kan
              redusere tapet i produksjonen med opp til 20% ved å jevne ut strømproduksjonen per streng på 15 paneler
              (ikke implementert enda).

              · Avansert sensorikk: akselerometer og gyroskop, temperatur, strekklapp, lastcelle, saltmåler, fuktmåler,
              trykkmåler, strømmåler (delvis implementert).

              · Rapid shutdown panelnivå. I følge undersøkelser vi har foretatt er det meget sannsynlig at den internasjonale
              elektrotekniske komiteen (IEC) vil kreve at solceller på havet må kunne skrus av individuelt, i motsetning til
              IEC-kravet for solceller på land hvor avstegningen tillates å skje på streng-nivå. Implementert.

              · Vanntetthet. Ved å implementere egen kraftelektronikk kan vi selv besørge komponentens vanntetthet.
              Denne komponenten er den i systemet som påvirkes mest av vanninntregning. Vi har også sett at
              standardpaneler (selv med IP65-klassifisering) ikke nødvendigvis er vanntette nok for bruk på hav.

              · Pris. Kraftelektronikk med featuresettet vi estimerer finnes ikke på markedet og må spesialbestilles.
              Elektronikk med et subsett av funksjonaliteten koster i størrelsesordenen 600kr pr kWp. Dette er mye
              dyrerere enn å lage det selv. Pr nå er pris pr KWp for vår prototyp allerede under 200kr, og vi estimerer at vi i
              den videre utviklingen vil kunne få prisen ned til under 80kr pr KWp.

Her er en video av kraftelektronikken. Man kan se en blinkende LED som er et enkelt program som kontrollerer
kortslutning av strømmen fra solcellepanelet. Man ser på strømmåleren at dette fungerer.

https://drive.google.com/file/d/1jlHaLH0_qVZGe-QBdH8kaUlmuFOsyvL9

I tillegg til kraftelektronikken har vi utviklet sensorikk for lastceller. Disse brukes i hjørnene av matrisen med
solcellepaneler til å måle bølgenes krefter over hele matrisen. Boksen i bildet fylles med potting før det sjøsettes. Chipen
på enden av ledningen er koblet til kraftelektronikken i videoen over.

https://drive.google.com/file/d/1DCTUwj_zoy5zkLoFguKXJL8It4PXKQ2A

Som del av arbeidet med kraftelektronikk har vi også jobbet med data og strømkabel i samme tykke kabel. Det viser seg
at dette markedet som antatt koker ned til at prisen på kabel korrelerer sterkt med kobberprisen når man kommer opp i litt
volum, og at man kan få kabler til nøyaktig den spesifikasjonen man ønsker. Vi har så langt handlet med NEC i Norge for
å komme i gang, men på sikt er det naturlig å bruke den leverandøren som kan gi best pris på vår spesifikasjon.

     Når det gjelder paneler har vi både gjort en del designarbeid og markedsundersøkelser. Det viser seg at vi kan klare å få
     til paneler som matcher størrelsen til våre flottører, ca 2m x 2m, og at vi kan få prototypet disse til en ok pris, samtidig
     som vi ved større volum kan få prisen ned på et konkurransedyktig nivå. Vi jobber med flere produsenter, men foreløpig
     har vi best respons fra noen firma i Litauen. Vi har modifisert panelene ved å endre kanten for å øke vanntettheten til
     panelene. Vi har også endret bakplaten for å få ned prisen, samtidig som stivheten i panelet beholdes ved sammenliming
     med flottør.



Vi har klart å få tak i en meget god vekselretter hos leverandøren Kaco. De har gitt oss priser som indikerer at de er
interessert i et langsiktig samarbeid. Vi jobber med å integrere en dataprosesseringsenhet i hver vekselretter. Så langt
ligger dette an til å bli en Raspberry Pi, men kravet til prosesseringshastighet og features er enda ikke spesifisert ferdig.
Vi jobber også med mikroelektronikk som kan kommunisere med enheten i hver flottør. Foreløpig er valgt protokoll
RS485, men dersom vi klarer å få redusert kravet til båndbredde vil dette endre seg (som igjen vil føre til billigere kabel).

Accura i England har jobbet og jobber fortsatt med formpressing av aluminium for oss. Vi hadde et håp om at de var
kommet lenger i prosessen fram til nå, men det har vist seg at kaldpressing av aluminium til vårt design av flottører ikke
er så lett. Å få framskaffet en fungerende prosess for pressing av flottører er det vi per nå regner som vårt mest kritiske
steg. Vi har satt igang følgende tiltak:

              · Accura har fått instruksjoner om å undersøke brukbarheten av varmpressing av aluminium som alternativ
              produksjonsprosess.

              · Vi har engasjert et firma i Sverige for å undersøke brukbarheten av hydroforming av aluminium som en
              alternativ produksjonsprosess.

              · Vi jobber videre med Sintef med hot-pressing av aluminium.

På den digitale siden har vi jobbet en del med å få opp en dataprosesserings-pipeline, samt et velegnet brukergrensesnitt
for operasjonell monitorering og vedlikehold. Grensesnittet er under arbeid, men allerede nå har vi begynt å høste effekt
av å kunne visualisere dataene fra flottørene på bølgene, både mtp produktutviklingen, matematisk modellering og
interaksjon med brukere.

Vedrørende leads har vi jobbet videre med Eidos. Vi har produsert en forenklet 3D-rendering av prosjektet som viser
størrelsen på matrisen av flottører i vannet, og hvordan bølger virker på konstruksjonen:

https://drive.google.com/drive/u/0/folders/1aPyAAFqFKsyvrTFE9rmGRO6tmEczZTBE

Vi følger opp Eidos videre over sommeren, men det er langt fra den eneste leaden vi har. Vi fokuserer mest av alt på å få
på plass prototyp nr 2 i løpet av høsten, og tror det vil være forløsende for kunders nysgjerrighet.

Vi har engasjert Neue Design Studio til å hjelpe oss med visuell profil. Vi mottok leveranse av denne nå på fredag, og vil
etter hvert bli inkorporert på vår webside med mer:

https://drive.google.com/drive/folders/1xgRwBN1VQzSJwxVO4l_HFvjLvnjsC7Ar

Vår Pakistanske branch er stadig under arbeid, men nærmer seg nå sluttføring. Vi har møte med ambassaden ila neste
uke, og leverer inn papirer for registrering av vårt Pakistanske datterselskap deretter. Umiddelbart etterpå vil vi følge opp
kontaktnettet der nede for å lokalisere pilotprosjekter. På sikt skal det sannsynligvis bygges ut solkraft på to store
demninger i Pakistan, og begge disse vil være gigantkontrakter vi håper å kunne posisjonere oss for.

Angående søknader har vi som sist nevnt jobbet med EIC Accelerator. Denne ble dessverre underkjent av EU. Samtidig
har vi levert søknad hos DOGA og Forskningsrådet, sistnevnte sammen med Institutt for Energiteknikk og UIO
Matematisk Institutt.

     Vi deltok nylig på en konferanse med Solenergiklyngen i Oslo. Det skjer veldig mye spennende i bransjen, og flytende
     solkraft er for alvor på vei opp og fram. Vi fikk møtt våre konkurrenter Ocean Sun og Moss Maritime, uten at det endret
     våre perspektiver vedrørende konkurransen. Vi traff også potensielle partnere, og fikk veldig mye oppmerksomhet fra
     Equinor og Fred Olsen Energy som begge ønsket møter så snart som mulig. Glint Solar var eksplisitte på at de ønsket et
     samarbeid, noe vi skal vurdere.



Aksjesalgene som har foregått så langt har vært til en gradvis økende valuering: Først 50 MNOK ved spredningssalg
runde A i desember/januar, så 60 MNOK og sist 75 MNOK i april. Vi har sterk interesse fra investorer som vil inn, og som
sannsynligvis ville gått inn på en 100 MNOK valuering. Vi har dog holdt igjen fordi vi ønsker å nå følgende milepæler før
vi selger mer:

         Lande en kontrakt på en kommersielt installasjon, størrelse ca 1 MW.
         Installere prototyp nr 2.

Pr nå har vi en total finansiering på 13 MNOK i selskapet. I skrivende stund har vi brukt 3.4 MNOK, og er ihht budsjett. Vi
har naturlig nok et meget strikt fokus på likviditet og kostnadskontroll i denne fasen.

Når vi gjør neste runde med kapitalinnhenting vil vi legge til rette for at eksisterende aksjonærer både kan kjøpe seg inn
ytterligere, eller ta gevinst på hele eller deler av aksjene sine. Foreløpig er detaljer rundt dette ikke spesifisert.

Per Lindberg PhD
Sunlit Sea AS
