# Importer funksjonen fra det første scriptet
from FIl2_Kolonne_temperatur import hent_kolonne_temp

# Hent verdiene fra den første scriptet
kolonne_temp = hent_kolonne_temp()

# Skriv ut listen
print("Verdiene i kolonne_temp:")
print(kolonne_temp)

# Du kan nå bruke kolonne_tid-listen til hva du vil
# Eksempel: iterere over elementene og skrive dem ut
for verdi in kolonne_temp:
    print(verdi)
