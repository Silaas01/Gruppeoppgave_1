# Importer funksjonen fra det første scriptet
from Kolonne_absolutt_trykk import hent_kolonne_trykk2

# Hent verdiene fra den første scriptet
hent_kolonne_trykk2 = hent_kolonne_trykk2()

# Skriv ut listen
print("Verdiene i kolonne_trykk2:")
print(hent_kolonne_trykk2)

for verdi in hent_kolonne_trykk2:
    print(verdi)
