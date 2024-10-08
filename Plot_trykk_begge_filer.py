import matplotlib.pyplot as plt

from Konvertering_trykk import data_list
from Fil2_Utskrift_Kolonne_trykk import kolonne_trykk
from Strip_dato_tid_Fil1 import extracted_datetimes
from Strip_dato_tid_Fil2 import dato_tid_liste

datoer_fil1 = extracted_datetimes
datoer_fil2 = dato_tid_liste

# Opprett figuren og aksene
plt.figure(figsize=(12, 6))

# Plott data fra den første filen
plt.plot(datoer_fil1, kolonne_trykk, label='Trykk fra Stasjon UiS', color='blue', marker='o')
# Plott data fra den andre filen
plt.plot(datoer_fil2, kolonne_trykk, label='Trykk fra Stasjon Sola', color='orange', marker='o')

plt.plot(datoer_fil1[:len(filtered_data)], filtered_data, label='Filtrert Trykk', color='green', marker='x')

# Formater x-aksen for å vise datoer bedre
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d.%m.%Y %H:%M'))
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=1))  # Vis hver time
plt.gcf().autofmt_xdate()  # Rotér datoene for bedre lesbarhet

# Legg til tittel og akseetiketter
plt.title('Trykk fra To Værstasjoner')
plt.xlabel('Tid')
plt.ylabel('Trykk (hPa)')
plt.legend()
plt.grid()

# Vis plottet
plt.tight_layout()
plt.show()