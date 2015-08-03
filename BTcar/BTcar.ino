#include <SoftwareSerial.h>
#include <dht11.h>
SoftwareSerial BT (12, 11);
char val = 'a';
int chk;
int random_;
int temp;
int humi;
const byte EA = 2;
const byte IA = 3;
const byte EB = 4;
const byte IB = 5;

byte echo = 9;
byte trig = 8;

const byte dhtPin = A0;
dht11 DHT11;
unsigned long dis;


byte speed = 255;

void forward() {
  analogWrite(EA, -speed);
  digitalWrite(IA, HIGH);
  analogWrite(EB, -speed);
  digitalWrite(IB, HIGH);
  
}
void backward() {
  analogWrite(EA, speed);
  digitalWrite(IA, LOW);
  analogWrite(EB, speed);
  digitalWrite(IB, LOW);
  
}
void stop() {
  analogWrite(EA, 0);
  digitalWrite(IA, LOW);
  digitalWrite(IB, LOW);
  analogWrite(EB, 0);
  
}
void right() {
  analogWrite(EA, -speed);
  digitalWrite(IA, HIGH);
  analogWrite(EB, speed);
  digitalWrite(IB, LOW);
  
}
void left() {
  analogWrite(EA, speed);
  digitalWrite(IA, LOW);
  analogWrite(EB, -speed);
  digitalWrite(IB, HIGH);
  
}
void BT_control() {  
  switch (val) {
    case '8':
      forward();
      delay(35);
      stop();      
      break;
    case '5':
      stop();      
      break;
    case '6':
      right();      
      delay(35);
      stop();
      break;
    case '4':
      left();      
      delay(35);
      stop();
      break;
    case '2':
      backward();
      delay(35);
      stop();      
      break;
    case '1':      
      chk = DHT11.read(A0);
      if (chk == 0) {
        temp = DHT11.temperature;
        BT.write(temp);
      }
      break;
    case '3':      
      chk = DHT11.read(A0);
      if (chk == 0) {
        humi = DHT11.humidity;
        BT.write(humi);
      }
      break;
  }

}
void US() {
  dis = ping() / 58;
  if (dis <= 25) {
    stop();
    backward();
    delay(250);
    stop();
  }
}
void BT_auto() {
  dis = ping()/58;
  forward();  
  random_ = random(0, 2);
  if (dis <= 5) {
    switch (random_) {
      case 0:
        right();
        delay(500);
        forward();
        delay(300);
        stop();
        break;
      case 1:
        left();
        delay(500);
        forward();
        delay(300);
        stop();
        break;
    }
  }
}
void AU(){
  if(val =='9'){
    BT_auto();
  }
}
unsigned long ping() {
  digitalWrite(trig, HIGH);
  delayMicroseconds(5);
  digitalWrite(trig, LOW);

  return pulseIn(echo, HIGH);
}
void setup() {
  pinMode(EA, OUTPUT);
  pinMode(IA, OUTPUT);
  pinMode(EB, OUTPUT);
  pinMode(IB, OUTPUT);
  pinMode(trig, OUTPUT);
  BT.begin(9600);
  Serial.begin(9600);   
}
void loop() {
  //Serial.println("read");  
  Serial.println(val+"\n");
  Serial.println(dis);
  
  if (BT.available()) {    
    val = BT.read(); 
    BT_control();      
  }
  AU();
   
}
