import csv

def hent_kolonne_temp():
    kolonne_temp = []  # Liste for å lagre verdiene i kolonnen

    # Åpne filen
    with open('C:/Users/Silje Aase/Documents/Dat120/Innleveringer/Gruppeoppg. 1/Ny datafiler/temperatur_trykk_met_samme_rune_time_datasett.csv.txt', 'r') as fil:
        csv_reader = csv.reader(fil, delimiter=';')  
        next(csv_reader)  # Hopper over overskriften

        # Iterer over hver rad i filen
        for rad in csv_reader:
            if len(rad) > 0:  # Sjekker at raden ikke er tom
                # Slå sammen alle kolonneverdiene til en streng
                rad_til_linje = " ".join(rad)

            # Sjekk om "am" eller "pm" finnes i hele linjen
            if "13." not in rad_til_linje and "14." not in rad_til_linje:
                kolonne_temp.append(rad[3])  # Legg til første kolonne hvis ikke "13." finnes i linjen


    return kolonne_temp  # Returner listen
