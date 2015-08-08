/*
 ******
 Arduino Project
 Name:DHT11 and IoT(Internet of thing)
 ******
 Use Arduino Uno and Arduino Ethernet Shieid

 Upload Location : thingspeak.com and dht11.ddns.net 

 p.s. My English is poor
 */
#include <SPI.h>
#include <Ethernet.h>
#include <dht.h>
#include <Temboo.h>
#include "TembooAccount.h"

// Local Network Settings
byte mac[] = { 0xD4, 0x28, 0xB2, 0xFF, 0xA0, 0xA1 };
// Must be unique on local network
//IPAddress ip(192,168,1, 25);
//IPAddress subnet(255, 255, 255, 0);
//IPAddress gateway(192,168,1, 1);
// ThingSpeak Settings
char thingSpeakAddress[] = "api.thingspeak.com";
String writeAPIKey = "0IEUMCWN76JU3HV2";
const int updateThingSpeakInterval = 16 * 1000;      // Time interval in milliseconds to update ThingSpeak (number of seconds * 1000 = interval)

// Variable Setup
long lastConnectionTime = 0;
boolean lastConnected = false;
int failedCounter = 0;
dht DHT;

String temp;
String humi;
int tempi;
int humii;
int clientPeople = 0;
int numRuns = 1;
char t;
// Initialize Arduino Ethernet Client
EthernetClient client;
EthernetServer server(80);

void setup()
{
  // Start Serial for debugging on the Serial Monitor
  Serial.begin(9600);

  // Start Ethernet on Arduino
  startEthernet();
  Ethernet.begin(mac);
  server.begin();
}

void loop()
{
  // Read value from Analog Input Pin 0
  DHT.read11(2);
  temp = String(DHT.temperature);
  humi = String(DHT.humidity);
  tempi = DHT.temperature;
  humii = DHT.humidity;

  // Print Update Response to Serial Monitor
  if (client.available())
  {
    char c = client.read();
    Serial.print(c);
  }

  // Disconnect from ThingSpeak
  if (!client.connected() && lastConnected)
  {
    Serial.println("...disconnected");
    Serial.println();

    client.stop();
  }

  // Update ThingSpeak
  if (tempi > 15 && tempi < 61 && humii > 20 && humii < 101) {
    ServerForWeb();   
    if (!client.connected() && (millis() - lastConnectionTime > updateThingSpeakInterval))
    {
      updateThingSpeak("field1=" + temp + "&field2=" + humi);
    }

  }
  else if ((tempi < 15 && tempi > 61 && humii < 20 && humii > 101) || (millis() - lastConnectionTime < updateThingSpeakInterval)) {
    ServerForWebError();
  }


  // Check if Arduino Ethernet needs to be restarted
  if (failedCounter > 3 ) {
    startEthernet();
  }

  lastConnected = client.connected();
}

void updateThingSpeak(String tsData)
{
  if (client.connect(thingSpeakAddress, 80))
  {
    client.print("POST /update HTTP/1.1\n");
    client.print("Host: api.thingspeak.com\n");
    client.print("Connection: close\n");
    client.print("X-THINGSPEAKAPIKEY: " + writeAPIKey + "\n");
    client.print("Content-Type: application/x-www-form-urlencoded\n");
    client.print("Content-Length: ");
    client.print(tsData.length());
    client.print("\n\n");

    client.print(tsData);

    lastConnectionTime = millis();

    if (client.connected())
    {
      Serial.println("Connecting to ThingSpeak...");
      Serial.println();

      failedCounter = 0;
    }
    else
    {
      failedCounter++;

      Serial.println("Connection to ThingSpeak failed (" + String(failedCounter, DEC) + ")");
      Serial.println();
    }

  }
  else
  {
    failedCounter++;

    Serial.println("Connection to ThingSpeak Failed (" + String(failedCounter, DEC) + ")");
    Serial.println();

    lastConnectionTime = millis();
  }
}

void startEthernet()
{

  client.stop();

  Serial.println("Connecting Arduino to network...");
  Serial.println();

  delay(1000);

  // Connect to network amd obtain an IP address using DHCP
  if (Ethernet.begin(mac) == 0)
  {
    Serial.println("DHCP Failed, reset Arduino to try again");
    Serial.println();
  }
  else
  {
    Serial.println("Arduino connected to network using DHCP\n");
    Serial.println();
    Serial.print("local ip is:");
    Serial.println(Ethernet.localIP());
  }

  delay(1000);
}
void ServerForWeb() {
  EthernetClient client = server.available();
  if (client) {
    /*
    Serial.println("\n");
    Serial.print("Client people:");
    Serial.println(clientPeople);
    Serial.println("\n");
    */
    while (client.connected()) {
      //getTime();
      if (client.available()) {
        client.println("HTTP/1.1 200 OK");
        client.println("Content-Type: text/html");
        client.println("Refresh: 1");
        client.println();

        client.println("<title>Temperature and Humidity</title>");
        client.println("<h1>DHT11 Temperature and Humidity:</h1>");
        client.println("<br>");
        client.println("Temperature:");
        client.println(temp);
        client.println("degC");
        client.println("<br>");
        client.println("<br>");
        client.println("Humidity:");
        client.println(humi);
        client.println("%");
        client.println("<br><br><br>");
       // client.println("Update time:");                
       // client.println(t);
        break;
      }
    }
    delay(1);
    client.stop();
  }
}
void ServerForWebError() {
  EthernetClient client = server.available();
  if (client) {
    while (client.connected()) {
      if (client.available()) {
        client.println("HTTP/1.1 200 OK");
        client.println("Content-Type: text/html");
        client.println("Refresh: 1");
        client.println();

        client.println("<title>Error!!!</title>");
        client.println("<h1>Sensor error.Please check the sensor</h1>");
        break;
      }
    }
    delay(1);
    client.stop();
  }
}
void getTime() {
  TembooChoreo GetDateChoreo(client);
  // Invoke the Temboo client
  GetDateChoreo.begin();
  // Set Temboo account credentials
  GetDateChoreo.setAccountName(TEMBOO_ACCOUNT);
  GetDateChoreo.setAppKeyName(TEMBOO_APP_KEY_NAME);
  GetDateChoreo.setAppKey(TEMBOO_APP_KEY);
  // Set Choreo inputs
  String AddHoursValue = "8";
  GetDateChoreo.addInput("AddHours", AddHoursValue);
  // Identify the Choreo to run
  GetDateChoreo.setChoreo("/Library/Utilities/Dates/GetDate");
  // Run the Choreo; when results are available, print them to serial
  GetDateChoreo.run();
  while (GetDateChoreo.available()) {
    t = GetDateChoreo.read();    
  }
  GetDateChoreo.close();  
}

