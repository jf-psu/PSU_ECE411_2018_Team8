//project ECE411
//Phong Nguyen
#include <Wire.h>    // imports the wire library for talking over I2C 
#include "Adafruit_INA219.h"  // import the Voltage and current Sensor Library
Adafruit_INA219 mySensor;  // create sensor object called mySensor

int LOAD_PIN = 11; // PB7
int LOAD_V_SENSE_PIN = 8; // PB4
#define AVG_COUNT 30
float V;  // Variable for holding temp in V
float I;  // Variable for holding temp in I
float P;
int16_t value;
char ch;
int ms_scaler = 1;//32;


void setup() {
  pinMode(LOAD_PIN, OUTPUT);
  pinMode(LOAD_V_SENSE_PIN, INPUT);

  // setup 62.5 kHz PWM mode, WARNING: modifies timer used for delay() and millis()
  TCCR0B = (TCCR0B & 0b11111000) | 0x01;
  Serial.begin(115200); //turn on serial monitor
  mySensor.begin();   //initialize mySensor
  mySensor.setCalibration_16V_400mA();
}


void set_load(int pwm_value)
{
  analogWrite(LOAD_PIN, pwm_value);

}


void get_power_sensor_data()
{
}

void read_sensor_loop()
{
  float v_shunt;
  int load_v;
  
  while (1)
  {
      V = mySensor.getBusVoltage_V();
      v_shunt = mySensor.getShuntVoltage_mV();
      I = mySensor.getCurrent_mA(); //Read Current
      load_v = analogRead(LOAD_V_SENSE_PIN);
      
      delay(10 * ms_scaler);
     
//      Serial.print('D'); // mark this as debug data
      Serial.print(V);
      Serial.print(" ");
      Serial.print(v_shunt);
      Serial.print(" ");
      Serial.print(I);
      Serial.print(" ");
      Serial.println(load_v);
  }  
}

void do_iv_trace()
{
  int pwm_step, average_step;
  
  Serial.println("Starting I-V trace");
  // print column header
  Serial.print("PWM_Value");
  Serial.print(" ");
  Serial.print("Voltage");
  Serial.print(" ");
  Serial.println("Current");
      
  for (pwm_step = 0; pwm_step <= 255; pwm_step++)
  {
    //V = mySensor.getShuntVoltage_mV();
    set_load(pwm_step);
    delay(100 * ms_scaler);
    float i_avg = 0, v_avg = 0, v_shunt = 0;
    int load_v_avg = 0;
    
    for (average_step = 0; average_step < AVG_COUNT; average_step++)
    {
      V = mySensor.getBusVoltage_V(); //  Read Bus Voltage
      v_shunt = mySensor.getShuntVoltage_mV();
      V += v_shunt;
      //getShuntVoltage_mV()
      I = mySensor.getCurrent_mA(); //Read Current
      //P = mySensor.getPower_mW();
      i_avg += I;
      v_avg += V;
      load_v_avg += analogRead(LOAD_V_SENSE_PIN);
      
      delay(10 * ms_scaler);
//      Serial.println(v_shunt);
/*
      Serial.print('D'); // mark this as debug data
      Serial.print(pwm_step);
      Serial.print(" ");
      Serial.print(V);
      Serial.print(" ");
      Serial.println(I);
*/
    }

    i_avg /= float(AVG_COUNT);
    v_avg /= float(AVG_COUNT);
    load_v_avg = load_v_avg / AVG_COUNT;
    
    Serial.print(pwm_step);
    Serial.print(" ");
    Serial.print(v_avg);
    Serial.print(" ");
    Serial.print(i_avg);
    Serial.print(" ");
    Serial.println(load_v_avg);
  }
  //value = mySensor.getBusVoltage_raw_jf();
  //Serial.print(" ");
  //Serial.println(P);
  //delay(250*ms_scaler); //Pause between readings.
  set_load(0);
  Serial.println("Trace complete");
}



void loop() {
  
  /*
    shuntvoltage = ina219.getShuntVoltage_mV();
    busvoltage = ina219.getBusVoltage_V();
    current_mA = ina219.getCurrent_mA();
    power_mW = ina219.getPower_mW();
    loadvoltage = busvoltage + (shuntvoltage / 1000);
  */

  // wait for command from computer
  ch = Serial.read();
  if (ch == 'G')  // (G)O command
    do_iv_trace();
  else if (ch == 'R') // (R)ead power sensor
    read_sensor_loop();
}
  
  
//https://learn.adafruit.com/adafruit-ina219-current-sensor-breakout/arduino-code
