from Split_konvertert_tid import tid_kolonne  
from Split_konverter_temp import temperatur_kolonne  

# Sikrer at hver temperatur konverteres til en flyte, og at bare gyldige numeriske verdier (int, float eller strenger som kan konverteres) er inkludert.
temperaturer = [float(temp.replace(',', '.')) for temp in temperatur_kolonne 
                if isinstance(temp, (int, float, str)) and str(temp).replace('.', '', 1).isdigit()]

# Sikrer at hver tid konverteres til en gyldig type.
tidspunkt = [tid for tid in tid_kolonne if isinstance(tid, (str, int, float))]

def beregn_gjennomsnitt(tidspunkt, temperaturer, n):
    gyldige_tidspunkt = []  # Tom liste for å lagre gyldige tidspunkter
    gjennomsnittelige_verdier = []  # Tom liste for å lagre gjennomsnittlige temperaturverdier

    # Gå gjennom gyldige utvalgte indekser for gjennomsnittsberegning
    for i in range(n, len(temperaturer) - n):
        # 'i' varierer fra n til "len(temperaturer) - n" for å sikre at vi ikke går utenfor grensene.
        
        maalinger = temperaturer[i-n:i+n+1]  # Slicing:temperature listen for å få de n forrige,nåværende, og de n neste målingene

        gjenn = sum(maalinger) / len(maalinger)  # Beregn gjennomsnittet av målingene

        # Legg til det tilsvarende gyldige tidsstempelet og det beregnede gjennomsnittete
        gyldige_tidspunkt.append(tidspunkt[i])  # Lagre tilsvarende tidspunktet fra 'tid_kolonne'
        gjennomsnittelige_verdier.append(gjenn)  # Lagre gjennomsnittstemperatur verdien 

    return gyldige_tidspunkt, gjennomsnittelige_verdier
    # Returner listene over gyldige tidspunkter og gjennomsnittstemperatur verdier

# Eksempel på å bruke funksjonen
n = 30  # Antall målinger å inkludere før og etter
gyldige_tidspunkt, gjennomsnittlige_temperaturer = beregn_gjennomsnitt(tidspunkt, temperaturer, n)

# Lagre resultatene i lister for plotting 
resultat_tidspunkter = gyldige_tidspunkt
resultat_temperaturer = gjennomsnittlige_temperaturer

