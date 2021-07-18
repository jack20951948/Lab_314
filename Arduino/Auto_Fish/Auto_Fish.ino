//-------- Control motor -----------------------------------------------------------------------------------------
#include "XL320.h"
#include <math.h>
#include <SoftwareSerial.h>
#define DepthPin 32
#define led 2
XL320 robot;
TaskHandle_t Task1; //Task 2 runs on core 1 which runs by default in Loop()

//--------- OTA Web Updater ----------------------------------------------------------------------------------
#include <WiFi.h>
#include <WiFiClient.h>
#include <WebServer.h>
#include <ESPmDNS.h>
#include <Update.h>

const char* host = "esp32";
const char* ssid = "fishisgood";
const char* password = "fishisgood";

WebServer server(80);

// Set your Static IP address
IPAddress local_IP(10, 1, 1, 41);
// Set your Gateway IP address
IPAddress gateway(10, 1, 1, 1);
IPAddress subnet(255, 255, 0, 0);
IPAddress primaryDNS(8, 8, 8, 8); 
IPAddress secondaryDNS(8, 8, 4, 4); 

/* Style */
String style =
"<style>#file-input,input{width:100%;height:44px;border-radius:4px;margin:10px auto;font-size:15px}"
"input{background:#f1f1f1;border:0;padding:0 15px}body{background:#3498db;font-family:sans-serif;font-size:14px;color:#777}"
"#file-input{padding:0;border:1px solid #ddd;line-height:44px;text-align:left;display:block;cursor:pointer}"
"#bar,#prgbar{background-color:#f1f1f1;border-radius:10px}#bar{background-color:#3498db;width:0%;height:10px}"
"form{background:#fff;max-width:258px;margin:75px auto;padding:30px;border-radius:5px;text-align:center}"
".btn{background:#3498db;color:#fff;cursor:pointer}</style>";

/* Login page */
String loginIndex = 
"<form name=loginForm>"
"<h1>AUTO FISH</h1>"
"<input name=userid placeholder='User ID'> "
"<input name=pwd placeholder=Password type=Password> "
"<input type=submit onclick=check(this.form) class=btn value=Login></form>"
"<script>"
"function check(form) {"
"if(form.userid.value=='admin' && form.pwd.value=='admin')"
"{window.open('/serverIndex')}"
"else"
"{alert('Error Password or Username')}"
"}"
"</script>" + style;
 
/* Server Index Page */
String serverIndex = 
"<script src='https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js'></script>"
"<form method='POST' action='#' enctype='multipart/form-data' id='upload_form'>"
"<input type='file' name='update' id='file' onchange='sub(this)' style=display:none>"
"<label id='file-input' for='file'>   Choose file...</label>"
"<input type='submit' class=btn value='Update'>"
"<br><br>"
"<div id='prg'></div>"
"<br><div id='prgbar'><div id='bar'></div></div><br></form>"
"<script>"
"function sub(obj){"
"var fileName = obj.value.split('\\\\');"
"document.getElementById('file-input').innerHTML = '   '+ fileName[fileName.length-1];"
"};"
"$('form').submit(function(e){"
"e.preventDefault();"
"var form = $('#upload_form')[0];"
"var data = new FormData(form);"
"$.ajax({"
"url: '/update',"
"type: 'POST',"
"data: data,"
"contentType: false,"
"processData:false,"
"xhr: function() {"
"var xhr = new window.XMLHttpRequest();"
"xhr.upload.addEventListener('progress', function(evt) {"
"if (evt.lengthComputable) {"
"var per = evt.loaded / evt.total;"
"$('#prg').html('progress: ' + Math.round(per*100) + '%');"
"$('#bar').css('width',Math.round(per*100) + '%');"
"}"
"}, false);"
"return xhr;"
"},"
"success:function(d, s) {"
"console.log('success!') "
"},"
"error: function (a, b, c) {"
"}"
"});"
"});"
"</script>" + style;

