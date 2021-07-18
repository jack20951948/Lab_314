//host
#include <WiFi.h>
#include <SoftwareSerial.h>
SoftwareSerial mySerial(16 , 17);//tx,rx

//const char* ssid = "fishisgood";
//const char* password =  "fishisgood";

const char* ssid = "qwertyuiop";//192.168.137.160
const char* password = "qwertyuiop";

//variabls for blinking an LED with Millis
const int led = 2; // ESP32 Pin to which onboard LED is connected
unsigned long previousMillis = 0;  // will store last time LED was updated
const long interval = 1000;  // interval at which to blink (milliseconds)
int ledState = LOW;  // ledState used to set the LED

WiFiServer wifiServer(80);
 
void setup() {
 
  Serial.begin(57600);
  mySerial.begin(57600);
  delay(1000);
 
  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi..");
  }
 
  Serial.println("Connected to the WiFi network");
  Serial.println(WiFi.localIP());
  pinMode(led,  OUTPUT);
 
  wifiServer.begin();
}

void loop() {
  WiFiClient client = wifiServer.available();
      //loop to blink without delay
      unsigned long currentMillis = millis();
      if (currentMillis - previousMillis >= interval) {
      // save the last time you blinked the LED
      previousMillis = currentMillis;
      // if the LED is off turn it on and vice-versa:
      ledState = not(ledState);
      // set the LED with the ledState of the variable:
      digitalWrite(led,  ledState);}
  if (client) {
    while (client.connected()) {
      ledState=HIGH;
      digitalWrite(led,  ledState);
      if(client.available()){
        while (client.available()) {
          char c = client.read();
          Serial.print(c);
          mySerial.print(c);    
          }
      }
    }
    client.stop();
    Serial.println("Client disconnected");
 
  }
}
