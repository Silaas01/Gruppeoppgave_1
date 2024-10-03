
# Importer funksjonen fra det første scriptet
from Fil2_Kolonne_tid import hent_kolonne_tid

# Hent verdiene fra den første scriptet
kolonne_tid = hent_kolonne_tid()

# Skriv ut listen
print("Verdiene i kolonne_tid:")
print(kolonne_tid)

# Du kan nå bruke kolonne_tid-listen til hva du vil
# Eksempel: iterere over elementene og skrive dem ut
for verdi in kolonne_tid:
    print(verdi)