//--------------------尾鰭馬達 tailmotor -------------------------------------------------------------------------------------------------------------------------------------
int ID1 = 1;//body
int ID2 = 2;//tail
int ID  = 3;//head
int M_ID_[3]  =  {ID, ID1, ID2}; //HEAD To TAIL
//------------------IR senser ------------------------------------------------------------------------------------------------------------------
int analogInPin_1 = 34;  // Analog input pin that the potentiometer is attached to
int analogInPin_2 = 35;  // Analog input pin that the potentiometer is attached to

int IRsensorValue_1=0;
int IRsensorValue_2=0;

//------------------ Parameter -----------------------------------------------------------------------------------------------------------------------
double Data_RF[4] = {1,0.0,0.0,3};// {movement type, amplitude, frequency, shifts} Amplitude 1.5-2, Frequency 0.6-0.9
int current_action = 0;//0-26 action, for row 
//---------mode------------------------------------------------------------------------------------------------------------------------------------------------------------
boolean Tail_bool_turn_Left = false;
boolean Tail_bool_turn_Right = false;
boolean Tail_bool_straight = false;
boolean DONE = true;

//--------------------------　Variable　-----------------------------------------------------------------------------------------------------------------------------------
int const A = 10; //總數 total
int i; //index　動作索引 action index
int n = 0;
int N;
int timer=100;
int OG_pos=0;
int G_pos=0;
int Height;
double avg;
double position_now;
double shift;
double t;
double w_1;
double w_2;
double amppt = 0.0;
double w = 1; //w　之倍數 multiplier
double delay_t = 80;
double theta_last_1=0;
double theta_last_2=0;
double v=0;
double init_V; //initial voltage reading 
double final_V;// final voltage reading

//-------------------　傅立葉參數 fourier number  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
double Period[9] = {1,1.4,1.2,1,1.4,1.2};//Cycle time
double Turn_1[7][17] = {
{0,-2,-11.9,-17.8,-18.8,-18.8,-18.8,-18.8,-18.8,-18.8,0,0},
{0,-1.2,-4,-5.3,-9.7,-15.3,-23.1,-23.1,-23.1,-23.1,-23.1,-23.1,-23.1,0,0,0},
{0,-1.5,-4.8,-19.3,-28.1,-31.9,-34.4,-34.4,-34.4,-34.4,-34.4,0,0,0},
{0,-2,-11.9,-17.8,-18.8,-18.8,-18.8,-18.8,-18.8,-18.8,5,0},
{0,-1.2,-4,-5.3,-9.7,-15.3,-23.1,-23.1,-23.1,-23.1,-23.1,-23.1,-23.1,-23.1,5,0},
{0,-1.5,-4.8,-19.3,-28.1,-31.9,-34.4,-34.4,-34.4,-34.4,-34.4,-34.4,5,0},
};

double Turn_2[7][17] = {
{0,1.5,-6.2,-14.3,-20.5,-24,-20,-13.5,-3.3,-1.4,-0.6},
{0,-2.1,-9.2,-23.3,-34.3,-38.6,-44.1,-41.1,-35.2,-26,-20,-14.1,-9.4,-3.8,-1.3},
{0,-0.7,-1.6,-13.5,-27.4,-39.3,-43.5,-40.6,-31.2,-24.4,-14,-3.4,-1.1},
{0,1.5,-6.2,-14.3,-20.5,-24,-20,-13.5,-3.3,-1.4,-0.6},
{0,-2.1,-9.2,-23.3,-34.3,-38.6,-44.1,-41.1,-35.2,-26,-20,-14.1,-9.4,-3.8,-1.3},
{0,-0.7,-1.6,-13.5,-27.4,-39.3,-43.5,-40.6,-31.2,-24.4,-14,-3.4,-1.1},
};

