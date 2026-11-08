from kontroller import (validate_choice, giltiga_menyval, giltiga_miljoval,
                        vill_avbryta, pinga_server)
from lagring import hamta_datafil, spara_servrar, exportera_csv
from datetime import datetime


# Visar och hanterar programmets textmeny.
def starta_meny(serverlista):

    while True:
        visa_meny()

        # Fångar felet om input inte är en siffra.
        try:
            val = int(input("Ditt val: "))
        except ValueError:
            print("Du måste ange en siffra!")
            continue
        print()

        # Kontrollerar att input finns som giltigt menyval.
        if validate_choice(val, giltiga_menyval):

            if val == 1:
                # Skriv ut alla server
                visa_alla(serverlista)

            elif val == 2:
                #(visa_servrar_i_miljo(serverlista))
                print("under construction...")

            elif val == 3:
                lagg_till(serverlista)

            elif val == 4:
                ta_bort_server(serverlista)
                print("under construction...")

            elif val == 5:
                kontrollera_server(serverlista)

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
    print("   1. Visa alla servrar           ")
    print("   2. Visa servrar i en miljö     ")
    print("   3. Lägg till server            ")
    print("   4. Ta bort server              ")
    print("   5. Kontrollera en server       ")
    print("   6. Kontrollera alla servrar    ")
    print("   7. Exportera CSV-fil           ")
    print("   0. Avsluta                     ")
    print("==================================")
    print("")

# Funktion för att skriva ut alla servrar
def visa_alla(serverlista):
    print()
    print(f"{'Namn':<15}{'Adress':<15}{'Miljö':<15}"
          f"{'Roll':<20}{'Status':<15}{'Senast kontrollerad':<15}")
    print()
    for server in serverlista:
        print(f"{server['namn']:<15}{server['adress']:<15}{server['miljo']:<15}"
              f"{server['roll']:<20}{server['status']:<15}{server['senast_kontrollerad']}")


# Funktion för att lägga till en ny server
def lagg_till(serverlista):
    # Servernamn
    while True:
        namn = (input("Ange serverns namn (0 för att återgå till huvudmenyn): ").strip().lower())
        namn_upptaget = False

        # Kontrollera om användaren vill återgå till huvudmenyn. Avslutar isåfall funktionen.
        if vill_avbryta(namn):
            return

        if namn == "":
            print("Namn får inte vara tomt.")
            continue

        for server in serverlista:
            # Kontrollera om servernamnet är upptaget
            if server["namn"].lower() == namn:
                print()
                print("En server med det namnet finns redan.")
                namn_upptaget = True
                # Avsluta for-loop om namnaet hittats
                break

        # Avbryt detta varv för att återgå till inmatning av namn/0.
        if namn_upptaget:
            continue

        # Avbryt while-loop när allt är rätt och gå vidare
        break

    # Adress
    while True:
        adress = input("Ange serverns adress (0 för att återgå till huvudmenyn): ").strip()

        # Kontrollera om användaren vill återgå till huvudmenyn. Avslutar isåfall funktionen.
        if vill_avbryta(adress):
            return

        if adress == "":
            print("Adress får inte vara tom.")
            continue

        break

    # Miljö
    while True:
        miljo = input("Ange miljö (dev/test/prod) (0 för att återgå till huvudmenyn): ").strip().lower()

        # Kontrollera om användaren vill återgå till huvudmenyn. Avslutar isåfall funktionen.
        if vill_avbryta(miljo):
            return

        # Kontrollerar att input finns som giltigt värde.
        if validate_choice(miljo, giltiga_miljoval):
            break

        print("Ogiltig miljö. Ange dev, test eller prod.")

    # Roll
    while True:
        roll = input("Ange serverns roll (0 för att återgå till huvudmenyn): ").strip()

        # Kontrollera om användaren vill återgå till huvudmenyn. Avslutar isåfall funktionen.
        if vill_avbryta(roll):
            return

        if roll == "":
            print("Roll får inte vara tom.")
            continue

        break

    # Skapa dictionary med den nya servern
    ny_server = {
            "namn": namn,
            "adress": adress,
            "miljo": miljo,
            "roll": roll,
            "status": "unknown",
            "senast_kontrollerad": ""
        }

    # Lägg servern sist i listan
    serverlista.append(ny_server)
    spara_servrar(serverlista)
    print()
    print(f"servern '{namn}' har lagts till")

def ta_bort_server(serverlista):
    while True:
        namn = (input("Ange serverns namn (0 för att återgå till huvudmenyn): ").strip().lower())

        # Kontrollera om användaren vill återgå till huvudmenyn. Avslutar isåfall funktionen.
        if vill_avbryta(namn):
            return

        # if giltigt_varde() kanske sen, samla ihop
        if namn == "":
            print("Namn får inte vara tomt.")
            continue

        # Värde som används för servrar i prod
        bekraftelse = None #null
        server_hittad = False
        print(len(serverlista))
        for server in serverlista:
            print(server["namn"].lower())
            print (namn)
            if server["namn"].lower() == namn:
                server_hittad = True
                if server["miljo"] == "prod":
                    # Bekräftelse för prodmiljö
                    while True:
                        print()
                        bekraftelse = input("Denna server är i prodmiljö. Är du riktigt säker tryck retur."
                                         " (0 för att välja annan server) " ).strip()
                        # Användaren vill ange en annan server. Avsluta bekräftelsens while-loop.
                        if bekraftelse == "0":
                            break
                        # Om användaren skrivit in ett felaktigt värde
                        elif bekraftelse != "":
                            print("Ogiltigt val")
                            continue
                        # Användaren har bekräftat. Avsluta bekräftelsens while-loop.
                        if bekraftelse == "":
                            break

            # Användaren vill ange en annan server. Avsluta for-loopen.
            if bekraftelse == "0":
                break

            # Servern finns. Användaren har bekräftat om prod-miljö. Ta bort servern. Avsluta funktionen.
            if server_hittad:
                # Mer felhantering....??
                serverlista.remove(server)
                spara_servrar(serverlista)
                print()
                print(f"servern '{namn}' har lagts till")
                return

        if not server_hittad:
            print(f"Servern '{namn}' finns inte")

        # Går vidare i yttre while-loopen och frågar efter servernaman
        if bekraftelse == "0":
            continue


# Uppdaterar status och senast_kontrollerad
def uppdatera_status(serverlista, server, status):

    server['status'] = status
    server['senast_kontrollerad'] = datetime.now().strftime("%Y-%m-%d %H:%M")
    spara_servrar(serverlista)


def kontrollera_server(serverlista):

    print()
    while True:
        namn = input("Ange serverns namn (0 för att återgå till huvudmenyn): ").strip().lower()

        if vill_avbryta(namn):
            return

        for server in serverlista:
            if server['namn'].lower() == namn:
                if pinga_server(server['adress']):
                    print("Servern är uppe")
                    status = "up"
                else:
                    print("Servern är nere")
                    status = "down"

                uppdatera_status(serverlista, server, status)
                return

        print(f"Servern '{namn}' finns inte")
