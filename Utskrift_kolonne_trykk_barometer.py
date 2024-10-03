# Importer funksjonen fra det første scriptet
from Kolonne_trykk_barometer import hent_kolonne_trykk1

# Hent verdiene fra den første scriptet
kolonne_trykk1 = hent_kolonne_trykk1()

# Skriv ut listen
print("Verdiene i kolonne_trykk1:")
print(kolonne_trykk1)

for verdi in kolonne_trykk1:
    print(verdi)
