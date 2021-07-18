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
const char* password = "lab314314";

WebServer server(80);

// Set your Static IP address
IPAddress local_IP(10, 1, 1, 40);
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
"<h1>AUTO Perfect</h1>"
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
int analogInPin_1 = 35;  // Analog input pin that the potentiometer is attached to

int IRsensorValue_1=0;

//------------------ Parameter -----------------------------------------------------------------------------------------------------------------------
int current_action = 0;//0-26 action, for row 
//---------mode------------------------------------------------------------------------------------------------------------------------------------------------------------
boolean Tail_bool_turn_Left = false;
boolean Tail_bool_turn_Right = false;
boolean Tail_bool_straight = false;
boolean DONE = true;

//--------------------------　Variable　-----------------------------------------------------------------------------------------------------------------------------------
int i; //index　動作索引 action index
int n = 0;
int turns =0;
int OG_pos=0;
int G_pos=0;
int Height;
double delay_t = 80;
double v=0;
double init_V; //initial voltage reading 
double final_V;// final voltage reading

//-------------------　傅立葉參數 fourier number  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

int Turn_Straight[2][8] = {
{ ID1,          ID2,           ID1,          ID2,           ID1,          ID2,           ID1,          ID2}, 
{ (130)/0.2929, (190)/0.2929 , (150)/0.2929, (150)/0.2929 , (170)/0.2929, (110)/0.2929 , (150)/0.2929, (150)/0.2929 }, 
};

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
  if (DONE==true){
    MARKOV();
  } 
  
  if(IRsensorValue_1>=1000){ 
    current_action = 12;
    Tail_bool_turn_Left = false;
    Tail_bool_turn_Right = false;
    Tail_bool_straight = false; 
    
    robot.setJointSpeed(M_ID_[1], 300);   
    robot.setJointSpeed(M_ID_[2], 307); 
    delay(10); 

    while(IRsensorValue_1>=1000 ){
      robot.moveJoint(M_ID_[1], 512);
      delay(10); 
      robot.moveJoint(M_ID_[2], 512);
      delay(10); 
      
      robot.moveJoint(M_ID_[1], 615);
      delay(50); 
      robot.moveJoint(M_ID_[2], 376);
      delay(200); 

      robot.moveJoint(M_ID_[1], 512);
      delay(50); 
      robot.moveJoint(M_ID_[2], 512);
      delay(200); 
    }
    
    DONE = true;
  }
  
  while(DONE!=true){
    if(IRsensorValue_1>=1000){
      DONE=true;
      robot.moveJoint(M_ID_[1], 512);
      robot.moveJoint(M_ID_[2], 512);
      delay(10); 
      break;
    }

    if(Tail_bool_turn_Left == true)  {Tail_control_turn_Left();}
    else if(Tail_bool_turn_Right == true)  {Tail_control_turn_Right();}
    else if(Tail_bool_straight == true)  {Tail_control_straight();}
  }
}

