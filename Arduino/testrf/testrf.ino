#include <SoftwareSerial.h>
SoftwareSerial mySerial(2 , 3);
  char mymessage[0xFF];
  int iMymessage = 0;
  int sensorValue = 0;
  int cm = 0;
  
void setup() {
  // put your setup code here, to run once:
Serial.begin(57600);
mySerial.begin(57600);
}

void loop() {

  // put your main code here, to run repeatedly:
  if (Serial.available()) // judge have data or not , if exist!! store into array
  {
    for (iMymessage = 0; 0 < Serial.available(); ++iMymessage)
    {
      char c =  Serial.read();
      mymessage[iMymessage] = c;
      delay(2);
    }
   mySerial.println(mymessage);

  }
  delay(10);
  
 //   mySerial.listen();
    if(Serial.available())
    {

            sensorValue =  Serial.read();
            cm =  Serial.read();
            Serial.print("senVal: ");
            Serial.print(sensorValue);
            Serial.print(", cm: ");
            Serial.println(cm);
    }
}
