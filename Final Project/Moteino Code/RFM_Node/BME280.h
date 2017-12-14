#ifndef BME280_H
#define BME280_H

#include <SparkFunBME280.h> //get it here: https://github.com/sparkfun/SparkFun_BME280_Breakout_Board/tree/master/Libraries/Arduino/src


 class BME : public BME280 
{
public:
    void reset_run_mode(void)
    {
        uint8_t dataToWrite = 0;
        // set ctrl_meas
        // set temp oversampling
        dataToWrite = (settings.tempOverSample << 0x05) & 0xE0;
        // set pressure oversampling
        dataToWrite |= (settings.pressOverSample << 0x02) & 0x1C;
        // set run mode
        dataToWrite |= (settings.runMode) & 0x03;
        // Load the byte
        writeRegister(BME280_CTRL_MEAS_REG, dataToWrite);
    }
};
#endif
