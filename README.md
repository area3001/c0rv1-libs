# c0rv1-libs - Micropython

## English
This branch contains the micropython library for the C0rv1 badge.

### Getting Micropython on your C0rv1
- Download the [Micropython Firmware](https://micropython.org/resources/firmware/esp32spiram-idf4-20191220-v1.12.bin)
- Install esptool using ```pip install esptool```
- ``` esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash ```
- ``` esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 esp32spiram-idf4-20191220-v1.12.bin ```

### Connecting to your C0rv1
``` screen /dev/ttyUSB0 115200 ```

### Uploading the libraries
TBD

### Developing
Once connected to your C0rv1, you may use the C0rv1 micropython library to get access to the sensors, display and buttons:

```
from c0rv1 import C0rv1
badge = C0rv1()
```

#### Neopixels
The badge contains 5 neopixels, each of which can display colors within the RGB color space. Each pixel has a tuple of 3 values; the first for Red, 
the second for Green and the last for Blue. Each of these hold a value between 0 and 255.

For example, ```(255, 0, 0)``` would show the pixel as Red, while ```(0, 0, 255)``` would show the pixel as Blue.

```
# -- set the first pixel to become red
badge.pixels[0] = (255, 0, 0)

# -- set the second pixel to become green
badge.pixels[1] = (0, 255, 0)

# -- set the third pixel to become blue
badge.pixels[2] = (0, 0, 255)

# -- write the changes to the pixels
badge.pixels.write()
```

#### Button
There are two buttons on the badge. The one on the left (Under the FRI3DCAMP text and logo) is meant for rebooting the badge, while the other one is exposed through the C0rv1 library.

```
# -- read the value of the button
badge.button.value()
```

The call above will return 0 if the button is pressed, and 1 otherwise.

