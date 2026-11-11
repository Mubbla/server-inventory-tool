# inputkontroll.py

# Kontroller för input från användaren

# Giltiga menyval
giltiga_menyval = [0,1,2,3,4,5,6,7]

# Giltiga miljöer
giltiga_miljoer = ["test", "dev", "prod"]

# Giltiga statuskoder
giltiga_statuskoder = ["up", "down", "unknown"]

# Jämför input med giltiga värden och returnerar True om input är giltigt.
def validera_val(indata, giltiga_varden):

    for varde in giltiga_varden:
        if varde == indata:
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

# Returnerar True om namnet inte är tomt och inte innehåller blanktecken.
def servernamn_ar_giltigt(namn):
    return bool(namn) and not any(tecken.isspace() for tecken in namn)
