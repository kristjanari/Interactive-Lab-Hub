# The MIT License (MIT)
#
# Copyright (c) 2020 Gregory M Paris
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


import time
import subprocess
import digitalio
import board
import busio
from random import randint
from time import strftime, sleep
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
import adafruit_apds9960.apds9960
from i2c_button import I2C_Button

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)

sensor.enable_proximity = True

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

# initialize I2C
i2c = busio.I2C(board.SCL, board.SDA)

# scan the I2C bus for devices
while not i2c.try_lock():
	pass
devices = i2c.scan()
i2c.unlock()
default_addr = 0x6f
if default_addr not in devices:
	print('warning: no device at the default button address', default_addr)

# initialize the button
button = I2C_Button(i2c)

def custom_clock(x, y, hour_now, min_now, sec_now): 
    fill = "#FFFFFF"
    min_1 = int(min_now) // 10
    min_2 = int(min_now) % 10
    
    pm = int(hour_now) // 12

    hours = [str(i) for i in range(12)]
    mins = [str(i) for i in range(6)] 
    minss = [str(i) for i in range(10)]
    for h in hours:
        text = str(h) + " " if h != "0" else "12" + " "
        fill = "#00FF00" if (int(hour_now) % 12) == int(h) else "#FFFFFF"
        draw.text((x, y), text, font=font, fill=fill)
        x += font.getsize(text)[0]
    
    x = width/4
    y += font.getsize("am")[1]
    
    fill = "#00FF00" if not pm else "#FFFFFF"
    draw.text((x, y), "am", font=font, fill=fill)
    
    x = 2*width/4
    fill = "#00FF00" if pm else "#FFFFFF"
    draw.text((x, y), "pm", font=font, fill=fill)
    
    x = 0
    y += font.getsize("am")[1]

    for m in mins:
        text = str(m) + " "
        fill = "#00FF00" if int(min_1) == int(m) else "#FFFFFF"
        draw.text((x, y), text, font=font, fill=fill)
        x += font.getsize(text)[0]
    
    x = 0
    y += font.getsize(text)[1]
    
    for m in minss:
        text = str(m) + " "
        fill = "#00FF00" if int(min_2) == int(m) else "#FFFFFF"
        draw.text((x, y), text, font=font, fill=fill)
        x += font.getsize(text)[0]

    x = 0
    y += 2*font.getsize(text)[1]
    text = "|"
    for i in range(int(sec_now)):
        draw.text((x,y), text, font=font, fill="#00FF00")
        x += 0.7 * font.getsize(text)[0]

    x = 0
    y += font.getsize(text)[1]
    if sensor.proximity > 200:
        draw.text((x,y), 'Wow!, this is dark!', font=font2, fill="#FFFFFF")
    disp.image(image, rotation)

def display_face(hour_now, min_now, sec_now):
    image = Image.open("mynd.JPG")
    backlight = digitalio.DigitalInOut(board.D22)
    backlight.switch_to_output()
    backlight.value = True
    
    
    # Scale the image to the smaller screen dimension
    image_ratio = image.width / image.height
    screen_ratio = width / height
    if screen_ratio < image_ratio:
        scaled_width = image.width * height // image.height
        scaled_height = height
    else:
        scaled_width = width
        scaled_height = image.height * width // image.width

    scaled_width = max(1, int(scaled_width * (int(sec_now) / 60)))
    image = image.resize((scaled_width, scaled_height), Image.BICUBIC)
    
    # Crop and center the image
    x = scaled_width // 2 - width // 2
    y = scaled_height // 2 - height // 2
   
    text = hour_now + ':' + min_now
    image = image.crop((x, y, x + width, y + height))
    draw = ImageDraw.Draw(image)
    size = font.getsize(text)[1]
    text_x = width // 2 - font.getsize(text)[0] // 2
    draw.rectangle((0, height - size, width, height), outline=0, fill=(0, 0, 0))
    changing_fill = '#FFFFFF'
    if sensor.proximity > 100:
        changing_fill = '#FF007d'
    elif sensor.proximity > 200:
        changing_fill = '#03FF23'
    draw.text((text_x, height - size), text, font=font2, fill=changing_fill)
    disp.image(image, rotation)


def button_action(status):
    button.clear() # status must be cleared manually
    
    if button.last_click_ms < 1000:
        button.led_bright = 0
        button.led_gran = 1
        button.led_cycle_ms = 0
        button.led_off_ms = 100
        return not status
    if button.last_click_ms > 30000:
        button.led_bright = 255
        button.led_gran = 1 
        button.led_cycle_ms = 100
        button.led_off = 100
    return status

img_display = True

while True:
    try:
        # Draw a black filled box to clear the image.
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
    
        #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 
        timenow = strftime("%m/%d/%Y %H:%M:%S")
        hour_now = strftime("%H")
        min_now = strftime("%M")
        min_1 = int(min_now) // 10
        min_2 = int(min_now) % 10
        sec_now = strftime("%S")
        x = 0
        y = padding
        fill = "#FFFFFF"
    
        img_display = button_action(img_display)
        # Display image
        if img_display:
            display_face(hour_now, min_now, sec_now)
        else:
            custom_clock(x, y, hour_now, min_now, sec_now)
    
        time.sleep(1)
    except KeyboardInterrupt:
        button.clear()
        button.led_bright = 0
        button.led_gran = 1
        button.led_cycle_ms = 0
        button.led_off_ms = 100
        break
