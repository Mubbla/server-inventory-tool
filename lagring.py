# servrar.py
import json


# Läs innehållet i JSON-fil
def ladda_servrar():
    with open("servrar.json", "r", encoding="utf-8") as fil:
        return json.load(fil)


# Sparar serverlista permanent i JSON-fil
def spara_servrar():
    with open("servrar.json", "w", encoding="utf-8") as fil:
        json.dump(
            serverlista,        # Info som sparas
            fil,                # Filobjekt
            indent=2,           # Indrag
            ensure_ascii=False  # För användning av å,ä,ö
        )


serverlista = ladda_servrar()