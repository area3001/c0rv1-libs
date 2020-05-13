from machine import Pin, I2C
import time

AHT10_ADDRESS = 0x38
AHT10_INIT_CMD = 0b11100001
AHT10_TRIGGER_CMD = 0b10101100
AHT10_RESET_CMD = 0b10111010

AHT10_STATUS_BUSY_MASK = 1<<7
AHT10_STATUS_MODE_MASK = 0b11<<5
AHT10_STATUS_CALIBRATED_MASK = 1<<3

class AHT10:
    def __init__(self, i2c, address=0x38):
        self.i2c = i2c
        self.address = address
    
    def status(self):
        status = self.i2c.readfrom(self.address, 1)[0]
        return {
            "status": "{:#010b}".format(status),
            "busy": "{}".format((s & AHT10_STATUS_BUSY_MASK) >> 7),
            "mode": "{}".format((s & AHT10_STATUS_MODE_MASK) >> 5),
            "calibrated": "{}".format((s & AHT10_STATUS_CALIBRATED_MASK) >> 3)
        }

    def read(self):
        data = self.i2c.readfrom(self.address, 6)
        rh_data = data[1]<<12 | data[2]<<4 | data[3]>>4
        rh = rh_data * 100/2**20
        t_data = (data[3] & 0x0F)<<16 | data[4]<<8 | data[5]
        t = ((t_data*200)/2**20)-50
        return t, rh

    def busy(self):
        status = self.i2c.readfrom(self.address, 1)[0]
        return bool(status & AHT10_STATUS_BUSY_MASK)
