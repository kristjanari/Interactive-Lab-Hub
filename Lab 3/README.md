# Chatterboxes
[![Watch the video](https://user-images.githubusercontent.com/1128669/135009222-111fe522-e6ba-46ad-b6dc-d1633d21129c.png)](https://www.youtube.com/embed/Q8FWzLMobx0?start=19)

In this lab, we want you to design interaction with a speech-enabled device--something that listens and talks to you. This device can do anything *but* control lights (since we already did that in Lab 1).  First, we want you first to storyboard what you imagine the conversational interaction to be like. Then, you will use wizarding techniques to elicit examples of what people might say, ask, or respond.  We then want you to use the examples collected from at least two other people to inform the redesign of the device.

We will focus on **audio** as the main modality for interaction to start; these general techniques can be extended to **video**, **haptics** or other interactive mechanisms in the second part of the Lab.

## Prep for Part 1: Get the Latest Content and Pick up Additional Parts - Complete

## Part 1.
### Text to Speech 

The file kristjan.sh makes the PI say my name.

### Speech to Text

The file speech.sh (in speechtotext folder) asks the user for his phone number. Then the program reads the phone number back to the user and asks for confirmation and reacts appropriately.



### Serving Pages

In Lab 1, we served a webpage with flask. In this lab, you may find it useful to serve a webpage for the controller on a remote device. Here is a simple example of a webserver.

```
pi@ixe00:~/Interactive-Lab-Hub/Lab 3 $ python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 162-573-883
```
From a remote browser on the same network, check to make sure your webserver is working by going to `http://<YourPiIPAddress>:5000`. You should be able to see "Hello World" on the webpage.

### Storyboard

Storyboard and/or use a Verplank diagram to design a speech-enabled device. (Stuck? Make a device that talks for dogs. If that is too stupid, find an application that is better than that.) 

\*\***Post your storyboard and diagram here.**\*\*

<img width="794" alt="image" src="https://user-images.githubusercontent.com/42963791/135949191-1d223489-d38d-44e8-8cdb-e6be72282ca1.png">

<img width="795" alt="image" src="https://user-images.githubusercontent.com/42963791/135950143-3d49ac96-ecd4-40bf-a315-31f50c1e15b9.png">


I tried to think of things that hve annoyed me in my daily life for the past few weeks. The first thing that came to mind is that I have forgotten to buy groceries for over a week, I just remember it when I open the fridge. I thought it would be helpful if I could tell a device every time I get an idea/think of a task that need to be observed later. The ideas/tasks would be displayed on a website and hence the task list can be shared. If I tell the device I need to buy milk, my roommate can see it and buy milk if he's on the way to the store. Speaking to the device is natural/effortless for the user and by deploying straight to an line dashboard the list can be shared with multiple users.


### Acting out the dialogue


Video of the interaction

https://youtu.be/F6JDfjIexfM

Before I acted out the dialog I did not see the need for an audio feedback from the device. After watching it however, I realise that the user is unaware if the note was successful if the device is silent. Hence, I'm going to add audio feedback to the dialog in the next part.

### Wizarding with the Pi (optional)
In the [demo directory](./demo), you will find an example Wizard of Oz project. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser.  You may use this demo code as a template. By running the `app.py` script, you can see how audio and sensor data (Adafruit MPU-6050 6-DoF Accel and Gyro Sensor) is streamed from the Pi to a wizard controller that runs in the browser `http://<YouPiIPAddress>:5000`. You can control what the system says from the controller as well!

\*\***Describe if the dialogue seemed different than what you imagined, or when acted out, when it was wizarded, and how.**\*\*

# Lab 3 Part 2

For Part 2, you will redesign the interaction with the speech-enabled device using the data collected, as well as feedback from part 1.

## Prep for Part 2

### 1. What are concrete things that could use improvement in the design of your device? For example: wording, timing, anticipation of misunderstandings...

#### I received two comments on Canvas:

Joseph Cera:

I love that you can now edit your notes as if you typed them, so you can make correctionis or otherwise. Onne thing I'd love to see is note bot putting reminders directly in your calendar if you provided a deadline. Grat job!
 
Angelca Kosasih:

Hey Kristjan! Good call on starting with problems you face in your everyday when ideating.

I wish there was more back and forth between the device and the user. For example, when the user asks for more eggs, it could ask the user when they need it by, when it should remind the user, let the user know of other items that they might need to buy soon as well, etc.

I am also curious to know what form factor the device will be in? Will this be linked to one's siri/alexa/etc.

I agree on using sound as a primary interactiionin technique to signal to the user the state of the device. Of course, though I wish there were more diaalouge, you may choose to build one that listens but minimally speaks. I think this opes up a lot of design challenges that you could explore!
 
#### Summary of feedback
I was happy to receive such detailed comments. I notice that the commennts from Angelica suggest similar changes as I had considered after watching the video: to incease the feedback from the device - make it more interactive. As ths problem has been pointed out by myself and other people now, it will be my priority to improve the interaction between the user and the device for the second part. 
 
Moreover, it was interesting to hear from Joseph that he liked that the notes were displayed in a format as if the user typed them in so they werte easily editable. This was not intentionnal, I simply used Google drive to wizard the device because the documents are updated live and I could control the text from another computer. However, this is a nice observation and I will try to keep this format and make sure the notes are easily editable.

For Angelica's comments about the form of the device I had a short discussion with the people at my table in the lab. We came to the coclusiion the most convenient costume would be a small earpiece. The devce is then always in reach.

### 2. What are other modes of interaction _beyond speech_ that you might also use to clarify how to interact?
As Joseph mentioned it would be convenient to be able to edit the notes afterwards. This could be implemented through the webpage I intended to display the notes in. Aother interaction possible is touch. Ideally, the interaction is voice instantiated but that might not always work - e.g. in a loud place. Hence, the device could include a button to initialise commuication (different methods on pressing butto could also have meaning - e.g. double tap to delete previous note).

### 3. Make a new storyboard, diagram and/or script based on these reflections.

<img width="794" alt="image" src="https://user-images.githubusercontent.com/42963791/136639406-7a561a86-d28a-4d44-b20e-176e60239856.png">

In the new and imprroved device the communication is more interactive. The device answers the user ad suggests more actions instead of just being silent as before. As explained in the storyboard the feedback from the device is not only to cofirm that the message was received, the device also suggests more actions which leads to the user comig up with a new task. I the final scene, the user is completing the laundry task at the set time and his roommate arrives with the laundry detergent he saw at the shared shopping list.

## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*

*Include videos or screencaptures of both the system and the controller.*

### Prototype video
https://youtu.be/x8XFX6MnAkI

When the system is tured on (when the script butto.py is run) the device waits for the user to press the button. The user can press the button to give the device voice commads. After listening to the user's input the device uploads the task to a online dashboard. The device then offers further assistance whch the user can deny or accept (oly available to dey in prototype).

All the code for the prototype is available in the folder Lab 3/prototype. The file butto.py simple waits for a button press, whe the butto. is pressed it runs a script that takes care of all voice commads. That said script then sends the results to the online dashboard by running server.py.

## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

Answer the following:

### What worked well about the system and what didn't?
\*\**your answer here*\*\*

### What worked well about the controller and what didn't?

\*\**your answer here*\*\*

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?

\*\**your answer here*\*\*


### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

\*\**your answer here*\*\*

