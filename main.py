# Service Inventory Tool
# main.py
# Läser argument från kommandoraden med argparse.
# Startar textmenyn om inga argument anges.
# Anropar rätt funktioner vid CLI-körning.

# Standardbibliotek för parsning
import argparse
# Används för att avsluta programmet med en exitkod via sys.exit().
import sys

from meny import (starta_meny, visa_servrar,
                  kontrollera_server_med_namn, kontrollera_alla_servrar,
                 visa_servrar_i_miljo)
from lagring import serverlista, exportera_rapporter
from inputkontroll import giltiga_miljoer

def main():

    # Skapa tolk för det som användaren skriver på kommandoraden
    parser = argparse.ArgumentParser(
        description="Server Inventory Tool hanterar och kontrollerar servrar.",
    epilog = """Exempel:
      python3 main.py
      python3 main.py --lista
      python3 main.py --lista --miljo prod
      python3 main.py --kontrollera web01
      python3 main.py --kontrollera-alla
      python3 main.py --export""",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    # Definiera vilka argument som kan användas från kommandoraden.
    parser.add_argument("--lista", action="store_true",
                        help="Visa alla servrar.")
    parser.add_argument("--miljo", choices=giltiga_miljoer,
                        help="Filtrera listan på miljö. Används tillsammans med --lista.")
    # metavar visar en tydlig platshållare för värdet i --help.
    parser.add_argument("--kontrollera", metavar="SERVERNAMN",
                        help="Pinga servern med det angivna namnet.")
    parser.add_argument("--kontrollera-alla", action="store_true",
                        help="Pinga alla servrar.")
    parser.add_argument("--export", action="store_true",
                        help="Skapa CSV-rapport och sammanfattning.")

    args = parser.parse_args()

    # CLI-kommandon som kör klart utan fel får automatiskt exitkod 0.
    if args.lista:
        # Om användaren angivit en miljö...
        if args.miljo:
            # ...skriv ut alla servrar däri.
            visa_servrar_i_miljo(serverlista, "miljo", args.miljo)
        # Om användaren inte angivit miljö, skriv ut alla.
        else:
            visa_servrar(serverlista)

    # Om användaren försöker använda endast --miljo miljo...
    elif args.miljo:
        # ...skriv ut ett felmeddelande.
        parser.error("--miljo måste användas tillsammans med --lista")

    # Om användaren angett ett servernamn...
    elif args.kontrollera:
        server = kontrollera_server_med_namn(serverlista, args.kontrollera)

        if server:
            if server['status'] == "down":
                sys.exit(1)
            else:
                sys.exit(0)
        # Om servern inte hittas...
        else:
            # ...avsluta med exit code 1.
            sys.exit(1)

    elif args.kontrollera_alla:
        kontrollera_alla_servrar(serverlista)

        # Om status är down för minst en server...
        if any(server["status"] == "down" for server in serverlista):
            # ...avsluta med exit code 1.
            sys.exit(1)

    elif args.export:
        exportera_rapporter(serverlista)

    else:
        starta_meny(serverlista)

# Om jag körs som ett eget program, starta main()
if __name__ == "__main__":
    main()







