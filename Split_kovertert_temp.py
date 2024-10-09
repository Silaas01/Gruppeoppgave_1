
from Konvertering_temp_per_min import data_list  # Import the existing data_list

def temperatur_hent(data_list):
    temperatur_liste = []  # List to store the temperature values

    for entry in data_list:
        temperatur = entry["temperatur"]  # Extract the temperature
        # Append only if temperature is not empty
        if temperatur:  # Check for non-empty values
            temperatur_liste.append(temperatur.replace(',', '.'))  # Convert if necessary

    return temperatur_liste

# Extract the temperature column from the data_list
temperatur_kolonne = temperatur_hent(data_list)

# Print the extracted temperature values
print("Extracted Temperature Column:")
for temperatur in temperatur_kolonne:
    print(temperatur)  # Print each temperature value on a new line
