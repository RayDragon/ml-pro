#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <ESP8266mDNS.h>

const char* ssid = "ray";
const char* password = "qwert1234";

ESP8266WebServer server(80);






class HomeAut{
  public:
  bool d[9];
  int dd[9];
  HomeAut(){
    dd[0]=D0;
    dd[1]=D1;
    dd[2]=D2;
    dd[3]=D3;
    dd[4]=D4;
    dd[5]=D5;
    dd[6]=D6;
    dd[7]=D7;
    dd[8]=D8;
    for(int i=0;i<10;i++) {d[i]=false; switch_on(i);}
    
  }
  void switch_on(int pin_number){
    d[pin_number]=true;
    Serial.println("switch "+String(pin_number)+" was made on");
    digitalWrite(dd[pin_number], HIGH);
  }
  void switch_off(int pin_number){
    d[pin_number]=false;
    Serial.println("switch "+String(pin_number)+" was made off");
    digitalWrite(dd[pin_number], LOW);
  }
  String get_json_status(){
    String data="[";
    for(int i=0;i<9;i++){
      data += String(d[i]?1:0);
      if(i!=8) data += ",";
      else data += "]";
    }
    return data;
  }
} aut;






















const int led = D5;

void handleRoot(int i) {
  if(i>=0 && i<9){
    if(aut.d[i]==false) aut.switch_on(i);
    else aut.switch_off(i);
  }
  else Serial.print(i);
  server.send(200, "json", aut.get_json_status());
}

void handleNotFound(){
  Serial.println("/"+String(char('0'+1)));
  digitalWrite(led, 1);
  String message = "File Not Found\n\n";
  message += "URI: ";
  message += server.uri();
  message += "\nMethod: ";
  message += (server.method() == HTTP_GET)?"GET":"POST";
  message += "\nArguments: ";
  message += server.args();
  message += "\n";
  for (uint8_t i=0; i<server.args(); i++){
    message += " " + server.argName(i) + ": " + server.arg(i) + "\n";
  }
  server.send(404, "text/plain", message);
  digitalWrite(led, 0);
}
int i;
void setup(void){
  for(int i=0;i<9;i++)
    pinMode(aut.dd[i], OUTPUT);
  pinMode(led, OUTPUT);
  digitalWrite(led, 0);
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  Serial.println("");

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

  if (MDNS.begin("esp8266")) {
    Serial.println("MDNS responder started");
  }

    server.on("/0", [](){handleRoot(0); Serial.print("/"+char('0'+i));});
    server.on("/1", [](){handleRoot(1); Serial.print("/"+char('0'+i));});
    server.on("/2", [](){handleRoot(2); Serial.print("/"+char('0'+i));});
    server.on("/3", [](){handleRoot(3); Serial.print("/"+char('0'+i));});
    server.on("/4", [](){handleRoot(4); Serial.print("/"+char('0'+i));});
    server.on("/5", [](){handleRoot(5); Serial.print("/"+char('0'+i));});
    server.on("/6", [](){handleRoot(6); Serial.print("/"+char('0'+i));});
    server.on("/7", [](){handleRoot(7); Serial.print("/"+char('0'+i));});
    server.on("/8", [](){handleRoot(8); Serial.print("/"+char('0'+i));});
    server.on("/9", [](){handleRoot(9); Serial.print("/"+char('0'+i));});
    

  server.on("/inline", [](){
    server.send(200, "text/plain", "this works as well");
  });

  server.onNotFound(handleNotFound);

  server.begin();
  Serial.println("HTTP server started");
}

void loop(void){
  server.handleClient();
}






