double S_1[1][20] = {
  //Joint 1                                                                  //Joint 2
  //a0        //a1          //b1        //a2        //b2         //a3        //b3          //a4        //b4        //w         //a0        //a1          //b1        //a2        //b2         //a3        //b3          //a4        //b4        //w 
{-3.312465891,-0.752097985,-2.910261165,0.129371098,-6.488593885,8.080123916,-2.010362741,-4.483814356,4.45164992,4.140782487,-4.791578161,-0.484967533,-3.995719208,6.09271922,-0.258748598,-0.090666236,9.389359856,0.057591342,-8.533668428,4.593799086},//1
};

double Period_S[1] = {1.4};
//--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

void setup() {
  Serial.begin(1000000);
  pinMode(led,  OUTPUT);
  digitalWrite(led,HIGH);
  OTA();
  digitalWrite(led,LOW);
  robot.begin(Serial);
  robot.moveJoint(ID2, 512);
  robot.moveJoint(ID1, 512);
  //G_pos=1;
  randomSeed(analogRead(0));
  delay(3000);
  init_V=analogRead(DepthPin)/4059.0*3.3;
  xTaskCreatePinnedToCore(
                    Task1code,   // Task function. 
                    "Task1",     // name of task. 
                    10000,       // Stack size of task 
                    NULL,        // parameter of the task
                    1,           // priority of the task 
                    &Task1,      // Task handle to keep track of created task 
                    0);          // pin task to core 0   
}

//-------------- Core 1 loop -----------------------------
void loop() {
  IRsensorValue_1 = analogRead(analogInPin_1);
  IRsensorValue_2 = analogRead(analogInPin_2);
  
  if (DONE==true){
    MARKOV();
  } 
  delay(10);
  //check if there' s obstacle 
  if(Tail_bool_turn_Left == true)  {Tail_control_turn_Left();}
  else if(Tail_bool_turn_Right == true)  {Tail_control_turn_Right();}
  else if(Tail_bool_straight == true)  {Tail_control_straight();}
  else{Do_nothing();}
}

//--------------- Core 0 loop ------------------------------
void Task1code( void * pvParameters ){
  for(;;){
    server.handleClient();
    Read_Height();
    delay(100);
    U_D();
  }
}

