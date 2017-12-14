#ifndef DEBUG_H
#define DEBUG_H


#define SERIAL_BAUD    115200
#ifdef SERIAL_EN
    #define DEBUGInit(input) {Serial.begin(input); delay(1);}
    #define DEBUG(input)   {Serial.print(input); delay(1);}
    #define DEBUGln(input) {Serial.println(input); delay(1);}
    #define DEBUGFlush() { Serial.flush(); }
#else
    #define DEBUGInit(input);
    #define DEBUG(input);
    #define DEBUGln(input);
    #define DEBUGFlush();
#endif


#endif