//--------------- Core 0 loop ------------------------------
void Task1code( void * pvParameters ){
  for(;;){
    server.handleClient();
    IRsensorValue_1 = analogRead(analogInPin_1);
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
          STRAIGHT(); 
          DONE = false;

      }
  
      else if (current_action == 1 ){ //Straight and UP
        UP();
        STRAIGHT(); 
        DONE=false;
      }
  
      else if (current_action == 2 ){ // Right 45* and UP
        UP();
        RIGHT();
        turns=1;
        DONE=false;
      }
  
      else if (current_action == 3 ){ // Right 90* and UP
        UP();
        RIGHT();
        turns=3;
        DONE=false;
      }
  
      else if (current_action == 4 ){ // Right 135* and UP
        UP();
        RIGHT();
        turns=5;
        DONE=false;
      }
  
      else if (current_action == 5 ){ // Right 180* and UP
        UP();
        RIGHT();
        turns=7;
        DONE=false;
      }
  
      else if (current_action == 6 ){ // Left 135* and UP
        UP();
        LEFT();
        turns=5;
        DONE=false;
      }
  
      else if (current_action == 8 ){ //Left 45* and UP
        UP();
        LEFT();
        turns=1;
        DONE=false;
      }
 
      else if (current_action == 9 ){ // Straight
        STRAIGHT(); 
        DONE=false;
      }
  
      else if (current_action == 10){ // Right 45*
        RIGHT();
        turns=1;
        DONE=false;
      }
 
      else if (current_action == 11){ // Right 90*
        RIGHT();
        turns=3;
        DONE=false;
      }
  
      else if (current_action == 12){ // Right 135*
        RIGHT();
        turns=5;
        DONE=false;
      }
  
      else if (current_action == 13){ // Right 180*
        RIGHT();
        turns=7;
        DONE=false;
      }
  
      else if (current_action == 14){ // Left 135*
        LEFT();
        turns=5;
        DONE=false;
      }
  
      else if (current_action == 16){ // Left 45*
        LEFT();
        turns=1;
        DONE=false;
      }
 
      else if (current_action == 17){ // Straight and Down
        DOWN();
        STRAIGHT(); 
        DONE=false;
      }
  
      else if (current_action == 18){ // Right 45* and Down
        DOWN();
        RIGHT();
        turns=1;
        DONE=false;
      }
  
      else if (current_action == 19){ // Right 90* and Down
        DOWN();
        RIGHT();
        turns=3;
        DONE=false;
      }
  
      else if (current_action == 21){ // Right 180* and Down
        DOWN();
        RIGHT();
        turns=7;
        DONE=false;
      }
  
      else if (current_action == 22){ // Left 135* and Down
        DOWN();
        LEFT();
        turns=5;
        DONE=false;
      }
  
      else if (current_action == 23){ //Left 90* and Down
        DOWN();
        LEFT();
        turns=3;
        DONE=false;
      }

      else if (current_action == 24){ // Right 90*
        RIGHT();
        turns=3;
        DONE=false;
      }
      else if (current_action == 25){ // Left 135*
        LEFT();
        turns=5;
        DONE=false;
      }
   
   Prob=0;
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

void Read_IR(){

  for(int j=0;j<10;j++){
    server.handleClient();
    IRsensorValue_1 = analogRead(analogInPin_1);
    delay(100);
  }
  
}

//------------------------------------Test motion------------------------------------
void Tail_control_turn_Right(){//right
    robot.setJointSpeed(M_ID_[1], 300);   
    robot.setJointSpeed(M_ID_[2], 307); 
    delay(10); 

    robot.moveJoint(M_ID_[1], 512);
    robot.moveJoint(M_ID_[2], 512);
    delay(10); 
    
    robot.moveJoint(M_ID_[1], 410);
    delay(50); 
    robot.moveJoint(M_ID_[2], 649);
    delay(200); 

    robot.moveJoint(M_ID_[1], 512);
    delay(50); 
    robot.moveJoint(M_ID_[2], 512);
    delay(200); 

    turns--;
    if(turns<=0){
      DONE = true;
    }
}

void Tail_control_turn_Left(){//left
    robot.setJointSpeed(M_ID_[1], 300);   
    robot.setJointSpeed(M_ID_[2], 307); 
    delay(10); 

    robot.moveJoint(M_ID_[1], 512);
    robot.moveJoint(M_ID_[2], 512);
    delay(10); 
    
    robot.moveJoint(M_ID_[1], 615);
    delay(50); 
    robot.moveJoint(M_ID_[2], 376);
    delay(200); 

    robot.moveJoint(M_ID_[1], 512);
    delay(50); 
    robot.moveJoint(M_ID_[2], 512);
    delay(200); 

    turns--;
    
    if(turns<=0){
       DONE = true;  
    }
     

}

void Tail_control_straight(){
    n=0;
    robot.moveJoint(M_ID_[1], 512); 
    robot.moveJoint(M_ID_[2], 512);
    delay(10); 
 
    robot.setJointSpeed(M_ID_[1], 300);   
    robot.setJointSpeed(M_ID_[2], 307); 
    delay(10); 
    
    while(n<8){
        //robot.moveJoint(Turn_Straight[0][n], Turn_Straight[1][n]);
        robot.moveJoint(Turn_Straight[0][n+1], Turn_Straight[1][n+1]);
        n=n+2;
        delay(170);
      }
      DONE=true;
}

//---------BOOL for action-----------------------------------------------
void STRAIGHT(){
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
  digitalWrite(led,LOW);
}

void DOWN(){
  G_pos=1;
  digitalWrite(led,HIGH);
}

void U_D(){    
    if (OG_pos<G_pos){ // DOWN
      robot.setJointSpeed(ID, 2047);
      delay(1060);
      robot.setJointSpeed(ID, 1024);
      delay(100);
      ++OG_pos;
    }
    else if (OG_pos>G_pos){ //UP
      robot.setJointSpeed(ID, 1023);
      delay(1060);
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
    for(int i=0;i<10;i++){
      delay(500);
      Serial.print(".");
    }
    break;
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
