#include "ESP8266WiFi.h"
#include "oursensor.h"
const char* ssid = "ray";
const char* password =  "qwert1234";
 

WiFiServer wifiServer(80);
OurSensor sensor;
void setup() {
 
  Serial.begin(115200);
 
  delay(1000);
 
  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting..");
  }
 
  Serial.print("Connected to WiFi. IP:");
  Serial.println(WiFi.localIP());
 
  wifiServer.begin();
  sensor.init();
}
 
void loop() {
 
  WiFiClient client = wifiServer.available();
 
  if (client) {
 
    while (client.connected()) {
      sensor.updateValues();
      client.print(sensor.get_ax());
      while (client.available()>0) {
        char c = client.read();
        if(c=='a') Serial.print("___________________________");
        else if(c=='r') sensor.init();
        //client.println(sensor.get_ax());
        Serial.println("Data Sent");
      }
 
      delay(10);
    }
 
    client.stop();
    Serial.println("Client disconnected");
 
  }
}
