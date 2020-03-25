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
float v1,v2,v3,v0;
drive_getTicks(&distLeft[0], &distRight[0]);
print("distLeft[0] = %d, distRight[0] = %d\n", distLeft[0], distRight[0]);
//--------------------------------------loop-----------------------------------------------//
 while (var < 7){
v3 = adc_volts(3);  //left 26
v2 = adc_volts(2);  //right 20
v1 = adc_volts(1);  //turn around 16
v0 = adc_volts(0);  //forward

if(v1 > 3.0){ //16
  //forward
  //drive_speed(0, 0); 
  drive_speed(25, 25);  
 // drive_speed(0, 0);                     // Forward 64 tps for 2 s
 // pause(1000);
}
//if(v0 > 3.8){
  //turns 360
 // drive_speed(0, 0);
 // drive_speed(45, 0);                        // Turn 26 tps for 1 s
 // pause(1000);
//  drive_speed(0, 0);
//  drive_speed(0, -45); 
//  drive_speed(0, 0);
//}
else if(v2 > 3.0){ //20
   //turns right at 90
   drive_speed(0, 0);                       // Turn 26 tps for 1 s
   drive_speed(25, 0);
   drive_speed(0, 0);
 } 
else if(v3 > 3.0){ //26
   //turns left at 90
   drive_speed(0, 0);
   drive_speed(0, 25);
   drive_speed(0, 0);
  //---------------remaining code is to turn 90 so that it can keep 'one hand on wall'
}    
//drive_getTicks(&distLeft[1], &distRight[1]);
//print("distLeft[1] = %d, distRight[1] = %d\n", distLeft[1], distRight[1]);
//print("A/D3 = %f V%c\n", v3, CLREOL);     // Display volts
//pause(1000);
 }    
}
