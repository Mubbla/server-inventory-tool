# Server Inventory Tool

## Beskrivning

Server Inventory Tool är ett Python-program för att hantera en inventering av servrar. Programmet lagrar information om servrar, kontrollerar om de svarar på ping och skapar rapporter.

Serverinformationen sparas i en JSON-fil så att ändringar finns kvar mellan körningar. Programmet kan användas via en textbaserad meny eller direkt från kommandoraden.

## Funktioner

Programmet kan:

- läsa in servrar från en JSON-fil och spara ändringar till filen
- visa alla servrar eller filtrera dem efter miljö
- lägga till och ta bort servrar
- kontrollera en eller alla servrar med ping
- uppdatera serverstatus och tidpunkten för den senaste kontrollen
- exportera serverinformationen till CSV
- skapa en sammanfattande textrapport med antal servrar per status, totalt och per miljö
- läsa datafilens namn från miljövariabeln `INVENTORY_DATAFIL`
- Kontrollera inmatning: programmet frågar igen om ett obligatoriskt fält är tomt, ett servernamn innehåller blanksteg eller ett menyval är ogiltigt.

Nya servrar får statusen `unknown`. En kontroll uppdaterar statusen till `up` eller `down` och sparar datum och tid för kontrollen.

## Krav

För att köra programmet behövs:

- Python 3
- Linux, macOS eller WSL med kommandot `ping` tillgängligt

Programmet använder moduler från Pythons standardbibliotek och kräver inga externa Python-paket. Ping-kontrollen använder flaggan "-c", som fungerar i Linux och macOS.

## Installation

Klona repositoryt och gå till projektmappen:

```bash
git clone https://github.com/Mubbla/server-inventory-tool.git
cd server-inventory-tool
```

## Köra programmet

Kör kommandona från projektmappen.

### Textmeny

Starta programmet utan argument:

```bash
python3 main.py
```

Menyn har alternativ för att visa servrar, filtrera efter miljö, lägga till eller ta bort servrar, kontrollera en eller alla servrar, exportera rapporter och avsluta.

### Kommandorad

Visa hjälp:

```bash
python3 main.py --help
```

Exempel på kommandon:

```bash
# Visa alla servrar
python3 main.py --lista

# Visa servrar i miljön prod
python3 main.py --lista --miljo prod

# Kontrollera en server
python3 main.py --kontrollera web01

# Kontrollera alla servrar
python3 main.py --kontrollera-alla

# Skapa rapporter
python3 main.py --export
```

`--miljo` används tillsammans med `--lista`. Giltiga miljöer är `dev`, `test` och `prod`.

Kontrollkommandona använder exitkoder så att de kan användas i skript:

- `0`: kontrollen lyckades; vid kontroll av flera servrar svarade alla
- `1`: servern som angavs finns inte, eller minst en kontrollerad server är nere

## Datafil och miljövariabel

Som standard läser och sparar programmet data i `servrar.json` i den aktuella arbetskatalogen. Om filen saknas startar programmet med en tom serverlista.

Du kan ange en annan datafil med miljövariabeln `INVENTORY_DATAFIL`. I Ubuntu, WSL eller en annan Bash-terminal kan du till exempel skriva:

```bash
export INVENTORY_DATAFIL="testdata.json"
python3 main.py --lista
```

Värdet gäller för den aktuella terminalsessionen. Om variabeln inte är satt används `servrar.json`.

Varje server lagras med fälten `namn`, `adress`, `miljo`, `roll`, `status` och `senast_kontrollerad`. Giltiga miljöer är `dev`, `test` och `prod`. Giltiga statusar är `up`, `down` och `unknown`.

## Rapporter

Kör `python3 main.py --export` eller välj exportalternativet i textmenyn. Programmet skapar katalogen `rapporter/` om den saknas och sparar två rapporter där:

- `inventering_ÅÅÅÅ-MM-DD_TTMM.csv` innehåller serverinformationen. Kolumnerna separeras med semikolon.
- `sammanfattning_ÅÅÅÅ-MM-DD_TTMM.txt` visar antal servrar med status `up`, `down` och `unknown`, både totalt och per miljö.

## Projektstruktur

| Fil | Ansvar |
| --- | --- |
| `main.py` | Programmets startpunkt. Läser CLI-argument med `argparse` och startar rätt läge. |
| `meny.py` | Textmenyn, inmatning och utskrift av serverinformation. |
| `lagring.py` | Läser och sparar JSON-data samt skapar CSV- och sammanfattningsrapporter. |
| `kontroller.py` | Kör ping-kontroller med `subprocess`. |
| `inputkontroll.py` | Innehåller giltiga menyval, miljöer och statusar samt funktioner för inmatningskontroll. |
| `servrar.json` | Programmets standardfil för serverdata. |
| `.gitignore` | Anger vilka filer och kataloger Git ska ignorera, till exempel cachefiler och genererade rapporter. |