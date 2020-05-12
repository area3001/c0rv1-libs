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