//---------------------- 無線傳輸 wireless transmiting------------------------------------------------------------------------------------------------------------------------------------------
void MARKOV(void)
{
 int Random=random(1,100);
 double Prob=0;
 
 int Action_prob[27][27] = {
  
 //  0,  1,  2,  3,  4,  5,  6, -7,  8,  9, 10, 11, 12, 13, 14,-15, 16, 17, 18, 19,-20, 21, 22, 23,-24,-25,-26
  { 75,  0,  0,  1,  0,  3,  2,  0,  0,  1,  1,  2,  0,  4,  2,  0,  1,  1,  1,  1,  0,  2,  2,  0,  0,  0,  0},//0
  { 60, 40,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0},//1
  { 67,  0, 33,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0},//2
  { 80,  0,  0, 20,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0},//3
  { 67,  0,  0,  0, 33,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0},//4
  { 82,  0,  0,  0,  0, 16,  2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0},//5
  { 77,  0,  0,  0,  0,  0, 20,  0,  0,  0,  0,  0,  0,  0,  3,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0},//6
  {  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0},//7
  { 67,  0,  0,  0,  0,  0,  0,  0, 33,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0},//8
  {100,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0},//9
  { 88,  0,  0,  6,  0,  0,  0,  0,  0,  0,  6,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0},//10
  { 89,  0,  0,  0,  0,  0,  0,  0,  0,  0,  4,  4,  0,  4,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0},//11
  {100,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0},//12
  { 85,  0,  0,  0,  0,  2,  0,  0,  0,  2,  0,  0,  2,  8,  0,  0,  0,  0,  0,  0,  0,  2,  0,  0,  0,  0,  0},//13
  { 96,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  4,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0},//14
  {  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0},//15
  {100,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0},//16
  { 81,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 14,  5,  0,  0,  0,  0,  0,  0,  0,  0},//17
  { 89,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 11,  0,  0,  0,  0,  0,  0,  0,  0},//18
  { 76,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 18,  0,  6,  0,  0,  0,  0,  0},//19
  {100,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0},//20
  { 85,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 12,  4,  0,  0,  0,  0},//21
  { 70,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  6,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0},//22
  {  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0},//23
  { 50,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 50,  0,  0,  0},//24
  {  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0},//25
  {  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0},//26

 };

 int Speed_prob[27][3] = {
  //slow, mid ,fast
  {100,  0,  0},
  { 60,  0, 40},
  { 33, 33, 33},
  { 40, 28, 32},
  {100,  0,  0},
  { 64, 25, 11},
  { 26, 46, 29},
  {  0,  0,  0},
  { 33, 50, 17},
  { 82,  9,  9},
  { 62, 25, 12},
  { 85,  7,  7},
  { 50, 50,  0},
  { 93,  3,  3},
  { 81, 19,  0},
  {  0,  0,  0},
  { 62, 12, 25},
  { 43, 24, 33},
  { 56, 11, 33},
  { 35, 47, 18},
  { 33, 33, 33},
  { 81, 15,  4},
  {  9, 30, 61},
  {  0,  0,  0},
  { 12, 88,  0},
  {  0,  0,  0},
  {  0,  0,  0},
 };

/*
    0 = stop
    1 = straight up
    2 = small right up (45 degree)
    3 = right up (90 degree)
    4 = Big right up (135 degree)
    5 = Big big right up(180 degree)
    6 = Big left up
    7 = left up
    8 = small left up 
    9 = straight
    10 = small right
    11 = right
    12 = big right 
    13 = big big right
    14 = big left
    15 = left
    16 = small left
    17 = straight down
    18 = small right down
    19 = right down
    20 = big right down
    21 = big big right down
    22 = big left down
    23 = left down
    24 = small left down
    25 = up
    26 = down
*/
  
 for(int next_action=0; next_action<27; next_action++){
  if(Action_prob[current_action][next_action]>0){
   Prob=Prob+Action_prob[current_action][next_action];
   if( Random < Prob ){
    current_action=next_action;
      if (current_action == 0 ){ //empty
        Tail_bool_turn_Left = false;
        Tail_bool_turn_Right = false;
        Tail_bool_straight = false;
        DONE = false;
      }
  
      else if (current_action == 1 ){ //Straight and UP
        Data_RF[1] = 1.6;
        UP();
        STRAIGHT(); 
        DONE=false;
      }
  
      else if (current_action == 2 ){ // Right 45* and UP
        Data_RF[1] = 1.0;
        Data_RF[0] = 1.0;
        UP();
        RIGHT();
        DONE=false;
      }
  
      else if (current_action == 3 ){ // Right 90* and UP
        Data_RF[1] = 1.0;
        Data_RF[0] = 3.0;
        UP();
        RIGHT();
        DONE=false;
      }
  
      else if (current_action == 4 ){ // Right 135* and UP
        Data_RF[1] = 1.0;
        Data_RF[0] = 3.0;
        UP();
        RIGHT();
        DONE=false;
      }
  
      else if (current_action == 5 ){ // Right 180* and UP
        Data_RF[1] = 1.0;
        Data_RF[0] = 3.0;
        UP();
        RIGHT();
        DONE=false;
      }
  
      else if (current_action == 6 ){ // Left 135* and UP
        Data_RF[1] = 1.0;
        Data_RF[0] = 3.0;
        UP();
        LEFT();
        DONE=false;
      }
  
      else if (current_action == 8 ){ //Left 45* and UP
        Data_RF[1] = 1.0;
        Data_RF[0] = 1.0;
        UP();
        LEFT();
        DONE=false;
      }
 
      else if (current_action == 9 ){ // Straight
        Data_RF[1] = 1.6;
        STRAIGHT(); 
        DONE=false;
      }
  
      else if (current_action == 10){ // Right 45*
        Data_RF[1] = 1.0;
        Data_RF[0] = 1.0;
        RIGHT();
        DONE=false;
      }
 
      else if (current_action == 11){ // Right 90*
        Data_RF[1] = 1.0;
        Data_RF[0] = 3.0;
        RIGHT();
        DONE=false;
      }
  
      else if (current_action == 12){ // Right 135*
        Data_RF[1] = 1.0;
        Data_RF[0] = 3.0;
        RIGHT();
        DONE=false;
      }
  
      else if (current_action == 13){ // Right 180*
        Data_RF[1] = 1.0;
        Data_RF[0] = 3.0;
        RIGHT();
        DONE=false;
      }
  
      else if (current_action == 14){ // Left 135*
        Data_RF[1] = 1.0;
        Data_RF[0] = 3.0;
        LEFT();
        DONE=false;
      }
  
      else if (current_action == 16){ // Left 45*
        Data_RF[1] = 1.0;
        Data_RF[0] = 3.0;
        LEFT();
        DONE=false;
      }
 
      else if (current_action == 17){ // Straight and Down
        Data_RF[1] = 1.6;
        DOWN();
        STRAIGHT(); 
        DONE=false;
      }
  
      else if (current_action == 18){ // Right 45* and Down
        Data_RF[1] = 1.0;
        Data_RF[0] = 1.0;
        DOWN();
        RIGHT();
        DONE=false;
      }
  
      else if (current_action == 19){ // Right 90* and Down
        Data_RF[1] = 1.0;
        Data_RF[0] = 3.0;
        DOWN();
        RIGHT();
        DONE=false;
      }
  
      else if (current_action == 21){ // Right 180* and Down
        Data_RF[1] = 1.0;
        Data_RF[0] = 3.0;
        DOWN();
        RIGHT();
        DONE=false;
      }
  
      else if (current_action == 22){ // Left 135* and Down
        Data_RF[1] = 1.0;
        Data_RF[0] = 3.0;
        DOWN();
        LEFT();
        DONE=false;
      }
  
      else if (current_action == 23){ //Left 90* and Down
        Data_RF[1] = 1.0;
        Data_RF[0] = 3.0;
        DOWN();
        LEFT();
        DONE=false;
      }

      else if (current_action == 24){ // Right 90*
        Data_RF[1] = 1.0;
        Data_RF[0] = 3.0;
        RIGHT();
        DONE=false;
      }
      else if (current_action == 25){ // Left 135*
        Data_RF[1] = 1.0;
        Data_RF[0] = 3.0;
        LEFT();
        DONE=false;
      }
   
   Prob=0;
   parameter_determine();
   break; 
   }
 }
}

  if((IRsensorValue_1<4095) && (IRsensorValue_2<4095)){ 
    current_action = 14;
    Data_RF[1] = 1.0;
    Data_RF[0] = 3.0;
    LEFT();
    DONE=false;
    parameter_determine();
  }
  else if((IRsensorValue_1<4095) && (IRsensorValue_2>=4095)){
    current_action = 12;
    Data_RF[1] = 1.0;
    Data_RF[0] = 3.0;
    RIGHT();
    DONE=false;
    parameter_determine();
  }

  
 for(int next_speed=0; next_speed<3; next_speed++){
  if(Speed_prob[current_action][next_speed]>0){
   Prob=Prob+Speed_prob[current_action][next_speed];
   if( Random < Prob ){
    if (next_speed==0){
      
      if (Tail_bool_straight == true){
        Data_RF[2] = 0.6;
      }
      else if (Tail_bool_straight == false){
        Data_RF[2] = 0.6;
      } 
      
    }
    
    else if (next_speed==1){
        
      if (Tail_bool_straight == true){
        Data_RF[2] = 0.75;
      }
      else if (Tail_bool_straight == false){
        Data_RF[2] = 0.6;
      } 
      
    }
    
    else if (next_speed==2){
        
      if (Tail_bool_straight == true){
        Data_RF[2] = 0.9;
      }
      else if (Tail_bool_straight == false){
        Data_RF[2] = 0.6;
      } 
      
    }
   parameter_determine(); 
   break;
   }
 }
 }     
 
}

