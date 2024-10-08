
from datetime import datetime
from Konvertering_temp_per_min import data_list  # Importerer listen fra konvertert datafil script

# Funksjonen for å trekke ut dato og klokkeslett fra en liste av ordbøker
def hent_ut_datetime(data_list):
    datetime_set = set()  # Bruker et sett for å unngå duplikater

    for entry in data_list:
        dato_tid_str1 = entry["dato_tid"]  # Extract the date and time string from the dictionary
        
        # Sjekekr at lengden og spesifikke tegnplasseringer er riktige. Hvis noen av disse betingelsene ikke er oppfylt, vil konverteringsprosessen bli hoppet over for entry
        if len(dato_tid_str1) == 16 and dato_tid_str1[2] == '.' and dato_tid_str1[5] == '.' and dato_tid_str1[13] == ':': 
            # Konverter dato-og klokkeslett strenger til datetime-objekter
            dato_tid_obj1 = datetime.strptime(dato_tid_str1, '%d.%m.%Y %H:%M')  # Formatet "%d.%m.%Y %H:%M" f.eks. "06.12.2021 23:58"

            # Legg til den ekstraherte datoen og klokkeslettet som en streng i settet
            datetime_set.add(dato_tid_obj1.strftime('%d.%m.%Y %H:%M'))  # Legg til dato og klokkeslett som en streng

    # Returner en sortert liste med unike datoer og klokkeslett
    return sorted(list(datetime_set))

# Hent ut dato og klokkeslett fra den importerte listen
extracted_datetimes = hent_ut_datetime(data_list)

# Skriv ut resultatene
print(extracted_datetimes)
