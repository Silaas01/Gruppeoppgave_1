import csv
from datetime import datetime

# Funksjonen for å trekke ut dato, time og minutt
def hent_ut_datetime(filnavn):
    dates = []   # Liste for å lagre datoene
    hours = []   # Liste for å lagre timene
    minutes = [] # Liste for å lagre minuttene

    with open(filnavn, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        
        for row in reader:
            if row:  # Sjekk om raden ikke er tom (dette er for å unngå å behandle tomme linjer)
                dato_tid_str1 = row[0]  
                
                # Konverter dato-og klokkeslett strenger til datetime-objekter
                dato_tid_obj1 = datetime.strptime(dato_tid_str1, '%d.%m.%Y %H:%M')  # Formatet '%d.%m.%Y %H:%M' spesifiserer at datoen er i formatet: DD.MM.ÅÅÅÅ TT:MM(f.eks. '06.11.2021 14:23')

                # Legg til de ekstraherte verdiene i listene
                dates.append(dato_tid_obj1.date())   # Legg til dato
                hours.append(dato_tid_obj1.hour)     # Legg til time
                minutes.append(dato_tid_obj1.minute)  # Legg til minutt

    return dates, hours, minutes  # Returner lister med ekstraherte verdier


