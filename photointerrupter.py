# photointerrupter, L.G. 24.09.21

import time
import digitalio
import board

initial = time.monotonic()

resistorPin = digitalio.DigitalInOut(board.D7)
resistorPin.direction = digitalio.Direction.INPUT
resistorPin.pull = digitalio.Pull.UP
# define resistor pin for photointerruptor - uses board as resistor

counter = 0  # counts # of times photointerruptor interrupted

val = False  # store value of resistorPin
state = False  # store state (LOW/HIGH) of resistorPin

while True:
    val = resistorPin.value
    if val and not state:
        counter += 1  # add one to counter when state change detected
    state = val

    now = time.monotonic()
    if now - initial >= 4:
        print("I have been interrupted", str(counter), "times")
        initial = now
    time.sleep(0.1)