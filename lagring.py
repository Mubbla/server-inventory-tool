import json
# Standardbibliotek för CSV-filer
import csv
# Standardbibliotek för att skapa kataloger och arbeta med filsökvägar
from pathlib import Path
# Standardbibliotek för datum och tid
from datetime import datetime
# Standardbibliotek för operativsystemfunktioner och miljövariabler
import os
from  inputkontroll import giltiga_miljoer


# Hämtar namnet på datafilen från miljövariabeln INVENTORY_DATAFIL.
# Om variabeln inte finns används servrar.json som standardvärde.
def hamta_datafil():
    return os.getenv(
        "INVENTORY_DATAFIL",
        "servrar.json"
    )

# Läs in servrar från JSON-filen
def ladda_servrar():

    # Hämta filnamnet från miljövariabeln eller standardfilen
    datafil = hamta_datafil()

    # Skapa ett Path-objekt för filkontroll
    fil = Path(datafil)

    # Returnera tom lista om filen inte finns
    if not fil.exists():
        return []

    # Läs in och returnera innehållet i JSON-filen
    with open(fil, "r", encoding="utf-8") as fil:
        return json.load(fil)


# Spara serverlista permanent i JSON-fil
def spara_servrar(serverlista):

    datafil = hamta_datafil()

    with open(datafil, "w", encoding="utf-8") as fil:
        json.dump(
            serverlista,        # Info som sparas
            fil,                # Filobjekt
            indent=2,           # Indrag
            ensure_ascii=False  # För användning av å,ä,ö
        )



#----- Rapporter ---#
def exportera_rapporter(serverlista):

    # Skapa rapportmapp om den inte finns
    rapportmapp = Path("rapporter")
    rapportmapp.mkdir(exist_ok=True)
    datum_tid = datetime.now().strftime("%Y-%m-%d_%H%M")

    exportera_csv(serverlista, rapportmapp, datum_tid)

    exportera_sammanfattning(serverlista, rapportmapp, datum_tid)


def exportera_csv(serverlista, rapportmapp, datum_tid):

    filnamn = rapportmapp / f"inventering_{datum_tid}.csv"

    with open(filnamn, "w", newline="", encoding="utf-8") as fil:

        # Lägger till delimiter för att få semikolon, vilket gör att värdena hamnar i var sin kolumn.
        writer = csv.writer(fil, delimiter=";")

        # skriv rubrik i olika kolumner
        writer.writerow([
            "namn",
            "adress",
            "miljo",
            "roll",
            "status",
            "senast_kontrollerad"
        ])

        # För varje server, skriv in värden i ode olika kolumnerna
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

def exportera_sammanfattning(serverlista, rapportmapp, datum_tid ):

    filnamn = rapportmapp / f"sammanfattning_{datum_tid}.txt"

    # Skapa dictionaries för serverantal
    totalt = {"up": 0, "down": 0, "unknown": 0}
    per_miljo = {
        miljo: {"up": 0, "down": 0, "unknown": 0}
        for miljo in giltiga_miljoer
    }

    #
    for server in serverlista:
        status = server["status"]
        miljo = server["miljo"]

        # Håller reda på hur många servrar som har en viss status.
        totalt[status] += 1

        # Håller reda på hur många servrar i varje miljö, som har en viss status.
        per_miljo[miljo][status] += 1

    with open(filnamn, "w", encoding="utf-8") as fil:
        fil.write("Sammanfattning av servrar\n\n")
        fil.write("Totalt:\n")

        # För varje par av nyckel och värde (items), skriv nyckel och värde till filen.
        for status, antal in totalt.items():
            fil.write(f"{status}: {antal}\n")

        fil.write("\nPer miljö:\n")
        # För varje par av nyckel och värde (items), skriv nyckel och värde till filen.
        # För varje miljö, skriv ut antal servrar som har en viss status.
        for miljo, statusar in per_miljo.items():
            fil.write(
                f"{miljo:<8}: up {statusar['up']}, "
                f"down {statusar['down']}, "
                f"unknown {statusar['unknown']}\n"
            )

    print(f"Sammanfattning sparad: {filnamn}")


# Skapar en lista från JSON-filen servrar
serverlista = ladda_servrar()