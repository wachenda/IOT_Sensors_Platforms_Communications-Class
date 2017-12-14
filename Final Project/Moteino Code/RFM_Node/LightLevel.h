#ifndef LIGHTLEVEL_H
#define LIGHTLEVEL_H

const int LIGHT_MONITOR_EN=8;
const int LIGHT_MONITOR=A0;

unsigned int readLightLevel()
{
    unsigned int readings=0;
    
    //enable battery monitor on WeatherShield (via mosfet controlled by A3)
    pinMode(LIGHT_MONITOR_EN, OUTPUT);
    digitalWrite(LIGHT_MONITOR_EN, HIGH);
    
    for (byte i=0; i<5; i++) //take several samples, and average
        readings+=analogRead(LIGHT_MONITOR);
    
    //disable battery monitor
    pinMode(LIGHT_MONITOR_EN, INPUT); //highZ mode will allow p-mosfet to be pulled high and disconnect the voltage divider on the weather shield
    
    return readings / 5;
}



#endif

