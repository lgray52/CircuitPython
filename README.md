# CircuitPython

CircuitPython course module work

## Table of Contents
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)

## Hello_CircuitPython

### Description & Code
The purpose of this assignment is to make an led built into a MetroExpress change colours using CircuitPython.

```python
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
```


### Evidence
![rainbow light blinking](https://github.com/lgray52/CircuitPython/blob/main/evidence/hello_circuitpython.gif)

### Wiring
Only the board required!

### Reflection
This was a fairly basic assignment. I changed the assignment a little bit,to make the light shift between rainbow shades, using different colour codes for different colours.


## CircuitPython_Servo

### Description & Code

Make a servo turn

```python
import board
import time
import pwmio
from adafruit_motor import servo

pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

myServo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 5):
        myServo.angle = angle
        time.sleep(0.025)
    for angle in range(180, 0, 5):
        myServo.angle = angle
        time.sleep(0.025)
```

### Evidence
![servo spinning](https://github.com/lgray52/CircuitPython/blob/main/evidence/servo.gif)

### Wiring
<img src="evidence/servo_wiring.PNG" alt="servo wiring diagram" height="300">

### Reflection
This assignment introduced ranges, which essentially circle a value in a specific range by a certain number, and expanded on CircuitPython syntax by introducing the key usage of servos.
