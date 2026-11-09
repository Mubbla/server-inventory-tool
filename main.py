# Service Inventory Tool
# main.py
# Läser argument från kommandoraden med argparse.
# Startar textmenyn om inga argument anges.
# Anropar rätt funktioner vid CLI-körning.

# Standardbibliotek för parsning
import argparse
from meny import (starta_meny, skriv_ut_servrar, hitta_servrar,
                  kontrollera_server_med_namn, kontrollera_alla_servrar,
                  skriv_ut_serverstatus)
from lagring import serverlista, exportera_csv
from inputkontroll import giltiga_miljoer

def main():

    # Skapa tolk för det som användaren skriver på kommandoraden
    parser = argparse.ArgumentParser()

    # Lägg argument till tolken.
    parser.add_argument("--lista", action="store_true")
    parser.add_argument("--miljo", choices=giltiga_miljoer)
    parser.add_argument("--kontrollera")
    parser.add_argument("--kontrollera-alla", action="store_true")
    parser.add_argument("--export", action="store_true")

    args = parser.parse_args()

    if args.lista:

        if args.miljo:
            servrar_i_miljo = hitta_servrar(serverlista, "miljo", args.miljo)
            skriv_ut_servrar(servrar_i_miljo)

        else:
            skriv_ut_servrar(serverlista)

    elif args.kontrollera:

        server = kontrollera_server_med_namn(
            serverlista,
            args.kontrollera
        )

        if server:
            skriv_ut_serverstatus(server)

    elif args.kontrollera_alla:
        kontrollera_alla_servrar(serverlista)

    elif args.export:
        exportera_csv(serverlista)

    else:
        starta_meny(serverlista)
# Om jag körs som ett eget program, starta main()
if __name__ == "__main__":
    main()







