# Reflektion

I arbetet fanns det både krav som bestämde hur programmet skulle fungera och val kring hur jag skulle lösa dem. I den här reflektionen beskriver jag kraven som utgångspunkt och värderar sedan hur jag implementerade dem.

## 1. Datastruktur för servrarna

G1 kräver att servrarna lagras som dictionaries i en lista. Jag följde det kravet och använder fälten `namn`, `adress`, `miljo`, `roll`, `status` och `senast_kontrollerad` för varje server. I `serverhantering.py` går funktionerna `hitta_server()` och `hitta_servrar_med_nyckel()` igenom listan för att hitta en server eller samla alla servrar som matchar ett värde.

Ett alternativ hade varit en dictionary där servernamnet är nyckeln. Då hade det gått snabbt att slå upp en server med namn, men det hade inte följt datastrukturen som uppgiften kräver. En lista passar bra när programmet ska visa eller kontrollera alla servrar. Nackdelen är att namnuppslagning kräver att listan genomsöks. Om uppgiftens krav ändrades och inventeringen blev mycket större skulle jag överväga en databas.

## 2. När serverdata sparas

G5 kräver att ändringar sparas till JSON-filen. I `meny.py` anropas `spara_servrar()` efter att en server har lagts till eller tagits bort. Efter en kontroll av en server sparas den uppdaterade statusen, och efter `kontrollera_alla_servrar()` sparas listan när kontrollerna är färdiga.

Ett alternativ hade varit att vänta med att spara tills programmet avslutas. Det hade minskat antalet skrivningar till filen, men ändringar skulle kunna gå förlorade om programmet stängdes oväntat. Med min lösning finns ändringarna kvar efter att operationen har slutförts. Nackdelen är att filen skrivs oftare. Om många uppdateringar gjordes automatiskt skulle jag överväga en databas för snabbare uppslagning och säkrare datauppdateringar.

## 3. Val av modulindelning och parametrar

G17 kräver att programmet delas upp i minst tre egna moduler. Kravet bestämde alltså att jag skulle använda flera filer, men jag valde själv hur jag skulle fördela ansvaret mellan dem. `main.py` startar programmet och hanterar CLI-argument. `meny.py` sköter textmenyn och användarinmatningen. I `serverhantering.py` finns funktioner för att hitta servrar och uppdatera deras data. `lagring.py` hanterar filer och rapporter, medan `kontroller.py` sköter ping och statuskontroll. `inputkontroll.py` innehåller funktioner och värden för validering.

Ett alternativ hade varit att ha färre filer och samla mer kod i exempelvis `meny.py`. Det hade varit enklare att navigera i början, men den filen skulle då blanda menyhantering med sökning, uppdatering, lagring och kontroll. Med den nuvarande uppdelningen är det tydligare var olika funktioner hör hemma. Nackdelen är att fler moduler innebär fler importer och att man behöver se upp så att modulerna inte börjar importera varandra i en cirkel.

Jag låter funktioner ta emot serverlistan som parameter i stället för att hämta en global lista själva. Det gör tydligare vilka data funktionen behöver, även om listan ibland måste skickas vidare genom flera funktionsanrop. Om programmet växte ytterligare skulle jag fundera på en separat modul för gemensam logik som används av både meny och CLI.

## 4. Datafil och miljövariabel

G6 kräver att datafilens namn kan anges med miljövariabeln `INVENTORY_DATAFIL`, med `servrar.json` som standardvärde. I `lagring.py` gör `hamta_datafil()` detta med `os.getenv()`. Funktionen `ladda_servrar()` använder en `Path`-sökväg och kontrollerar om filen finns innan den läses.

Kravet bestämde att miljövariabeln skulle användas, men implementationen behövde hantera både värdet från miljön och standardvärdet. Fördelen är att samma program kan använda olika datafiler utan att filnamnet behöver ändras i koden. Nackdelen är att det inte alltid är synligt vilken fil programmet använder, särskilt om miljövariabeln redan är satt i terminalen. Om programmet fick fler inställningar skulle jag överväga en konfigurationsfil och beskriva tydligt vilken inställning som har företräde.

## 5. Ping och kommandoradsgränssnitt

