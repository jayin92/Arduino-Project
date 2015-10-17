#include <dht.h>

dht DHT;

long DataNumber;
float temp;
float humi;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  DHT.read11(2);
  temp = DHT.temperature;
  humi = DHT.humidity;
  DataNumber++;
  Serial.print("Temperature:");
  Serial.println(temp);  
  Serial.print("Humidity:");
  Serial.println(humi);
  Serial.print("Entries:");
  Serial.println(DataNumber);
  Serial.println("\n");
  delay(500);  
}

