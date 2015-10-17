long delayTime1;
long delayTime2;
void setup() {
  // put your setup code here, to run once:
  pinMode(13,OUTPUT);
  randomSeed(A0);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  
  digitalWrite(13,HIGH); 
  delay(delayTime1);
  digitalWrite(13,LOW);  
  delay(delayTime1);
  if(delayTime1 < 1000){
    delayTime1 ++;
    if(delayTime1 = 1000){
    delayTime1 --;
    if(delayTime1 = 0){
      delayTime1 ++;
    }       
    }
     
  }
  
  
}

