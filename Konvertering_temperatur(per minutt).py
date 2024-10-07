
from Utskrift_dato import kolonne_tid
from Utskrift_sek import kolonne_sek
from Utskrift_temperatur import kolonne_temp 

def minutegjennomsnitt(data_list):
    # Dictionaries for å lagre total temperatur og antall avlesninger per minutt 
    minutt_data = {}   
    minutt_antall = {} 

    for entry in data_list:
        # Henter ut tidsstemplet, sekunder og temperatur 
        dato_tid = entry["dato_tid"]
        sek = entry["seconds"]  # Sekunder siden start
        temperatur = entry["temperatur"]

        # Hopp over hvis temperatur mangler 
        if temperatur == '':
            continue

        # Konverter temperatur til float og erstatt "," med "."
        temperatur = float(temperatur.replace(',', '.'))

        # Filter for gyldige sekunder (i.e., multipler av 10)
        if int(sek) % 10 != 0:
            continue

        # Hent ut "dato og minutt" delen av tidsstemplet 
        # f.eks., hvis dato_tid er "06.11.2021 14:23" -> "06.11.2021 14:23"
        minutt_key = dato_tid[:16]

        #Lager en nøkkel fra tidsstemplet, ved hjelp av både dato og minutt, for å gruppere alle data fra samme minutt.
        if minutt_key not in minutt_data:
            minutt_data[minutt_key] = 0
            minutt_antall[minutt_key] = 0

        #Holder en løpende sum av temperaturene og teller hvor mange avlesninger det er for hvert minutt.
        minutt_data[minutt_key] += temperatur
        minutt_antall[minutt_key] += 1

    # Beregn og skriv ut gjennomsnittelig temperatur per minutt  
    for minute, total_temperatur in minutt_data.items():
        gjennomsnittelig_temperatur = total_temperatur / minutt_antall[minute]
        print(f"Minute: {minute}, Average Temperature: {gjennomsnittelig_temperatur:.2f}")

# Lag datalisten ved å kombinere kolonne_temp, kolonne_tid og kolonne_sek
data_list = [{"dato_tid": kolonne_tid[i], "seconds": kolonne_sek[i], "temperatur": kolonne_temp[i]}
             for i in range(len(kolonne_tid))]

print("Processing data list:")
minutegjennomsnitt(data_list)
 
