const unsigned int BAUD_RATE = 9600;
const unsigned int PIR_INPUT_PIN = 2;//SR501 Digital pin 2
const unsigned int TEMP_INPUT_PIN = 3;//Temperature Digital pin 3
const unsigned int DIS_TRIG_PIN = 4;//Distance Digital pin 4
const unsigned int DIS_ECHO_PIN = 5;//Distance Digital pin 5

//SR501
void motion_detected() {
  if(digitalRead(PIR_INPUT_PIN) == HIGH){
    Serial.println("motion:true");
  }else{
    Serial.println("motion:false");
  }
}

//Temperature
#include <dht11.h>
dht11 DHT11;
void read_temperature(){
  int chk = DHT11.read(TEMP_INPUT_PIN);

  Serial.println("Debug:Tempature sensor");
  switch (chk)
  {
    case DHTLIB_OK: 
                Serial.println("Debug:OK"); 
                break;
    case DHTLIB_ERROR_CHECKSUM: 
                Serial.println("Debug:Checksum error"); 
                break;
    case DHTLIB_ERROR_TIMEOUT: 
                Serial.println("Debug:Time out error"); 
                break;
    default: 
                Serial.println("Debug:Unknown error"); 
                break;
  }
  
  Serial.print("Humidity: ");
  Serial.println((float)DHT11.humidity, 2);

  Serial.print("Temperature:");
  Serial.println((float)DHT11.temperature, 2);
}


//Ping Distance
void distance_detected(){
  long duration, distance;
  digitalWrite(DIS_TRIG_PIN, LOW);
  delayMicroseconds(2);

  digitalWrite(DIS_TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(DIS_TRIG_PIN, LOW);
  duration = pulseIn(DIS_ECHO_PIN, HIGH);
  distance = (duration/2) / 29.1;
  if (distance >= 200 || distance <= 0){
    Serial.println("distance:Out of range");
  }
  else {
    Serial.print("distance:");
    Serial.print(distance);
    Serial.println(" cm");
  }
  delay(500);
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(BAUD_RATE);
  
  //distance
  pinMode(DIS_TRIG_PIN, OUTPUT);
  pinMode(DIS_ECHO_PIN, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly: 
//  motion_detected();
//  read_temperature();
  distance_detected();
  delay(300);
}
