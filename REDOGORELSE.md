# Redogörelse

## 1. Tre konstruktioner i Python-koden

I `meny.py`, i funktionen `lagg_till()`, används en `while True`-loop för att fråga efter servernamn tills användaren skriver in ett godkänt namn. Villkoren kontrollerar bland annat om namnet är tomt eller redan används. `continue` börjar om loopen, medan `break` lämnar den när namnet är godkänt.

I `inputkontroll.py`, i funktionen `validera_val()`, används en `for`-loop för att jämföra ett angivet värde med alla giltiga värden i en lista. Funktionen returnerar `True` när en matchning hittas och `False` om loopen inte hittar någon.

I `serverhantering.py`, i funktionen `hitta_server()`, används parametrarna `serverlista`, `nyckel` och `sokvarde` för att söka efter en server. Om funktionen hittar en matchande server returnerar den serverns dictionary. Om ingen matchning hittas returnerar den `None`.

## 2. Lista med dictionaries och datatyper
Jag använder en lista med dictionaries för att lagra servrarna. Listan samlar alla servrar, och varje dictionary innehåller uppgifter om en server. I lagring.py läses listan in från JSON-filen. Funktionerna i meny.py får listan som parameter när de behöver visa eller ändra serverdata. I serverhantering.py finns sökfunktionerna hitta_server() och hitta_servrar_med_nyckel(), som söker igenom listan efter servrar som matchar namn eller miljö.

Värdena för namn, adress, miljo, roll, status och senast_kontrollerad är strängar. Varje server lagras alltså som en dictionary med strängnycklar och strängvärden, och alla dessa dictionaries ligger i en lista.

## 3. JSON och CSV

Jag använder JSON för att spara serverdata mellan körningar. I `lagring.py` använder `ladda_servrar()` och `spara_servrar()` modulen `json` för att läsa och skriva data. JSON passar bra för att spara dictionaries och listor på ett strukturerat sätt.

CSV används för rapporten eftersom serverinformationen då kan öppnas som tabell i exempelvis ett kalkylprogram. Funktionen `exportera_csv()` skriver en rubrikrad och sedan en rad per server. Sammanfattningen sparas separat som text av `exportera_sammanfattning()`.

## 4. Programmets moduler och funktioner

I `main.py` finns funktionen `main()`. Den använder `argparse` för att läsa kommandoradsargument och anropa rätt funktion. Om programmet startas utan argument startar textmenyn.

`meny.py` innehåller textmenyn och funktioner som hanterar inmatning, visar servrar, lägger till och tar bort servrar samt anropar serverkontrollerna.

`serverhantering.py` innehåller funktioner för att hitta servrar och uppdatera serverdata, till exempel `hitta_server()`, `hitta_servrar_med_nyckel()` och `uppdatera_serverdata()`.

`lagring.py` ansvarar för att läsa och spara serverdata i JSON samt skapa CSV- och sammanfattningsrapporter.

`kontroller.py` innehåller funktionerna `pinga_server()` och `kontrollera_status()`. De kör pingkommandot och uppdaterar serverns status.

`inputkontroll.py` innehåller listor med giltiga menyval, miljöer och statusar samt funktionerna `validera_val()`, `vill_avbryta()` och `servernamn_ar_giltigt()`.

Jag låter funktionerna ta emot listan med servrar som parameter i stället för att använda en global variabel. På så sätt blir det tydligt vilka data funktionen arbetar med och funktionerna blir enklare att återanvända. I `main.py` skickas listan vidare till funktioner i `meny.py`, som använder den vid behov.

## 5. Moduler från standardbiblioteket

Jag använder `argparse` i `main.py` för att läsa kommandoradsargument. `sys` används där för att avsluta pingkommandon med rätt exitkod.

I `lagring.py` används `json` för JSON-data, `csv` för CSV-rapporten, `os` för att läsa miljövariabeln och `pathlib.Path` för att hantera sökvägar och skapa rapportkatalogen. `datetime` används för tidsstämpeln i rapporternas filnamn och för tidpunkten då en server senast kontrollerades.

I `kontroller.py` används `subprocess` för att köra ping-kommandot.

## 6. Exempel på god praxis

I `lagg_till()` i `meny.py` kontrolleras inmatningen innan en server läggs till. Funktionen frågar igen om namnet eller adressen är tom, om namnet innehåller blanktecken eller om miljön inte är giltig. Den kontrollerar också att namnet inte redan används. Det minskar risken för felaktiga eller dubbla uppgifter i serverlistan.

I `kontroller.py` finns `kontrollera_status()`, som används både när en server kontrolleras och när alla servrar kontrolleras. Den gemensamma funktionen gör att ping- och statuslogiken bara behöver finnas på ett ställe. Funktionen `uppdatera_serverdata()` i `serverhantering.py` uppdaterar statusen och tidpunkten för den senaste kontrollen.

I `kontroller.py` skickas pingkommandot till `subprocess.run()` som en lista. Programmets kod kontrollerar sedan kommandots exitkod för att avgöra om servern svarade. I `main.py` används serverns status för att avsluta CLI-kommandot med exitkod 1 om servern är nere eller inte hittas.

## 7. Källor och hjälpmedel

Jag har använt kursmaterialet och uppgiftsbeskrivningen för att förstå kraven och planera programmets funktioner. Jag använde W3Schools för att slå upp [undantagshantering](https://www.w3schools.com/python/python_try_except.asp) och [filhantering](https://www.w3schools.com/python/python_file_handling.asp). För att förstå hur ett Python-program startas från terminalen läste jag Pythons officiella dokumentation, avsnittet [Using the Python Interpreter](https://docs.python.org/3/tutorial/interpreter.html).

För CLI-argument, till exempel `--lista` och `--kontrollera`, använde jag kursmaterialet och fick hjälp av en AI-assistent att förstå hur `argparse` används. Jag använde också en AI-assistent för förklaringar av Python-kod, felsökning och stöd med programmets Markdown-dokumentation.