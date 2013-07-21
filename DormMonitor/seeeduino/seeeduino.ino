#include <math.h>
#include <SoftwareSerial.h> 
#include <SerialLCD.h>
#include <DHT.h>
//#include <IRSendRev.h>
//#include <IRremote.h>

const int ANALOG_ANGLE = 0;
const int ANALOG_NOISE = 1;
const int ANALOG_LIGHT = 2;

//const int DIGITAL_IR = 3;
const int DIGITAL_TEM_HUM = 7;
const int DIGITAL_RELAY = 8;
const int DIGITAL_LED = 9;
const int DIGITAL_LCD_1 = 10;
const int DIGITAL_LCD_2 = 11;
const int DIGITAL_MOTION = 12;

float light_bright = 50;

SerialLCD slcd(DIGITAL_LCD_1, DIGITAL_LCD_2);
DHT dht(DIGITAL_TEM_HUM, DHT11);
//IRrecv irrecv(DIGITAL_IR);
//decode_results decodedSignal;

void setup() {
  Serial.begin(9600);

  slcd.begin();
  dht.begin();
//  IR.Init(DIGITAL_IR);
//  irrecv.enableIRIn();

  pinMode(DIGITAL_MOTION, INPUT); 
  pinMode(DIGITAL_RELAY,OUTPUT);
  pinMode(DIGITAL_LED,OUTPUT);
  
  slcd.backlight();
  slcd.print(" lunzii & juna");
  slcd.setCursor(6, 1);
  slcd.print("home");
  delay(3000);
  slcd.noBacklight();
  slcd.clear();
}

void loop() {
  light_bright = readAngle();
  lightProcess();
  showDisplay();
  lcdLightProcess();
//  delay(500);
}

void showDisplay(){
  float temp = readTemper();
  float humi = readHumidity();
  float noise = readNoise();
  
  //Temp
  slcd.setCursor(0, 0);
  slcd.print("Temp:");
  slcd.setCursor(5, 0);
  slcd.print(temp, 0);
  slcd.setCursor(7, 0);
  slcd.print("`C");
  
  //Humi
  slcd.setCursor(10, 0);
  slcd.print("Hu:");
  slcd.setCursor(13, 0);
  slcd.print(humi, 0);
  slcd.setCursor(15, 0);
  slcd.print("%");
  
  //Noise
  slcd.setCursor(0, 1);
  slcd.print("Nois:");
  slcd.setCursor(5, 1);
  slcd.print(noise, 0);
  if(noise < 10){
    slcd.setCursor(6, 1);
    slcd.print("  ");
  }else if(noise < 100){
    slcd.setCursor(7, 1);
    slcd.print(" ");
  }
  
  //Light
  slcd.setCursor(9, 1);
  slcd.print("Lig:");
  slcd.setCursor(13, 1);
  slcd.print(light_bright, 0);
  if(light_bright < 10){
    slcd.setCursor(14, 1);
    slcd.print("  ");
  }else if(light_bright < 100){
    slcd.setCursor(15, 1);
    slcd.print(" ");
  }
}

boolean ledStatus = false;
boolean relayStatus = false;
int relayDelay = 50;
int relayCurrent = 0;

void lightProcess(){
    //Light process
  if(readLight() <= light_bright){
    //turn on led
    if(!ledStatus){
      turnLED(true);
      ledStatus = true;
    }
    //turn on relay
    if(!relayStatus){
      if(readMotion()){
        turnRelay(true);
        relayStatus = true;
        relayCurrent = 0;
      }
    }else{
      if(readMotion()){
        relayCurrent = 0;
      }
      Serial.print("Relay Current: ");
      Serial.println(relayCurrent);
      if(relayCurrent < relayDelay){
        relayCurrent++;
      }else{
        turnRelay(false);
        relayStatus = false;
      }
    }
  }else{
    if(ledStatus){
      turnLED(false);
      ledStatus = false;
    }
    if(relayStatus){
      turnRelay(false);
      relayStatus = false;
    }
  }
}

boolean lcdStatus = false;
int lcdDelay = 5;
int lcdCurrent = 0;

void lcdLightProcess(){
  if(!lcdStatus){
    if(readMotion()){
      slcd.backlight();
      lcdStatus = true;
      lcdCurrent = 0;
    }
  }else{
    if(readMotion()){
      lcdCurrent = 0;
    }
    if(lcdCurrent < lcdDelay){
      lcdCurrent++;
    }else{
      slcd.noBacklight();
      lcdStatus = false;
    }
  }
}

float readLight(){
  float val = analogRead(ANALOG_LIGHT);
  Serial.print("Light: ");
  Serial.println(val);
  return val;
}

float readNoise(){
  float val = analogRead(ANALOG_NOISE);
  Serial.print("Noise: ");
  Serial.println(val);
  return val;
}

//float readTemp(){
//  int val = analogRead(ANALOG_TEMP);
//  float resistance = (float)(1023-val)*10000/val;
//  float temp = 1/(log(resistance/10000)/3975+1/298.15)-273.15;
//  Serial.print("Temperature: ");
//  Serial.println(temp);
//  
//  return temp;
//}

float readTemper(){
  float temp = dht.readTemperature();
  if (isnan(temp)) {
    Serial.println("Read temperature failed");
    return 0.0;
  } else {
    Serial.print("Temperature: "); 
    Serial.print(temp);
    Serial.println(" *C");
    return temp;
  }
}

float readHumidity(){
  float humi = dht.readHumidity();
  if (isnan(humi)) {
    Serial.println("Read humidity failed");
    return 0.0;
  } else {
    Serial.print("Humidity: "); 
    Serial.print(humi);
    Serial.println(" %");
    return humi;
  }
}

boolean readMotion(){
  int val = digitalRead(DIGITAL_MOTION);
  Serial.print("Motion: ");
  if(val == HIGH){
      Serial.println("true");
      return true;
    }else{
      Serial.println("false");
      return false;
    }
}

float readAngle(){
  float val = analogRead(ANALOG_ANGLE) / 2;
  Serial.print("Angle: ");
  Serial.println(val);
  return val;
}

//void readIR(){
//  unsigned char data[20];
//  if(IR.IsDta()){
//    Serial.print("IR: ");
//    int length = IR.Recv(data);
//    for(int i=0;i<length;i++){
//      Serial.print(data[i]);
//    }
//    Serial.println();
//  }else{
//    Serial.println("IR: null");
//  }
//  if(irrecv.decode(&decodedSignal)){
//    Serial.print("IR: recevied");
//    Serial.println(decodedSignal.value, HEX);
//  }else{
//    Serial.println("IR: no data");
//  }
//  irrecv.resume();
//}

void turnLED(boolean value){
  if(value){
    digitalWrite(DIGITAL_LED,HIGH);
  }else{
    digitalWrite(DIGITAL_LED,LOW);
  }
}

void turnRelay(boolean value){
  if(value){
    digitalWrite(DIGITAL_RELAY,HIGH);
  }else{
    digitalWrite(DIGITAL_RELAY,LOW);
  }
}
