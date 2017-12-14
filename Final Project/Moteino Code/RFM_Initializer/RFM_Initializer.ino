/** Code to initialize moteino  nodefor RFM weather monitoring with BME280 **/

#include <EEPROM.h>

struct NODE{
    uint8_t NODEID;
    uint8_t NETWORKID;
    uint8_t GATEWAYID;
    uint16_t UPDATE_INTERVAL;
    uint16_t MOTION_DUPLICATE_INTERVAL;
    char ENCRYPTKEY[17];
};

NODE node = {
    12,             //unique for each node on same network
    100,            //the same on all nodes that talk to each other
    1,
    60000,
    60000,
    "01234567890abcdef" //exactly the same 16 characters/bytes on all nodes!

};

void saveConfig() {
  for (unsigned int t=0; t<sizeof(node); t++)
    EEPROM.write(t, *((char*)&node + t));
}

void setup() 
{

    NODE node;
    saveConfig();
    
    float f = 0.00f;   //Variable to store data read from EEPROM.
    int eeAddress = 0; //EEPROM address to start reading from
    unsigned char c;
    
    Serial.begin(56700);
    while (!Serial) {
        ; // wait for serial port to connect. Needed for native USB port only
    }
    Serial.println("Read float from EEPROM: ");
    
    EEPROM.get(eeAddress, node);
    Serial.print("NODEID:\t\t"); Serial.println(node.NODEID);
    Serial.print("NETWORKID:\t"); Serial.println(node.NETWORKID);
    Serial.print("GATEWAYID:\t"); Serial.println(node.GATEWAYID);
    Serial.print("UPDATE_INTERVAL:\t"); Serial.println(node.UPDATE_INTERVAL);
    Serial.print("MOITION_DUPLICATE_INTERVAL:\t"); Serial.println(node.MOTION_DUPLICATE_INTERVAL);
    Serial.print("ENCRYPTKEY:\t"); Serial.println(node.ENCRYPTKEY);

}

void loop() {
  /* Empty loop */
}
