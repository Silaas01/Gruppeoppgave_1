import csv

def hent_kolonne_tid():
    kolonne_tid = []  # Liste for å lagre verdiene i kolonnen

    # Åpne filen
    with open('C:/Users/Silje Aase/Documents/Dat120/Innleveringer/Gruppeoppg. 1/Ny datafiler/temperatur_trykk_met_samme_rune_time_datasett.csv.txt', 'r') as fil:
        csv_reader = csv.reader(fil, delimiter=';')  
        next(csv_reader)  # Hopper over overskriften

        # Iterer over hver rad i filen
        for rad in csv_reader:
            if len(rad) > 0:  # Sjekker at raden ikke er tom
                kolonne_tid.append(rad[2])  # Legg til første kolonne hvis ikke "am" eller "pm" finnes i linjen

    return kolonne_tid  # Returner listen