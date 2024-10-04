# Importer funksjonen fra det første scriptet
from Fil2_Kolonne_trykk import hent_kolonne_trykk

# Hent verdiene fra den første scriptet
kolonne_trykk = hent_kolonne_trykk()

# Skriv ut listen
print("Verdiene i kolonne_trykk:")
print(kolonne_trykk)

# Du kan nå bruke kolonne_tid-listen til hva du vil
# Eksempel: iterere over elementene og skrive dem ut
for verdi in kolonne_trykk:
    print(verdi)
