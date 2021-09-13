

# Staging Interaction

In the original stage production of Peter Pan, Tinker Bell was represented by a darting light created by a small handheld mirror off-stage, reflecting a little circle of light from a powerful lamp. Tinkerbell communicates her presence through this light to the other characters. See more info [here](https://en.wikipedia.org/wiki/Tinker_Bell). 

There is no actor that plays Tinkerbell--her existence in the play comes from the interactions that the other characters have with her.

For lab this week, we draw on this and other inspirations from theatre to stage interactions with a device where the main mode of display/output for the interactive device you are designing is lighting. You will plot the interaction with a storyboard, and use your computer and a smartphone to experiment with what the interactions will look and feel like. 

_Make sure you read all the instructions and understand the whole of the laboratory activity before starting!_



## Prep

### To start the semester, you will need:
1. Set up your own Github "Lab Hub" repository to keep all you work in record by [following these instructions](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md).
2. Set up the README.md for your Hub repository (for instance, so that it has your name and points to your own Lab 1) and [learn how to](https://guides.github.com/features/mastering-markdown/) organize and post links to your submissions on your README.md so we can find them easily.
3. (extra: Learn about what exactly Git is from [here](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F).)

### For this lab, you will need:
1. Paper
2. Markers/ Pens
3. Scissors
4. Smart Phone -- The main required feature is that the phone needs to have a browser and display a webpage.
5. Computer -- We will use your computer to host a webpage which also features controls.
6. Found objects and materials -- You will have to costume your phone so that it looks like some other devices. These materials can include doll clothes, a paper lantern, a bottle, human clothes, a pillow case, etc. Be creative!

### Deliverables for this lab are: 
1. Storyboard
1. Sketches/photos of costumed device
1. Any reflections you have on the process
1. Video sketch of the prototyped interaction
1. Submit the items above in the lab1 folder of your class [Github page], either as links or uploaded files. Each group member should post their own copy of the work to their own Lab Hub, even if some of the work is the same from each person in the group.

### The Report
This README.md page in your own repository should be edited to include the work you have done (the deliverables mentioned above). Following the format below, you can delete everything but the headers and the sections between the **stars**. Write the answers to the questions under the starred sentences. Include any material that explains what you did in this lab hub folder, and link it in your README.md for the lab.

## Lab Overview
For this assignment, you are going to:

A) [Plan](#part-a-plan) 

B) [Act out the interaction](#part-b-act-out-the-interaction) 

C) [Prototype the device](#part-c-prototype-the-device)

D) [Wizard the device](#part-d-wizard-the-device) 

E) [Costume the device](#part-e-costume-the-device)

F) [Record the interaction](#part-f-record)

Labs are due on Mondays. Make sure this page is linked to on your main class hub page.

## Part A. Plan 

To stage the interaction with your interactive device, think about:

_Setting:_ This interaction takes place wherever a person mines crypocurrency, at an office, by a home computer, at a place full of coomputers deticated for mining, etc. The player can also choose to display the notification where he is most likely to notice it and than he can act appropriately when needed.

_Players:_ The individuals that interact with this gadget are people than mine cryptocurrencies, wheather they do it y themselves at home or professionally at a mining center.

_Activity:_ The activity is individuals mining cryptocurrenciies.

_Goals:_ Cryptocurrency miners receive currency as a reward for completing "blocks" of verified transactions, which are added to the blockchain. Mining rewards are paid to the miner who discovers a solution to a complex hashing puzzle first, and the probability that a participant will be the one to discover the solution is related to the portion of the total mining power on the network. The goal of the the players is to mine as many coins as possible. The gadget will notify the players of the status of their mining computers/algorithms. If the computer starts receiving unusually many invalid shares the light becomes more red and the player should take action, perhaps restart the system because. If it is green there is n action needed. If he is notified when the system breaks he can react quickly which reduces energy and computing power waste.


### The storyboard:

<img width="785" alt="image" src="https://user-images.githubusercontent.com/42963791/132271811-9caad968-d086-4ed9-a147-5b82faa66c22.png">

### Presenting the idea to the other people in the breakout room

Originally the idea was just to display a red light when an invalid share appears. After discussing it in a group the idea evolved. The people pointed out that theindicator should display different shades of red and green for the average of the past few shares, then one failure is not dramatic but if many fail in a row the warning becomes more aggressive.

## Part B. Act out the Interaction

Try physically acting out the interaction you planned. For now, you can just pretend the device is doing the things you’ve scripted for it. 

### Are there things that seemed better on paper than acted out?
The light looked more noticable on paper than in reality. There are are a lot of lights aroound the desk,  from the monitor, keyboard, computter itself, etc.

### Are there new ideas that occur to you or your collaborators that come up from the acting?
After discovering this we changed the placement of the light to be in a more noticable part of the room, e.g. the cieling or on the wall.


## Part C. Prototype the device

You will be using your smartphone as a stand-in for the device you are prototyping. You will use the browser of your smart phone to act as a “light” and use a remote control interface to remotely change the light on that device. 

Code for the "Tinkerbelle" tool, and instructions for setting up the server and your phone are [here](https://github.com/FAR-Lab/tinkerbelle).

We invented this tool for this lab! 

If you run into technical issues with this tool, you can also use a light switch, dimmer, etc. that you can can manually or remotely control.

### Feedback on Tinkerbelle
I had some issues starting Tinkerbelle at first, but we got it working on my computer. After we got it gooing it worked quite smoothly and it proved to be a nice tool for prototyping.


## Part D. Wizard the device

Setting up Tinkerbelle

https://youtu.be/eSSHQjrBd6M

To mimic a miner software we wrote a simple script in Python, miner.py in the lab folder.

We then ran that script in the terminal and manually representaed the status of the miner on the device by using Tinkerbelle.


## Part E. Costume the device

Only now should you start worrying about what the device should look like. Develop a costume so that you can use your phone as this device.

Think about the setting of the device: is the environment a place where the device could overheat? Is water a danger? Does it need to have bright colors in an emergency setting?

### sketches of how the device might look like

<img width="976" alt="image" src="https://user-images.githubusercontent.com/42963791/132271856-0e9e3ae7-6b76-4a5c-82eb-877779668ede.png">

### Prototype final design:

<img width="537" alt="image" src="https://user-images.githubusercontent.com/42963791/132271978-dcd0c188-49c7-492c-87b3-fa875f3b4784.png">


\*\***What concerns or opportunitities are influencing the way you've designed the device to look?**\*\*


## Part F. Record

### A video of the prototype:

https://youtu.be/jeE3tEhL88A

### Collaboration
I worked with Donal, dml333, on this assignment.



# Staging Interaction, Part 2 

This describes the second week's work for this lab activity.


## Prep (to be done before Lab on Wednesday)

### Feedback form classmates

I only got one comooment on Canvas. There it was suggested that we added a warning light to indicate when the software starts to compute wrong hashes. That mechanism was already inicluded in the device but it was probably not clear in the video. The light was supposed to go gradually from green to red as more wrong hashes are caalculated. It seems the orange and yellow lights fail to indicate the warning that something is beginning to go wrong.

As I only recieved one comment on Caanvas I asked the students at my table in the lab. They felt that the video was not clear, the light wasn't visible enough, the backround was too distracting and the actor doesn't show enough interaction wth the device.

I feel that those are valuable observations and I will try to improve them in the next round by improving the warning sign and focusing more on the device in the video. After the comments I feel the green light is distracting, mot of the time the software is up and running smoothly so the light should just be off at that time. When the software begins to compute wrong hashes and orange light will blink. If too many wrong hashes occur in a row red and blue light will alternate adn an alarm will sound. 

## Make it your own

In the new protootype the device displays neutral (white) light when the miner is working as intended. When the system begins to behave somewhat incorrectly the device flashes a yellow/orange light to indicate some minor error that should be observed. If the system then starts to experience more severe failure the device flashes a red warning light and plays an alarming sound. These changes were made after considering the comments we got. The green light of the old prototype was too prominent and the user did not notice the change to the yellow light that was supposed to warn about small failure. By having a natural light and flashing the orange light we feel the warning is much more clear and the user will be more likely to notice it and interviene before complete failure. The flashing red light and alarm are moreover far more noticable than the constant red light of the old device. 
We also tried to improve the video quality because of the comment we got. We tried to express the purpose of the device more clearly splitting the sceen, showing the miner status separately, and displaying text to explain some scenarios of the video.

### The storyboard:

<img width="866" alt="image" src="https://user-images.githubusercontent.com/42963791/133124487-98a5c077-ef24-4d72-a041-5ca352a11e12.png">

### A video of the improved prototype:
https://www.youtube.com/watch?v=96IsJhStaT4
