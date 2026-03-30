"""
Created by: Devon
Created on: Mar 2026
This module is a that displays light determined on neopixels.
"""

from microbit import *
import neopixel


# variables needed
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

        if lightLevel > 52:
            myNeopixelStrip[0] = (255, 255, 255)

        if lightLevel > 104:
            myNeopixelStrip[1] = (255, 255, 255)

        if lightLevel > 156:
            myNeopixelStrip[2] = (255, 255, 255)

        if lightLevel > 208:
            myNeopixelStrip[3] = (255, 255, 255)

        myNeopixelStrip.show()

        display.scroll("Light level is " + str(lightLevel))

    # Resets it
    if button_b.is_pressed():
        display.clear()
        myNeopixelStrip.clear()
        myNeopixelStrip.show()
        display.show(Image.HAPPY)
