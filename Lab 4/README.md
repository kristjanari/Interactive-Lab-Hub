# Ph-UI!!!

For lab this week, we focus on both on sensing, to bring in new modes of input into your devices, as well as prototyping the physical look and feel of the device. You will think about the physical form the device needs to perform the sensing as well as present the display or feedback about what was sensed. 

## Part 1 Lab Preparation

### Get the latest content:
As always, pull updates from the class Interactive-Lab-Hub to both your Pi and your own GitHub repo. As we discussed in the class, there are 2 ways you can do so:

**\[recommended\]**Option 1: On the Pi, `cd` to your `Interactive-Lab-Hub`, pull the updates from upstream (class lab-hub) and push the updates back to your own GitHub repo. You will need the personal access token for this.

```
pi@ixe00:~$ cd Interactive-Lab-Hub
pi@ixe00:~/Interactive-Lab-Hub $ git pull upstream Fall2021
pi@ixe00:~/Interactive-Lab-Hub $ git add .
pi@ixe00:~/Interactive-Lab-Hub $ git commit -m "get lab4 content"
pi@ixe00:~/Interactive-Lab-Hub $ git push
```

Option 2: On your your own GitHub repo, [create pull request](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md) to get updates from the class Interactive-Lab-Hub. After you have latest updates online, go on your Pi, `cd` to your `Interactive-Lab-Hub` and use `git pull` to get updates from your own GitHub repo.

