from kontroller import (validate_choice, giltiga_menyval, giltiga_miljoval, giltiga_statuskoder,
                        vill_avbryta)
from lagring import spara_servrar, exportera_csv
# Standardbibliotek för hantering av sökvägar
from pathlib import Path

# Visar och hanterar programmets textmeny.
def starta_meny(serverlista):

    while True:
        visa_meny()
        try:
            val = int(input("Ditt val: "))
        except ValueError:
            print("Du måste ange en siffra!")
            continue
        print()

        if validate_choice(val, giltiga_menyval):
            if val == 1:
                # Skriv ut alla server
                visa_alla(serverlista)

            elif val == 2:
                #(visa_server_i_miljo(serverlista))
                print("under construction...")

            elif val == 3:
                lagg_till(serverlista)

            elif val == 4:
                #ta_bort(serverlista)
                print("under construction...")

            elif val == 5:
                #kontrollera_server(serverlista)
                print("under construction...")

            elif val == 6:
                #kontrollera_alla_servrar(serverlista)
                print("under construction...")

            elif val == 7:
                exportera_csv(serverlista)

            elif val == 0:
                print(f"Avslutar....")
                print()
                break;
        else:
            print(f"Ogiltigt val. Försök igen.")


# Funktion för att visa meny
def visa_meny():
    print("")
    print("==================================")
    print("   === Server Inventory Tool ===  ")
    print("   1. Visa alla server            ")
    print("   2. Visa servrar i en miljö     ")
    print("   3. Lägg till server            ")
    print("   4. Ta bort server              ")
    print("   5. Kontrollera en server       ")
    print("   6. Kontrollera alla servrar    ")
    print("   7. Exportera CSV-fil           ")
    print("   8. Spara rapport ??            ")
    print("   9. Ändra status??              ")
    print("   0. Avsluta                     ")
    print("==================================")
    print("")

# Funktion för att skriva ut alla server
def visa_alla(serverlista):
    print()
    for server in serverlista:
        print(f"{server['namn']:<15}{server['status']}")

# Funktion för att skriva ut en viss server
def visa_en(serverlista):

    # här ska vara en loop
    # strip() avlägsnar blanktecken
    namn = input("Ange serverns namn: ").strip().lower()
    hittad = False

    for server in serverlista:
        if server['namn'].lower() == namn:
            print(f"{server['namn'].lower()}")
            print(f"--- En server ---")
            print(f"{server['namn']} - {server['status']}")
            return

    print(f"servern '{namn}' hittades inte")


# Funktion för att lägga till en ny server
def lagg_till(serverlista):
    # Servernamn
    while True:
        namn = (input("Ange serverns namn (0 för att återgå till huvudmenyn): ").strip().lower())
        if vill_avbryta(namn):
            return

        for server in serverlista:
            if server["namn"].lower() == namn.lower():
                print("En server med det namnet finns redan.")
                return

        if namn == "":
            print("Namn får inte vara tomt.")
            continue

        break

    # Adress
    while True:
        adress = input("Ange serverns adress: ").strip()

        if adress == "":
            print("Adress får inte vara tom.")
            continue

        break

    # Miljö
    while True:
        miljo = input("Ange miljö (dev/test/prod): ").strip().lower()

        if validate_choice(miljo, giltiga_miljoval):
            break

        print("Ogiltig miljö. Ange dev, test eller prod.")

    # Roll
    while True:
        roll = input("Ange serverns roll: ").strip()

        if roll == "":
            print("Roll får inte vara tom.")
            continue

        break

    # Detta vill jag ha i  lagring
    ny_server = {
            "namn": namn,
            "adress": adress,
            "miljo": miljo,
            "roll": roll,
            "status": "unknown",
            "senast_kontrollerad": ""
        }

    serverlista.append(ny_server)  # ny server sist i listan som skapats fån json-filen
    spara_servrar()  # spara till json-filen
    print()
    print(f"servern '{namn}' har lagts till")

# Funktion för att ändra status för en server
def andra_status(serverlista):

    print()
    namn = input("Ange serverns namn (0 för att återgå till huvudmenyn): ").strip().lower()
    if vill_avbryta(namn):
        return

    for server in serverlista:
        if server['namn'].lower() == namn:
            while True:
                ny_status = input("Ange ny status (up/down/unknown): ").strip().lower()

                if validate_choice(ny_status, giltiga_statuskoder):
                    server["status"] = ny_status
                    spara_servrar(serverlista)
                    print(f"Status för '{namn}' har uppdaterats till {server['status']}")
                    return  # avslutar hela funktionen

                print("Ogiltig status.")

        print(f"servern '{namn}' hittades inte")

def check_service(namn, status):

    if status == "up":
        print(f"{'[OK]':<5} {namn}")
    elif status == "down":
        print(f"{'[FEL]':<5} {namn}")
    else:
        print("Ogiltig status")

def print_report(serverlista):

    for server in serverlista:
        check_service(server['namn'], server['status'])


def spara_rapport(serverlista):

    # Skapa mappen 'rapporter' om den inte redan finns
    mapp = Path("rapporter")
    mapp.mkdir(exist_ok=True)

    # Kombinera mappen och filnamnet. Fungerar för alla operativsystem.
    filsokvag = mapp / "rapport.txt"

    with open(filsokvag, "w", encoding="utf-8") as fil:
        fil.write("=== Service Inventory Tool===\n\n")
        for server in serverlista:
            namn = server["namn"]
            status = server["status"]
            fil.write(f"{namn:<15} {status}\n")

    print("Filen rapport.txt har sparats.")