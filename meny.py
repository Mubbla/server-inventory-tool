# meny.py

from inputkontroll import (giltiga_menyval, giltiga_miljoer,
                        vill_avbryta, validera_val,servernamn_ar_giltigt)
from kontroller import pinga_server
from lagring import spara_servrar, exportera_rapporter
from serverhantering import hitta_server, hitta_servrar_med_nyckel, uppdatera_serverdata

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
        if validera_val(val, giltiga_menyval):

            if val == 1:
                visa_servrar(serverlista)

            elif val == 2:
                hantera_input_miljo(serverlista)

            elif val == 3:
                lagg_till(serverlista)

            elif val == 4:
                ta_bort_server(serverlista)

            elif val == 5:
                hantera_input_servernamn(serverlista)

            elif val == 6:
                kontrollera_alla_servrar(serverlista)

            elif val == 7:
                exportera_rapporter(serverlista)

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
    print("   7. Exportera rapporter         ")
    print("   0. Avsluta                     ")
    print("==================================")
    print("")

# Funktion för att skriva ut alla servrar i en lista.
# Används av både textmeny och CLI.
def visa_servrar(serverlista):
    print()
    print(f"{'Namn':<15}{'Adress':<15}{'Miljö':<15}"
          f"{'Roll':<20}{'Status':<15}{'Senast kontrollerad'}")
    print()
    for server in serverlista:
        print(f"{server['namn']:<15}{server['adress']:<15}{server['miljo']:<15}"
              f"{server['roll']:<20}{server['status']:<15}{server['senast_kontrollerad']}")

# Inputkontroll - ska lägga till meddelande om inga servrar i miljö
def hantera_input_miljo(serverlista):

    while True:
        print()
        miljo = (input("Ange miljö (dev/test/prod) (0 för att avbryta): ").strip().lower())

        # Kontrollera om användaren vill återgå till huvudmenyn. Avslutar isåfall funktionen.
        if vill_avbryta(miljo):
            return

        # Avbryt detta varv för att återgå till inmatning av miljo/0.
        if miljo == "" or miljo not in giltiga_miljoer:
            print("Ogiltigt värde.")
            continue

        visa_servrar_i_miljo(serverlista, "miljo", miljo)


# Hitta och skriv ut alla servrar i en miljö.
# Används av både textmeny och CLI.
def visa_servrar_i_miljo (serverlista, nyckel, varde):

    # Hämta servrarna för aktuell miljö.
    servrar_i_miljo = hitta_servrar_med_nyckel(serverlista, nyckel, varde)

    if servrar_i_miljo:
        visa_servrar(servrar_i_miljo)
    else:
        print(f"Inga servrar hittades i miljön '{varde}'.")

# Funktion för att lägga till en ny server
def lagg_till(serverlista):

    # Servernamn
    while True:
        namn = (input("Ange serverns namn (0 för att avbryta): ").strip().lower())

        # Om användaren vill avbryta, avsluta funktionen.
        if vill_avbryta(namn):
            return

        # Avbryt detta varv för att återgå till inmatning av namn/0.
        if not servernamn_ar_giltigt(namn):
            print("Namnet får inte vara tomt eller innehålla blanktecken.")
            continue

        # Om servern redan finns, avbryt detta varv för att återgå till inmatning av namn/0.
        if hitta_server(serverlista, "namn", namn):
            continue

        # Avbryt while-loop när allt är rätt och gå vidare
        break

    # Adress
    while True:
        adress = input("Ange serverns adress (0 för att avbryta): ").strip()

        # Kontrollera om användaren vill återgå till huvudmenyn. Avslutar isåfall funktionen.
        if vill_avbryta(adress):
            return

        if adress == "":
            print("Adress får inte vara tom.")
            continue

        break

    # Miljö
    while True:
        miljo = input("Ange miljö (dev/test/prod) (0 för att avbryta): ").strip().lower()

        # Kontrollera om användaren vill återgå till huvudmenyn. Avslutar isåfall funktionen.
        if vill_avbryta(miljo):
            return

        # Kontrollera att input finns som giltigt värde.
        if validera_val(miljo, giltiga_miljoer):
            break

        print("Ogiltig miljö.")

    # Roll
    while True:
        roll = input("Ange serverns roll (0 för att avbryta): ").strip()

        # Kontrollera om användaren vill återgå till huvudmenyn. Avslutar isåfall funktionen.
        if vill_avbryta(roll):
            return

        if roll == "":
            print("Roll får inte vara tomt.")
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
        print()
        namn = (input("Ange vilken server vill du ta bort (0 för att avbryta): ").strip().lower())

        # Kontrollera om användaren vill återgå till huvudmenyn. Avslutar isåfall funktionen.
        if vill_avbryta(namn):
            return

        if not servernamn_ar_giltigt(namn):
            print("Namn får inte vara tomt/innehålla blanktecken.")
            continue

        server = hitta_server(serverlista, "namn", namn)

        # Om servern inte hittas...
        if server is None:
            print(f"Servern '{namn}' finns inte.")
            # ...fråga efter ett nytt namn i while-loopen
            continue

        if server["miljo"] == "prod":
            vill_ta_bort_i_prod = False
            # Bekräftelse för prodmiljö
            while True:
                print()
                #
                svar = input(
                    "Servern är i prodmiljö. Tryck Retur för att bekräfta (0 för att avbryta): ").strip()
                # Användaren har bekräftat. Avsluta bekräftelsens while-loop.
                if svar == "":
                    vill_ta_bort_i_prod = True
                    break
                # Om användaren vill avbryta ...
                elif svar == "0":
                    # ...avbryt bekräftelse-loopen.
                    break
                # Om användaren skrivit ett ogiltigt värde...
                else:
                    print("Ogiltigt val.")
                    # ... fråga om bekräftelse igen.
                    continue

            if not vill_ta_bort_i_prod:
                # ...fortsätt yttre while-loop och fråga efter ett nytt servernamn.
                continue

        # Servern finns. Användaren har bekräftat om prod-miljö. Ta bort servern. Avsluta funktionen.
        serverlista.remove(server)
        spara_servrar(serverlista)
        print()
        print(f"Servern '{namn}' har tagits bort.")
        # Fortsätt yttre while-loop och fråga efter ytterligare en server.


# Anropas från menyn
def hantera_input_servernamn(serverlista):

    while True:
        print()
        namn = input("Ange servernamn (0 för att avbryta): ").strip().lower()

        # Återgå till huvudmenyn.
        if vill_avbryta(namn):
            return

        # Oavsett om servern finns eller ej, körs nästa varv i
        # while-loopen; användaren får möjlighet att försöka igen.
        kontrollera_server_med_namn(serverlista, namn)

# Kontrollera en server.
# Används av både textmeny och CLI.
def kontrollera_server_med_namn(serverlista, namn):

    server = hitta_server( serverlista, "namn", namn)

    if not server:
        print(f"Servern '{namn}' finns inte.")
        print()
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
# Används av både textmeny och CLI.
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
# Denna används både för att kontrollera en server och för att kontrollera alla.
def kontrollera_status(server):

    status = "unknown"

    # Om servern svarar, sätt status till up...
    if pinga_server(server['adress']):
        status = "up"
    # ...om inte, sätt status till down
    else:
        status = "down"

    # Uppdatera serverlistan
    uppdatera_serverdata(server, "status", status)



# Denna används både för att kontrollera en server och för att kontrollera alla.
def skriv_ut_serverstatus(server):

    print(f"{server['namn']:<15}{server['status']:<15}")


