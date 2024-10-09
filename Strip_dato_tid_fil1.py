

from datetime import datetime
from Konvertering_temp_per_min import data_list  # Importerer listen fra konvertert datafil script

# Funksjonen for å trekke ut dato og klokkeslett fra en liste av ordbøker
def hent_ut_dato_tid(data_list):
    dato_tid_set = set()  # Bruker et sett for å unngå duplikater

    for entry in data_list:
        dato_tid_str1 = entry["dato_tid"]  # Trekk ut dato- og klokkeslettstrengen fra ordboken
        
        # Sjekker at lengden og spesifikke tegnplasseringer er riktige
        if len(dato_tid_str1) == 16 and dato_tid_str1[2] == '.' and dato_tid_str1[5] == '.' and dato_tid_str1[13] == ':': 
            # Konverter dato-og klokkeslett strenger til datetime-objekter
            dato_tid_obj1 = datetime.strptime(dato_tid_str1, '%d.%m.%Y %H:%M')  # Formatet "%d.%m.%Y %H:%M"

            # Legg til den ekstraherte datoen og klokkeslettet som en streng i settet, nå som DD HH:MM
            dato_tid_set.add(dato_tid_obj1.strftime("%d %H:%M"))  # Format: DD HH:MM

    # Returner en sortert liste med unike datoer og klokkeslett
    return sorted(list(dato_tid_set))

# Hent ut dato og klokkeslett fra den importerte listen
hentet_datetimes = hent_ut_dato_tid(data_list)

print("Dato og tid:")
for datetime_str in hentet_datetimes: #Skriv ut hver dato og klokkeslett fra listen på en egen linje
    print(datetime_str)
