
// ========================================
// Dynamixel XL-320 Arduino library example
// ========================================

// Read more:
// https://github.com/hackerspace-adelaide/XL320

#include "XL320.h"

// Name your robot!
XL320 robot;

// If you want to use Software Serial, uncomment this line
#include <SoftwareSerial.h>

// Set the SoftwareSerial RX & TX pins
SoftwareSerial mySerial(10, 11); // (RX, TX)

// Set some variables for incrementing position & LED colour
char rgb[] = "rgbypcwo";
int servoPosition = 0;
int ledColour = 0;

float pos;

// Set the default servoID to talk to
int servoID1 = 1;
int servoID2 = 2;

void setup() {

  // Talking standard serial, so connect servo data line to Digital TX 1
  // Comment out this line to talk software serial
  Serial.begin(1000000);

  // Initialise your robot
  robot.begin(Serial); // Hand in the serial object you're using
  
  // I like fast moving servos, so set the joint speed to max!
  robot.setJointSpeed(servoID1, 200);
  // robot.setJointSpeed(servoID2, 200);

}

void loop() {

  // LED test.. let's randomly set the colour (0-7)
//  robot.LED(servoID2, &rgb[random(0,7)] );

  // LED test.. select a random servoID and colour
  robot.LED(random(1,3), &rgb[random(0,7)] );

  // LED colour test.. cycle between RGB, increment the colour and return 1 after 3
//  robot.LED(servoID2, &rgb[ledColour]);
//   ledColour = (ledColour + 1) % 3;

  // Set a delay to account for the receive delay period
  // delay(100);

  // Servo test.. let's randomly set the position (0-1023)
//  robot.moveJoint(servoID, random(0, 1023));

  // Servo test.. select a random servoID and colour
  // robot.moveJoint(1, random(0,1023));
  // robot.moveJoint(2, random(0,1023));
  // Servo test.. increment the servo position by 100 each loop
//  robot.moveJoint(servoID1, servoPosition);
//   servoPosition = (servoPosition + 100) % 1023;
  
  // Set a delay to account for the receive delay period
  sineMode();
  WheelMode(2, 1, 500); //servoID, round, speed (CCW)
  delay(3000);
}

void sineMode()
{
    for (int n = 0; n < 360; n++)
   {
     pos = ((100 * sin(n * PI / 180.0) * 1023.0) / 300.0) + 512.0;
     robot.moveJoint(servoID1, pos);
    //  robot.moveJoint(servoID2, pos);
      delay(5); 
   }
}

void WheelMode(int servo, int round, int speed)
{
  robot.setJointSpeed(servo, speed);
  delay(round*1410/(speed*0.111/60));
  robot.setJointSpeed(servo, 0);
  return 0;
}