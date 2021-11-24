# How to load a Tensorflow model using OpenCV
# Jean Vitor de Paulo Blog - https://jeanvitor.com/tensorflow-object-detecion-opencv/
# David edited some stuff
import time
import board
import busio
from i2c_button import I2C_Button
import os
import numpy as np
import cv2
import sys

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

# initiatilize the button
button = I2C_Button(i2c)


# Load a model imported from Tensorflow
tensorflowNet = cv2.dnn.readNetFromTensorflow('frozen_inference_graph.pb', 'ssd_mobilenet_v2_coco_2018_03_29.pbtxt')

img = None
webCam = False
if(len(sys.argv)>1 and not sys.argv[-1]== "noWindow"):
   try:
      print("I'll try to read your image");
      img = cv2.imread(sys.argv[1])
      if img is None:
         print("Failed to load image file:", sys.argv[1])
   except:
      print("Failed to load the image are you sure that:", sys.argv[1],"is a path to an image?")
else:
   try:
      print("Trying to open the Webcam.")
      cap = cv2.VideoCapture(0)
      if cap is None or not cap.isOpened():
         raise("No camera")
      webCam = True
   except:
      img = cv2.imread("../data/test.jpg")
      print("Using default image.")


while(True):
    if webCam:
        ret, img = cap.read()

    rows, cols, channels = img.shape

    # Use the given image as input, which needs to be blob(s).
    tensorflowNet.setInput(cv2.dnn.blobFromImage(img, size=(300, 300), swapRB=True, crop=False))

    # Runs a forward pass to compute the net output
    networkOutput = tensorflowNet.forward()
    
    print('output shape: ',networkOutput.shape) 

    numObjs = 0
    for detection in networkOutput[0,0]:
        score = float(detection[2])
        if score > 0.2:
            numObjs += 1 
    isGreen = True if numObjs == 3 else False 
    color = (0, 255, 0) if isGreen else (0, 0, 255)

    # Loop on the outputs
    for detection in networkOutput[0,0]:
        score = float(detection[2])
        if score > 0.2:
            left = detection[3] * cols
            top = detection[4] * rows
            right = detection[5] * cols
            bottom = detection[6] * rows
            color = (0, 255, 0) if isGreen else (0, 0, 255)

            #draw a red rectangle around detected objects
            cv2.rectangle(img, (int(left), int(top)), (int(right), int(bottom)), color, thickness=2)
    if webCam:
        if sys.argv[-1] == "noWindow":
           print("Finished a frame")
           cv2.imwrite('detected_out.jpg',img)
           continue
        cv2.imshow('detected (press q to quit)',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite('outpuut.jpg', img)
            cap.release()
            break
        if isGreen:
            os.system("./speak.sh")
            button.led_bright = 255
            button.led_gran = 1
            button.led_cycle_ms = 100
            button.led_off = 100
            time.sleep(4)
            button.clear()
            button.led_bright = 0
            button.led_gran = 1
            button.led_cycle_ms = 0
            button.led_off_ms = 100
        else:    
            button.clear()
            button.led_bright = 0
            button.led_gran = 1
            button.led_cycle_ms = 0
            button.led_off_ms = 100
    else:
        break

cv2.imwrite('detected_out.jpg',img)
cv2.destroyAllWindows()


