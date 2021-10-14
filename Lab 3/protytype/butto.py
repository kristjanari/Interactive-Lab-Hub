import time
from random import randint
import board
import busio
from i2c_button import I2C_Button
import os

# initialize I2C
i2c = busio.I2C(board.SCL, board.SDA)


# scan the I2C bus for devices
while not i2c.try_lock():
	pass
devices = i2c.scan()
i2c.unlock()
print('I2C devices found:', [hex(n) for n in devices])
default_addr = 0x6f
if default_addr not in devices:
	print('warning: no device at the default button address', default_addr)

# initialize the button
button = I2C_Button(i2c)

def button_action():
    button.clear() # status must be cleared manually

    if button.last_click_ms < 1000:
        print(button.last_click_ms)
        return True
    return False

while True:
    getMessage = button_action()
    if getMessage:
        print("butto pressed")
        break

os.system("./speech.sh")
