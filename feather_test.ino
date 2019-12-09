
#include <Wire.h>
#include <SPI.h>
#include <SD.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>

#define cardSelect 4
#define BUFFER_SIZE 150
#define LED_PIN 13

//Can remove whenever not needed
#define Serprint(x) //Serial.print(x)
#define Serprintln(x) //Serial.println(x)

File logfile;
/*int16_t accelx[BUFFER_SIZE];
int16_t accely[BUFFER_SIZE];
int16_t accelz[BUFFER_SIZE];
int16_t gyrox[BUFFER_SIZE];
int16_t gyroy[BUFFER_SIZE];
int16_t gyroz[BUFFER_SIZE];
*/

int16_t accelx;
int16_t accely;
int16_t accelz;
int16_t gyrox;
int16_t gyroy;
int16_t gyroz;
int16_t tmp;

const int MPU_addr=0x68;
Adafruit_MPU6050 mpu;
 
void setup(void) {
  
  /*
  Serial.begin(115200);
  while (!Serial)
    delay(10); // will pause Zero, Leonardo, etc until serial console opens
  */
  
  // Try to initialize!
  if (!mpu.begin()) {
    Serprintln("Failed to find MPU6050 chip");
    while (1) {
      delay(10);
    }
  }
  Serprintln("MPU6050 Found!");

  mpu.setAccelerometerRange(MPU6050_RANGE_2_G);
  mpu.setGyroRange(MPU6050_RANGE_500_DEG);
  mpu.setFilterBandwidth(MPU6050_BAND_94_HZ);
  
  delay(100);

  pinMode(LED_PIN, OUTPUT);
  
  //Make sure LED is initially off
  digitalWrite(LED_PIN, LOW);
  if (!SD.begin(cardSelect)) {
    Serprintln("Card init. failed!");
    while(1){ delay(10); }
  }
}


void loop() {

  
  sensors_event_t a, g, temp;
  int counter = 0;
  char data[100];
  char filename[16];

  //Define file to write to, make sure it does not exist
  strcpy(filename, "OUTPUT00.csv");
  for (uint8_t i = 0; i < 100; i++) {
    filename[6] = '0' + i/10;
    filename[7] = '0' + i%10;
    // create if does not exist, do not open existing, write, sync after write
    if (! SD.exists(filename)) {
      break;
    }
  }

  logfile = SD.open(filename, FILE_WRITE);
  logfile.println("accel_x,accel_y,accel_z,gyro_x,gyro_y,gyro_z"); 

  
  //Blink three times to signal data acquisition. Then hold on fourth blink
  digitalWrite(LED_PIN, HIGH);
  delay(750);
  digitalWrite(LED_PIN, LOW);
  delay(750);
  digitalWrite(LED_PIN, HIGH);
  delay(750);
  digitalWrite(LED_PIN, LOW);
  delay(750);
  digitalWrite(LED_PIN, HIGH);
  delay(750);
  digitalWrite(LED_PIN, LOW);
  delay(750);
  digitalWrite(LED_PIN, HIGH);  

  unsigned long start_time;
  start_time = millis();
  
  while(counter < BUFFER_SIZE) {



    //Data acquisition code credit:
    //https://playground.arduino.cc/Main/MPU-6050/

    Wire.beginTransmission(MPU_addr);
    Wire.write(0x3B);  // starting with register 0x3B (ACCEL_XOUT_H)
    Wire.endTransmission(false);
    Wire.requestFrom(MPU_addr,14,true);  // request a total of 14 registers
    accelx=Wire.read()<<8|Wire.read();  // 0x3B (ACCEL_XOUT_H) & 0x3C (ACCEL_XOUT_L)    
    accely=Wire.read()<<8|Wire.read();  // 0x3D (ACCEL_YOUT_H) & 0x3E (ACCEL_YOUT_L)
    accelz=Wire.read()<<8|Wire.read();  // 0x3F (ACCEL_ZOUT_H) & 0x40 (ACCEL_ZOUT_L)
    tmp=Wire.read()<<8|Wire.read();  // 0x41 (TEMP_OUT_H) & 0x42 (TEMP_OUT_L)
    gyrox=Wire.read()<<8|Wire.read();  // 0x43 (GYRO_XOUT_H) & 0x44 (GYRO_XOUT_L)
    gyroy=Wire.read()<<8|Wire.read();  // 0x45 (GYRO_YOUT_H) & 0x46 (GYRO_YOUT_L)
    gyroz=Wire.read()<<8|Wire.read();  // 0x47 (GYRO_ZOUT_H) & 0x48 (GYRO_ZOUT_L)
    //End of credited code
    
    //Print to SD card
    sprintf(data,"%d,%d,%d,%d,%d,%d",accelx,accely,accelz,gyrox,gyroy,gyroz);
    logfile.println(data);
    Serial.println(data);
    
    counter++;
    //Delay to create timing for DAQ
    delay(20);
  }

  Serprint(millis() - start_time);
  
  //Signal climber that DAQ is complete by turning off LED
  digitalWrite(LED_PIN, LOW);
  logfile.close();
  
  //Only execute once. Reset for next data aquisition instance
  while(1) {
    delay(10);
  }
}
