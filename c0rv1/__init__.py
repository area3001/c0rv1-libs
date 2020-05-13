from buzzer import BuzzerPlayer
import machine, neopixel

PIN_BUZZER = 32
PIN_NEOPIXEL = 2

class C0rv1:
    def __init__(self):
        self.buzz = BuzzerPlayer(pin=PIN_BUZZER)
        self.pixels = neopixel.NeoPixel(machine.Pin(PIN_NEOPIXEL), 5)
        pass