//-----------------------Data decoding---------------------------              
void Read_Height(){
  final_V=0;
  for (int i =0 ;i<10;i++)
       {
       final_V = final_V +(analogRead(DepthPin)/4059.0*3.3);
       delay(100);
       }
  final_V=final_V/10;
  Height=(final_V-init_V)*(59.375);
}
//------------------------------------parameter_determine----------------------------
void parameter_determine(){ 
if(Tail_bool_turn_Left == true)
  {  i =  Data_RF[0] -1;  //the number of movement
     amppt = Data_RF[1];//Amppt determine
     delay_t = Data_RF[2]*80;
     N = Period[i]*10;//cycle time
     n=0;
   }
else if(Tail_bool_turn_Right == true)
  {  i =  Data_RF[0] -1;  //the number of movement
     amppt = Data_RF[1];//Amppt determine
     delay_t = Data_RF[2]*80;
     N = Period[i]*10;//cycle time
     n=0;
   }
else if(Tail_bool_straight == true){
     i =  Data_RF[0] -1;  //the number of movement
     amppt = Data_RF[1];//Amppt determine
     w = Data_RF[2];// W determine
     shift = Data_RF[3];
     N = Period_S[i]/w*10;
     w_1 =  S_1[i][9]*w;
     w_2 =  S_1[i][19]*w;
}}


