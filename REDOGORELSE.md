# Redogörelse

## 1. Tre konstruktioner i Python-koden

I `meny.py`, i funktionen `lagg_till()`, används en `while True`-loop för att fråga efter servernamn tills användaren skriver in ett godkänt namn. Villkoren kontrollerar bland annat om namnet är tomt eller redan används. `continue` börjar om loopen, medan `break` lämnar den när namnet är godkänt.

I `inputkontroll.py`, i funktionen `validate_choice()`, används en `for`-loop för att jämföra ett angivet värde med alla giltiga värden i en lista. Funktionen returnerar `True` när en matchning hittas och `False` om loopen inte hittar någon.

I `meny.py`, i funktionen `hitta_server()`, används parametrarna `serverlista`, `nyckel` och `sokvarde` för att söka efter en server. Om funktionen hittar en matchande server returnerar den serverns dictionary. Om ingen matchning hittas returnerar den `None`.

## 2. Lista med dictionaries och datatyper

Jag använder en lista med dictionaries för att lagra servrarna. Listan samlar alla servrar, och varje dictionary innehåller uppgifter om en server. Det gör det möjligt att gå igenom servrarna med loopar och hitta dem med exempelvis namn eller miljö. I `lagring.py` läses listan in från JSON-filen, och funktionerna i `meny.py` får listan som parameter när de behöver visa eller ändra serverdata.

Värdena för `namn`, `adress`, `miljo`, `roll`, `status` och `senast_kontrollerad` är strängar. Listan innehåller alltså dictionaries vars nycklar och värden sparas som text.

## 3. JSON och CSV

Jag använder JSON för att spara serverdata mellan körningar. I `lagring.py` använder `ladda_servrar()` och `spara_servrar()` modulen `json` för att läsa och skriva data. JSON passar bra för att spara dictionaries och listor på ett strukturerat sätt.

CSV används för rapporten eftersom serverinformationen då kan öppnas som tabell i exempelvis ett kalkylprogram. Funktionen `exportera_csv()` skriver en rubrikrad och sedan en rad per server. Sammanfattningen sparas separat som text av `exportera_sammanfattning()`.

## 4. Programmets moduler och funktioner

I `main.py` finns funktionen `main()`. Den använder `argparse` för att läsa kommandoradsargument och anropa rätt funktion. Om programmet startas utan argument startar textmenyn.

`meny.py` innehåller textmenyn och funktioner som hanterar inmatning, visar servrar, lägger till och tar bort servrar samt anropar serverkontrollerna.

`lagring.py` ansvarar för att läsa och spara serverdata i JSON samt skapa CSV- och sammanfattningsrapporter.

`kontroller.py` innehåller funktionen `pinga_server()`, som kör ping-kommandot och avgör om servern svarar.

`inputkontroll.py` innehåller listor med giltiga menyval, miljöer och statusar samt funktionerna `validate_choice()` och `vill_avbryta()`.

Jag låter funktionerna ta emot listan med servrar som parameter i stället för att använda en global variabel. På så sätt blir det tydligt vilka data funktionen arbetar med och funktionerna blir enklare att återanvända. Detta används bland annat i `meny.py`, där funktioner som visar eller ändrar servrar arbetar mot listan som skickas in från `main.py`.

## 5. Moduler från standardbiblioteket

Jag använder `argparse` i `main.py` för att läsa kommandoradsargument. `sys` används där för att avsluta pingkommandon med rätt exitkod.

I `lagring.py` används `json` för JSON-data, `csv` för CSV-rapporten, `os` för att läsa miljövariabeln och `pathlib.Path` för att hantera sökvägar och skapa rapportkatalogen. `datetime` används för tidsstämpeln i rapporternas filnamn och för tidpunkten då en server senast kontrollerades.

I `kontroller.py` används `subprocess` för att köra ping-kommandot.

## 6. Exempel på god praxis

I `lagg_till()` i `meny.py` kontrolleras inmatningen innan en server sparas. Programmet frågar igen om namn eller adress är tomma, om namnet innehåller blanksteg eller om miljön inte är giltig. Det hindrar en del felaktiga värden från att hamna i serverlistan.

I `meny.py` finns `kontrollera_status()`, som används när en server eller alla servrar kontrolleras. Då behöver ping- och statuslogiken inte skrivas på flera ställen.

I `kontroller.py` skickas ping-kommandot till `subprocess.run()` som en lista. Resultatets exitkod används för att avgöra om servern svarade. Det gör också att programmets CLI kan ge exitkod 1 om en server saknas eller är nere.

## 7. Källor och hjälpmedel
Jag har använt kursmaterialet och uppgiftsbeskrivningen för att förstå kraven och planera programmets funktioner. Jag använde W3Schools Python Tutorial för att slå upp undantagshantering och filhantering. För att förstå hur ett Python-program startas från terminalen läste jag Pythons officiella dokumentation, avsnittet Using the Python Interpreter. För CLI-argumenten, till exempel --lista och --kontrollera, använde jag kursmaterialet och fick hjälp av en AI-assistent med att förstå hur argparse används.

Jag har även använt en AI-assistent för att få förklaringar av Python-kod, hjälp med felsökning och stöd med programmets Markdown-dokumentation.