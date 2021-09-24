# Lucy Gray, 17.09.21, Distance Sensor

import board
import time
import neopixel
import adafruit_hcsr04

led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 0.2

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)

while True:
    try:
        dist = sonar.distance
        print((dist))
        if dist < 5:
            led.fill((255, 0, 0))
        if dist > 35:
            led.fill((0, 255, 0))
        if dist > 5 and dist < 20:
            r = (255 - ((dist-5)*(255/15)))
            b = 0
            g = (0 + ((dist-5)*(255/15)))
            led.fill((int(r), int(b), int(g)))
        if dist > 20 and dist < 35:
            r = 0
            b = (0 + ((dist-20)*(255/15)))
            g = (255 - ((dist-20)*(255/15)))
            led.fill((int(r), int(b), int(g)))
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)