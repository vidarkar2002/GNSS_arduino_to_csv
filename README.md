# GNSS_arduino_to_csv

Oppgaven går ut på å sammenlikne to måleinstrumenter for bruk i div utregninger og hypotesetester.

En Arduino UNO kopplet med en Adafruit GPS og brukt i målinger av koordinat og høydemeter ihht WGS84. Det ble brukt to forskjellige antenner; en dårlig og en god.
Arduinoen utførte og skrev ut en måling i minuttet til en csv fil. Målinger fra GPS i en iPhone (app: phyphox) ble også brukt som kontrollmåler.

Det ble utført målinger på en fottballbane (åpen himmel; ideelt gps miljø) og ved nordøstlig inngangen til NTNU i Ålesund (blokkert himmelsikte; begrenset satelitt-fix)

Det ble målt kontinuerlig i 5 minutter for hvert enkelt datasett.
