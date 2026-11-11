# kontroller.py

from serverhantering import uppdatera_serverdata
# Standardbibliotek för att köra operativsystemskommandon.
# Här används det för att köra ping-kommandon.
import subprocess


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

# Returnerar True om servern svarar, annars False
# Används av både textmeny och CLI.
def pinga_server(adress):

    # Skickar ett ping-paket till servern
    resultat = subprocess.run(
        ["ping", "-c", "1", adress],
        # Följande rader döljer utskriften av serversvaret
        capture_output=True,
        text=True
    )

    # Om returncode blir 0, lyckades ping
    return resultat.returncode == 0