# Server Inventory Tool

## Status

Projektet utvecklas fortlöpande under kursens gång. Dokumentationen uppdateras efterhand som nya funktioner implementeras och testas.

## Beskrivning

Server Inventory Tool är ett Python-program för att hantera en serverinventering. Programmet används för att lagra information om servrar, kontrollera om servrar svarar på nätverket och exportera rapporter.

Informationen sparas i en JSON-fil så att data finns kvar mellan olika körningar av programmet.

Programmet kan användas på två olika sätt:

- Via en textbaserad meny
- Via kommandoraden med hjälp av argparse

## Funktioner

Programmet kan:

- Läsa in servrar från en JSON-fil
- Spara ändringar till JSON-filen
- Visa alla registrerade servrar
- Visa servrar i en specifik miljö
- Lägga till nya servrar
- Ta bort servrar
- Kontrollera en server med ping
- Kontrollera alla servrar
- Uppdatera serverstatus
- Exportera serverinventeringen till CSV
- Läsa datafilens namn från en miljövariabel

## Krav

Följande krävs för att köra programmet:

- Python 3
- Linux, Ubuntu, WSL eller annan miljö där kommandot `ping` fungerar

Programmet använder följande standardbibliotek:

- json
- csv
- os
- pathlib
- datetime
- subprocess
- argparse
- sys

## Installation

### Klona repositoryt

```bash
git clone <repo-url>