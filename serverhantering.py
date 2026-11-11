# serverhantering.py

from datetime import datetime
from inputkontroll import giltiga_statuskoder

# Har valt denna design för att eventuellt kunna återanvända funktionen.
# Returnera den första servern med matchande värde i nyckeln.
def hitta_server(serverlista, nyckel, sokvarde):

    for server in serverlista:
        if server[nyckel].lower() == sokvarde.lower():
            return server

    return None

# Har valt denna design för att eventuellt kunna återanvända funktionen.
# Returnera en lista av servrar med matchande värden i nyckeln.
def hitta_servrar_med_nyckel(serverlista, nyckel, sokvarde):
    resultatlista = []

    for server in serverlista:
        if server[nyckel].lower() == sokvarde.lower():
            resultatlista.append(server)

    return resultatlista

# Uppdatera ett fält för en server.
# Har valt denna design för att kunna återanvända funktionen om andra fält än
# status kan komma att uppdateras.
def uppdatera_serverdata(server, nyckel, nytt_varde):

    server[nyckel] = nytt_varde

    # Uppdatera tidpunkten när status ändras till en giltig status.
    if nyckel == "status" and nytt_varde in giltiga_statuskoder:
        server["senast_kontrollerad"] = datetime.now().strftime("%Y-%m-%d %H:%M")