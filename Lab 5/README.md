# Observant Systems


For lab this week, we focus on creating interactive systems that can detect and respond to events or stimuli in the environment of the Pi, like the Boat Detector we mentioned in lecture. 
Your **observant device** could, for example, count items, find objects, recognize an event or continuously monitor a room.

This lab will help you think through the design of observant systems, particularly corner cases that the algorithms needs to be aware of.

## Prep

1.  Pull the new Github Repo.
2.  Install VNC on your laptop if you have not yet done so. This lab will actually require you to run script on your Pi through VNC so that you can see the video stream. Please refer to the [prep for Lab 2](https://github.com/FAR-Lab/Interactive-Lab-Hub/blob/Fall2021/Lab%202/prep.md), we offered the instruction at the bottom.
3.  Read about [OpenCV](https://opencv.org/about/), [MediaPipe](https://mediapipe.dev/), and [TeachableMachines](https://teachablemachine.withgoogle.com/).
4.  Read Belloti, et al.'s [Making Sense of Sensing Systems: Five Questions for Designers and Researchers](https://www.cc.gatech.edu/~keith/pubs/chi2002-sensing.pdf).

### For the lab, you will need:

1. Raspberry Pi
1. Webcam 
1. Microphone (if you want to have speech or sound input for your design)

### Deliverables for this lab are:
1. Show pictures, videos of the "sense-making" algorithms you tried.
1. Show a video of how you embed one of these algorithms into your observant system.
1. Test, characterize your interactive device. Show faults in the detection and how the system handled it.

## Overview
Building upon the paper-airplane metaphor (we're understanding the material of machine learning for design), here are the four sections of the lab activity:

A) [Play](#part-a)

B) [Fold](#part-b)

C) [Flight test](#part-c)

D) [Reflect](#part-d)

---

### Part A
### Play with different sense-making algorithms.

#### OpenCV
A more traditional method to extract information out of images is provided with OpenCV. The RPI image provided to you comes with an optimized installation that can be accessed through python. We included 4 standard OpenCV examples: contour(blob) detection, face detection with the ``Haarcascade``, flow detection (a type of keypoint tracking), and standard object detection with the [Yolo](https://pjreddie.com/darknet/yolo/) darknet.

Most examples can be run with a screen (e.g. VNC or ssh -X or with an HDMI monitor), or with just the terminal. The examples are separated out into different folders. Each folder contains a ```HowToUse.md``` file, which explains how to run the python example. 

Following is a nicer way you can run and see the flow of the `openCV-examples` we have included in your Pi. Instead of `ls`, the command we will be using here is `tree`. [Tree](http://mama.indstate.edu/users/ice/tree/) is a recursive directory colored listing command that produces a depth indented listing of files. Install `tree` first and `cd` to the `openCV-examples` folder and run the command:

```shell
pi@ixe00:~ $ sudo apt install tree
...
pi@ixe00:~ $ cd openCV-examples
pi@ixe00:~/openCV-examples $ tree -l
.
├── contours-detection
│   ├── contours.py
│   └── HowToUse.md
├── data
│   ├── slow_traffic_small.mp4
│   └── test.jpg
├── face-detection
│   ├── face-detection.py
│   ├── faces_detected.jpg
│   ├── haarcascade_eye_tree_eyeglasses.xml
│   ├── haarcascade_eye.xml
│   ├── haarcascade_frontalface_alt.xml
│   ├── haarcascade_frontalface_default.xml
│   └── HowToUse.md
├── flow-detection
│   ├── flow.png
│   ├── HowToUse.md
│   └── optical_flow.py
└── object-detection
    ├── detected_out.jpg
    ├── detect.py
    ├── frozen_inference_graph.pb
    ├── HowToUse.md
    └── ssd_mobilenet_v2_coco_2018_03_29.pbtxt
```

The flow detection might seem random, but consider [this recent research](https://cseweb.ucsd.edu/~lriek/papers/taylor-icra-2021.pdf) that uses optical flow to determine busy-ness in hospital settings to facilitate robot navigation. Note the velocity parameter on page 3 and the mentions of optical flow.

Now, connect your webcam to your Pi and use **VNC to access to your Pi** and open the terminal. Use the following command lines to try each of the examples we provided:
(***it will not work if you use ssh from your laptop***)

```
pi@ixe00:~$ cd ~/openCV-examples/contours-detection
pi@ixe00:~/openCV-examples/contours-detection $ python contours.py
...
pi@ixe00:~$ cd ~/openCV-examples/face-detection
pi@ixe00:~/openCV-examples/face-detection $ python face-detection.py
...
pi@ixe00:~$ cd ~/openCV-examples/flow-detection
pi@ixe00:~/openCV-examples/flow-detection $ python optical_flow.py 0 window
...
pi@ixe00:~$ cd ~/openCV-examples/object-detection
pi@ixe00:~/openCV-examples/object-detection $ python detect.py
```

**\*\*\*Try each of the following four examples in the `openCV-examples`, include screenshots of your use and write about one design for each example that might work based on the individual benefits to each algorithm.\*\*\***

#### Contour detection
<img width="685" alt="image" src="https://user-images.githubusercontent.com/42963791/139276451-681f7873-aaed-4d7d-a1bc-db1aae559103.png">
There are plenty of application for contour detection. One popular design where it is commonly applied is in license plate detection, for use by law enforcement or toll tracking. Another good design that could be used might be checking products for imperfections. Products could range from consumer products like a laptop or perhaps a car, to structural renovations or builds. By taking a picture of the final product and comparing its contours to the contours on a perfect version of the  final product, (a concept car / auto cad model of the structure) you can identify if there is any spot with an imperfection. 

#### Face detection
<img width="666" alt="image" src="https://user-images.githubusercontent.com/42963791/139278249-cd66e540-acdf-441a-b026-d293fb1716da.png">
Face detection is already used in many use cases, for example I use it every day in order to unlock my phone. One interesting use case could be to augment the common front door. By mounting a camera on the door and scanning for faces, this would help tell us whether or not a human may be at the door or perhaps an animal running by. It could also tell us if someone is just pranking us. 

#### Flow detection
<img width="656" alt="image" src="https://user-images.githubusercontent.com/42963791/139279868-1b477655-a2e3-4ced-aeca-9e4d4306ef03.png">
Flow detection is another algorithm with plenty of use cases. The first that comes to mind would be usage in traffic situations, on a highway for example. You could detect whether people are driving in their lane and staying safe, or if they are perhaps swerving a bit identifying something might be wrong. This could be done by looking at how straight/constant the lines in the flow detection are, and whether they are following a certain axis. It could also be used to identify how fast cars are going for congestion detection, based on how fast the flow lines are growing. 

#### Object detection
<img width="725" alt="image" src="https://user-images.githubusercontent.com/42963791/139278029-5ed105da-0838-417c-aa0a-b07e61d548fc.png">
Object detection also has many potential applications. For one, object detection could be used to check if a loading bay of sorts has items in it. In a manufacturing environment, it might be of use to identify whether or not some area contains products, either intermediary or final output products. Object detection could also be helpful in automated cleaning services, being able to identify if there is an object out of place that needs to be cleaned up or moved elsewhere. These could both be done by identifying any objects and seeing if they match one of the expected items to be there, which may be no item at all. 


#### MediaPipe

A more recent open source and efficient method of extracting information from video streams comes out of Google's [MediaPipe](https://mediapipe.dev/), which offers state of the art face, face mesh, hand pose, and body pose detection.

![Alt Text](mp.gif)

To get started, create a new virtual environment with special indication this time:

```
pi@ixe00:~ $ virtualenv mpipe --system-site-packages
pi@ixe00:~ $ source mpipe/bin/activate
(mpipe) pi@ixe00:~ $ 
```

and install the following.

```
...
(mpipe) pi@ixe00:~ $ sudo apt install ffmpeg python3-opencv
(mpipe) pi@ixe00:~ $ sudo apt install libxcb-shm0 libcdio-paranoia-dev libsdl2-2.0-0 libxv1  libtheora0 libva-drm2 libva-x11-2 libvdpau1 libharfbuzz0b libbluray2 libatlas-base-dev libhdf5-103 libgtk-3-0 libdc1394-22 libopenexr23
(mpipe) pi@ixe00:~ $ pip3 install mediapipe-rpi4 pyalsaaudio
```

Each of the installs will take a while, please be patient. After successfully installing mediapipe, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the hand pose detection script we provide:
(***it will not work if you use ssh from your laptop***)


```
(mpipe) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(mpipe) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python hand_pose.py
```

Try the two main features of this script: 1) pinching for percentage control, and 2) "[Quiet Coyote](https://www.youtube.com/watch?v=qsKlNVpY7zg)" for instant percentage setting. Notice how this example uses hardcoded positions and relates those positions with a desired set of events, in `hand_pose.py` lines 48-53. 

**\*\*\*Consider how you might use this position based approach to create an interaction, and write how you might use it on either face, hand or body pose tracking.\*\*\***

There are plenty of interactions we could create using this position based approach. For example, we could use a variety of hand gestures to help control various settings on our computer. One way we could do this is by being able to make phone calls with gestures. First the user would make a phone gesture, i.e. the middle three fingers held in while the thumb and pinky fingers are held out, and then follow up with the number of fingers up for each digit in the number they want to call. This way, the user could make a phone call without having to say anything, and avoid pressing any buttons on their device. 

#### Had pose detection

https://youtu.be/wdfKeltiqHE

#### Quiet Coyote

<img width="688" alt="image" src="https://user-images.githubusercontent.com/42963791/139281950-4c601b0c-1fb8-4866-8894-fa26889f3356.png">

(You might also consider how this notion of percentage control with hand tracking might be used in some of the physical UI you may have experimented with in the last lab, for instance in controlling a servo or rotary encoder.)



#### Teachable Machines
Google's [TeachableMachines](https://teachablemachine.withgoogle.com/train) might look very simple. However, its simplicity is very useful for experimenting with the capabilities of this technology.

![Alt Text](tm.gif)

To get started, create and activate a new virtual environment for this exercise with special indication:

```
pi@ixe00:~ $ virtualenv tmachine --system-site-packages
pi@ixe00:~ $ source tmachine/bin/activate
(tmachine) pi@ixe00:~ $ 
```

After activating the virtual environment, install the requisite TensorFlow libraries by running the following lines:
```
(tmachine) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ sudo chmod +x ./teachable_machines.sh
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ ./teachable_machines.sh
``` 

This might take a while to get fully installed. After installation, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the example script:
(***it will not work if you use ssh from your laptop***)

```
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python tm_ppe_detection.py
```


(**Optionally**: You can train your own model, too. First, visit [TeachableMachines](https://teachablemachine.withgoogle.com/train), select Image Project and Standard model. Second, use the webcam on your computer to train a model. For each class try to have over 50 samples, and consider adding a background class where you have nothing in view so the model is trained to know that this is the background. Then create classes based on what you want the model to classify. Lastly, preview and iterate, or export your model as a 'Tensorflow' model, and select 'Keras'. You will find an '.h5' file and a 'labels.txt' file. These are included in this labs 'teachable_machines' folder, to make the PPE model you used earlier. You can make your own folder or replace these to make your own classifier.)

**\*\*\*Whether you make your own model or not, include screenshots of your use of Teachable Machines, and write how you might use this to create your own classifier. Include what different affordances this method brings, compared to the OpenCV or MediaPipe options.\*\*\***

#### Teachable Machine Test

The video shows an interaction with TeachableMachines.

https://youtu.be/7RJTa5-CEOs

The great advantage TeachableMachines has over the other options is that we can train it for specific use. The other options have predetirmined functionality but the possibility of training our own model with TeachableMachine opens a lot of opportunities. We could for example train the classifier to see if a person is wearing pants or not. Occationally, I leave my apartment, e.g. to take out the trash, and forget that I am not wearing pants. The device could be at the door and warn the users if they are about to exit without pants. Such a personalized model is not possible with the other options.


### Part B
### Construct a simple interaction.

Pick one of the models you have tried, pick a class of objects, and experiment with prototyping an interaction.
This can be as simple as the boat detector earlier.
Try out different interaction outputs and inputs.

**\*\*\*Describe and detail the interaction, as well as your experimentation here.\*\*\***

For our interaction, we decided to use the object detection model. For a class of objects, we wanted to use common objects - an airpods case, a Cornell id card, and a usb to hdmi converter cord. We also used the brown raspberry pi box. Our interaction was going to be detecting that all the items were in fact inside the raspberry pi box. This could be used in manufacturing, as described above - to make sure that all items are prepped in a box and ready to be shipped somewhere. 

Below is a picture of the box with nothing in it:

<img width="529" alt="Screen Shot 2021-10-31 at 8 30 33 PM" src="https://user-images.githubusercontent.com/52221419/139606798-e93c7124-e41e-4994-906c-cbf9d78499fa.png">

Here is a photo of the box with all the correct components in it: 

<img width="522" alt="Screen Shot 2021-10-31 at 8 30 47 PM" src="https://user-images.githubusercontent.com/52221419/139606810-76fe8ade-baf4-4d7d-90ed-22b7afb61cc8.png">

For our experiment, our plan was to place all the objects in the box and see whether or not the object detection would detect all three different objects. We used objects of different shapes and sizes (3d prism - airpods, flat planar card - Cornell ID, black cord - HDMI converter). We also used the card since it had reflective properties to it, as some products might have as well. The goal is to have all three objects detected in the box. We also wanted to see what positioning for the objects would be best within the box, and whether it would be able to detect multiple objects if they were on top of each other. 

### Part C
### Test the interaction prototype

Now flight test your interactive prototype and **note down your observations**:
For example:
1. When does it what it is supposed to do?

The device does what it is supposed to mostly when the objects are clearly set apart, and the camera has a good angle to view all of them, and not much motion was being applied to the camera at the time of detection:

<img width="565" alt="image" src="https://user-images.githubusercontent.com/42963791/139606190-38179aed-083d-4f28-b1a2-688488da62cc.png">

2. When does it fail?

The device failed fairly often. It took a while of positioning the camera at different angles in order to detect whether or not the objects were placed in the box correctly:

<img width="644" alt="image" src="https://user-images.githubusercontent.com/42963791/139606132-fb50cfcc-0541-4a27-b962-9ba64a50bc2a.png">

<img width="567" alt="image" src="https://user-images.githubusercontent.com/42963791/139606147-b9047393-5cef-4303-b30c-caa697eb14fa.png">

<img width="566" alt="image" src="https://user-images.githubusercontent.com/42963791/139606375-724a77e1-c7b7-41fa-baae-c08e3d9d54ce.png">

The photos shown above all describe how the device failed to detect these objects in the box. We also found that it failed to detect the items when they were on top of each other. We figured this might be important, because in a manufacturing enviornment where items might be rolling off a conveyor belt and into the box, there is a high chance that these oobjects might land on top of each other. We found this made it difficult to detect the objects:

<img width="559" alt="image" src="https://user-images.githubusercontent.com/42963791/139606525-c0d77d5a-05af-46c5-af98-f1357dc5b266.png">

3. When it fails, why does it fail?

We did not move the objects while attempting to detect them, so we know it has nothing to do with the motion of the objects. This did not prove that motion of the camera causes detection issues, which when we were attempting to get a good angle, we noticed played a significant part. So, too much motion of the camera certainly pushed the system to fail. We found that getting a good camera angle of the box and items inside it was quite important as well, and a bad angle made the system fail. We also thought maybe the system had trouble detecting the objects themselves, so we tried detecting each object on their own: 

<img width="556" alt="image" src="https://user-images.githubusercontent.com/42963791/139606160-f761c643-1ec4-4fe1-917a-845f7881a07b.png">

<img width="564" alt="image" src="https://user-images.githubusercontent.com/42963791/139606172-418da89d-fd09-4c55-a916-0be706620c03.png">

<img width="547" alt="image" src="https://user-images.githubusercontent.com/42963791/139606177-6f32cea2-7525-4f78-a528-2a199b8b2bd4.png">

We found here that there were no issues with the detection of the objects on their own, rather with the ability to detect multiple objects together. 

4. Based on the behavior you have seen, what other scenarios could cause problems?

There are plenty of reasons that could cause problems here. Some of these include the lighting of the room, shadows, or perhaps the color and material of the objects we are trying to detect. The contrast of the objects with their surroundings likely plays a role in this as well. 

**\*\*\*Think about someone using the system. Describe how you think this will work.\*\*\***
1. Are they aware of the uncertainties in the system?

When setting up the system a user should be aware of it's limitations. It is not apparent what the limitations are and the user should be notified beforehand. Otherwise, a user might e.g. try to use the system to try to count blank pieces of paper on a white background, an environment in which the device does not perform well.

2. How bad would they be impacted by a miss classification?

A miss classification is a serious error in this environment. A package that is not containing all the desired parts would be classified as ready and might be shipped out to a customer or other division. This should be avoided by all means.

3. How could change your interactive system to address this?

By fixing the camera’s position and orientation, we could further avoid misclassification by getting the ideal camera angle every time and avoiding motion of the camera. There could be additional checks as well to increase accuracy, perhaps a scale under the box to weigh the box and all the items to ensure they match the shipped box specifications. On the conveyor belt leading into the box, we could have a button pressed everytime something moves off the conveyor and into the box to count how many items are in the box. 

4. Are there optimizations you can try to do on your sense-making algorithm.

We thought it would be helpful if we could optimize the system to count how many items were in the box. This way, once a correct number of items had been reached, we knew the box would be ready to be shipped, for example. Moreover, if we could identify what the items placed in the box were, then we could have a specific idea of if the correct objects were in each shipped box. 

### Part D
### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:
* What can you use X for?
* What is a good environment for X?
* What is a bad environment for X?
* When will X break?
* When it breaks how will X break?
* What are other properties/behaviors of X?
* How does X feel?

**\*\*\*Include a short video demonstrating the answers to these questions.\*\*\***

https://youtu.be/AhBG9kmPv8s

### Part 2.

Following exploration and reflection from Part 1, finish building your interactive system, and demonstrate it in use with a video.

**\*\*\*Include a short video demonstrating the finished result.\*\*\***
