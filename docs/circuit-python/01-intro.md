# Introduction to CircuitPython

1. CircuitPython is a fork of MicroPython done by Adafruit
2. According to [Google Trends](https://trends.google.com/trends/explore?date=today%205-y&q=micropython,circuitpython), MicroPython is more popular than CircuitPython when we look at worldwide web search comparison
3. Done for "simplicity" but does not support multiple cores
4. CircuitPython has lots of drivers
5. The code is generally incompatible with MicroPython although you can often manually convert one program into another
6. It might be useful for testing devices where the MicroPython drivers do not work

## Setting up a CircuitPython Virtual Environment
Because MicroPython and CircuitPython are incompatible, it is important that you don't intermix your python libraries.

Here is how we setup a virtual environment for CircuitPython using [Conda](https://docs.conda.io/en/latest/).

```sh
conda create -n circuitpython python=3
conda activate circuitpython
```

### Installing the SSD1306 CircuitPython Library

[Per Directions Here](https://github.com/adafruit/Adafruit_CircuitPython_SSD1306)

```sh
pip3 install adafruit-circuitpython-ssd1306
```

```sh
pip3 install adafruit-circuitpython-displayio-ssd1306
```

!!! Note
    ERROR: Could not find a version that satisfies the requirement adafruit-circuitpython-displayio-ssd1306
    ERROR: No matching distribution found for adafruit-circuitpython-displayio-ssd1306


```
Successfully installed Adafruit-Blinka-6.3.2 Adafruit-PlatformDetect-3.2.0 Adafruit-PureIO-1.1.8 adafruit-circuitpython-busdevice-5.0.6 adafruit-circuitpython-framebuf-1.4.6 adafruit-circuitpython-ssd1306-2.11.1 pyftdi-0.52.9 pyserial-3.5 pyusb-1.1.1
```

```py
# Basic example of clearing and drawing pixels on a SSD1306 OLED display.
# This example and library is meant to work with Adafruit CircuitPython API.
# Author: Tony DiCola
# License: Public Domain

# Import all board pins.
from board import SCL, SDA
import busio

# Import the SSD1306 module.
import adafruit_ssd1306


# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
# Alternatively you can change the I2C address of the device with an addr parameter:
#display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x31)

# Clear the display.  Always call show after changing pixels to make the display
# update visible!
display.fill(0)

display.show()

# Set a pixel in the origin 0,0 position.
display.pixel(0, 0, 1)
# Set a pixel in the middle 64, 16 position.
display.pixel(64, 16, 1)
# Set a pixel in the opposite 127, 31 position.
display.pixel(127, 31, 1)
display.show()
```

## Trend analysis

As of March 2021, MicroPython is about two to four times more popular than CircuitPython.

[Google Worldwide Search Trends](https://trends.google.com/trends/explore?date=today%205-y&q=micropython,circuitpython)

