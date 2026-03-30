"""
Created by: Devon
Created on: Mar 2026
This module is a Micro:bit MicroPython program
"""

from microbit import *
import neopixel 

# the variables needed
lightLevels = 0
myNeopixelStrip = neopixel.NeoPixel(pin16, 4)

# setup
display.show(Image.HAPPY)
myNeopixelStrip.clear()
myNeopixelStrip.show()

# running Button A
while True:
    if button_a.is_pressed():
        lightLevels = display.read_light_level()
        myNeopixelStrip.clear()

        # if light level is less than 52
        if lightLevels > 52:
            myNeopixelStrip[0] = (255, 255, 255) 

        # if light level is less than 104
        if lightLevels > 104:
            myNeopixelStrip[1] = (255, 255, 255)

        # if light level is less than 156
        if lightLevels > 156:
            myNeopixelStrip[2] = (255, 255, 255)

        # if light level is less than 208
        if lightLevels > 208:
            myNeopixelStrip[3] = (255, 255, 255)
        myNeopixelStrip.show()
        display.scroll("Light level is " + (lightLevels))
