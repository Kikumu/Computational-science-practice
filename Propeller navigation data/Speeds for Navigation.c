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
//adc_init(21, 20, 19, 18); 
int var = 5;
//float v1,v2,v3,v0,turn_around
int v1,v2,v3,v0,turn_around,status;
drive_getTicks(&distLeft[0], &distRight[0]);
print("distLeft[0] = %d, distRight[0] = %d\n", distLeft[0], distRight[0]);
int count = 0;
//--------------------------------------loop-----------------------------------------------//
 while (var < 7){
//v3 = adc_volts(3);  //left 26
//v2 = adc_volts(2);  //right 20
//v1 = adc_volts(1);  //forward 16
//v0 = adc_volts(0);  //turn around 21
turn_around = input(10);
v1 = input(1);
v2 = input(0);
v3 = input(2);

//forward(16)
if(v1 ==0){
  status = 0;
  drive_speed(0, 0);
  }
else if(v1 == 1){
  status = 1;
  drive_speed(25, 25);
 }
//turn_around = 21
else if(turn_around==1){
    drive_speed(45, 0);                       
    drive_speed(0, -45);
}
//left(20)
else if(v2==1){drive_speed(25, 0);}  
 //right(26)
else if(v1==1){drive_speed(0, 25);}  
//---------------remaining code is to turn 90 so that it can keep 'one hand on wall'
//print("A/D3 = %f V%c\n", turn_around, CLREOL);     // Display volts
 }    
}
