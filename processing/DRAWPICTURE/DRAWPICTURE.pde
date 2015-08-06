int R;
int G;
int B;
int A;
int r = 75;
char mode;

void setup(){
  size(1000,500);
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
  println("");
  if(mode == '1'){
    noFill();
    stroke(R,G,B,A);
    ellipse(mouseX,mouseY,r,r);
  }
  
  if(mousePressed && (mouseButton == LEFT) && mode == '1'){
    noStroke();
    fill(R,G,B,A);
    ellipse(mouseX,mouseY,r,r);
  }
  if(mousePressed && (mouseButton == RIGHT)&& mode == '1'){
    noStroke();
    fill(255);
    rect(0,0,1000,500);
  }
  if(mode == '2'){
    fill(255);
    noStroke();
    ellipse(mouseX,mouseY,r,r);    
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
  }
}
    
  
  

    
    
    
    
    
  
  
