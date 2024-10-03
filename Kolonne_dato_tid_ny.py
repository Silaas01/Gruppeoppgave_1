
import csv

def hent_kolonne_tid():
    kolonne_tid = []  # Liste for å lagre verdiene i kolonnen

    # Åpne filen
    with open('C:/Users/Silje Aase/Documents/Dat120/Innleveringer/Gruppeoppg. 1/Ny datafiler/trykk_og_temperaturlogg_rune_time.csv.txt', 'r') as fil:
        csv_reader = csv.reader(fil, delimiter=';')  
        next(csv_reader)  # Hopper over overskriften

        # Iterer over hver rad i filen
        for rad in csv_reader:
            if len(rad) > 0:  # Sjekker at raden ikke er tom
                kolonne_verdi = rad[0]  # Henter første kolonne
                if "am" not in kolonne_verdi and "pm" not in kolonne_verdi: 
                    kolonne_tid.append(kolonne_verdi)  #Legg til hvis "am" eller "pm" ikke finnes

    return kolonne_tid  # Returner listen
