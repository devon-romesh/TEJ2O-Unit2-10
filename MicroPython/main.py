"""
Created by: Devon
Created on: Mar 2026
This module is a Micro:bit MicroPython program
"""

from microbit import *
import neopixel 

# the variables needed
lightLevel = 0
myNeopixelStrip = neopixel.NeoPixel(pin16, 4)

# setup
display.show(Image.HAPPY)
myNeopixelStrip.clear()
myNeopixelStrip.show()

# running Button A
while True:
    if button_a.is_pressed():
        lightLevel = display.read_light_level()
        myNeopixelStrip.clear()

        # if light level is less than 52
        if lightLevel > 52:
            myNeopixelStrip[0] = (255, 0, 0) 

        # if light level is less than 104
        if lightLevel > 104:
            myNeopixelStrip[1] = (255, 255, 255)

        # if light level is less than 156
        if lightLevel > 156:
            myNeopixelStrip[2] = (255, 255, 255)

        # if light level is less than 208
        if lightLevel > 208:
            myNeopixelStrip[3] = (255, 255, 255)
        myNeopixelStrip.show()
        display.scroll("Light level is " + (lightLevel))
