

import csv
from datetime import datetime

# Funksjonen for å trekke ut dato og tid
def hent_ut_datetime(filnavn2):
    dato_tid_lister = []  # Liste for å lagre dato og tid i ønsket format

    with open(filnavn2, 'r', encoding='utf-8-sig') as file:  
        reader = csv.reader(file, delimiter=';')

        for row in reader:
            if row:  # Sjekk om raden ikke er tom (dette er for å unngå å behandle tomme linjer)
                dato_tid_str2 = row[2]  # Hent dato- og klokkeslettstrengen fra den tredje kolonnen

                # Sjekk om datostrengen er i rett format
                if len(dato_tid_str2) == 16 and dato_tid_str2[2] == '.' and dato_tid_str2[5] == '.' and dato_tid_str2[10] == ' ' and dato_tid_str2[13] == ':':
                    
                    # Konverter dato-og klokkeslett strenger til datetime-objekter
                    dato_tid_obj2 = datetime.strptime(dato_tid_str2, '%d.%m.%Y %H:%M')  # Formatet '%d.%m.%Y %H:%M'
                    
                    # Endre dato og tid formetat til ønsket format:
                    formatted_date_time = dato_tid_obj2.strftime('%d.%m.%Y %H:%M')
                    dato_tid_lister.append(formatted_date_time)  # Legg til den formaterte dato og tid
                else:
                    print(f"Skipping row due to invalid date format: {dato_tid_str2}")

    return dato_tid_lister  # Returner listen med dato og tid i ønsket format

filnavn2 = "/Users/lameeshabeeb/Library/Mobile Documents/com~apple~CloudDocs/Uni/BCH/Y1/DAT120/code/datafiler/temperatur_trykk_met_samme_rune_time_datasett.csv.txt"

dato_tid_liste = hent_ut_datetime(filnavn2)

print(f"Dato og tid: {dato_tid_liste}")
