# Lucy Gray 17.09.21, Servo turn

import board
import time
import pwmio
import servo

pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

myServo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 5):
        myServo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5):
        myServo.angle = angle
        time.sleep(0.05)