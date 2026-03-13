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
myNeopixelStrip.setPixelColor(0, neopixel.colors(NeoPixelColors.Black))
myNeopixelStrip.setPixelColor(1, neopixel.colors(NeoPixelColors.Black))
myNeopixelStrip.setPixelColor(2, neopixel.colors(NeoPixelColors.Black))
myNeopixelStrip.setPixelColor(3, neopixel.colors(NeoPixelColors.Black))

// code for lighting up neopixels
input.onButtonPressed(Button.A, function() {
   if (lightLevels > 52){
   myNeopixelStrip.setPixelColor(0, neopixel.colors(NeoPixelColors.Red))
    }
    if (lightLevels > 104) {
        myNeopixelStrip.setPixelColor(1, neopixel.colors(NeoPixelColors.Red))
    }
    if (lightLevels > 156) {
        myNeopixelStrip.setPixelColor(3, neopixel.colors(NeoPixelColors.Red))
    } 
    if (lightLevels > 208) {
        myNeopixelStrip.setPixelColor(0, neopixel.colors(NeoPixelColors.Red))
    }
})
