from Utskrift_dato import kolonne_tid
from Utskrift_sek import kolonne_sek
from Utskrift_barometer_trykk import kolonne_trykk1 

def minutegjennomsnitt(data_list):
    # Dictionaries for å lagre total trykk og antall avlesninger per minutt 
    minutt_data = {}   
    minutt_antall = {} 

    for entry in data_list:
        # Henter ut tidsstemplet, sekunder og barometer trykk 
        dato_tid = entry["dato_tid"]
        sek = entry["seconds"]  # Sekunder siden start
        barometer_trykk = entry["barometer_trykk"]

        # Hopp over hvis barometer trykk mangler 
        if barometer_trykk == '':
            continue

        # Konverter barometer trykk til float og erstatt "," med "."
        barometer_trykk = float(barometer_trykk.replace(',', '.'))

        # Filter for gyldige sekunder (i.e., multipler av 10)
        if int(sek) % 10 != 0:
            continue

        # Hent ut "dato og minutt" delen av tidsstemplet 
        # f.eks., hvis dato_tid er "06.11.2021 14:23" -> "06.11.2021 14:23"
        minutt_key = dato_tid[:16]

        #Lager en nøkkel fra tidsstemplet (bruker både dato og minutt) for å gruppere alle data fra samme minutt.
        if minutt_key not in minutt_data:
            minutt_data[minutt_key] = 0
            minutt_antall[minutt_key] = 0

        #Holder en løpende sum av barometertrykket og teller hvor mange avlesninger det er for hvert minutt.
        minutt_data[minutt_key] += barometer_trykk
        minutt_antall[minutt_key] += 1

    # Beregn og skriv ut gjennomsnittelig barometer trykk per minutt  
    for minute, total_trykk in minutt_data.items():
        gjennomsnittelig_trykk = total_trykk / minutt_antall[minute]
        print(f"Minute: {minute}, Average Barometer Pressure: {gjennomsnittelig_trykk:.2f}")

# Lag datalisten ved å kombinere kolonne_trykk1, kolonne_tid og kolonne_sek
data_list = [{"dato_tid": kolonne_tid[i], "seconds": kolonne_sek[i], "barometer_trykk": kolonne_trykk1[i]}
             for i in range(len(kolonne_tid))]

print("Processing data list:")
minutegjennomsnitt(data_list)
