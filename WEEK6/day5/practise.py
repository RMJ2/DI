import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'postgres'
DATABASE = 'bootcamp'

connection = pyscopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)

------

Unit 8 - lesson 5 (HARD)
//Make Karel fill the world
//with beepers
function main() {
   final();
   
}

function final() {
   while(frontIsClear()){
      putBeeperLine();
      if (leftIsClear()){
         goBack();
         goUp();
   }
   }
}


function putBeeperLine(){
   putBeeper();
   while(frontIsClear()) {
      move();
      putBeeper();
   }
}

function goBack(){ 
   turnAround();
   while(frontIsClear()){
   move();
   }
}

function goUp(){
   turnRight();
   move();
   turnRight();
}


Unit 9 - Lesson 2

//Karel must help rebuild 
//broken columns. Make a 
//column of beepers above
//each beeper you find on
//the first row
function main() {
   while(frontIsClear()){
      move();
      build();
   }
   comeBack();
   while(frontIsClear()){
      move();
      build();
   }
   comeBack();
   while(frontIsClear()){
      move();
      build();
   }
}

function build(){
   if (beepersPresent()){
      turnLeft();
      while(frontIsClear()){  
         move();
         putBeeper();
      }
   }      
}

function comeBack(){
   turnAround(); 
   while(frontIsClear()){
      move();   
   }
   turnLeft();
}
   



   