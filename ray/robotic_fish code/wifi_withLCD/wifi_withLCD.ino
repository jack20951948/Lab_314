//host
#include <WiFi.h>
#include <SoftwareSerial.h>
#include <Wire.h>  // Arduino IDE 內建
#include <LiquidCrystal_I2C.h>
SoftwareSerial mySerial(16 , 17);//tx,rx

//const char* ssid = "fishisgood";
//const char* password =  "lab314314";

const char* ssid = "12345678";
const char* password =  "12345678";

//variabls for blinking an LED with Millis
const int led = 2; // ESP32 Pin to which onboard LED is connected
unsigned long previousMillis = 0;  // will store last time LED was updated
const long interval = 1000;  // interval at which to blink (milliseconds)
int ledState = LOW;  // ledState used to set the LED

int connecting_Flag = 0; 
int connected_Flag = 0; 
int client_Flag = 0;

char c_tmp;

WiFiServer wifiServer(80);

// Set the pins on the I2C chip used for LCD connections:
//                    addr, en,rw,rs,d4,d5,d6,d7,bl,blpol
LiquidCrystal_I2C lcd(0x27, 2, 1, 0, 4, 5, 6, 7, 3, POSITIVE);  // 設定 LCD I2C 位址
 
void setup() {
 
  Serial.begin(57600);
  mySerial.begin(57600);
  lcd.begin(16, 2);      // 初始化 LCD，一行 16 的字元，共 2 行，預設開啟背光
  delay(1000);
 
  WiFi.begin(ssid, password);
  pinMode(led,  OUTPUT);
  wifiServer.begin();

}

void loop() {
  while (WiFi.status() != WL_CONNECTED) {
    digitalWrite(led,  LOW);
    delay(1000);
    Serial.println("Connecting to WiFi..");
    //set the lcd for just one time
    if (connecting_Flag == 0){
        lcd.clear();
        lcd.setCursor(0, 0); // 設定游標位置在第一行行首
        lcd.print("Connecting to");
        lcd.setCursor(0, 1); // 設定游標位置在第二行行首
        lcd.print("WIFI.......");
        connecting_Flag = 1; 
      }
  }
  connecting_Flag = 0; 
  
  if (connected_Flag == 0){
      Serial.println("Connected to the WiFi network");
      Serial.println(WiFi.localIP());
      delay(100);
      lcd.clear();
      lcd.setCursor(0, 0); 
      lcd.print("Connected to IP:");
      lcd.setCursor(0, 1); 
      lcd.print(WiFi.localIP());
      connected_Flag = 1; 
    }
  
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
      connected_Flag = 0;
      ledState=HIGH;
      if (client_Flag == 0){
          lcd.clear();
          lcd.setCursor(0, 0); 
          lcd.print("Client is ready!");
          lcd.setCursor(0, 1); 
          lcd.print("Wait for command.");
          client_Flag = 1;
        }
      digitalWrite(led,  ledState);
      if(client.available()){
        
        while (client.available()) {
          char c = client.read();
          mySerial.print(c);    
          Serial.print(c);
          if (c != c_tmp){
            if (String(c) != "\n"){
                lcd.clear();
                lcd.setCursor(0, 0); 
                lcd.print("Your command:");
                lcd.setCursor(0, 1); 
                lcd.print(c);
                c_tmp = c;
              }
            }
         }
      }
    }
    client.stop();
    client_Flag = 0;
    Serial.println("Client disconnected");
    lcd.clear();
    lcd.setCursor(0, 0); 
    lcd.print("Client");
    lcd.setCursor(0, 1); 
    lcd.print("disconnected......");
    delay(2000);
  }
}