//------------------------------------Test motion------------------------------------
void Tail_control_turn_Right(){//right
         n %= (N+2);
         for (int m = 1, mm = 2; m <= mm; ++m)
            { double theta_now; 
              v=1000;
              if(m == 1){theta_now = abs(Turn_1[i][n]);
                         theta_now = amppt*theta_now;
                         position_now = -(theta_now/300*1023) + 512.0;
                         if(n==0){v=20;}
                         else if(abs(theta_last_1-theta_now)<2){v=50;}
                         else if(abs(theta_last_1-theta_now)>2&&abs(theta_last_1-theta_now)<5){v=128;}
                         else if(abs(theta_last_1-theta_now)>5&&abs(theta_last_1-theta_now)<10){v=256;}
                         else if(abs(theta_last_1-theta_now)>10){v=512;}
                         if(theta_now >= 0){v=64;}
                         robot.setJointSpeed(M_ID_[m], v);
                         robot.moveJoint(M_ID_[m], position_now);  
                         theta_last_1=theta_now;}
              else if(m == 2){theta_now = abs(Turn_2[i][n]);
                              theta_now = amppt*theta_now;
                              position_now = theta_now/300*1023 + 512.0;
                              /*if(n==0){v=20;}
                              else if(abs(theta_last_2-theta_now)<2){v=50;}
                              else if(abs(theta_last_2-theta_now)>2&&abs(theta_last_2-theta_now)<5){v=128;}
                              else if(abs(theta_last_2-theta_now)>5&&abs(theta_last_2-theta_now)<10){v=256;}
                              else if(abs(theta_last_2-theta_now)>10){v=512;}*/
                              robot.setJointSpeed(M_ID_[m], v);
                              robot.moveJoint(M_ID_[m], position_now);
                              theta_last_2=theta_now;}
            }
            ++n;
            delay(delay_t); // time for motor
            if(n==N+2){ //N+2=12 bcuz turn is only size 12
              Tail_bool_turn_Right = false; 
              DONE=true;
              theta_last_1=0;
              theta_last_2=0;
              delay(1500);}
}

