import csv
import os
print("Current Working Directory:", os.getcwd()) # en pwd for pythonen. brukes til å finne path til csv



def extract_column_to_array(file_path, column_name):
    data_array = []
    row_count = 0

    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            if row_count >= 210: # skal ta 210 - 10 målinger i et array
                break

            if not row_count < 10: # skipper de første 10 målingene for å bare hente stabil data
                data_array.append(float(row[column_name]))

            row_count += 1

    return data_array

### File path til csv'en ; må endres for ny fil eller pc ###
file_path = './Desktop/GNSS_data/fotballbane/RawData.csv' 

### Navn på kolonne som skal indexes ###
lon_column = 'Longitude' 
lat_column = 'Latitude'
alt_column = 'Altitude'

### Henter ut dataene som skal brukes i oppgaven ###
lon_array: list[float] = extract_column_to_array(file_path, lon_column)
lat_array: list[float] = extract_column_to_array(file_path, lat_column)
alt_array: list[float] = extract_column_to_array(file_path, alt_column)

def average(array): # gjennomsnitt
    n = len(array)
    sum = 0
    for i in range(n):
        sum += array[i]

    return sum/n

def e_varians(array): # empirisk varians
    n = len(array)
    av = average(array)
    sum = 0
    for i in range(n):
        sum += (array[i] - av)**2

    return sum/(n-1)

### Gjennomsnitt av dataene ###
lon_av: float = average(lon_array)
lat_av: float = average(lat_array)
alt_av: float = average(alt_array)

### Varians av dataene ###
lon_var: float = e_varians(lon_array)
lat_var: float = e_varians(lat_array)
alt_var: float = e_varians(alt_array)

### Printer data i konsoll ###
print(f'n = {len(alt_array)}')
print(f'gjennomsnitt = lat: {lat_av}, lon: {lon_av}, alt: {alt_av}')
print(f'varians = lat: {lat_var}, lon: {lon_var}, alt: {alt_var}')
