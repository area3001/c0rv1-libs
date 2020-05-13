from .buzzer import BuzzerPlayer
import machine, neopixel
from .lis2hh12 import LIS2HH12
from .aht10 import AHT10

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
        self.acc = LIS2HH12(self.i2c, address=I2C_ADDR_LIS2D)
        self.aht10 = AHT10(self.i2c, address=I2C_ADDR_AHT10)
