//-------- Control motor -----------------------------------------------------------------------------------------
#include "XL320.h"
#include <math.h>
#include <SoftwareSerial.h>
#define DepthPin 32
XL320 robot;
TaskHandle_t Task1; //Task 2 runs on core 1 which runs by default in Loop()

//------- variabls for blinking an LED with Millis------------------------------------
const int led = 2; // ESP32 Pin to which onboard LED is connected

//--------- OTA Web Updater ----------------------------------------------------------------------------------
#include <WiFi.h>
#include <WiFiClient.h>
#include <WebServer.h>
#include <ESPmDNS.h>
#include <Update.h>

const char* host = "esp32";

// For Lab Wifi
const char* ssid = "fishisgood";//10.1.1.30
const char* password = "fishisgood";
// Set your Static IP address
IPAddress local_IP(10, 1, 1, 40);
// Set your Gateway IP address
IPAddress gateway(10, 1, 1, 1);

/*// For Laptop Hotspot
const char* ssid = "qwertyuiop";//192.168.137.70
const char* password = "qwertyuiop";
// Set your Static IP address
IPAddress local_IP(192, 168, 137, 70);
// Set your Gateway IP address
IPAddress gateway(192, 168, 137, 1);
*/

WebServer server(80);

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
"<h1>Project OTA</h1>" //TITLE
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

//------------------無線接收 wireless signal receiving -----------------------------------------------------------------------------------------------------------------------
char mymessage[255];
char * p_buf;
double Data_RF[4] = {0.0,0.0,0.0,0.0};// Data_RF[0]:第幾個動作 which action  Data_RF[1]:Ampplitude Data_RF[2]:W(velocity of angle)
SoftwareSerial mySerial(18, 19); // (RX, TX)

//---------mode------------------------------------------------------------------------------------------------------------------------------------------------------------
boolean Tail_bool_turn_Left = false;
boolean Tail_bool_turn_Right = false;
boolean Tail_bool_straight = false;

//--------------------------　Variable　-----------------------------------------------------------------------------------------------------------------------------------
int const A = 10; //總數 total
int i; //index　動作索引 action index
int n = 0;
int N;
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
  mySerial.begin(57600);
  Serial.begin(1000000);
  pinMode(led,  OUTPUT);
  digitalWrite(led,HIGH);
  OTA();
  digitalWrite(led,LOW);
  robot.begin(Serial);
  robot.moveJoint(ID2, 512);
  robot.moveJoint(ID1, 512);
  //G_pos=1;
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
  RF_xSerial();  //接收指令 receiving signal data    
  delay(10);
  if(Tail_bool_turn_Left == true)  {Tail_control_turn_Left();}
  else if(Tail_bool_turn_Right == true)  {Tail_control_turn_Right();}
  else if(Tail_bool_straight == true)  {Tail_control_straight();}
  empty();
}

//--------------- Core 0 loop ------------------------------
void Task1code( void * pvParameters ){
  for(;;){
    server.handleClient();
    Read_Height();
    delay(100);
    
    if (OG_pos>2){
      OG_pos=2;
    }
    else if (OG_pos<0){
      OG_pos=0;
    }

    if (G_pos>2){
      G_pos=2;
    }
    else if (G_pos<0){
      G_pos=0;
    }
    
    if (OG_pos<G_pos){ // DOWN
      digitalWrite(led,HIGH);
      robot.setJointSpeed(ID, 2047);
      delay(530);
      robot.setJointSpeed(ID, 1024);
      delay(100);
      digitalWrite(led,LOW);
      ++OG_pos;
    }
    else if (OG_pos>G_pos){ //UP
      digitalWrite(led,HIGH);
      robot.setJointSpeed(ID, 1023);
      delay(530);
      robot.setJointSpeed(ID, 0);
      delay(100);
      digitalWrite(led,LOW);
      --OG_pos;
    }
    else if (OG_pos==G_pos){
      robot.setJointSpeed(ID, 0);
    }
  }
}

