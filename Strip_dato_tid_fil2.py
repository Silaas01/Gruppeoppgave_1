import csv
from datetime import datetime

# Funksjonen for å trekke ut dato, time og minutt
def hent_ut_datetime(filnavn):
    datoer = []   # Liste for å lagre datoene
    timer = []   # Liste for å lagre timene
    minutter = [] # Liste for å lagre minuttene

    with open(filnavn, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        
        for row in reader:
            if row:  # Sjekk om raden ikke er tom (dette er for å unngå å behandle tomme linjer)
                dato_tid_str2 = row[0]  
                
                # Konverter dato-og klokkeslett strenger til datetime-objekter
                dato_tid_obj2 = datetime.strptime(dato_tid_str2, '%d.%m.%Y %H:%M')  # Formatet '%d.%m.%Y %H:%M' spesifiserer at datoen er i formatet: DD.MM.ÅÅÅÅ TT:MM(f.eks. '06.11.2021 14:23')

                # Legg til de ekstraherte verdiene i listene
                datoer.append(dato_tid_obj2.date())   # Legg til dato
                timer.append(dato_tid_obj2.hour)     # Legg til time
                minutter.append(dato_tid_obj2.minute)  # Legg til minutt

    return datoer, timer, minutter  # Returner lister med ekstraherte verdier
