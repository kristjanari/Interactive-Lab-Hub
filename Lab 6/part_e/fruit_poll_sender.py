import time
import board
import busio
import adafruit_mpr121
import os
import paho.mqtt.client as mqtt
import uuid

client = mqtt.Client(str(uuid.uuid1()))
client.tls_set()
client.username_pw_set('idd', 'device@theFarm')

client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

topic = 'IDD/coolteamfruit'

i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)
fruits = ['apple', 'lime', 'banana']

while True:
    for i, fruit in enumerate(fruits): 
        if mpr121[i].value:
            os.system('./' + fruit + '_selected.sh')
            client.publish(topic, fruit)
    time.sleep(0.25)
