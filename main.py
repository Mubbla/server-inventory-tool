# Service Inventory Tool
# main.py
# Läser argument från kommandoraden med argparse.
# Startar textmenyn om inga argument anges.
# Anropar rätt funktioner vid CLI-körning.

import argparse
from meny import starta_meny

def main():
    # Skapa tolk för det som användaren skriver på kommandoraden
    parser = argparse.ArgumentParser()

    parser.add_argument("--lista", action="store_true")
    parser.add_argument("--export", action="store_true")

    args = parser.parse_args()

    if args.lista:
        print("Visa servrar")

    elif args.export:
        print("Exportera CSV")

    else:
        starta_meny()
# Om jag körs som ett eget program, starta main()
if __name__ == "__main__":
    main()







