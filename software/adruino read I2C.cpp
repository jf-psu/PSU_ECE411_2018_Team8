
#project ECE411
#Phong Nguyen
#include <Wire.h>    // imports the wire library for talking over I2C 
#include "Adafruit_INA219.h"  // import the Voltage and current Sensor Library
Adafruit_BMP085 mySensor;  // create sensor object called mySensor
 
float V;  // Variable for holding temp in V
float I;  // Variable for holding temp in I

 
void setup(){
Serial.begin(115200); //turn on serial monitor
mySensor.begin();   //initialize mySensor
}
 
void loop() {
V = mySensor.getBusVoltage_V(); //  Read Bus Voltage
I = mySensor.getCurrent_mA(); //Read Current
 
Serial.println(V); //Print Your results
Serial.print(" , ");
Serial.println(I);
delay(250); //Pause between readings.
}


//https://learn.adafruit.com/adafruit-ina219-current-sensor-breakout/arduino-code
