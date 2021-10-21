# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
import random
import busio
import time
import adafruit_ssd1306
import adafruit_mpr121

from PIL import Image, ImageDraw, ImageFont



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

# Load a font in 2 different sizes.
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)

while True:

    index = random.randint(0, 3)
    image = Image.new("1", (oled.width, oled.height))

    draw = ImageDraw.Draw(image)
    oled.fill(0)
    draw.text((0, 0), colors[index], font=font2, fill=255)
    draw.text((96, 0), str(score), font=font2, fill=255)
    oled.image(image)
    oled.show()
    
    message = "NICE JOB! :D"
    print(colors[index])
    t_end = time.time() + 5
    incorrect = True
    while time.time() < t_end:
        if mpr121[sensors[index]].value:
            print(f"Twizzler {index} touched!")
            score += 1
            incorrect = False
            break
    if incorrect:
        score -= 1
        message = "TOO BAD :("

    image = Image.new("1", (oled.width, oled.height))

    draw = ImageDraw.Draw(image)
    oled.fill(0)
    draw.text((0, 0), message, font=font2, fill=255)
    draw.text((96, 0), str(score), font=font2, fill=255)
    oled.image(image)
    oled.show()
    time.sleep(random.randint(2,5))  # Small delay to keep from spamming output messages.
    
