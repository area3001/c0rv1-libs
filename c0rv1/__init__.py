from buzzer import BuzzerPlayer
import machine, neopixel
from lis2dh12 import LIS2DH12_I2C
from aht10 import AHT10

PIN_BUZZER = 32
PIN_NEOPIXEL = 2
PIN_I2C_SCL = 22
PIN_I2C_SDA = 21


I2C_ADDR_LIS2D = 0x18
I2C_ADDR_AHT10 = 0x38

class C0rv1:
    def __init__(self):
        self.buzz = BuzzerPlayer(pin=PIN_BUZZER)
        self.pixels = neopixel.NeoPixel(machine.Pin(PIN_NEOPIXEL), 5)

        self.i2c = machine.I2C(scl=machine.Pin(PIN_I2C_SCL), sda=machine.Pin(PIN_I2C_SDA), freq=100000)
        self.acc = LIS2DH12_I2C(i2c, address=I2C_ADDR_LIS2D)
        self.aht10 = AHT10(i2c, address=I2C_ADDR_AHT10)