void Tail_control_turn_Left(){//left
         n %= (N+2);
         for (int m = 1, mm = 2; m <= mm; ++m)
            { double theta_now; 
              v=1000;
              if(m == 1){theta_now = Turn_1[i][n];
                         theta_now = amppt*theta_now;
                         position_now = -(theta_now/300*1023) + 512.0;
                         if(n==0){v=20;}
                         else if(abs(theta_last_1-theta_now)<2){v=50;}
                         else if(abs(theta_last_1-theta_now)>2&&abs(theta_last_1-theta_now)<5){v=128;}
                         else if(abs(theta_last_1-theta_now)>5&&abs(theta_last_1-theta_now)<10){v=256;}
                         else if(abs(theta_last_1-theta_now)>10){v=512;}
                         if(theta_now >= 0){v=64;}
                         robot.setJointSpeed(M_ID_[m], v);
                         robot.moveJoint(M_ID_[m], position_now);  
                         theta_last_1=theta_now;}
              else if(m == 2){theta_now = Turn_2[i][n];
                              theta_now = amppt*theta_now;
                              position_now = theta_now/300*1023 + 512.0;
                              /*if(n==0){v=20;}
                              else if(abs(theta_last_2-theta_now)<2){v=50;}
                              else if(abs(theta_last_2-theta_now)>2&&abs(theta_last_2-theta_now)<5){v=128;}
                              else if(abs(theta_last_2-theta_now)>5&&abs(theta_last_2-theta_now)<10){v=256;}
                              else if(abs(theta_last_2-theta_now)>10){v=512;}*/
                              robot.setJointSpeed(M_ID_[m], v);
                              robot.moveJoint(M_ID_[m], position_now);
                              theta_last_2=theta_now;}
            }
            ++n;
            delay(delay_t); // time for motor
            if(n==N+2){ //N+2=12 bcuz turn is only size 12
              Tail_bool_turn_Left = false;
              DONE=true;
              theta_last_1=0;
              theta_last_2=0;
              delay(1500);}
}

void Tail_control_straight(){
    n %= (N+1); //n/(N+1)　餘數 remaining number
    t = n*0.1;  //time for fomula
         for (int m = 1, mm = 2; m <= mm; ++m)
            { double theta_now; 
                if(m == 1){theta_now = S_1[i][0] + S_1[i][1]*cos(t*w_1) + S_1[i][2]*sin(t*w_1) + S_1[i][3]*cos(2*t*w_1) + S_1[i][4]*sin(2*t*w_1)+S_1[i][5]*cos(3*t*w_1) + S_1[i][6]*sin(3*t*w_1)+S_1[i][7]*cos(4*t*w_1) + S_1[i][8]*sin(4*t*w_1);
                           theta_now = amppt*(theta_now+shift);
                           position_now = -(theta_now/300*1023) + 512.0;
                           if(n==0){v=20;}
                           else if(abs(theta_last_1-theta_now)<2){v=50;}
                           else if(abs(theta_last_1-theta_now)>2&&abs(theta_last_1-theta_now)<5){v=128;}
                           else if(abs(theta_last_1-theta_now)>5&&abs(theta_last_1-theta_now)<10){v=256;}
                           else if(abs(theta_last_1-theta_now)>10){v=512;}
                           robot.setJointSpeed(M_ID_[m], v);
                           robot.moveJoint(M_ID_[m], position_now);
                           theta_last_1=theta_now;}
              else if(m == 2){theta_now = S_1[i][10] + S_1[i][11]*cos(t*w_2) + S_1[i][12]*sin(t*w_2) + S_1[i][13]*cos(2*t*w_2) + S_1[i][14]*sin(2*t*w_2)+S_1[i][15]*cos(3*t*w_2) + S_1[i][16]*sin(3*t*w_2)+S_1[i][17]*cos(4*t*w_2) + S_1[i][18]*sin(4*t*w_2);
                              theta_now = amppt*(theta_now+shift);
                              position_now = theta_now/300*1023 + 512.0;
                              if(n==0){v=20;}
                              else if(abs(theta_last_2-theta_now)<2){v=50;}
                              else if(abs(theta_last_2-theta_now)>2&&abs(theta_last_2-theta_now)<5){v=128;}
                              else if(abs(theta_last_2-theta_now)>5&&abs(theta_last_2-theta_now)<10){v=256;}
                              else if(abs(theta_last_2-theta_now)>10){v=512;}
                              robot.setJointSpeed(M_ID_[m], v);
                              robot.moveJoint(M_ID_[m], position_now); 
                              theta_last_2=theta_now;}}
                              ++n;
             delay(delay_t);
             if(n==N+1){ //stop when n=3
              Tail_bool_straight = false;
              DONE=true;
              robot.moveJoint(M_ID_[1], 512);  
              robot.moveJoint(M_ID_[2], 512);}}