### Start brasinstorming ideas by reading: 
* [What do prototypes prototype?](https://www.semanticscholar.org/paper/What-do-Prototypes-Prototype-Houde-Hill/30bc6125fab9d9b2d5854223aeea7900a218f149)
* [Paper prototyping](https://www.uxpin.com/studio/blog/paper-prototyping-the-practical-beginners-guide/) is used by UX designers to quickly develop interface ideas and run them by people before any programming occurs. 
* [Cardboard prototypes](https://www.youtube.com/watch?v=k_9Q-KDSb9o) help interactive product designers to work through additional issues, like how big something should be, how it could be carried, where it would sit. 
* [Tips to Cut, Fold, Mold and Papier-Mache Cardboard](https://makezine.com/2016/04/21/working-with-cardboard-tips-cut-fold-mold-papier-mache/) from Make Magazine.
* [Surprisingly complicated forms](https://www.pinterest.com/pin/50032245843343100/) can be built with paper, cardstock or cardboard.  The most advanced and challenging prototypes to prototype with paper are [cardboard mechanisms](https://www.pinterest.com/helgangchin/paper-mechanisms/) which move and change. 
* [Dyson Vacuum Cardboard Prototypes](http://media.dyson.com/downloads/JDF/JDF_Prim_poster05.pdf)
<p align="center"><img src="https://dysonthedesigner.weebly.com/uploads/2/6/3/9/26392736/427342_orig.jpg"  width="200" > </p>

### Gathering materials for this lab:

* Cardboard (start collecting those shipping boxes!)
* Found objects and materials--like bananas and twigs.
* Cutting board
* Cutting tools
* Markers

(We do offer shared cutting board, cutting tools, and markers on the class cart during the lab, so do not worry if you don't have them!)

## Deliverables \& Submission for Lab 4

The deliverables for this lab are, writings, sketches, photos, and videos that show what your prototype:
* "Looks like": shows how the device should look, feel, sit, weigh, etc.
* "Works like": shows what the device can do.
* "Acts like": shows how a person would interact with the device.

For submission, the readme.md page for this lab should be edited to include the work you have done:
* Upload any materials that explain what you did, into your lab 4 repository, and link them in your lab 4 readme.md.
* Link your Lab 4 readme.md in your main Interactive-Lab-Hub readme.md. 
* Group members can turn in one repository, but make sure your Hub readme.md links to the shared repository.
* Labs are due on Mondays, make sure to submit your Lab 4 readme.md to Canvas.


## Lab Overview

A) [Capacitive Sensing](#part-a)

B) [OLED screen](#part-b) 

C) [Paper Display](#part-c)

D) [Materiality](#part-d)

E) [Servo Control](#part-e)

F) [Record the interaction](#part-f)

## The Report (Part 1: A-D, Part 2: E-F)

### Part A
### Capacitive Sensing, a.k.a. Human-Twizzler Interaction 

We want to introduce you to the [capacitive sensor](https://learn.adafruit.com/adafruit-mpr121-gator) in your kit. It's one of the most flexible input devices we are able to provide. At boot, it measures the capacitance on each of the 12 contacts. Whenever that capacitance changes, it considers it a user touch. You can attach any conductive material. In your kit, you have copper tape that will work well, but don't limit yourself! In the example below, we use Twizzlers--you should pick your own objects.


<p float="left">
<img src="https://cdn-learn.adafruit.com/guides/cropped_images/000/003/226/medium640/MPR121_top_angle.jpg?1609282424" height="150" />
<img src="https://cdn-shop.adafruit.com/1200x900/4401-01.jpg" height="150">
</p>

Plug in the capacitive sensor board with the QWIIC connector. Connect your Twizzlers with either the copper tape or the alligator clips (the clips work better). In this lab, we will continue to use the `circuitpython` virtual environment we created before. Activate `circuitpython` and `cd` to your Lab 4 folder to install the requirements by:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ pip3 install -r requirements.txt
```

<img src="https://media.discordapp.net/attachments/679721816318803975/823299613812719666/PXL_20210321_205742253.jpg" width=400>
These Twizzlers are connected to pads 6 and 10. When you run the code and touch a Twizzler, the terminal will print out the following

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python cap_test.py 
Twizzler 10 touched!
Twizzler 6 touched!
```

#### Testing out the capacitive sensor

https://youtu.be/w_GNMGVBeIA

### Part B
### More sensors

#### Light/Proximity/Gesture sensor (APDS-9960)

We here want you to get to know this awesome sensor [Adafruit APDS-9960](https://www.adafruit.com/product/3595). It is capable of sensing proximity, light (also RGB), and gesture! 

<img src="https://cdn-shop.adafruit.com/970x728/3595-03.jpg" width=200>

Connect it to your pi with Qwiic connector and try running the 3 example scripts individually to see what the sensor is capable of doing!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python light_test.py
...
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python proximity_test.py
...
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python gesture_test.py
...
```

You can go the the [Adafruit GitHub Page](https://github.com/adafruit/Adafruit_CircuitPython_APDS9960) to see more examples for this sensor!

#### Testing out the proximity sensor

https://youtu.be/enST2dVSKes

#### Rotary Encoder

A rotary encoder is an electro-mechanical device that converts the angular position to analog or digital output signals. The [Adafruit rotary encoder](https://www.adafruit.com/product/4991#technical-details) we ordered for you came with separated breakout board and encoder itself, that is, they will need to be soldered if you have not yet done so! We will be bringing the soldering station to the lab class for you to use, also, you can go to the MakerLAB to do the soldering off-class. Here is some [guidance on soldering](https://learn.adafruit.com/adafruit-guide-excellent-soldering/preparation) from Adafruit. When you first solder, get someone who has done it before (ideally in the MakerLAB environment). It is a good idea to review this material beforehand so you know what to look at.

<p float="left">
<img src="https://cdn-shop.adafruit.com/970x728/4991-01.jpg" height="200" />
<img src="https://cdn-shop.adafruit.com/970x728/377-02.jpg" height="200" />
<img src="https://cdn-shop.adafruit.com/970x728/4991-09.jpg" height="200">
</p>

Connect it to your pi with Qwiic connector and try running the example script, it comes with an additional button which might be useful for your design!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python encoder_test.py
```

You can go to the [Adafruit Learn Page](https://learn.adafruit.com/adafruit-i2c-qt-rotary-encoder/python-circuitpython) to learn more about the sensor! The sensor actually comes with an LED (neo pixel): Can you try lighting it up?

#### Testing out the Rotary sensor

https://youtu.be/GbnVW8G-lCs

#### Joystick

A [joystick](https://www.sparkfun.com/products/15168) can be used to sense and report the input of the stick for it pivoting angle or direction. It also comes with a button input!

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/3/5/5/8/15168-SparkFun_Qwiic_Joystick-01.jpg" height="200" />
</p>

Connect it to your pi with Qwiic connector and try running the example script to see what it can do!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python joystick_test.py
```

You can go to the [SparkFun GitHub Page](https://github.com/sparkfun/Qwiic_Joystick_Py) to learn more about the sensor!

#### Testing out the Joystick

https://youtu.be/Ysw0t7rFopQ

#### (Optional) Distance Sensor

Note: We did not distribute this sensor to you, so if you are interested in playing with it, please come pick it up from the TA!

Earlier we have asked you to play with the proximity sensor, which is able to sense object within a short distance. Here, we offer [Qwiic Multi Distance Sensor](https://www.sparkfun.com/products/17072), which has a field of view of about 25° and is able to detect objects up to 3 meters away! 

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/6/0/3/4/17072-Qwiic_Multi_Distance_Sensor_-_VL53L3CX-01.jpg" height="200" />
</p>

Connect it to your pi with Qwiic connector and try running the example script to see how it works!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python distance_test.py
```

You can go to the [SparkFun GitHub Page](https://github.com/sparkfun/Qwiic_VL53L1X_Py) to learn more about the sensor and see other examples!

### Part C
### Physical considerations for sensing

Usually, sensors need to positioned in specific locations or orientations to make them useful for their application. Now that you've tried a bunch of the sensors, pick one that you would like to use, and an application where you use the output of that sensor for an interaction. For example, you can use a distance sensor to measure someone's height if you position it overhead and get them to stand under it.

**\*\*\*Draw 5 sketches of different ways you might use your sensor, and how the larger device needs to be shaped in order to make the sensor useful.\*\*\***


### Sensor

Afer trying out all of the sensors we chose to use the capacitive sensor. We had the most fun playing around with that sensor and saw some exciting opportunities. The favorites are listed below.

#### Alarm System

This device is designed to protect valuable metals, such as jewelry. The user can place a valuable item on the device and put it on lock mode. If an intruder touches the object that shall not be touched an alarm goes off. The object must be conductive. The surface would be made of conductive material and connected to the capacitive sensor.

<img width="709" alt="image" src="https://user-images.githubusercontent.com/42963791/137664459-d2cdda1e-ea3e-41b6-8ee5-9b8fe21da699.png">

#### Item Piano

This device plays different sounds when various items are touched. It can play up to 12 notes and the notes could e.g. be made of bananas. Each banana/note would be connected to the capacitive sensor and a different pitch is played for each one of them on touch.

<img width="719" alt="image" src="https://user-images.githubusercontent.com/42963791/137664476-4120e74e-e764-4ccf-9e08-0a69cd3f693a.png">

#### Fruit Hero

This device is a game that is similar to guitar hero. The device displays a color on the screen and the user is supposed to touch the fruit of that color. The display is in tune with a song and the user gets points for each correct touch. 

<img width="797" alt="image" src="https://user-images.githubusercontent.com/42963791/137664533-a289046a-0b43-4860-9d8d-7a3ac3e00ec2.png">

#### Kitchen for Special Needs

This device is for people with disabilities (especially those who struggle with using force) to use in the kitchen. It is connected to various devices in the kitchen (fridge, oven, microwave, etc.) and can open each device on touch. So, to open the fridge for example, one could simply touch the front door.

<img width="715" alt="image" src="https://user-images.githubusercontent.com/42963791/137664574-5afc9094-311c-49ef-8891-3958b0fff73d.png">

#### Touch Based Calculator

The pi-calc operates simply by taking binary input, and then applying basic operations such as add, subtract, multiply, and divide. You press each of the “0”/“1” keys, and they show up on the screen. Then you can press the operations, and input more binary digits. Finally, if you press the equate button, it will calculate your answer. 

<img width="894" alt="image" src="https://user-images.githubusercontent.com/42963791/137666067-b9491550-ba2b-44e1-bc22-2ee4b3a513a0.png">


**\*\*\*What are some things these sketches raise as questions? What do you need to physically prototype to understand how to anwer those questions?\*\*\***

#### Alarm System

The main question of this device is wheater the surface will detect if a conducting object that is placed on it is touched. To answer this question we would have to try out different materials for the surface and see which ones gives the best reaction. Another question that arises is how to allow the user to get the item without setting off the alarm. Prototyping would help solve this issue by testing out different ways to turn off the sensor without triggering the alarm by touching the surface. The user could e.g. have access to a keypad to unlock the device (turn off the sensor).

#### Item Piano

The first question we thought of related to this device was how to organise the items (notes) of the piano. This could be done in a similar manner to a regular piano which could easily be prototyped with cardboard. Ideally, the user only sees the items and not the wires and the items would be approximately 1m above the ground. This would require a lot of cardboard but would be very helpful in designing the layout of the items.

#### Fruit Hero

The biggest question for this device is how to display which fruit to touch next. The fruits will be connected to some control device that controls the game. The device needs some monitor to display this data and it should have a speaker to play the music. Ideally, it contains a camera to take pictures of users while they play the game. The device must include all these sensors, displays and wires and a perfect tool to decide on the design is prototyping it with carboard. We can move the different sensors around and see which design delivers the best user experience. 

#### Kitchen for Special Needs

There are certainly a few questions that come to mind for the special needs kitchen. First, some items will be more difficult than others to open: for example, how will we open the fridge? It is essentially an insulated, refrigerated box, so it would be difficult to get inside the fridge and open the door. To answer this question, we would need to include some sort of insulated box in our prototype. Moreover, we would want to ensure that the door is somewhat heavy, as fridge doors often hold goods as well and will be more difficult, than say, a regular kitchen cabinet to open. Another question is how to reach cabinets / parts of the kitchen that are far apart. We could prototype this by using a wide area to prototype our kitchen, to ensure we can handle larger spaces. Lastly, we were wondering how this prototype might help those with special needs open cabinets that are either too low or too high. This could simply be included in our prototyping by having low and high cabinets, so when our testers prototype the kitchen we can see how it works for them and how we could potentially improve it. 

#### Touch Based Calculator

One of the first questions we had was how we would manage the input to the calculator. To answer this, we realized that since the touch capacitor only had 12 inputs, that would only leave room for one operation and a compute button. So, we decided to utilize a binary calculator to have more operations available. This would also simply the code as binary is natively understood by the Pi. We would also have to consider the placement of the buttons, so they would be intuitively placed. To answer this, we could place each key in different locations or arrangements on the box and feel it out. We felt that the design shown in the sketch would be the most ideal. Another question was what material would be best used for the “keys” of the calculator. We figured something like aluminum foil would be an effective key, as it is known to be a conductor of electricity and is easily moldable and flat. We could also write on it effectively. To physically prototype this, we would simply test out multiple different materials. Lastly, we wondered what would be the best way to limit the digits so they would fit on the screen, and so that the result would similarly fit on the screen. This could be done by testing out various font sizes and limits on digit quantities through the software side of the device, and then we can observe how they fit on the actual screen. 

**\*\*\*Pick one of these designs to prototype.\*\*\***

We decided on **Fruit Hero** as our design to prototype. 


### Part D
### Physical considerations for displaying information and housing parts


Here is an Pi with a paper faceplate on it to turn it into a display interface:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/paper_if.png?raw=true"  width="250"/>


This is fine, but the mounting of the display constrains the display location and orientation a lot. Also, it really only works for applications where people can come and stand over the Pi, or where you can mount the Pi to the wall.

Here is another prototype for a paper display:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/b_box.png?raw=true"  width="250"/>

Your kit includes these [SparkFun Qwiic OLED screens](https://www.sparkfun.com/products/17153). These use less power than the MiniTFTs you have mounted on the GPIO pins of the Pi, but, more importantly, they can be more flexibily be mounted elsewhere on your physical interface. The way you program this display is almost identical to the way you program a  Pi display. Take a look at `oled_test.py` and some more of the [Adafruit examples](https://github.com/adafruit/Adafruit_CircuitPython_SSD1306/tree/master/examples).

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/6/1/3/5/17153-SparkFun_Qwiic_OLED_Display__0.91_in__128x32_-01.jpg" height="200" />
<img src="https://cdn.discordapp.com/attachments/679466987314741338/823354087105101854/PXL_20210322_003033073.jpg" height="200">
</p>


It holds a Pi and usb power supply, and provides a front stage on which to put writing, graphics, LEDs, buttons or displays.

This design can be made by scoring a long strip of corrugated cardboard of width X, with the following measurements:

| Y height of box <br> <sub><sup>- thickness of cardboard</sup></sub> | Z  depth of box <br><sub><sup>- thickness of cardboard</sup></sub> | Y height of box  | Z  depth of box | H height of faceplate <br><sub><sup>* * * * * (don't make this too short) * * * * *</sup></sub>|
| --- | --- | --- | --- | --- | 

Fold the first flap of the strip so that it sits flush against the back of the face plate, and tape, velcro or hot glue it in place. This will make a H x X interface, with a box of Z x X footprint (which you can adapt to the things you want to put in the box) and a height Y in the back. 

Here is an example:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/horoscope.png?raw=true"  width="250"/>

Think about how you want to present the information about what your sensor is sensing! Design a paper display for your project that communicates the state of the Pi and a sensor. Ideally you should design it so that you can slide the Pi out to work on the circuit or programming, and then slide it back in and reattach a few wires to be back in operation.
 
**\*\*\*Sketch 5 designs for how you would physically position your display and any buttons or knobs needed to interact with it.\*\*\***

<img width="276" alt="Screen Shot 2021-10-17 at 11 04 02 PM" src="https://user-images.githubusercontent.com/52221419/137662927-bf0c4af7-825d-47dd-a9d2-6b0efe68af11.png">

<img width="286" alt="Screen Shot 2021-10-17 at 11 04 09 PM" src="https://user-images.githubusercontent.com/52221419/137662939-b8a30cc6-bd4f-4bb6-b002-8c8d54937b30.png">

<img width="285" alt="Screen Shot 2021-10-17 at 11 04 20 PM" src="https://user-images.githubusercontent.com/52221419/137662952-b4874a71-8624-446c-af74-bfa0d1fc06d8.png">

<img width="307" alt="Screen Shot 2021-10-17 at 11 04 26 PM" src="https://user-images.githubusercontent.com/52221419/137662960-b847eec0-56a6-4d6e-83b0-dc30a58c669b.png">

<img width="283" alt="Screen Shot 2021-10-17 at 11 04 33 PM" src="https://user-images.githubusercontent.com/52221419/137662968-15787519-9983-472e-8d97-9d80e3a0de6e.png">


**\*\*\*What are some things these sketches raise as questions? What do you need to physically prototype to understand how to anwer those questions?\*\*\***

Here were the main questions we had with these sketches:
- How much leeway do we want the cables to have with the fruits and vegetables?
- Do we went to look down at the game or look across at it?
- Should the game be played standing up or sitting down? 
- Which screen should we use to show the color to press - the Adafruit PiTFT or the external corded monitor?

**\*\*\*Pick one of these display designs to integrate into your prototype.\*\*\***

We decided on **Design 2.**

We beleived it would be realistic to create a functional prototpy of that device and that the device would be rather entertaining.

**\*\*\*Explain the rationale for the design.\*\*\*** (e.g. Does it need to be a certain size or form or need to be able to be seen from a certain distance?)

We chose design 2 for a number of reasons:
- By putting the cables to the fruits and vegetables at the front of the box, we are able to have more length between the box and the fruits, allowing for more user customization of how to play. 
- We did not want to use design 5 as it required the user to stand up while playing, and we figured to play games on a keyboard it would be better to play sitting down. 
- With the camera on the front, we realized this would create balance based issues - since it would be protruding out the front, it would weigh down the box and it would fall forward. However, with design 2, by having the camera on top it was held down by gravity and actually kind of helped holding the box in the right angle.
- We wanted to initially use the ADAfruit PiTFT as our monitor for simplicity, as shown in design 4. However, this caused it to be too small to see and created design issues within the interior of the box. By using the external screen connected by a cable, it is more flexible to place both the screen and organize the interior of the box. It also allowed us to put the cables to the fruits and vegetables as the front of the box, which we found ideal, as described in the first bullet point.  

Build a cardbord prototype of your design.

**\*\*\*Document your rough prototype.\*\*\***

### The Cardboard Prototype

The prototype is displayed below. The screen on the bow displays the next fruit to touch and the speacker on the camera plays the music. The raspberyy pi is inside the box as well as all the wires.

<img width="552" alt="image" src="https://user-images.githubusercontent.com/42963791/137662957-0c0d1bd6-7381-4b38-95ad-6b03ef84e118.png">

The video below shows the internal structure of the device, there is a special compartment for the raspberry pi and the vires and sensors are properly mounted with tape and glue.

https://youtu.be/7MgRAdgzGWg


LAB PART 2

### Part 2

Following exploration and reflection from Part 1, complete the "looks like," "works like" and "acts like" prototypes for your design, reiterated below.

### Received feedback

#### Angleica Kosach:
I think Fruit Hero is definitely a fun idea! The idea of tapping the fruit according to the music is much more fun than just making it act as a piano, for example. Some other interesting ideas would be to display the fruit in a spatial structure instead of just laying it out on the floor, so the user can even get a workout in while playing the game. You can also introduce difficulty levels to the game by making higher levels require the use of feet as well.

#### Rebecca Lassmann:
I love the creativity of the fruit hero game! The prototype looks great. A few questions: 1) the softer fruits like raspberries probably wont last so may make sense to swap out with an apple or other veggies. 2) Is there a way to cover the wires and clamps so the player doesn't disconnect them by accident? Same question for the speaker - curious if you tested a version where the speaker was inside of the device instead on on top to make it look like one single device and less likely for things to be taken apart,

#### Jiacheng Peng
I really like your idea of making a game! I think the game will be fun. I think some of the things you did not consider is that how to start and reset the game. Maybe add some feature to change the songs playing or different playing modes would be more fun. 

#### Summarized Comments: 
- One of the comments we received noted we have no to reset and start the game, which is an important thing to think about. We will add this to our prototype. 
- We also were told to incorporate different modes of playing the game or perhaps add more songs which the player can switch through. 

### Part E (Optional)
### Servo Control with Joystick

In the class kit, you should be able to find the [Qwiic Servo Controller](https://www.sparkfun.com/products/16773) and [Micro Servo Motor SG51](https://www.adafruit.com/product/2201). The Qwiic Servo Controller will need external power supply to drive, which we will be distributing the battery packs in the class. Connect the servo controller to the miniPiTFT through qwiic connector and connect the external battery to the 2-Pin JST port (ower port) on the servo controller. Connect your servo to channel 2 on the controller, make sure the brown is connected to GND and orange is connected to PWM.

<img src="https://scontent-lga3-1.xx.fbcdn.net/v/t1.15752-9/245605956_303690921194525_3309212261588023460_n.jpg?_nc_cat=110&ccb=1-5&_nc_sid=ae9488&_nc_ohc=FvFLlClTKuUAX9nJ3LR&_nc_ht=scontent-lga3-1.xx&oh=b7ec1abc8d458b6c1b7a00a6f11398ac&oe=618D7D96" width="400"/>

In this exercise, we will be using the nice [ServoKit library](https://learn.adafruit.com/16-channel-pwm-servo-driver/python-circuitpython) developed by Adafruit! We will continue to use the `circuitpython` virtual environment we created. Activate the virtual environment and make sure to install the latest required libraries by running:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ pip3 install -r requirements.txt
```

A servo motor is a rotary actuator or linear actuator that allows for precise control of angular or linear position. The position of a servo motor is set by the width of an electrical pulse, that is, we can use PWM (pulse-width modulation) to set and control the servo motor position. You can read [this](https://learn.adafruit.com/adafruit-arduino-lesson-14-servo-motors/servo-motors) to learn a bit more about how exactly a servo motor works.

Now that you have a basic idea of what a servo motor is, look into the script `qwiic_servo_example.py` we provide. In line 14, you should see that we have set up the min_pulse and max_pulse corresponding to the servo turning 0 - 180 degree. Try running the servo example code now and see what happens:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python servo_test.py
```

It is also possible to control the servo using the sensors mentioned in as in part A and part B, and/or from some of the buttons or parts included in your kit, the simplest way might be to chain Qwiic buttons to the other end of the Qwiic OLED. Like this:

<p align="center"> <img src="chaining.png"  width="200" ></p>

You can then call whichever control you like rather than setting a fixed value for the servo. For more information on controlling Qwiic devices, Sparkfun has several python examples, such as [this](https://learn.sparkfun.com/tutorials/qwiic-joystick-hookup-guide/all#python-examples).

We encourage you to try using these controls, **while** paying particular attention to how the interaction changes depending on the position of the controls. For example, if you have your servo rotating a screen (or a piece of cardboard) from one position to another, what changes about the interaction if the control is on the same side of the screen, or the opposite side of the screen? Trying and retrying different configurations generally helps reveal what a design choice changes about the interaction -- _make sure to document what you tried_!

### Part F
### Record

Document all the prototypes and iterations you have designed and worked on! Again, deliverables for this lab are writings, sketches, photos, and videos that show what your prototype:
* "Looks like": shows how the device should look, feel, sit, weigh, etc.
* "Works like": shows what the device can do
* "Acts like": shows how a person would interact with the device

