

from Konvertering_temp_per_min import data_list  

def tid_hentet(data_list):
    tid_liste = []  # List to store the time values

    for entry in data_list:
        dato_tid = entry["dato_tid"]
        tid = dato_tid[11:16]  # Extract the time (HH:MM) from the timestamp
        tid_liste.append(tid)

    return tid_liste

# Extract the time column from the data_list
tid_kolonne = tid_hentet(data_list)

# Print only the extracted time values without additional formatting
print("Extracted Time Column:")
for tid in tid_kolonne:
    print(tid)  # Print each time value on a new line


