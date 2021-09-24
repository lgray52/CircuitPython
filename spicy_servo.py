import board
import time
import pwmio
import servo
import touchio
# https://learn.adafruit.com/circuitpython-essentials/circuitpython-cap-touch

pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

touch_clcw = touchio.TouchIn(board.D9)
touch_anti = touchio.TouchIn(board.D8)

myServo = servo.ContinuousServo(pwm)


while True:
    if touch_clcw.value:
        print("clockwise")
        myServo.throttle = 1
        time.sleep(0.05)
    if touch_anti.value:
        print("anticlockwise")
        myServo.throttle = -1
        time.sleep(0.05)
    else:
        print("NO")
        myServo.throttle = 0
        time.sleep(0.05)