void Do_nothing(){
  n %= timer;
  delay(1);
  ++n;
  if(n==timer){
    DONE=true;
  }
}

//---------BOOL for action-----------------------------------------------
void STRAIGHT(){
  Data_RF[0] = 1.0;
  Tail_bool_straight = true;
  Tail_bool_turn_Left = false;
  Tail_bool_turn_Right = false; 
}
void LEFT(){
  Tail_bool_turn_Left = true;
  Tail_bool_straight = false;
  Tail_bool_turn_Right = false;
  
}
void RIGHT(){
  Tail_bool_turn_Right = true;
  Tail_bool_straight = false;
  Tail_bool_turn_Left = false;  
}

//---------UP DOWN--------------------------------------------------------
void UP(){
  G_pos=0;
}

void DOWN(){
  G_pos=2;
}

void U_D(){    
    if (OG_pos<G_pos){ // DOWN
      robot.setJointSpeed(ID, 2047);
      delay(530);
      robot.setJointSpeed(ID, 1024);
      delay(100);
      ++OG_pos;
    }
    else if (OG_pos>G_pos){ //UP
      robot.setJointSpeed(ID, 1023);
      delay(530);
      robot.setJointSpeed(ID, 0);
      delay(100);
      --OG_pos;
    }
    else if (OG_pos==G_pos){
      robot.setJointSpeed(ID, 0);
    }
}

//----------OTA Web Updater----------------------------------------------
void OTA()
{
  // Connect to Wifi network
  WiFi.begin(ssid, password);
  Serial.println("");
  
  // Configures static IP address
  if (!WiFi.config(local_IP, gateway, subnet, primaryDNS, secondaryDNS)) {
  Serial.println("STA Failed to configure");
  }
  
  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  /*use mdns for host name resolution*/
  if (!MDNS.begin(host)) { //http://esp32.local
    Serial.println("Error setting up MDNS responder!");
    while (1) {
      delay(1000);
    }
  }
  Serial.println("mDNS responder started");
  /*return index page which is stored in serverIndex */
  server.on("/", HTTP_GET, []() {
    server.sendHeader("Connection", "close");
    server.send(200, "text/html", loginIndex);
  });
  server.on("/serverIndex", HTTP_GET, []() {
    server.sendHeader("Connection", "close");
    server.send(200, "text/html", serverIndex);
  });
  /*handling uploading firmware file */
  server.on("/update", HTTP_POST, []() {
    server.sendHeader("Connection", "close");
    server.send(200, "text/plain", (Update.hasError()) ? "FAIL" : "OK");
    ESP.restart();
  }, []() {
    HTTPUpload& upload = server.upload();
    if (upload.status == UPLOAD_FILE_START) {
      Serial.printf("Update: %s\n", upload.filename.c_str());
      if (!Update.begin(UPDATE_SIZE_UNKNOWN)) { //start with max available size
        Update.printError(Serial);
      }
    } else if (upload.status == UPLOAD_FILE_WRITE) {
      /* flashing firmware to ESP*/
      if (Update.write(upload.buf, upload.currentSize) != upload.currentSize) {
        Update.printError(Serial);
      }
    } else if (upload.status == UPLOAD_FILE_END) {
      if (Update.end(true)) { //true to set the size to the current progress
        Serial.printf("Update Success: %u\nRebooting...\n", upload.totalSize);
      } else {
        Update.printError(Serial);
      }
    }
  });
  server.begin();
}
