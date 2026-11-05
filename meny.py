from lagring import serverlista
from varden import meny_val
from lagring import ladda_servrar, spara_servrar

# Visar och hanterar programmets textmeny.
def starta_meny():

    while True:
        visa_meny()
        try:
            val = int(input("Ditt val: "))
        except ValueError:
            print("Du måste ange en siffra!")
            continue
        print()

        if validate_choice(val, meny_val):
            if val == 1:
                # Skriv ut alla server
                visa_alla(serverlista)

            elif val == 2:
                visa_en(serverlista)

            elif val == 3:
                lagg_till(serverlista)

            elif val == 4:
                andra_status(serverlista)

            elif val == 5:
                spara_rapport(serverlista)

            elif val == 6:
                las_rapport()            

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
    print("   2. Visa en server              ")
    print("   3. Lägg till en server         ")
    print("   4. Ändra status                ")
    print("   5. Spara rapport               ")
    print("   6. Läs rapport                 ")
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
    # strip() avlägsnar blanktecken
    namn = input("Ange serverns namn: ").strip().lower()
    hittad = False

    for server in serverlista:
        if server['namn'].lower() == namn:
            print(f"{server['namn'].lower()}")
            print(f"--- En server ---")
            print(f"{server['namn']} - {server['status']}")
            return

    print(f"serveren '{namn}' hittades inte")

# Funktion för att lägga till en ny server
def lagg_till(serverlista):
    namn = input("Ange den nya serverns namn: ").strip()
    ny_server = {
        "namn": namn,
        "status": "unknown"
    }

    serverlista.append(ny_server)  # ny server sist i listan som skapats fån json-filen
    spara_servrar()  # spara till json-filen
    print()
    print(f"serveren '{namn}' har lagts till")

# Funktion för att ändra status för en server
def andra_status(serverlista):
    print()
    namn = input("Ange serverns namn: ").strip().lower()

    for server in serverlista:
        if server['namn'].lower() == namn:
            server["status"] = input("Ange ny status: ").strip().lower()
            serverlista.spara_servrar()
            print(f"Status för '{namn}' har uppdaterats till {server['status']}")
            return  # avslutar hela funktionen

    print(f"serveren '{namn}' hittades inte")

def check_service(namn, status):

    if status == "running":
        print(f"{'[OK]':<5} {namn}")
    elif status == "stopped":
        print(f"{'[FEL]':<5} {namn}")
    else:
        print("Ogiltig status")

def print_report(serverlista):

    for server in serverlista:
        check_service(server['namn'], server['status'])

def validate_choice(input, valid_choices):

    for choice in valid_choices:
        if choice == input:
            return True

    return False

def spara_rapport(serverlista):
    with open("rapport.txt", "w") as fil:
        fil.write("=== Service Status Tool===\n\n")
        for server in serverlista:
            namn = server["namn"]
            status = server["status"]
            fil.write(f"{namn:<15} {status}\n")

    print("Filen rapport.txt har sparats.")

def las_rapport():
    with open("rapport.txt", "r") as fil:
        for rad in fil:
            print(rad.strip())

        print()