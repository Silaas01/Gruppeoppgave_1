

import csv
import numpy as np
import matplotlib.pyplot as plt
import datetime


with open('C:/Users/katri/.vscode/GitHub/Gruppeoppgave_1/temperatur_trykk_met_samme_rune_time_datasett.csv.txt', 'r') as solastasjon_csv:
    fil2_lines = solastasjon_csv.readlines()
with open('C:/Users/katri/.vscode/GitHub/Gruppeoppgave_1/trykk_og_temperaturlogg_rune_time.csv.txt', 'r') as uis_csv:
    fil1_lines = uis_csv.readlines()

# Oppretter dictionaries for å lagre Sola-data

fil2_name = []
fil2_station = []
fil2_time = []
fil2_temp = []
fil2_press = []

# Fyller inn verdier for Sola-dictionary

for line in fil2_lines[1:72]:
    name1, station1, time1, temp1, press1 = line.strip().split(";")

    # Konverter datoformatet fra norsk stil (DD.MM.YYYY HH:MM)
    try:
        fil2_date_obj = datetime.datetime.strptime(time1, "%d.%m.%Y %H:%M")
    except ValueError:
        print(f"Feil ved parsing av dato for Sola: {time1}")
        continue

    fil2_temp.append(float(temp1.replace(",", ".")))
    fil2_press.append(float(press1.replace(",", ".")))

    fil2_name.append(name1)
    fil2_station.append(station1)
    fil2_time.append(fil2_date_obj)


# Oppretter dictionaries for å lagre UiS-data

fil1_dates = []
fil1_time_since_start = []
fil1_press = []
fil1_abs_press = []
fil1_temp = []
fil1_temp_max_min = []
fil1_dates_max_min = []

# Fyller inn verdier for UiS-dictionary

for line in fil1_lines[1:20221]:
    date2, time_since_start2, press2, abs_press2, temp2 = line.strip().split(";")

    # Konverter datoformatet fra amerikansk stil (MM.DD.YYYY HH:MM)
    try:
        fil1_date_obj = datetime.datetime.strptime(date2, "%m.%d.%Y %H:%M")
    except ValueError:
        print(f"Feil ved parsing av dato for UIS: {date2}")
        continue

    fil1_dates.append(fil1_date_obj)

    fil1_temp.append(float(temp2.replace(",", ".")))
    fil1_abs_press.append(float(abs_press2.replace(",", ".")) * 10)

    # Sjekk om press2 inneholder en gyldig verdi før konvertering
    if press2:
        try:
            fil1_press.append(float(press2.replace(",", ".")) * 10)
        except ValueError:
            # Legg inn NaN hvis det er en ugyldig verdi
            fil1_press.append(np.nan)

    else:
        fil1_press.append(np.nan)  # Legg inn NaN hvis feltet er tomt

    if date2 == '06.11.2021 17:31':
        fil1_temp_max_min.append(float(temp2.replace(",", ".")))
        fil1_dates_max_min.append(fil1_date_obj)

    if date2 == '06.12.2021 03:05':
        fil1_temp_max_min.append(float(temp2.replace(",", ".")))
        fil1_dates_max_min.append(fil1_date_obj)

    fil1_time_since_start.append(time_since_start2)


def gjennomsnitt_temperatur(tider, temperaturer, n):
    tider1 = []
    gjennomsnittstemperaturer = []

    for i in range(n, len(temperaturer) - n):
        gjennomsnitt = sum(temperaturer[i-n:i+n+1]) / (2*n + 1)
        tider1.append(tider[i])
        gjennomsnittstemperaturer.append(gjennomsnitt)
    return tider1, gjennomsnittstemperaturer


tider2 = fil1_dates
temperaturer = fil1_temp

n = 30
tider1, gjennomsnittstemperaturer = gjennomsnitt_temperatur(
    tider2, temperaturer, n)


# Plotting av gjennomsnittstemperatur og original temperatur for UiS
plt.figure()
plt.plot(fil1_dates, fil1_temp, label='Original temperatur (UiS)', color='blue')
plt.plot(tider1, gjennomsnittstemperaturer,
         label='Gjennomsnittstemperatur (UiS)', color='orange')
plt.plot(fil1_dates_max_min, fil1_temp_max_min,
         label='Temperaturfall maksimal til minimal', color='purple')
plt.plot(fil2_time, fil2_temp, label='Temperatur (Sola)', color='green')
plt.xlabel('Tid (Dag, Måned, Timer)')
plt.ylabel('Temperatur (°C)')
plt.title('Temperatur ved UiS - original og glattet')
plt.legend()
plt.show()


# Plotting av trykk fra UiS og Sola
plt.figure()
plt.plot(fil2_time, fil2_press, color='orange')
plt.plot(fil1_dates, fil1_press, 'o-', color='green')
plt.plot(fil1_dates, fil1_abs_press, color='blue')
plt.xlabel('Tid (Dag, Måned, Timer)')
plt.ylabel('Trykk (Bar)')
plt.title('Trykk fra UiS og Sola')
plt.show()
