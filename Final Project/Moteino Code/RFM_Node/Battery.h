#ifndef BATTERY_H
#define BATTERY_H

const int BATT_MONITOR = A7;  // Sense VBAT_COND signal (when powered externally should read ~3.25v/3.3v (1000-1023), when external power is cutoff it should start reading around 2.85v/3.3v * 1023 ~= 883 (ratio given by 10k+4.7K divider from VBAT_COND = 1.47 multiplier)
const int BATT_MONITOR_EN = A3;

#define BATT_FORMULA(reading) reading * 0.00322 * 1.49 // >>> fine tune this parameter to match your voltage when fully charged
                                                       // details on how this works: https://lowpowerlab.com/forum/index.php/topic,1206.0.html
float readBattery()
{
    unsigned int readings=0;
    
    //enable battery monitor on WeatherShield (via mosfet controlled by A3)
    pinMode(BATT_MONITOR_EN, OUTPUT);
    digitalWrite(BATT_MONITOR_EN, LOW);
    
    for (byte i=0; i<5; i++) //take several samples, and average
        readings+=analogRead(BATT_MONITOR);
    
    //disable battery monitor
    pinMode(BATT_MONITOR_EN, INPUT); //highZ mode will allow p-mosfet to be pulled high and disconnect the voltage divider on the weather shield
    
    return BATT_FORMULA(readings / 5.0);
}




#endif

