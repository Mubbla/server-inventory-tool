# servrar.py
import json
# Standardbibliotek för CSV-filer
import csv
# Standardbibliotek för att skapa kataloger och arbeta med filsökvägar
from pathlib import Path
# Standardbibliotek för datum och tid
from datetime import datetime


# Läs innehållet i JSON-fil
def ladda_servrar():
    with open("servrar.json", "r", encoding="utf-8") as fil:
        return json.load(fil)


# Sparar serverlista permanent i JSON-fil
def spara_servrar(serverlista):
    with open("servrar.json", "w", encoding="utf-8") as fil:
        json.dump(
            serverlista,        # Info som sparas
            fil,                # Filobjekt
            indent=2,           # Indrag
            ensure_ascii=False  # För användning av å,ä,ö
        )


def exportera_csv(serverlista):

    # Skapa rapportmapp om den inte finns
    rapportmapp = Path("rapporter")
    rapportmapp.mkdir(exist_ok=True)

    datum_tid = datetime.now().strftime("%Y-%m-%d_%H%M")
    filnamn = rapportmapp / f"inventering_{datum_tid}.csv"

    with open(filnamn, "w", newline="", encoding="utf-8") as fil:
        # writer = csv.writer(fil)
        # byter till nedan för att få semikolon, vilket gör att värdena hamnar i var sin kolumn
        writer = csv.writer(
            fil,
            delimiter=";"
        )

        writer.writerow([
            "namn",
            "adress",
            "miljo",
            "roll",
            "status",
            "senast_kontrollerad"
        ])

        for server in serverlista:
            writer.writerow([
                server["namn"],
                server["adress"],
                server["miljo"],
                server["roll"],
                server["status"],
                server["senast_kontrollerad"]
            ])

    print(f"Rapport sparad: {filnamn}")

# Skapar en lista från JSON-filen servrar
serverlista = ladda_servrar()