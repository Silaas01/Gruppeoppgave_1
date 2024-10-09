import matplotlib.pyplot as plt

# Funksjon for å lese trykkdata fra fil
def les_trykkdata(filnavn):
    trykk = []
    with open(filnavn, 'r') as fil:
        for linje in fil:
            trykk.append(linje.strip())  # Leser inn hver linje som den er
    return trykk

# Funksjon for å lese tidsdata fra fil
def les_tidsdata(filnavn):
    tid = []
    with open(filnavn, 'r') as fil:
        for linje in fil:
            tid.append(linje.strip())  # Leser tidsdata direkte uten konvertering
    return tid

# Filstier
trykk_file_1 = 'C:/Users/Silje Aase/Documents/Dat120/Innleveringer/Gruppeoppg. 1/Konvertering_trykk.py'
trykk_file_2 = 'C:/Users/Silje Aase/Documents/Dat120/Innleveringer/Gruppeoppg. 1/Fil2_Utskrift_Kolonne_trykk.py'
datetime_file_1 = 'C:/Users/Silje Aase/Documents/Dat120/Innleveringer/Gruppeoppg. 1/Strip_dato_tid_Fil1.py'
datetime_file_2 = 'C:/Users/Silje Aase/Documents/Dat120/Innleveringer/Gruppeoppg. 1/Strip_dato_tid_Fil2.py'

# Les trykk- og tidsdata fra filene
trykk_1 = les_trykkdata(trykk_file_1)
trykk_2 = les_trykkdata(trykk_file_2)
tid_1 = les_tidsdata(datetime_file_1)
tid_2 = les_tidsdata(datetime_file_2)

# Plotting av trykkdata mot tid
plt.figure(figsize=(10, 6))
plt.plot(tid_1, trykk_1, label='Værstasjon 1', color='blue')
plt.plot(tid_2, trykk_2, label='Værstasjon 2', color='green')

# Tilpasse plottet
plt.title('Trykk over tid fra to værstasjoner')
plt.xlabel('Tid (dag, time, minutt)')
plt.ylabel('Trykk (hPa)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)  # Roterer x-akse verdiene for å gjøre dem lettere å lese

# Vise plottet
plt.tight_layout()
plt.show()
