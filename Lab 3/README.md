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
As Joseph mentioned it would be convenient to be able to edit the notes afterwards. This could be implemented through the webpage I intended to display the notes in. Another interaction possible is touch. Ideally, the interaction is voice instantiated but that might not always work - e.g. in a loud place. Hence, the device could include a button to initialise communication (different methods on pressing button could also have meaning - e.g. double tap to delete previous note).

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

#### Prototype design

To prototype the earpeace design I taped the button to initialize voice commands to an AirPod. I then used the longest cable I found to connect the button to the raspberry pi to minimise the effect the computer had on the user's experience. The device would ideally only be the earpeace and hence I tried to prototype it in similar fashion.

<img width="543" alt="image" src="https://user-images.githubusercontent.com/42963791/137237140-61bbf947-427c-4573-82a2-f9531a526121.png">


### Prototype video
https://youtu.be/x8XFX6MnAkI

When the system is turned on (when the script butto.py is run) the device waits for the user to press the button. The user can press the button to give the device voice commads. After listening to the user's input the device uploads the task to a online dashboard. The device then offers further assistance whch the user can deny or accept (only available to deny in prototype).

All the code for the prototype is available in the folder Lab 3/prototype. The file butto.py simple waits for a button press, when the button is pressed it runs a script that takes care of all voice commads. That said script then sends the results to the online dashboard by running server.py.

## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)


#### User test 1
https://youtu.be/dvVkK6DXvOU

The first user test with the prototype was relatively successful. I told this user that there were only certain words which the device recognises. He was happy with the design (earpeace) and had little trouble interacting with the device. However, after the video the user asked if he could only list one task to the dashboard durinig each run. When I told him that was the casse he mentioned that this was a big issue for the usability. After hearing this feed back, I decided to improve the prototype for the next iterview. 

In the new version, the device listens to user commands until he denies further assistance. Only then it posts the commands to the online dashboard. This way, users can create multiple tasks at once. 

#### User test 2
https://youtu.be/HUyZQz6qpi8

The later user test was on the improved prototype. This time,  dd not tell the user that the vocabulary which the device understands is limited. The user's communitcation with the device was relatively smooth apart from one problem. In the new prototype, the user has to say "no" to the device when asked for further input. Then, the device stops taking voice commands and uploads them to the dashboard. However, the device did not recognize the word "no" until after a few rounds. This was confusing for the user as the device kept prompting him for more input no matter what he did. To fix this I am adding more words that indicate denial and I will also interpretet onkwon inout as "no" (the user can always press the button again if he wanted to list more tasks). The user liked these suggestionis of improvements.

In general though, the user was impressed that the device recognised some of his tasks and displayed them on a dashboard he could access on his own phone (even though the vocabulary was limited he used some of the registered words, e.g 'homework').

#### Improved prototype video
https://youtu.be/aNKH_dKQFMA

In he new prototype the device allows the user to list multiple ttasks in one go. This time, it stops recording tasks if it does not recognise the user's command instead of going on forever until he says "no". (In the video video the devce does not list all tasks exactly as I told iit to, this is because of the limis of the speechtotext library of the prototype.)

### What worked well about the system and what didn't?

As discussed here above the users found thee device easy to understand and use. They also enjoyed seeing the results on their own devices. The main issues were related to listing multiple tasks in one go. However, that process greatly improved throoughout the developement process as explained above.

### What worked well about the controller and what didn't?

The users found the button easy to understand. They liked being able to control the device by voce commands. On the other hand, the voice controller was the part that caused tthe most trouble. The device sometimes had trouble understanding what the users said and the limited vocabulary was hindering. Overall, the controllers' was acceptable and I was able to prototype a relatively realistic prototype with them. For the device to becomereally usable though, the quality of the voice controller must be improved.

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?

As discussed above the device had some trouble allowing users to lst many tasks in a row. After the WoZ interactions I believe the device has improved, but fort it to become autonomous I would have to master this process. That is, the users could promt the device at any time and list as may tasks as they desire.


### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

I could storre the words/tasks that different users say. Then I can analyze which ones are more common and others to improve the device's ability to listen to tasks. It could favour popular words over others when there is noise in input. Other sensing modalities the device could capture are e.g. movement and locatiion. When the person is at the grocery store the device could f.x. remind them of their shopping list.

