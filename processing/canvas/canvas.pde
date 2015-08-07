/*
******
Processing Project 
Name:Canvas with random color
******

How to Control:
Up Arrow: Open the brush(have fill).
down Arrow: Open the eraser.
left Arrow: Open the brush(no fill).
Ctrl: Nothing.
mouse wheel: change brush size.
'M' on keyboard: change brush size to 20.
'N' on keyboard: change brush size to 200.

Made by Jay Li in Taoyaun, Taiwan
*/

int R;
int G;
int B;
PFont f;

int A;
int r = 75;
char mode;
long time;

void setup(){
  size(1000,500);
  f = createFont("Monaco",25,true); 
}
void draw(){
  
  R = int(random(255));
  G = int(random(255));
  B = int(random(255));
  A = int(random(255));
  println("R:" + R);
  println("G:" + G);
  println("B:" + B);
  println("Alpha:" + A);
  println("r:" + r);
  println("Point on the canvas:" + time);
  println(""); 
  textFont(f);
  fill(127);
  text(("Red:" + R),20,15);
  text(("Green:" + G),20,30);
  text(("Blue:" + B),20,45);
  
  if(mousePressed && (mouseButton == LEFT) && mode == '1'){
    noStroke();
    fill(R,G,B,A);
    ellipse(mouseX,mouseY,r,r);
    time++;
  }
  if(mousePressed && (mouseButton == RIGHT)&&(mode == '1' || mode == '3'|| mode == '4')){
    noStroke();
    fill(200);
    rect(0,0,1000,500);
    time = 0;
  }
  if(mousePressed && (mouseButton == LEFT) && mode == '2'){
    fill(255);
    noStroke();
    ellipse(mouseX,mouseY,r,r);    
  }
  if (mode == '3'){
  }
  if (mousePressed && (mouseButton == LEFT) && mode == '4'){  
    noFill();
    stroke(R,G,B,A);
    ellipse(mouseX,mouseY,r,r);
    time++;
  }    
  if (keyPressed){
    if (key == 'n' || key == 'N'){
      r = 200;
    }
    else if (key == 'm' || key == 'M'){
      r = 20;
    }
  }
}
void mouseWheel(MouseEvent event){
  float e = event.getAmount();
    if(e>0){
      r++;
    }
    if(e<0){
      r--;
    }
}

void keyPressed(){
  if(key == CODED){
    if(keyCode == UP){
      mode = '1';
    }
    else if(keyCode == DOWN){
      mode = '2';
    }
    else if(keyCode == CONTROL){
      mode = '3';
    }
    else if(keyCode == LEFT){
      mode = '4';
    }
  }
}
    
  
  

    
    
    
    
    
  
  
