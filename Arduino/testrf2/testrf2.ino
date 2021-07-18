#include <SoftwareSerial.h>


///////////////////////////  RF  ///////////////////////////
SoftwareSerial mySerial(2,3);  //建立軟體串列埠腳位 (TX, RX)
char mymessage[0xFF];
int iMymessage = 0;
char * p_buf = mymessage ;
int sensorValue = 0;
int cm = 0;

///////////////////////////  LED  ///////////////////////////


void setup() 
{
  Serial.begin(57600);
  mySerial.begin(57600);
    pinMode(A0,INPUT);
  delay(10);
}

void loop() 
{

 RF_xSerial();
 Decide();

}


void RF_xSerial()
{    mySerial.listen();
    if(mySerial.available())
    {
       for(iMymessage=0; 0<mySerial.available(); ++iMymessage) 
        {
            char c =  mySerial.read();
            mymessage[iMymessage]=c;
            delay(2);            
        }  
          //  Decide();

    }    
}

void Decide()
{
 switch (*p_buf)
  {
    case 'O': case 'o': //直線動作
    { 
       red();
      Serial.write(sensorValue);
        Serial.write(cm);
        Serial.flush();
    }        
      break; 
      
    case 'S': case 's': //直線動作
    {
      Serial.write(0);
        Serial.write(0);
        Serial.flush();
    }        
      break; 
}
}

void red()
{
  sensorValue = analogRead(A0);
  cm = 10284*(pow(sensorValue,(-0.976)));

  delay(10);
}
