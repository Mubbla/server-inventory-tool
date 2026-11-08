# kontroller.py

# Standardbibliotek för att köra operativsystemskommandon.
# Här används det för att köra ping-kommandon.
import subprocess

##----    Kontroller för input från användaren    ----##

# Giltiga menyval
giltiga_menyval = [0,1,2,3,4,5,6,7]

# Giltiga miljöer
giltiga_miljoval = ["test", "dev", "prod"]

# Giltiga statuskoder behövs inte till något i nuläget
# giltiga_statuskoder = ["up", "down", "unknown"]

# Jämför input med giltiga värden och returnerar True om input är giltigt.
def validate_choice(input, giltiga_varden):

    for choice in giltiga_varden:
        if choice == input:
            return True

    return False

# Returnerar True om användaren matat in 0.
def vill_avbryta(indata):
    # Fångar ValueError om input innehåller sträng
    try:
        if int(indata) == 0:
            return True
        else:
            return False

    except ValueError:
        return False


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