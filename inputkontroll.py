# inputkontroll.py
# Kontroller för input från användaren

# Giltiga menyval
giltiga_menyval = [0,1,2,3,4,5,6,7]

# Giltiga miljöer
giltiga_miljoer = ["test", "dev", "prod"]

# Giltiga statuskoder
giltiga_statuskoder = ["up", "down", "unknown"]

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