//---------------------- 無線傳輸 wireless transmiting------------------------------------------------------------------------------------------------------------------------------------------
void RF_xSerial(void)
{
  mySerial.listen();
  if (mySerial.available()) // judge have data or not , if exist!! store into array
  {
    for (int iMymessage = 0; 0 < mySerial.available(); ++iMymessage)
    {
      char c =  mySerial.read();
      mymessage[iMymessage] = c;
      delay(2);
    }
    p_buf = mymessage;
    
      switch (*p_buf) // [data formula] : H, data 1 , data 2 , data 3 , ...
      {        
        case 'L': case 'l': //轉彎動作 turning left action
        {
            Tail_bool_turn_Left = true;
            Tail_bool_turn_Right = false;
            Tail_bool_straight = false;
            decode_Data();
            parameter_determine();
        }        
        break;   
        
        case 'R': case 'r': //轉彎動作 turning right action
        {
            Tail_bool_turn_Right = true;
            Tail_bool_turn_Left = false;
            Tail_bool_straight = false;
            decode_Data();
            parameter_determine();
        }        
        break;
        
        case 'O': case 'o': //直線動作 straight action
        {
            Tail_bool_straight = true;
            Tail_bool_turn_Left = false;
            Tail_bool_turn_Right = false;  
            decode_Data();
            parameter_determine();
        }        
        break;    
        
        case 'S': case 's': //　　　停止 stop action
        {
          Tail_bool_turn_Left = false;
          Tail_bool_turn_Right = false;
          Tail_bool_straight = false;
          robot.moveJoint(ID2, 512);
          robot.moveJoint(ID1, 512);
        }break;

        case 'D': case 'd': 
        {
            if (G_pos<2){
              ++G_pos;
            }
        } 
        break;

        case 'U': case 'u': 
        {
            if (G_pos>0){
              --G_pos;
            }
        } 
        break;

        case 'F': case 'f': 
        {
            digitalWrite(led,HIGH);
            robot.setJointSpeed(ID, 2047);
            delay(250);
            robot.setJointSpeed(ID, 1024);
            delay(100);
            digitalWrite(led,LOW);
        } 
        break;

        case 'B': case 'b': 
        {
            digitalWrite(led,HIGH);
            robot.setJointSpeed(ID, 1023);
            delay(250);
            robot.setJointSpeed(ID, 0);
            delay(100);
            digitalWrite(led,LOW);
        } 
        break;
        
        case 'K': case 'k': //　追縱深度 depth sensory
        { 
          
        }
        break;
      }
 }
}

//-----------------------Data decoding---------------------------
void decode_Data(){//store all messages into Data_RF
  char* p;
  char buf[0x3F];
          if (',' == *(++p_buf)) 
            {
            for (int m = 0, mm = 4; m < mm; ++m) //NofData=4, run 4 times
            {
              for (p = buf, ++p_buf; (',' != *p_buf) && (-1 != *p_buf); ++p, (++p_buf)) //see value after ' ,' and stop when next value is ' ,' and store null for ' ,'
                  { (*p) = *p_buf;}//store value if not ' ,'
              (*p) = '\0'; //' ,' will be store as null
              Data_RF[m] = atof(buf);// convert value and null together into integer value and store into array
              }}}  
                 
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
     delay_t =80;
     shift = Data_RF[3];
     N = Period_S[i]/w*10;
     w_1 =  S_1[i][9]*w;
     w_2 =  S_1[i][19]*w;
     n=0;
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
              //Tail_bool_turn_Right = false; 
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
              //Tail_bool_turn_Left = false;
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
              //Tail_bool_straight = false;
              //done=true;
              robot.moveJoint(M_ID_[1], 512);  
              robot.moveJoint(M_ID_[2], 512);
              }
}

//-------Clear Array---------------
void empty(){
  uint32_t *q = (uint32_t *) &mymessage[0] ;
  while(q < (uint32_t *)(mymessage+0XFF)) {
    *q = (uint32_t)0;
    q++;
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
