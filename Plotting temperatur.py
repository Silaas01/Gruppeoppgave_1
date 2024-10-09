import matplotlib.pyplot as plt
import matplotlib.dates as mdates  # Import mdates for date formatting
import matplotlib.ticker as mticker
from datetime import datetime

from Konvertering_temperatur_per_min import data_list
from Utskrift_kolonne_temperatur import kolonne_temp
from Strip_dato_tid_fil1 import hentet_datetimes
from Strip_dato_tid_fil2 import dato_tid_liste

# Get the date lists
datoer_fil1 = hentet_datetimes
datoer_fil2 = dato_tid_liste

# Sjekk innholdet i datoene
print("Datoer fra Fil 1:")
print(datoer_fil1[:5])  # Skriv ut de første 5 datoene

print("Datoer fra Fil 2:")
print(datoer_fil2[:5])  # Skriv ut de første 5 datoene

# Konverter datoer til datetime
def convert_dates(dates):
    converted_dates = []
    for dato in dates:
        try:
            # Hvis datoen allerede er i datetime-format, så bruk den direkte
            if isinstance(dato, datetime):
                converted_dates.append(dato)
            else:
                # Hvis datoen er i formatet 'dd HH:MM', anta standard måned og år
                # F.eks. '11 14:00' blir '2023-10-11 14:00'
                dato = dato.strip()  # Fjerne unødvendige mellomrom
                month = 10  # Standard måned
                year = 2023  # Standard år
                # Anta at datoen er i formatet 'dd HH:MM'
                day_hour_minute = dato.split()
                if len(day_hour_minute) == 2:
                    day = int(day_hour_minute[0])
                    hour_minute = day_hour_minute[1]
                    converted_date = datetime(year, month, day, *map(int, hour_minute.split(':')))
                    converted_dates.append(converted_date)
                else:
                    print(f"Uventet datoformat: {dato}")
        except ValueError as e:
            print(f"Feil ved konvertering av dato: {dato}. Feilmelding: {e}")
    return converted_dates

# Konverter datoene
datoer_fil1 = convert_dates(datoer_fil1)
datoer_fil2 = convert_dates(datoer_fil2)

# Konverter pressedata til float
kolonne_temp_clean = [float(temp.replace(',', '.')) for temp in kolonne_temp 
                       if isinstance(temp, (int, float, str)) and str(temp).replace(',', '').replace('.', '', 1).isdigit()]

# Debug: print lengths of the data
print(f"Length of datoer_fil1: {len(datoer_fil1)}")
print(f"Length of datoer_fil2: {len(datoer_fil2)}")
print(f"Length of kolonne_temp_clean: {len(kolonne_temp_clean)}")

# Ensure the lengths match between dates and pressures
min_length = min(len(datoer_fil1), len(datoer_fil2), len(kolonne_temp_clean))
filtered_data = kolonne_temp_clean[:min_length]  # Ensure the lengths match for plotting

# Debug: print sample data to verify everything looks correct
print(f"Sample from datoer_fil1: {datoer_fil1[:5]}")
print(f"Sample from datoer_fil2: {datoer_fil2[:5]}")
print(f"Sample from kolonne_trykk_clean: {kolonne_temp_clean[:5]}")

# Create the plot
plt.figure(figsize=(12, 6))

# Plot data from the first file
plt.plot(datoer_fil1[:min_length], kolonne_temp_clean[:min_length], label='Temperatur fra Stasjon UiS', color='blue', marker='o')

# Plot data from the second file
plt.plot(datoer_fil2[:min_length], kolonne_temp_clean[:min_length], label='Temperatur fra Stasjon Sola', color='orange', marker='o')

# Optionally plot filtered data
plt.plot(datoer_fil1[:min_length], filtered_data, label='Filtrert Temperatur', color='green', marker='x')

# Format x-axis for better date visibility
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d.%m.%Y %H:%M'))

# Set major locator to show a tick every 12 hours (adjust this as necessary)
plt.gca().xaxis.set_major_locator(mticker.MaxNLocator(20))

# Rotate the x-axis labels for better readability
plt.gcf().autofmt_xdate(rotation=45)

# Add title and axis labels
plt.title('Temperatur fra To Værstasjoner')
plt.xlabel('Tid')
plt.ylabel('Temperatur (oC)')
plt.legend()
plt.grid()

# Show the plot
plt.tight_layout()
plt.show()
