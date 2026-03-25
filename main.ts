/* Copyright (c) 2020 MTHS All rights reserved
*
* Created by: Devon
* Created on: Mar 2026
* This program lights up neopixels determind by light.
*/


//variables
let lightLevels: number = 0
const myNeopixelStrip = neopixel.create(DigitalPin.P16, 4, NeoPixelMode.RGB)


//setup
basic.showIcon(IconNames.Happy)
myNeopixelStrip.clear()
myNeopixelStrip.show()


// code for lighting up neopixels
input.onButtonPressed(Button.A, function () {
    lightLevels = input.lightLevel()


    // shows the current light level
    basic.showNumber(lightLevels)
    myNeopixelStrip.clear()


    if (lightLevels > 52) {
        myNeopixelStrip.setPixelColor(0, neopixel.colors(NeoPixelColors.Red))
    }


    if (lightLevels > 104) {
        myNeopixelStrip.setPixelColor(1, neopixel.colors(NeoPixelColors.Red))
    }


    if (lightLevels > 156) {
        myNeopixelStrip.setPixelColor(2, neopixel.colors(NeoPixelColors.Red))
    }


    if (lightLevels > 208) {
        myNeopixelStrip.setPixelColor(3, neopixel.colors(NeoPixelColors.Red))
    }


    myNeopixelStrip.show()
})
