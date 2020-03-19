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

int var = 5;
 
 while (var < 7){

drive_speed(64, 64);                       // Forward 64 tps for 2 s
pause(1000);

//turns 360
drive_speed(0, 0);
drive_speed(45, 0);                        // Turn 26 tps for 1 s
pause(1000);
drive_speed(0, 0);
drive_speed(0, -45); 

//turns right
drive_speed(0, 0);
drive_speed(45, 0);                        // Turn 26 tps for 1 s
pause(1000);

//turns left
drive_speed(0, 0);
drive_speed(0, 45);                        // Turn 26 tps for 1 s
pause(1000);

//forward
drive_speed(64, 64);                     // Forward 128 tps for 1 s
pause(1000);
 }    
}