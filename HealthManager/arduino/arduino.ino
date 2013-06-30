const unsigned int BAUD_RATE = 9600;
const unsigned int PIR_INPUT_PIN = 2;//SR501 Digital pin 2
const unsigned int TEMP_INPUT_PIN = 3;//Temperature Digital pin 3
const unsigned int DIS_TRIG_PIN = 4;//Distance Digital pin 4
const unsigned int DIS_ECHO_PIN = 5;//Distance Digital pin 5
const unsigned int DSM_INPUT_PIN = 0;//DSM Analog pin 0
const unsigned int AIR_INPUT_PIN = 1;//AIR Analog pin 1
const unsigned int LIGHT_INPUT_PIN = 2;//LIGHT Analog pin 2

//SR501
void read_motioin() {
  if(digitalRead(PIR_INPUT_PIN) == HIGH){
    Serial.println("motion:true");
//    Serial.write("motion:true");
  }else{
    Serial.println("motion:false");
//    Serial.write("motion:false");
  }
}

//Temperature
#include <dht11.h>
dht11 DHT11;
void read_temperature(){
  int chk = DHT11.read(TEMP_INPUT_PIN);

//  Serial.println("Debug:Tempature sensor");
//  switch (chk)
//  {
//    case DHTLIB_OK: 
//                Serial.println("Debug:OK"); 
//                break;
//    case DHTLIB_ERROR_CHECKSUM: 
//                Serial.println("Debug:Checksum error"); 
//                break;
//    case DHTLIB_ERROR_TIMEOUT: 
//                Serial.println("Debug:Time out error"); 
//                break;
//    default: 
//                Serial.println("Debug:Unknown error"); 
//                break;
//  }
  
  Serial.print("humidity:");
  Serial.print((float)DHT11.humidity, 2);

  Serial.print(",temperature:");
  Serial.println((float)DHT11.temperature, 2);
}


//Ping Distance
void read_distance(){
  long duration, distance;
  digitalWrite(DIS_TRIG_PIN, LOW);
  delayMicroseconds(2);

  digitalWrite(DIS_TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(DIS_TRIG_PIN, LOW);
  duration = pulseIn(DIS_ECHO_PIN, HIGH);
  distance = (duration/2) / 29.1;
  if (distance >= 200 || distance <= 0){
    Serial.println("distance:error");
  }
  else {
    Serial.print("distance:");
    Serial.print(distance);
    Serial.println("cm");
  }
  delay(500);
}

//fenchen DSM501A
void read_fenchen(){
  int value = analogRead(DSM_INPUT_PIN);
  Serial.print("dust:");
  Serial.println(value);
}

//Air MQ-135
void read_air(){
  int value = analogRead(AIR_INPUT_PIN);
  Serial.print("air:");
  Serial.println(value);
}

//Light LM358
void read_light(){
  int value = analogRead(LIGHT_INPUT_PIN);
  Serial.print("light:");
  Serial.println(value);
}


//connnection
void handle_connect(){
  if(Serial.available() > 0){
//    Serial.println("error:nothing");
    char inCase = Serial.read();
//    Serial.print("character recieved: ");
//    Serial.println(inCase);

    switch(inCase){
    case 'm':
      read_motioin();
      break;
    case 't':
      read_temperature();
      break;
    case 'd':
      read_distance();
      break;
    case 'f':
      read_fenchen();
      break;
    case 'a':
      read_air();
      break;
    case 'l':
      read_light();
      break;
    default:
      Serial.println("info:nothing");
      break;
    }
    Serial.flush();
//    delay(300);
  }
}


void setup() {
  // put your setup code here, to run once:
  Serial.begin(BAUD_RATE);
  
  //distance
  pinMode(DIS_TRIG_PIN, OUTPUT);
  pinMode(DIS_ECHO_PIN, INPUT);
}

void loop() {
  handle_connect();
}
