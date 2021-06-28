import time
import busio
import digitalio
from board import SCK, MOSI, D25, D8, D24 # MISO, D2, D3 # fixed, the three items not used

"""
Reference from st7735 Layout

GND Ground (pins 6, 9, 14, 20, 25, 30, 34 or 39)

VCC 5v Power (pins 2 or 4)

SCL GPIO 11 (pin 23) SPIO SCLK

SDA GPIO 10 (pin 19) SPIO MOSI

RES GPIO 25 (pin 22)

DC GPIO 24 (pin 18)

CS GPIO 8 (pin 24) SPIO CS0

BL Not connected
"""
from adafruit_rgb_display import color565
import adafruit_rgb_display.ili9341 as ili9341
# Configuration for CS and DC pins:
CS_PIN = D8
DC_PIN = D24
RS_PIN = D25

# Setup SPI bus using hardware SPI:
#spi = busio.SPI(clock=SCK, MOSI=MOSI, MISO=MISO) # Don't use that
spi = busio.SPI(clock=SCK, MOSI=MOSI)

# Create the ILI9341 display:
"""
    def __init__(
        self,
        spi,
        dc,
        cs,
        rst=None,
        width=240,
        height=320,
        baudrate=16000000,
        polarity=0,
        phase=0,
        rotation=0,
    )
"""
display = ili9341.ILI9341(spi, cs=digitalio.DigitalInOut(CS_PIN), dc=digitalio.DigitalInOut(DC_PIN), rst = digitalio.DigitalInOut(RS_PIN))

# Main loop:
while True:
    # Clear the display
    display.fill(0)
    # Draw a red pixel in the center.
    display.pixel(240, 240, color565(255, 0, 0))
    # Pause 2 seconds.
    time.sleep(2)
    # Clear the screen blue.
    display.fill(color565(0, 0, 255))
    # Pause 2 seconds.
    time.sleep(2)