G9 kräver att ping körs med `subprocess.run()`, att kommandot skickas som en lista och att exitkoden avgör resultatet. I `kontroller.py` gör `pinga_server()` detta. Funktionen använder Linux-flaggan `-c` och returnerar `True` om pingkommandot får exitkod 0. Kommandot skickas som en lista så att `ping`, flaggorna och adressen blir separata argument. Det gör anropet tydligare och innebär att kommandot inte behöver byggas ihop till en enda textsträng som ett skal ska tolka.

Uppgiften kräver också både textmeny och CLI. Jag återanvänder funktioner för kontroll och lagring så att samma grundläggande arbete inte behöver skrivas två gånger. I `main.py` används `argparse` för att läsa argument, och exitkoderna gör att kontrollkommandona kan användas i skript. För en användare som arbetar manuellt är menyn lätt att följa, medan CLI passar bättre för automatisering. Nackdelen är att programmet behöver hantera två sätt att starta samma funktioner.

Pingkommandots flaggor skiljer sig mellan operativsystem, så den nuvarande lösningen passar bäst i Linux eller WSL. Om verktyget skulle köras på flera plattformar skulle jag anpassa kommandot efter operativsystemet. Om kontrollerna kördes automatiskt mot många servrar skulle jag också lägga till tidsgränser, eftersom en långsam kontroll annars kan fördröja resten.

## 6. Säkrare inmatning

Säkrare inmatning är en av fördjupningarna jag har lagt till. I `lagg_till()` kontrolleras att namn, adress och roll inte är tomma. Namn med blanktecken avvisas, och miljön måste finnas bland de giltiga värdena. I `starta_meny()` fångas en `ValueError` om användaren skriver något som inte kan omvandlas till ett heltal.

Fördelarna är att programmet fångar flera vanliga inmatningsfel direkt och låter användaren försöka igen i stället för att spara ogiltiga uppgifter. Nackdelen med att förbjuda blanktecken i servernamn är att det är en fast regel. Om programmet senare skulle behöva namn med mellanslag skulle jag behöva skilja mellan ett tekniskt server-ID och ett visningsnamn.

## 7. Sammanfattningsrapport och CSV-avgränsare

VG-fördjupningen kräver att CSV-exporten kompletteras med en textrapport som räknar statusar totalt och per miljö. I `lagring.py` samlar `exportera_rapporter()` rapportarbetet. Den skapar rapportkatalogen och skickar serverlistan, sökvägen och tidsstämpeln vidare till `exportera_csv()` och `exportera_sammanfattning()`. Det ger två separata filer med samma tidsstämpel. En fördel är att CSV-filen innehåller serverraderna medan textfilen snabbt visar den övergripande statusen.

I `exportera_csv()` valde jag semikolon som avgränsare. Ett alternativ var kommatecken, men när jag provade filen i svensk Excel hamnade värdena i en enda kolumn. Med semikolon delades de upp i kolumner direkt. Nackdelen är att olika kalkylprogram och regionala inställningar kan förvänta sig olika avgränsare. Om rapporten skulle användas internationellt skulle jag överväga att göra avgränsaren konfigurerbar.

## 8. Om verktyget skulle växa

För en mindre inventering är det enkelt att läsa in JSON-filen och kontrollera servrarna efter varandra. Vid 1 000 servrar eller nattliga körningar kan den sekventiella kontrollen ta lång tid, särskilt om flera servrar svarar långsamt. Då skulle tidsgränser, loggning och eventuellt parallella kontroller bli viktigare.

JSON-filen är lätt att förstå och passar projektets omfattning, men jag skulle överväga en databas om många processer behövde läsa och ändra data samtidigt. Jag skulle också lägga mer vikt vid återhämtning efter avbrott, upprepade försök mot servrar som inte svarade och tydliga loggar som visar vilka kontroller som misslyckades. Det skulle göra verktyget mer lämpligt för automatisk körning i en pipeline.

## Sammanfattning

Uppgiften bestämde flera grundläggande krav, bland annat datastrukturen, JSON-lagringen, pingkontrollen och att både meny och CLI skulle finnas. Mina implementationer är anpassade till ett litet verktyg som ska vara begripligt och enkelt att använda. Om antalet servrar, antalet samtidiga användare eller graden av automatisering ökade skulle jag främst se över lagringen, hastigheten på kontrollerna och loggningen.