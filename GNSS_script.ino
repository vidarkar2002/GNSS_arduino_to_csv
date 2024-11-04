#include <Adafruit_GPS.h>
#include <SoftwareSerial.h>

SoftwareSerial mySerial(3, 4); // RX, TX
Adafruit_GPS GPS(&mySerial);

unsigned long lastTime = 0;  // Variable to store the last time a message was sent
const unsigned long interval = 1000;  // Interval in milliseconds (1 second)

void setup() {
  Serial.begin(115200);
  mySerial.begin(9600);
  GPS.begin(9600);

  Serial.println("Waiting for GPS fix...");

  // Set up the GPS to output RMC and GGA sentences every second
  GPS.sendCommand(PMTK_SET_NMEA_OUTPUT_RMCGGA);
  GPS.sendCommand(PMTK_SET_NMEA_UPDATE_1HZ);

  delay(1000);
}

void loop() {
  char c = GPS.read();
  if (c) Serial.print(c);

  if (GPS.newNMEAreceived()) {
    if (!GPS.parse(GPS.lastNMEA())) return;  // Skip if the sentence is invalid

    // Only print or send data if a fix is available
    if (GPS.fix) {
      // Check if 1 second has passed since the last message
      unsigned long currentTime = millis();
      if (currentTime - lastTime >= interval) {
        lastTime = currentTime;  // Update the last time a message was sent

        // Create CSV formatted data
        String csvData = String(GPS.latitudeDegrees, 6) + "," +
                         String(GPS.longitudeDegrees, 6) + "," +
                         String(GPS.altitude);

        // Send the CSV data
        Serial.println(csvData);  // You can modify this line to send the data over another communication interface if needed
      }
    } else {
      Serial.println("Still searching for GPS fix...");
    }
  }
}
