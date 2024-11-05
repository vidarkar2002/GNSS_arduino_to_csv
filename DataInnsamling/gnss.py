import serial
import csv

ser = serial.Serial('/dev/ttyACM0', 115200) # Porten '/dev/ttyACM0' må være usb-porten arduino er påkopplet
ser.flush()

with open('gps_data.csv', 'w', newline='') as csvfile: # Den lager en ny csv fil hvis det ikke finnes en i wd
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Latitude', 'Longitude', 'Altitude'])

    try:
        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8', errors='ignore').strip()
                data = line.split(',')
                if len(data) == 3:
                    csv_writer.writerow(data)
                    print(f"Data saved: {data}")
    except KeyboardInterrupt: # ctrl+c i terminal for å stoppe
        print("Data collection stopped.")
