import matplotlib.pyplot as plt
import matplotlib.dates as mdates  # Import mdates for date formatting
import matplotlib.ticker as mticker

from Konvertering_trykk import data_list
from Utskrift_fil2_kolonne_trykk import kolonne_trykk
from Strip_dato_tid_fil1 import hentet_datetimes
from Strip_dato_tid_fil2 import dato_tid_liste

# Get the date lists
datoer_fil1 = hentet_datetimes
datoer_fil2 = dato_tid_liste

# Convert pressures to float, handling commas and ensuring valid numbers
kolonne_trykk_clean = [float(temp.replace(',', '.')) for temp in kolonne_trykk 
                       if isinstance(temp, (int, float, str)) and str(temp).replace(',', '').replace('.', '', 1).isdigit()]

# Debug: print lengths of the data
print(f"Length of datoer_fil1: {len(datoer_fil1)}")
print(f"Length of datoer_fil2: {len(datoer_fil2)}")
print(f"Length of kolonne_trykk_clean: {len(kolonne_trykk_clean)}")

# Ensure the lengths match between dates and pressures
min_length = min(len(datoer_fil1), len(datoer_fil2), len(kolonne_trykk_clean))
filtered_data = kolonne_trykk_clean[:min_length]  # Ensure the lengths match for plotting

# Debug: print sample data to verify everything looks correct
print(f"Sample from datoer_fil1: {datoer_fil1[:5]}")
print(f"Sample from datoer_fil2: {datoer_fil2[:5]}")
print(f"Sample from kolonne_trykk_clean: {kolonne_trykk_clean[:5]}")

# Create the plot
plt.figure(figsize=(12, 6))

# Plot data from the first file
plt.plot(datoer_fil1[:min_length], kolonne_trykk_clean[:min_length], label='Trykk fra Stasjon UiS', color='blue', marker='o')

# Plot data from the second file
plt.plot(datoer_fil2[:min_length], kolonne_trykk_clean[:min_length], label='Trykk fra Stasjon Sola', color='orange', marker='o')


# Optionally plot filtered data
plt.plot(datoer_fil1[:min_length], filtered_data, label='Filtrert Trykk', color='green', marker='x')

# Format x-axis for better date visibility
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d.%m.%Y %H'))

# Set major locator to show a tick every 12 hours (adjust this as necessary)
plt.gca().xaxis.set_major_locator(mticker.MaxNLocator(20))

# Rotate the x-axis labels for better readability
plt.gcf().autofmt_xdate(rotation=45)

# Add title and axis labels
plt.title('Trykk fra To Værstasjoner')
plt.xlabel('Tid')
plt.ylabel('Trykk (hPa)')
plt.legend()
plt.grid()

# Show the plot
plt.tight_layout()
plt.show()
