#ifndef CONFIG_H
#define CONFIG_H

#include <EEPROM.h>


struct NODE{
    uint8_t NODEID;
    uint8_t NETWORKID;
    uint8_t GATEWAYID;
    uint16_t UPDATE_INTERVAL;
    uint16_t MOTION_DUPLICATE_INTERVAL;
    char ENCRYPTKEY[17];
};

NODE node;

void Get_Node_Config(void)
{
    EEPROM.get(0, node);
}

#endif

