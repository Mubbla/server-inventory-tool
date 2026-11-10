# meny.py

from inputkontroll import (giltiga_statuskoder, giltiga_menyval, giltiga_miljoer,
                        vill_avbryta, validate_choice)
from kontroller import pinga_server
from lagring import spara_servrar, exportera_csv
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
                skriv_ut_servrar(serverlista)

            elif val == 2:
                visa_servrar_i_miljo(serverlista)

            elif val == 3:
                lagg_till(serverlista)

            elif val == 4:
                ta_bort_server(serverlista)

            elif val == 5:
                kontrollera_serverinput(serverlista)

            elif val == 6:
                kontrollera_alla_servrar(serverlista)

            elif val == 7:
                exportera_csv(serverlista)

            elif val == 0:
                print(f"Avslutar....")
                print()
                break
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

# Funktion för att skriva ut alla servrar i en lista
def skriv_ut_servrar(serverlista):
    print()
    print(f"{'Namn':<15}{'Adress':<15}{'Miljö':<15}"
          f"{'Roll':<20}{'Status':<15}{'Senast kontrollerad'}")
    print()
    for server in serverlista:
        print(f"{server['namn']:<15}{server['adress']:<15}{server['miljo']:<15}"
              f"{server['roll']:<20}{server['status']:<15}{server['senast_kontrollerad']}")

#
def kontrollera_input_miljo(serverlista):

    while True:
        print()
        miljo = (input("Ange miljö (0 för att avbryta): ").strip().lower())

        # Kontrollera om användaren vill återgå till huvudmenyn. Avslutar isåfall funktionen.
        if vill_avbryta(miljo):
            return

        # Avbryt detta varv för att återgå till inmatning av miljo/0.
        if miljo == "":
            print("Namn får inte vara tomt.")
            continue



# Hitta och skriv ut alla servrar i en miljö.
def visa_servrar_i_miljo (serverlista, nyckel, varde):

    # Hämta alla servrar i miljön till en lista
    servrar_i_miljo = hitta_servrar_med_nyckel(serverlista, nyckel, varde)

    if servrar_i_miljo:
        skriv_ut_servrar(servrar_i_miljo)


# Funktion för att lägga till en ny server
def lagg_till(serverlista):

    # Servernamn
    while True:
        namn = (input("Ange serverns namn (0 för att avbryta): ").strip().lower())
        namn_upptaget = False

        # Kontrollera om användaren vill avbryta. Avslutar isåfall funktionen.
        if vill_avbryta(namn):
            return

        # Avbryt detta varv för att återgå till inmatning av namn/0.
        if namn == "":
            print("Namn får inte vara tomt.")
            continue

        for server in serverlista:
            # Kontrollera om servernamnet är upptaget
            if server["namn"].lower() == namn:
                print()
                print("En server med det namnet finns redan.")
                namn_upptaget = True
                # Avsluta for-loop om namnet hittats
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
        if validate_choice(miljo, giltiga_miljoer):
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
        namn = (input("Ange serverns namn (0 för att avbryta): ").strip().lower())

        # Kontrollera om användaren vill återgå till huvudmenyn. Avslutar isåfall funktionen.
        if vill_avbryta(namn):
            return

        # if giltigt_varde() kanske sen, samla ihop
        if namn == "":
            print("Namn får inte vara tomt.")
            continue

        server_hittad = False

        bekraftelse = None  # null

        # Här kan jag använda hitta_server. Sen...
        for server in serverlista:
            if server["namn"].lower() == namn:
                server_hittad = True
                if server["miljo"] == "prod":
                    # Bekräftelse för prodmiljö
                    while True:
                        print()
                        bekraftelse = input("Denna server är i prodmiljö. Är du säker tryck retur."
                                         " (0 för att avbryta) " ).strip()
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
                print(f"Servern '{namn}' har tagits bort.")
                return

        if not server_hittad:
            print(f"Servern '{namn}' finns inte.")

        # Går vidare i yttre while-loopen och frågar efter servernaman
        if bekraftelse == "0":
            continue


# Har valt denna design för att eventuellt kunna återanvända funktionen.
# Returnera den första servern med matchande värde i nyckeln.
def hitta_server(serverlista, nyckel, sokvarde):

    for server in serverlista:
        if server[nyckel].lower() == sokvarde.lower():
            return server

    return None

# Returnera en lista av servrar med matchande värden i nyckeln.
def hitta_servrar_med_nyckel(serverlista, nyckel, sokvarde):
    resultatlista = []

    for server in serverlista:
        if server[nyckel].lower() == sokvarde.lower():
            resultatlista.append(server)

    return resultatlista

##### ----- Funktioner för att kontrollera servrar -----#####

# Anropas från menyn
def kontrollera_serverinput(serverlista):

    while True:
        print()
        namn = input("Ange servernamn (0 för att avbryta): ").strip().lower()

        # Återgå till huvudmenyn.
        if vill_avbryta(namn):
            return

        # Oavsett om servern finns eller ej, körs nästa varv i
        # while-loopen; användaren får möjlighet att försöka igen.
        server = kontrollera_server_med_namn(serverlista, namn)

        if server:
            continue
        else:
            print(f"Servern '{namn}' finns inte.")
            print()
            continue

def kontrollera_server_med_namn(serverlista, namn):

    server = hitta_server( serverlista, "namn", namn)

    if not server:
        return None

    print()
    print(f"{server['namn']} kontaktas...")
    print()
    print(f"{'Namn':<15}{'Status':<15}")

    kontrollera_status(server)
    skriv_ut_serverstatus(server)
    spara_servrar(serverlista)

    return server

# Anropa kontrollera_server för varje server i listan.
def kontrollera_alla_servrar(serverlista):
    print()
    print(f"{len(serverlista)} servrar kontaktas...")
    print()
    print(f"{'Namn':<15}{'Status':<15}")
    for server in serverlista:
        kontrollera_status(server)
        skriv_ut_serverstatus(server)

    spara_servrar(serverlista)

# Pinga och uppdatera status.
# Denna används både för att kontrollera en server och för att kontrollera alla
# samt från både textmeny och kommandorad.
def kontrollera_status(server):

    status = "unknown"

    # Om servern svarar, sätt status till up...
    if pinga_server(server['adress']):
        status = "up"
    # ...om inte, sätt status till down
    else:
        status = "down"

    # Uppdatera serverlistan
    uppdatera_data(server, "status", status)


# Uppdatera ett fält för en server.
# Har valt denna design för att kunna återanvända funktionen om andra fält än
# status kan komma att uppdateras.
def uppdatera_data(server, nyckel, nytt_varde):
    server[nyckel] = nytt_varde

    # Uppdatera tidpunkten när status ändras till en giltig status.
    if nyckel == "status" and nytt_varde in giltiga_statuskoder:
        server["senast_kontrollerad"] = datetime.now().strftime("%Y-%m-%d %H:%M")

# Denna används både för att kontrollera en server och för att kontrollera alla
# samt från både textmeny och kommandorad.
def skriv_ut_serverstatus(server):

    print(f"{server['namn']:<15}{server['status']:<15}")


