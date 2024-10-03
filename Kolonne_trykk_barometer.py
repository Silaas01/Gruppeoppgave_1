
import csv

def hent_kolonne_trykk1():
    kolonne_trykk1 = []  # Liste for å lagre verdiene i kolonnen

    # Åpne filen
    with open('C:/Users/Silje Aase/Documents/Dat120/Innleveringer/Gruppeoppg. 1/Ny datafiler/trykk_og_temperaturlogg_rune_time.csv.txt', 'r') as fil:
        csv_reader = csv.reader(fil, delimiter=';')  
        next(csv_reader)  # Hopper over overskriften

        # Iterer over hver rad i filen
        for rad in csv_reader:
            if len(rad) > 0:  # Sjekker at raden ikke er tom
                # Slå sammen alle kolonneverdiene til en streng
                rad_til_linje = " ".join(rad)

                # Sjekk om "am" eller "pm" finnes i hele linjen
                if "am" not in rad_til_linje and "pm" not in rad_til_linje:
                    kolonne_trykk1.append(rad[2])  # Legg til første kolonne hvis ikke "am" eller "pm" finnes i linjen
    return kolonne_trykk1  # Returner listen
