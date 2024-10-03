# Importer funksjonen fra det første scriptet
from Kolonne_temperatur import hent_kolonne_temp

# Hent verdiene fra den første scriptet
hent_kolonne_temp = hent_kolonne_temp()

# Skriv ut listen
print("Verdiene i kolonne_temp:")
print(hent_kolonne_temp)

for verdi in hent_kolonne_temp:
    print(verdi)