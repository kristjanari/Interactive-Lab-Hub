# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
import random
import busio
import time
import adafruit_ssd1306
import adafruit_mpr121



# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

#Create capatitive sensor
mpr121 = adafruit_mpr121.MPR121(i2c)

center_x = 63
center_y = 15
# how fast does it move in each direction
x_inc = 1
y_inc = 1
# what is the starting radius of the circle
radius = 8


# start with a blank screen
oled.fill(0)
# we just blanked the framebuffer. to push the framebuffer onto the display, we call show()
oled.show()

colors = ["Banana", "Apple", "Lime", "Orange"]
sensors = [0, 11, 7, 2]

score = 0

while True:

    index = random.randint(0, 3)
    oled.text(colors[index], 0, 10, 1)
    oled.text(str(score), 20, 10, 1)
    oled.show()

    print(colors[index])
    t_end = time.time() + 5
    while time.time() < t_end:
        print("well hello")
        if mpr121[sensors[index]].value:
            print(f"Twizzler {index} touched!")
            score += 1
    time.sleep(random.randint(0,5))  # Small delay to keep from spamming output messages.
    
