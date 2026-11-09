# kontroller.py

# Standardbibliotek för att köra operativsystemskommandon.
# Här används det för att köra ping-kommandon.
import subprocess


##----    Kontroller för servrarna    ----##

# Returnerar True om servern svarar, annars False
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