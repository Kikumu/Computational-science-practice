/* 
  Speeds for Navigation.c
  
  Navigate by making your ActivityBot go certain speeds for certain amounts
  of time.

  http://learn.parallax.com/activitybot/set-certain-speeds
*/


#include "simpletools.h"                      // simpletools library
#include "abdrive.h"                          // abdrive library
#include "adcDCpropab.h" 

int main()                   
{
adc_init(21, 20, 19, 18); 
int var = 5;
float v1,v2,v3,v0;

//--------------------------------------loop-----------------------------------------------//
 while (var < 7){
v3 = adc_volts(3);  //left
v2 = adc_volts(2);  //right
v1 = adc_volts(1);  //turn around
v0 = adc_volts(0);  //forward

if(v0 > 2.5){
  //forward
  drive_speed(64, 64);                       // Forward 64 tps for 2 s
  pause(1000);
  }
else if(v1 > 2.5){
  //turns 360
  drive_speed(0, 0);
  drive_speed(45, 0);                        // Turn 26 tps for 1 s
  pause(1000);
  drive_speed(0, 0);
  drive_speed(0, -45); 
  }
 else if(v2 > 2.5){
   //turns right
  drive_speed(0, 0);
  drive_speed(45, 0);                        // Turn 26 tps for 1 s
  pause(1000);
 } 
else if(v3 > 2.5){
  //turns left
  drive_speed(0, 0);
  drive_speed(0, 45);                        // Turn 26 tps for 1 s
  pause(1000);
}    

 }    
}