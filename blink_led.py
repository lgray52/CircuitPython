import board
import neopixel
import time

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.2

print("make it rainbow!")

while True:
    dot.fill((255, 0, 0))
    time.sleep(0.5)
    dot.fill((255, 128, 0))
    time.sleep(0.5)
    dot.fill((255, 255, 0))
    time.sleep(0.5)
    dot.fill((0, 255, 0))
    time.sleep(0.5)
    dot.fill((0, 0, 255))
    time.sleep(0.5)
    dot.fill((255, 0, 255))