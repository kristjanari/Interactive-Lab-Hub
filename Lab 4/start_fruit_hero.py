# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
import os
import board
import random
import busio
import time
import adafruit_ssd1306
import adafruit_mpr121
from adafruit_bus_device.i2c_device import I2CDevice
from PIL import Image, ImageDraw, ImageFont

IS_PRESSED = 0x4
DEVICE_ADDRESS = 0x6f
STATUS = 0x03

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)
buttonDevice = I2CDevice(i2c, DEVICE_ADDRESS)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

#Create capatitive sensor
mpr121 = adafruit_mpr121.MPR121(i2c)

# start with a blank screen
oled.fill(0)
# we just blanked the framebuffer. to push the framebuffer onto the display, we call show()
oled.show()

colors = ["Banana", "Tomato", "Lime", "Orange"]
sensors = [9, 7, 11, 0]
score = 0

# Load a font in 2 different sizes.
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
font3 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)

def read_register(dev, register, n_bytes=1):
    # write a register number then read back the value
    reg = register.to_bytes(1, 'little')
    buf = bytearray(n_bytes)
    with dev:
        dev.write_then_readinto(reg, buf)
    return int.from_bytes(buf, 'little')

gameStarted = False
# Red = Twizzler 0
# White = Twizzler 7
# Yellow = Twizzler 9
# Green = Twizzler 11

image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)
oled.fill(0)
draw.text((0, 0), "Press button to play!", font=font3, fill=255)
oled.image(image)
oled.show()
os.system("./welcome.sh")

while True:
    if gameStarted:
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
            else:
                isbroken = False
                for i in range(4):
                    if i != index and  mpr121[sensors[i]].value:
                        print('print boy')
                        isbroken = True
                        break
                if isbroken:
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
        time.sleep(random.randrange(1,2))  # Small delay to keep from spamming output messages.        
        if score == 15:
            score = 0
            image = Image.new("1", (oled.width, oled.height))
            draw = ImageDraw.Draw(image)
            oled.fill(0)
            draw.text((0, 0), "Congrats! You win!", font=font3, fill=255)
            draw.text((0, 20), "Press to play again.", font=font3, fill=255)
            oled.image(image)
            oled.show()
            os.system("./take_photo.sh")
            gameStarted = False 
    else:
        print('Waiting to start...')
        btn_status = read_register(buttonDevice, STATUS)
        if (btn_status & IS_PRESSED) !=0:
            print('game start!')
            gameStarted = True
        time.sleep(.1)
