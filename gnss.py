import serial
import csv

# Set up the serial connection
ser = serial.Serial('/dev/ttyACM0', 115200)
ser.flush()

# Open a CSV file to save the data
with open('gps_data.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Latitude', 'Longitude', 'Altitude'])  # Header row

    try:
        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').strip()
                data = line.split(',')
                if len(data) == 3:
                    csv_writer.writerow(data)
                    print(f"Data saved: {data}")
    except KeyboardInterrupt:
        print("Data collection stopped.")
