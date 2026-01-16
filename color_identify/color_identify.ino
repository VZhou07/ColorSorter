/*
 * Automated Color Sorter - Arduino 
 * Author: Vincent Zhou
 * Interfaces with TCS3200 sensor and communicates via Pulse Protocol to Raspberry Pi.
 */

//Pin Definitions
const int S0=8;
const int S1=9;
const int S2=10;
const int S3=11;
const int PIN_SENSOR_OUT=12;
const int PIN_COM=4; // Output to Raspberry Pi

//Struct for defining each color and information
struct ColorProfile {
  String name;
  int r_target,g_target,b_target;
  int tolerance;  
  int pulseCount; // Number of pulses to send to Pi
};

//Creating colors
ColorProfile orange={"Orange",10,18,19,3,2};
ColorProfile purple={"Purple",12,19,19,3,3}; 
ColorProfile red={"Red",20,50,50,10,4};
ColorProfile green={"Green",50,20,50,10,5};

int redFreq=0,greenFreq=0,blueFreq=0; 

void setup() {
  pinMode(S0,OUTPUT);
  pinMode(S1,OUTPUT);
  pinMode(S2,OUTPUT);
  pinMode(S3,OUTPUT);
  pinMode(PIN_COM,OUTPUT);
  pinMode(PIN_SENSOR_OUT,INPUT);
  // Set Frequency scaling to 20%
  digitalWrite(S0,HIGH);
  digitalWrite(S1,HIGH); 
  Serial.begin(9600);
}

void loop() {
  readColorSensor();
  String detectedColor=identifyColor();
  Serial.print("Detected: "); Serial.println(detectedColor);
  delay(2000);  //small delay
}

void readColorSensor() {
  // Read Red
  digitalWrite(S2,LOW);
  digitalWrite(S3,LOW);
  redFreq=pulseIn(PIN_SENSOR_OUT,LOW);
  delay(10);
  // Read Blue
  digitalWrite(S2,LOW);
  digitalWrite(S3,HIGH);
  blueFreq=pulseIn(PIN_SENSOR_OUT,LOW);
  delay(10);
  // Read Green
  digitalWrite(S2,HIGH);
  digitalWrite(S3,HIGH);
  greenFreq=pulseIn(PIN_SENSOR_OUT,LOW);
  delay(10);


  //output for debugging
  Serial.print("R:"); Serial.print(redFreq);
  Serial.print(" G:"); Serial.print(greenFreq);
  Serial.print(" B:"); Serial.println(blueFreq);
}

String identifyColor() {
  // Logic for Orange
  if (abs(redFreq-orange.r_target)<orange.tolerance && abs(greenFreq-orange.g_target)<orange.tolerance) {   
    sendPulses(orange.pulseCount);
    return orange.name;  
  }
  // Logic for Purple
  else if (abs(redFreq-purple.r_target)<purple.tolerance && abs(greenFreq-purple.g_target)<purple.tolerance) {
    sendPulses(purple.pulseCount);
    return purple.name;
  }
  // Logic for Red
  else if (redFreq<blueFreq && redFreq<greenFreq && redFreq<25) {
    sendPulses(red.pulseCount);
    return red.name;
  }
  // Logic for Green
  else if (greenFreq<redFreq && greenFreq<blueFreq) {
    sendPulses(green.pulseCount);
    return green.name;
  }
  // Unknown
  else {
    sendPulses(6); // 6 pulses for unknown
    return "Unknown";
  }
}
// Sends a specific number of 1s to the Raspberry Pi
void sendPulses(int count) {
  for (int i=0; i<count; i++) {
    digitalWrite(PIN_COM,HIGH);
    delay(50); // Signal ON for 50ms
    digitalWrite(PIN_COM,LOW);
    delay(50); // Signal OFF for 50ms
  }
  delay(500); // Cooldown
}