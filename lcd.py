# LCD, Lucy G 01.10.21

import board
from lcd.lcd import LCD  # weird lcd library thing
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import time
import touchio

i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x3f), num_rows=2, num_cols=16)

touch_A5 = touchio.TouchIn(board.A5)
touch_A0 = touchio.TouchIn(board.A0)

counter = 0  # set counter value to zero
reverse=1 # reverse value

lcd.print("on")
while True:
    if touch_A5.value:
        counter+=reverse
        lcd.set_cursor_pos(0,0)  # set the cursor to the first row, first column
        if reverse==1:  # when reverse is pos (going up)
            lcd.print("Up: ")
        else:
            lcd.print("Down: ")
        lcd.print(str(counter))  # print the counter
        lcd.print("   ")  # give it some space
        while touch_A5.value:
            time.sleep(.01)  # idk this is j's thing

    if touch_A0.value:
        reverse=-reverse  # negative (down)
        while touch_A0.value:
            time.sleep(.1)
        lcd.clear()
        if reverse==1:
            lcd.print("Up: ")
        else:
            lcd.print("Down: ")
        lcd.print(str(counter))