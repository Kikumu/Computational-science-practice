/* 
  Speeds for Navigation.c
  
  Navigate by making your ActivityBot go certain speeds for certain amounts
  of time.

  http://learn.parallax.com/activitybot/set-certain-speeds
*/


#include "simpletools.h"                      // simpletools library
#include "abdrive.h"                          // abdrive library
#include "adcDCpropab.h" 

int distLeft[4], distRight[4];
int main()                   
{
adc_init(21, 20, 19, 18); 
int var = 5;
float v1,v2,v3,v0,turn_around;
drive_getTicks(&distLeft[0], &distRight[0]);
print("distLeft[0] = %d, distRight[0] = %d\n", distLeft[0], distRight[0]);
int count = 0;
//--------------------------------------loop-----------------------------------------------//
 while (var < 7){
v3 = adc_volts(3);  //left 26
v2 = adc_volts(2);  //right 20
v1 = adc_volts(1);  //forward 16
v0 = adc_volts(0);  //turn around
turn_around = input(10);
//if (count > 100)
//{
  if(v1 > 2.0){ //16
  //forward
  //drive_speed(0, 0); 
  drive_speed(25, 25);  
 // drive_speed(0, 0);                     
 // pause(1000);
}
else if(turn_around > 0){ //21
 //turns 360
 //drive_speed(0, 0);
 drive_speed(45, 0);                       
// drive_speed(0, 0);
 drive_speed(0, -45); 
//  drive_speed(0, 0);
}
else if(v2 > 2.0){ //20                   
   drive_speed(25, 0);
   drive_speed(25, 25);
 } 
else if(v3 > 2.0){ //26
   drive_speed(0, 25);
   drive_speed(25, 25);
  //---------------remaining code is to turn 90 so that it can keep 'one hand on wall'
} 
//  }
count++;   
//print("A/D3 = %f V%c\n", v1, CLREOL);     // Display volts
//pause(1000);
 }    
}
