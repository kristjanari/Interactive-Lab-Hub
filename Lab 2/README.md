# Interactive Prototyping: The Clock of Pi

Does it feel like time is moving strangely during this semester?

For our first Pi project, we will pay homage to the [timekeeping devices of old](https://en.wikipedia.org/wiki/History_of_timekeeping_devices) by making simple clocks.

It is worth spending a little time thinking about how you mark time, and what would be useful in a clock of your own design.

**Please indicate anyone you collaborated with on this Lab here.**

I worked with Donal Lowsey-Williams, dml333, on this lab project.

## Prep

[Lab prep](prep.md) is extra long this week! Make sure you read it over in time to prepare for lab on Thursday.

### Get your kit
If you are remote but in the US, let the teaching team know you need the parts mailed.


If you are in New York, you can come to the campus and pick up your parts. If you have not picked up your parts by Thursday lab you should come to Tata 351.

### Set up your Lab 2

1. [Pull changes from the Interactive Lab Hub](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md#to-pull-lab-updates) so that you have your own copy of Lab 2 on your own lab hub. (This may have to be done again at the start of lab on Thursday.)
  If you are organizing your Lab Hub through folder in local machine, go to terminal, cd into your Interactive-Lab-Hub folder and run:

  ```
  Interactive-Lab-Hub $ git remote add upstream https://github.com/FAR-Lab/Interactive-Lab-Hub.git
  Interactive-Lab-Hub $ git pull upstream Fall2021
  ```
  
  The reason why we are adding a upstream with **course lab-hub** instead of yours is because the local Interactive-Lab-Hub folder is linked with your own git repo already. Try typing ``git remote -v`` and you should see there is the origin branch with your own git repo. We here add the upstream to get latest updates from the teaching team by pulling the **course lab-hub** to your local machine. After your local folder got the latest updates, push them to your remote git repo by running:
  
  ```
  Interactive-Lab-Hub $ git add .
  Interactive-Lab-Hub $ git commit -m "message"
  Interactive-Lab-Hub $ git push
  ```
  Your local and remote should now be up to date with the most recent files.

2. Go to the [lab prep page](prep.md) to inventory your parts and set up your Pi before the lab session on Thursday.


## Overview
For this assignment, you are going to 

A) [Connect to your Pi](#part-a)  

B) [Try out cli_clock.py](#part-b) 

C) [Set up your RGB display](#part-c)

D) [Try out clock_display_demo](#part-d) 

E) [Modify the code to make the display your own](#part-e)

F) [Make a short video of your modified barebones PiClock](#part-f)

G) [Sketch and brainstorm further interactions and features you would like for your clock for Part 2.](#part-g)

## The Report
This readme.md page in your own repository should be edited to include the work you have done. You can delete everything but the headers and the sections between the \*\*\***stars**\*\*\*. Write the answers to the questions under the starred sentences. Include any material that explains what you did in this lab hub folder, and link it in the readme.

Labs are due on Mondays. Make sure this page is linked to on your main class hub page.

## Part A. 
### Connect to your Pi

I followed the steps in the lab prep to set up the Raspberry Pi without problems.


## Part B. 
### Try out the Command Line Clock


The clock running in the terminal:

<img width="547" alt="image" src="https://user-images.githubusercontent.com/42963791/134097701-96a361c1-1ded-44ed-8da0-4fa424020e4c.png">


## Part C. 
### Set up your RGB Display

I finished the process of setting up the hardware in the  lab prep.

#### Displaying an image

I exhanged the Cornell Tech logo with a picture of myself.

<img width="549" alt="image" src="https://user-images.githubusercontent.com/42963791/134097490-0fe3b8db-db8b-4647-bd05-34e1a01eee79.png">


## Part D. 
### Set up the Display Clock Demo

To display the time on the Raspberry Pi I got the time value as in cli_clock.py and displayed it with the same methods as are used in stats.py.

## Part E.
### My barebones clock

Our design is quite simple. Each possible value for the given hour and minutes are displayed. The current time is then given by coloring the the values of each given time. Similarly am and pm is indicated by the color of the text. We felt that displaying all possible values of seconds was too cumbersome so we display the seconds as a growing pipe. For each second passed, we add a line.

The code for the modified clock can be found in the file screen_clock.py.


## Part F. 
## A short video of my modified barebones PiClock

This short video shows how the clock changes with time.

https://youtu.be/jB_KjMRUFls

## Part G. 
## Sketch and brainstorm further interactions and features you would like for your clock for Part 2.

I would like to develop two more designs to display time and make them all available on the barebones clock. By pressing the button on the screen, the user should be able to switch between time displays.

One idea is to display an image on the screen that slowly fades away as the minute passes to reveal the current time.

Another one is to represent it with a grid display. The x-axis is the hours and y-axis is minutes. The cell colored is the current time and the brightness determines seconds.

<img width="734" alt="image" src="https://user-images.githubusercontent.com/42963791/134100536-43bc9fb7-8bc7-4019-9c59-53b3ff499097.png">

# Prep for Part 2

1. Pick up remaining parts for kit on Thursday lab class. Check the updated [parts list inventory](partslist.md) and let the TA know if there is any part missing.
  

2. Look at and give feedback on the Part G. for at least 2 other people in the class (and get 2 people to comment on your Part G!)

# Lab 2 Part 2

Pull Interactive Lab Hub updates to your repo.

Modify the code from last week's lab to make a new visual interface for your new clock. You may [extend the Pi](Extending%20the%20Pi.md) by adding sensors or buttons, but this is not required.

## A video of the improved clock

https://youtu.be/oA4hQ3SbxkQ

As always, make sure you document contributions and ideas from others explicitly in your writeup.

You are permitted (but not required) to work in groups and share a turn in; you are expected to make equal contribution on any group work you do, and N people's group project should look like N times the work of a single person's lab. What each person did should be explicitly documented. Make sure the page for the group turn in is linked to your Interactive Lab Hub page. 


