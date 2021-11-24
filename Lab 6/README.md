# Little Interactions Everywhere

## Prep

1. Pull the new changes from the class interactive-lab-hub. (You should be familiar with this already!)
2. Install [MQTT Explorer](http://mqtt-explorer.com/) on your laptop.
3. Readings before class:
   * [MQTT](#MQTT)
   * [The Presence Table](https://dl.acm.org/doi/10.1145/1935701.1935800) and [video](https://vimeo.com/15932020)


## Overview

The point of this lab is to introduce you to distributed interaction. We have included some Natural Language Processing (NLP) and Generation (NLG) but those are not really the emphasis. Feel free to dig into the examples and play around the code which you can integrate into your projects if wanted. However, we want to emphasize that the grading will focus on your ability to develop interesting uses for messaging across distributed devices. Here are the four sections of the lab activity:

A) [MQTT](#part-a)

B) [Send and Receive on your Pi](#part-b)

C) [Streaming a Sensor](#part-c)

D) [The One True ColorNet](#part-d)

E) [Make It Your Own](#part-)

## Part 1.

### Part A
### MQTT

MQTT is a lightweight messaging portal invented in 1999 for low bandwidth networks. It was later adopted as a defacto standard for a variety of [Internet of Things (IoT)](https://en.wikipedia.org/wiki/Internet_of_things) devices. 

#### The Bits

* **Broker** - The central server node that receives all messages and sends them out to the interested clients. Our broker is hosted on the far lab server (Thanks David!) at `farlab.infosci.cornell.edu/8883`. Imagine that the Broker is the messaging center!
* **Client** - A device that subscribes or publishes information to/on the network.
* **Topic** - The location data gets published to. These are *hierarchical with subtopics*. For example, If you were making a network of IoT smart bulbs this might look like `home/livingroom/sidelamp/light_status` and `home/livingroom/sidelamp/voltage`. With this setup, the info/updates of the sidelamp's `light_status` and `voltage` will be store in the subtopics. Because we use this broker for a variety of projects you have access to read, write and create subtopics of `IDD`. This means `IDD/ilan/is/a/goof` is a valid topic you can send data messages to.
*  **Subscribe** - This is a way of telling the client to pay attention to messages the broker sends out on the topic. You can subscribe to a specific topic or subtopics. You can also unsubscribe. Following the previouse example of home IoT smart bulbs, subscribing to `home/livingroom/sidelamp/#` would give you message updates to both the light_status and the voltage.
* **Publish** - This is a way of sending messages to a topic. Again, with the previouse example, you can set up your IoT smart bulbs to publish info/updates to the topic or subtopic. Also, note that you can publish to topics you do not subscribe to. 


**Important note:** With the broker we set up for the class, you are limited to subtopics of `IDD`. That is, to publish or subcribe, the topics will start with `IDD/`. Also, setting up a broker is not much work, but for the purposes of this class, you should all use the broker we have set up for you!


#### Useful Tooling

Debugging and visualizing what's happening on your MQTT broker can be helpful. We like [MQTT Explorer](http://mqtt-explorer.com/). You can connect by putting in the settings from the image below.


![input settings](imgs/mqtt_explorer.png?raw=true)


Once connected, you should be able to see all the messages under the IDD topic. , go to the **Publish** tab and try publish something! From the interface you can send and plot messages as well. Remember, you are limited to subtopics of `IDD`. That is, to publish or subcribe, the topics will start with `IDD/`.

![publish settings](imgs/mqtt_explorer_2.png?raw=true)

### Setting up MQTT

<img width="1430" alt="image" src="https://user-images.githubusercontent.com/42963791/141323636-3e119ce9-f26e-48ef-a0e6-11b66ad6af05.png">



### Part B
### Send and Receive on your Pi

[sender.py](./sender.py) and and [reader.py](./reader.py) show you the basics of using the mqtt in python. Let's spend a few minutes running these and seeing how messages are transferred and shown up. Before working on your Pi, keep the connection of `farlab.infosci.cornell.edu/8883` with MQTT Explorer running on your laptop.

**Running Examples on Pi**

* Install the packages from `requirements.txt` under a virtual environment, we will continue to use the `circuitpython` environment we setup earlier this semester:
  ```
  pi@ixe00:~ $ source circuitpython/bin/activate
  (circuitpython) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 6
  (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ pip install -r requirements.txt
  ```
* Run `sender.py`, fill in a topic name (should start with `IDD/`), then start sending messages. You should be able to see them on MQTT Explorer.
  ```
  (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ python sender.py
  pi@ReiIDDPi:~/Interactive-Lab-Hub/Lab 6 $ python sender.py
  >> topic: IDD/ReiTesting
  now writing to topic IDD/ReiTesting
  type new-topic to swich topics
  >> message: testtesttest
  ...
  ```
* Run `reader.py`, and you should see any messages being published to `IDD/` subtopics.
  ```
  (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ python reader.py
  ...
  ```
  ### Using the sender
  
  <img width="553" alt="image" src="https://user-images.githubusercontent.com/42963791/141324866-55a87f5f-a51c-435b-8b74-6846e9e07174.png">

  <img width="853" alt="image" src="https://user-images.githubusercontent.com/42963791/141324849-cded8773-9294-4e45-b85c-8daaa6711e51.png">

### Using the reader

<img width="622" alt="image" src="https://user-images.githubusercontent.com/42963791/141325096-00969ae3-9bca-4eaf-b7d7-eff8c3addf98.png">

**\*\*\*Consider how you might use this messaging system on interactive devices, and draw/write down 5 ideas here.\*\*\***

#### Robotic Surveillace Camera

<img width="698" alt="image" src="https://user-images.githubusercontent.com/42963791/141418244-da805020-f764-448e-9d63-36189d8c0618.png">

A security gueard can rotate the camera from distace to focus on different parts of the property he is resposible for. 

### Remote Gate Controller

<img width="758" alt="RemoteGateController" src="https://user-images.githubusercontent.com/52221419/141924952-48acb9fd-1b14-4632-ae7e-4d431bab135d.png">

With the remote gate controller, guests will be detected by a distance/proximity sensor notifying the security guard far away. Then, the guard can speak to the guest and ask for identification through a microphone, and the guest can speak through a microphone back with this information. If the information is valid and they deserve access, then the guard can unlock the gate by using the sirvo motor on the gate's computer.

### Fruit Vendor Polling

<img width="753" alt="FruitPoller" src="https://user-images.githubusercontent.com/52221419/141924977-0a4467be-5cc7-4c95-8c29-2b499d49c8bd.png">

Here, there is a polling station in public that allows potential customers to a fruit store select their favorite fruit. Then, at the fruit store's warehouse, the fruit vendor employee can observe how much each fruit is getting chosen. They can use this informatin to stock their store accordingly. 

### Bathroom Help Button

<img width="747" alt="BathroomHelpButton" src="https://user-images.githubusercontent.com/52221419/141925003-6dab9d41-9428-482f-9612-2562b604b12a.png">

The bathrooom help button is a button in the bathrm that allows people to call for help. They press the button and can ask for things or help if they have gotten hurt. It will stream to another raspberry pi in perhaps the main office or reception that broadcasts a message for help. 

### Parking Spot Detector

<img width="744" alt="ParkingSpotDetector" src="https://user-images.githubusercontent.com/52221419/141925023-058d1006-bdc8-4fe0-a6df-73ee98f9bb51.png">

The parking spot detector is a computer at a given parking spot that uses a distance/proximity sensor to detect if a car is in the parking spot. Then, it realys this information to the apartment of the owner of the parking spot and informs them if the car is at the spot or not. This way, the apartment owner can know if their car is in the spot or not. This could be useful if they have multiple roomates and share the car and live many floors away from the car, they can check if it is there without going down to the spot or calling their roomates who could potentially be driving and cannot answer the phone. 

### Part C
### Streaming a Sensor

We have included an updated example from [lab 4](https://github.com/FAR-Lab/Interactive-Lab-Hub/tree/Fall2021/Lab%204) that streams the [capacitor sensor](https://learn.adafruit.com/adafruit-mpr121-gator) inputs over MQTT. We will also be running this example under `circuitpython` virtual environment.

Plug in the capacitive sensor board with the Qwiic connector. Use the alligator clips to connect a Twizzler (or any other things you used back in Lab 4) and run the example script:

<p float="left">
<img src="https://cdn-learn.adafruit.com/assets/assets/000/082/842/large1024/adafruit_products_4393_iso_ORIG_2019_10.jpg" height="150" />
<img src="https://cdn-shop.adafruit.com/970x728/4210-02.jpg" height="150">
<img src="https://cdn-learn.adafruit.com/guides/cropped_images/000/003/226/medium640/MPR121_top_angle.jpg?1609282424" height="150"/>
<img src="https://media.discordapp.net/attachments/679721816318803975/823299613812719666/PXL_20210321_205742253.jpg" height="150">
</p>

 ```
 (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ python distributed_twizzlers_sender.py
 ...
 ```

**\*\*\*Include a picture of your setup here: what did you see on MQTT Explorer?\*\*\***

Here is a [video of using our capacative sensor](https://youtu.be/ckndrSJwUqY) to stream data to the MQTT server. As you can see, we are connected to positions 0 and 5 on the capacative sensor, and our thread within MQTT is called `coolteam`. You can see our twizzler contact messages being displayed after touching the cables connected to 0 and 5. 

![IMG_5750](https://user-images.githubusercontent.com/52221419/141361515-b2912b51-31fe-4c2d-847b-aaa792b128c4.PNG)

**\*\*\*Pick another part in your kit and try to implement the data streaming with it.\*\*\***

We tried to implement data streaming with the joystick. This was not too difficult, and we were able to figure it out fairly quickly. Here is a [video demonstrating our implementation](https://youtu.be/WeErTX74Y4Y). Similar to above, our thread within MQTT is called `coolteam` and once we move the joystick, the joystick values are streamed to MQTT. 

Here is a picture showing the interaction as well.  

<img width="1515" alt="Screen Shot 2021-11-11 at 3 05 12 PM" src="https://user-images.githubusercontent.com/52221419/141361774-e9c47aa5-f5bb-4515-b7ec-b98c3e18f1fb.png">

### Part D
### The One True ColorNet

It is with great fortitude and resilience that we shall worship at the altar of the *OneColor*. Through unity of the collective RGB, we too can find unity in our heart, minds and souls. With the help of machines, we can overthrow the bourgeoisie, get on the same wavelength (this was also a color pun) and establish [Fully Automated Luxury Communism](https://en.wikipedia.org/wiki/Fully_Automated_Luxury_Communism).

The first step on the path to *collective* enlightenment, plug the [APDS-9960 Proximity, Light, RGB, and Gesture Sensor](https://www.adafruit.com/product/3595) into the [MiniPiTFT Display](https://www.adafruit.com/product/4393). You are almost there!

<p float="left">
  <img src="https://cdn-learn.adafruit.com/assets/assets/000/082/842/large1024/adafruit_products_4393_iso_ORIG_2019_10.jpg" height="150" />
  <img src="https://cdn-shop.adafruit.com/970x728/4210-02.jpg" height="150">
  <img src="https://cdn-shop.adafruit.com/970x728/3595-03.jpg" height="150">
</p>


The second step to achieving our great enlightenment is to run `color.py`. We have talked about this sensor back in Lab 2 and Lab 4, this script is similar to what you have done before! Remember to ativate the `circuitpython` virtual environment you have been using during this semester before running the script:

 ```
 (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ python color.py
 ...
 ```

By running the script, wou will find the two squares on the display. Half is showing an approximation of the output from the color sensor. The other half is up to the collective. Press the top button to share your color with the class. Your color is now our color, our color is now your color. We are one.

(A message from the previous TA, Ilan: I was not super careful with handling the loop so you may need to press more than once if the timing isn't quite right. Also, I haven't load-tested it so things might just immediately break when everyone pushes the button at once.)

You may ask "but what if I missed class?" Am I not admitted into the collective enlightenment of the *OneColor*?

Of course not! You can go to [https://one-true-colornet.glitch.me/](https://one-true-colornet.glitch.me/) and become one with the ColorNet on the inter-webs. Glitch is a great tool for prototyping sites, interfaces and web-apps that's worth taking some time to get familiar with if you have a chance. Its not super pertinent for the class but good to know either way. 

**\*\*\*Can you set up the script that can read the color anyone else publish and display it on your screen?\*\*\***

### Interacting with the color sensor

I'm wearing a purple sweater in the video, when I aimed the color sensor at it and pressed the button the color of the screen changed and the value on the MQTT server was updated.

https://youtu.be/tL7v_wAlsx4

<img width="549" alt="image" src="https://user-images.githubusercontent.com/42963791/141327669-3f6fad30-b9d2-4b2f-ad92-933544885d5b.png">

### Part E
### Make it your own

Find at least one class (more are okay) partner, and design a distributed application together based on the exercise we asked you to do in this lab.

**\*\*\*1. Explain your design\*\*\*** For example, if you made a remote controlled banana piano, explain why anyone would want such a thing.

To make this lab our own, we decided to implement the fruit polling system mentioned above. This would be wanted by fruit vendors (or really any store that wants to figure out what products to stock, here we chose fruits and a fruit store) so that they can choose the ideal quantity of fruit to stock the next day. They wouldn't even have to leave their store or office! This would similarly be wanted by potential customers in public so that they can ensure that the products they desire are in stock the next day at the store. A storyboard describing this situation is shown below. 

<img width="766" alt="FruitPollStoryboard" src="https://user-images.githubusercontent.com/52221419/141923695-61be63f9-381e-4169-9305-088fca3930f3.png">

**\*\*\*2. Diagram the architecture of the system.\*\*\*** Be clear to document where input, output and computation occur, and label all parts and connections. For example, where is the banana, who is the banana player, where does the sound get played, and who is listening to the banana music?

The below diagram discusses the architecture of the system and how it works. Essentially, potential customers tap which fruit they want, at which point the raspberry pi stationed in the public will dictate that their vote has been confirmed. Then, the public raspberry pi will relay the information through the MQTT server to the private raspberry pi in the fruit vendors office. Then, the private raspberry pi will print out the total vote quantities for each fruit, and the fruit vendor employee can observe these values and update their stock for the coming days accordingly. 

<img width="606" alt="FruitPollDiagram" src="https://user-images.githubusercontent.com/52221419/141923711-a4ef177e-d6b2-4300-a0c1-e1d1fd8c1039.png">

**\*\*\*3. Build a working prototype of the system.\*\*\*** Do think about the user interface: if someone encountered these bananas somewhere in the wild, would they know how to interact with them? Should they know what to expect?

Yes! As you can see below, it is very simple to interact with the user interface. There is only one instruction, which is to touch your favorite food. It even offers audio confirmation to let the potential customer know that they have submitted their answer - at least from this end. the only faulty part that we realized after testing is that they can vote as many times as they want. The potential customer will not need to expect anything, as they are simply picking their favorite fruit. They may be a little confused exactly what it is for, except that it is for the "fruit store."

<img width="264" alt="PublicEncounter" src="https://user-images.githubusercontent.com/52221419/141923767-a5140314-895a-449d-969e-05a37a8ae007.png">

**\*\*\*4. Document the working prototype in use.\*\*\*** It may be helpful to record a Zoom session where you should the input in one location clearly causing response in another location.

Here is a [video documenting out prototype](https://youtu.be/tSC4AZRU4TU). It features a zoom of the POV from each party member - the potential customer in public, and the fruit vendor employee in the fruit vendor office. The office worker can observe the items getting added to the polled list and be ready for the next day, and the potential customer can easily add fruit items to the poll. 

<!--**\*\*\*5. BONUS (Wendy didn't approve this so you should probably ignore it)\*\*\*** get the whole class to run your code and make your distributed system BIGGER.-->

