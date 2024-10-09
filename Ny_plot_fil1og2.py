import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from datetime import datetime

# Importing data processing functions
from Konvertering_trykk_per_min import data_list  # Ensure this is the correct import
from Utskrift_fil2_kolonne_trykk import kolonne_trykk
from Strip_dato_tid_fil1 import hentet_datetimes  # This should import the function
from Strip_dato_tid_fil2 import dato_tid_liste  # Ensure this is also a function

# Get the date lists
datoer_fil1 = hentet_datetimes()  # Call the function to get dates from file 1
datoer_fil2 = dato_tid_liste()      # Call the function to get dates from file 2

# Ensure that datoer_fil1 and datoer_fil2 are in datetime format
datoer_fil1 = [datetime.strptime(date, '%d %H:00') for date in datoer_fil1]  # Adjust the format as needed
datoer_fil2 = [datetime.strptime(date, '%d %H:00') for date in datoer_fil2]  # Adjust the format as needed

# Convert pressures in kolonne_trykk to float, handling commas and ensuring valid numbers
kolonne_trykk_clean = [
    float(temp.replace(',', '.')) for temp in kolonne_trykk 
    if isinstance(temp, (int, float, str)) and str(temp).replace(',', '').replace('.', '', 1).isdigit()
]

# Convert pressures in data_list to float, similar to kolonne_trykk
data_list_clean = [
    float(temp.replace(',', '.')) for temp in data_list 
    if isinstance(temp, (int, float, str)) and str(temp).replace(',', '').replace('.', '', 1).isdigit()
]

# Debug: print lengths of the data
print(f"Length of datoer_fil1: {len(datoer_fil1)}")
print(f"Length of datoer_fil2: {len(datoer_fil2)}")
print(f"Length of kolonne_trykk_clean: {len(kolonne_trykk_clean)}")
print(f"Length of data_list_clean: {len(data_list_clean)}")

# Ensure the lengths match between dates and pressures
min_length = min(len(datoer_fil1), len(datoer_fil2), len(kolonne_trykk_clean), len(data_list_clean))
datoer_fil1_filtered = datoer_fil1[:min_length]
datoer_fil2_filtered = datoer_fil2[:min_length]
filtered_kolonne_trykk = kolonne_trykk_clean[:min_length]
filtered_data_list = data_list_clean[:min_length]

# Create the plot
plt.figure(figsize=(12, 6))

# Plot data from the first file
plt.plot(datoer_fil1_filtered, filtered_kolonne_trykk, label='Trykk fra Stasjon UiS', color='blue', marker='o')

# Plot data from the second file using data_list
plt.plot(datoer_fil2_filtered, filtered_data_list, label='Trykk fra Stasjon Sola', color='orange', marker='o')

# Set the x-axis major locator to display ticks
plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(integer=True))

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
