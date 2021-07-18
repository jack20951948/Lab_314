#include "XL320.h"
#include <math.h>
#define pin 32
XL320 robot;

char rgb[] = "rgbypcwo";
int servoPosition = 0;
int position_now=512;
int ledColour = 0;
int n;
int N;

int delay_t;

int ID1 = 1;//body
int ID2 = 2;//tail
int ID  = 3;//head
int M_ID_[3]  =  {ID, ID1, ID2};
/*
int Turn_Straight[4][8] = {
{ ID1,          ID2,           ID1,          ID2,           ID1,          ID2,           ID1,          ID2}, 
{ (130)/0.2929, (210)/0.2929 , (150)/0.2929, (150)/0.2929 , (170)/0.2929, (90)/0.2929 , (150)/0.2929, (150)/0.2929 }, 
{ (140)/0.2929, (170)/0.2929 , (150)/0.2929, (150)/0.2929 , (160)/0.2929, (130)/0.2929, (150)/0.2929, (150)/0.2929 }, 
{ (130)/0.2929, (220)/0.2929 , (150)/0.2929, (150)/0.2929 , (170)/0.2929, (80)/0.2929 , (150)/0.2929, (150)/0.2929 }, 
};

//for pili auto fourier
int Turn_Straight[2][8] = {
{ ID1,          ID2,           ID1,          ID2,           ID1,          ID2,           ID1,          ID2}, 
{ (130)/0.2929, (190)/0.2929 , (150)/0.2929, (150)/0.2929 , (170)/0.2929, (110)/0.2929 , (150)/0.2929, (150)/0.2929 }, 
};

*/

int Turn_Right[2][4] = {
{ID1,        ID2,        ID1,       ID2},
{120/0.2929,190/0.2929 , 150/0.2929,150/0.2929},
};

int Turn_Left[2][4] = {
{ID1,       ID2,        ID1,       ID2},
{180/0.2929,110/0.2929 , 150/0.2929,150/0.2929},
};

void setup() {
  Serial.begin(1000000);
  robot.begin(Serial); 
  robot.moveJoint(M_ID_[1], 512);   
  robot.moveJoint(M_ID_[2], 512);
  delay(1000);
}

void loop() {

    
    robot.setJointSpeed(M_ID_[1], 300);   
    robot.setJointSpeed(M_ID_[2], 307); 
    delay(10); 

    robot.moveJoint(M_ID_[1], 512);
    delay(10); 
    robot.moveJoint(M_ID_[2], 512);
    delay(10); 
    
    robot.moveJoint(M_ID_[1], 410);
    delay(50); 
    robot.moveJoint(M_ID_[2], 649);
    delay(200); 

    robot.setJointSpeed(M_ID_[1], 100);   
    robot.setJointSpeed(M_ID_[2], 100); 
    delay(10);
    
    robot.moveJoint(M_ID_[1], 512);
    delay(150); 
    robot.moveJoint(M_ID_[2], 512);
    delay(1000); 


    robot.setJointSpeed(M_ID_[1], 300);   
    robot.setJointSpeed(M_ID_[2], 307); 
    delay(10); 

    robot.moveJoint(M_ID_[1], 512);
    delay(10); 
    robot.moveJoint(M_ID_[2], 512);
    delay(10); 
    
    robot.moveJoint(M_ID_[1], 615);
    delay(50); 
    robot.moveJoint(M_ID_[2], 376);
    delay(200); 

    robot.setJointSpeed(M_ID_[1], 100);   
    robot.setJointSpeed(M_ID_[2], 100); 
    delay(10);
    
    robot.moveJoint(M_ID_[1], 512);
    delay(150); 
    robot.moveJoint(M_ID_[2], 512);
    delay(1000);
    
    
  }

  
//turn
/*

  robot.setJointSpeed(M_ID_[1], 1023);   
  robot.setJointSpeed(M_ID_[2], 818); 
  delay_t= 150;
  N = 20;//cycle time
  n=0;

  n %= (N);
  robot.moveJoint(Turn_Right[0][n], Turn_Left[1][n]);  
  robot.moveJoint(Turn_Right[0][n+1], Turn_Left[1][n+1]); 
  n=n+2;
  delay(delay_t); 
  
 */

 
//straight
  /*
  if(i==1){ //big and slow
    robot.setJointSpeed(M_ID_[1], 75);   
    robot.setJointSpeed(M_ID_[2], 205); 
    delay_t= 450;
    i=1;
   }
   
  else if(i==2){ //big and fast
    robot.setJointSpeed(M_ID_[1], 280);   
    robot.setJointSpeed(M_ID_[2], 818); 
    delay_t= 153;
    i=1;
   }
   
  else if(i==3){ //small and slow 
    robot.setJointSpeed(M_ID_[1], 50);   
    robot.setJointSpeed(M_ID_[2], 100); 
    delay_t= 360;
    i=2;
   }
  
  else if(i==4){ //small and fast 
    robot.setJointSpeed(M_ID_[1], 1023);   
    robot.setJointSpeed(M_ID_[2], 510); 
    delay_t= 125;
    i=2;
   }
  else if(i==5){ //crazy
    robot.setJointSpeed(M_ID_[1], 340);   
    robot.setJointSpeed(M_ID_[2], 1023); 
    delay_t= 153;
    i=3;
   }
   N = 8;
   n=0; 

    n %= (N);
    robot.moveJoint(Turn_Straight[0][n], Turn_Straight[i][n]);
    robot.moveJoint(Turn_Straight[0][n+1], Turn_Straight[i][n+1]);
    n=n+2;
    delay(delay_t);
  */
 
