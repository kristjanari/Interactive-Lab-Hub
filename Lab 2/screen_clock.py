import time
import subprocess
import digitalio
import board
from time import strftime, sleep
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

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

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 
    timenow = strftime("%m/%d/%Y %H:%M:%S")
    hour_now = strftime("%H")
    min_now = strftime("%M")
    min_1 = int(min_now) // 10
    min_2 = int(min_now) % 10
    sec_now = strftime("%S")
    
    pm = int(hour_now) // 12

    hours = [str(i) for i in range(12)]
    mins = [str(i) for i in range(6)] 
    minss = [str(i) for i in range(10)]

    y = top
    x = 0
    fill = "#FFFFFF"
    for h in hours:
        text = str(h) + " "
        fill = "#00FF00" if (int(hour_now) % 12) == int(h) else "#FFFFFF"
        draw.text((x, y), text, font=font, fill=fill)
        x += font.getsize(text)[0]
        sleep(1)
    
    x = width/4
    y += font.getsize("am")[1]
    
    fill = "#00FF00" if not pm else "#FFFFFF"
    draw.text((x, y), "am", font=font, fill=fill)
    
    x = 2*width/4
    fill = "#00FF00" if pm else "#FFFFFF"
    draw.text((x, y), "am", font=font, fill=fill)
    
    x = 0
    y += font.getsize("am")[1]

    for m in mins:
        text = str(m) + " "
        fill = "#00FF00" if int(min_1) == int(m) else "#FFFFFF"
        draw.text((x, y), text, font=font, fill=fill)
        x += font.getsize(text)[0]
        sleep(1)
    
    x = 0
    y += font.getsize(text)[1]
    
    for m in minss:
        text = str(m) + " "
        fill = "#00FF00" if int(min_2) == int(m) else "#FFFFFF"
        draw.text((x, y), text, font=font, fill=fill)
        x += font.getsize(text)[0]
        sleep(1)

    # Display image
    disp.image(image, rotation)
    time.sleep(1)
