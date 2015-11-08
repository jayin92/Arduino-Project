void setup() {
 
  Serial.begin(9600);
  while (!Serial);
 
  
  for (int i = 0; i < 100; i++) {
    Serial.println (100);             // Data Points   0 -  99
  }
 
  for (int i = 0; i < 100; i++) {
    Serial.println (50);              // Data Points 100 - 199
  }
 
  for (int i = 0; i < 100; i++) {
    Serial.println (100);             // Data Points 200 - 299
  }
 
  for (int i = 0; i < 100; i++) {
    Serial.println (50);              // Data Points 300 - 399
  } 
 
  for (int i = 0; i < 100; i++) {
    Serial.println (100);             // Data Points 400 - 499
  }
  
}
 
void loop() {
 
}
