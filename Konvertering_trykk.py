from Utskrift_dato import kolonne_tid
from Utskrift_sek import kolonne_sek
from Utskrift_barometer_trykk import kolonne_trykk1 

def timegjennomsnitt(data_list):
    # Dictionaries for å lagre total trykk og antall avlesninger per time 
    time_data = {}   
    time_antall = {} 

    for entry in data_list:
        # Henter ut tidsstemplet, sekunder og barometer trykk 
        dato_tid = entry["dato_tid"]
        sek = entry["seconds"]  # Sekunder siden start
        barometer_trykk = entry["barometer_trykk"]

       #Hopp over hvis barometer trykk mangler 
        if barometer_trykk == '':
            continue

        # Konverter barometer trykk til float og erstatt ","
        barometer_trykk = float(barometer_trykk.replace(',', '.'))

        # Filter for gjyldige sekunder (i.e., multipler av 10)
        if int(sek) % 10 != 0:
            continue

        # Hent ut "dato og time" delen av tidsstemplet 
        # f.eks., hvis dato_tid er "06.11.2021 14:23" -> "06.11.2021 14"
        time_key = dato_tid[:13]

        # Still inn time key hvis den ikke finnes 
        if time_key not in time_data:
            time_data[time_key] = 0
            time_antall[time_key] = 0

        # Legg til trykk til timens total og øk tellingen
        time_data[time_key] += barometer_trykk
        time_antall[time_key] += 1

    # Beregn og skriv ut gjennomsnittelig barometer trykk per time  
    for hour, total_trykk in time_data.items():
        gjennomsnittelig_trykk = total_trykk / time_antall[hour]
        print(f"Hour: {hour}, Average Barometer Pressure: {gjennomsnittelig_trykk:.2f}")

#Lag datalisten ved å kombinere kolonne_trykk1, kolonne_tid og kolonne_sek
data_list = [{"dato_tid": kolonne_tid[i], "seconds": kolonne_sek[i], "barometer_trykk": kolonne_trykk1[i]}
             for i in range(len(kolonne_tid))]

print("Processing data list:")
timegjennomsnitt(data_list)
