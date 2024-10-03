
# Importer funksjonen fra det første scriptet
from Kolonne_sek import hent_kolonne_sek

# Hent verdiene fra den første scriptet
kolonne_sek = hent_kolonne_sek()

# Skriv ut listen
print("Verdiene i kolonne_sek:")
print(kolonne_sek)

for verdi in kolonne_sek:
    print(verdi)
