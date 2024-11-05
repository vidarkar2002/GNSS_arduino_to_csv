#include <Adafruit_GPS.h>
#include <SoftwareSerial.h>

SoftwareSerial mySerial(3, 4); // RX, TX
Adafruit_GPS GPS(&mySerial);

unsigned long lastTime = 0;
const unsigned long interval = 1000;  // 1 sekkund

void setup() {
  Serial.begin(115200);
  mySerial.begin(9600);
  GPS.begin(9600);

  Serial.println("Waiting for GPS fix...");

  // GPS output RMC og GGA 1 gang per sekund
  GPS.sendCommand(PMTK_SET_NMEA_OUTPUT_RMCGGA);
  GPS.sendCommand(PMTK_SET_NMEA_UPDATE_1HZ);

  delay(1000);
}

void loop() {
  char c = GPS.read();
  if (c) Serial.print(c);

  if (GPS.newNMEAreceived()) {
    if (!GPS.parse(GPS.lastNMEA())) return;  // Skip hvis nan-melding

    // Printer bare med satelitt fix
    if (GPS.fix) {
      unsigned long currentTime = millis(); // klokken
      if (currentTime - lastTime >= interval) {
        lastTime = currentTime;

        // Lager CSV formatert data
        String csvData = String(GPS.latitudeDegrees, 6) + "," +
                         String(GPS.longitudeDegrees, 6) + "," +
                         String(GPS.altitude);

        // Sender CSV data
        Serial.println(csvData);
      }
    } else {
      Serial.println("Still searching for GPS fix...");
    }
  }
}
