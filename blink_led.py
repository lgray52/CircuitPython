import board
import neopixel
import time

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.2

print("make it blue and green!")

while True:
    dot.fill((0, 0, 255))
    time.sleep(1)
    dot.fill((0, 255, 0))
    time.sleep(1)