#!/usr/bin/env python

import time
import sys
import random
from psychopy import visual,event,core,gui

"""
5. Now let's implement some feedback. 
Let's allow either a 'f' or 'l' response for each trial. 
If the response is correct, show a green 'O' before the start of the next trial. 
If the response is wrong, show a red 'X' (you can use textStim objects for feedback). 
Show the feedback for 500 ms. 
Note: we have someone in a class whose last name is a common first name. 
If this were an experiment, how might this affect responses?
"""

names = open('names.txt', 'r').readlines()
firstNames = [name.split(' ')[0] for name in names]
lastNames = [name.split(' ')[1].rstrip() for name in names]
Names = firstNames + lastNames
"""
the two line above are a more compact way of writing: 
names = open('names.txt', 'r').readlines()
firstNames=[]
for name in names:
    firstNames.append(name.split(' ')[0])
"""	

win = visual.Window([800,600],color="black", units='pix')
NameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
fixationStim = visual.TextStim(win,text="+", height=40, color="white",pos=[0,0])
# feedback correct
cStim = visual.TextStim(win,text="0", height=40, color="green",pos=[0,0])
# feedback wrong
wStim = visual.TextStim(win,text="X", height=40, color="red",pos=[0,0])
while True:
    fixationStim.draw()
    win.flip()
    core.wait(.5)
    win.flip()
    # random.choice takes a list as an argument
    nameShown = random.choice(Names)
    NameStim.setText(nameShown)
    NameStim.draw()
    win.flip()
    
    while True:
        resp = event.waitKeys()
        if ( ('f' in resp) and (nameShown in firstNames) ) | ( ('l' in resp) and (nameShown in lastNames) ) : 
            cStim.draw()
            win.flip()
            core.wait(.5)
            win.flip()
            break
        elif ( ('l' in resp) and (nameShown in firstNames) ) | ( ('f' in resp) and (nameShown in lastNames) ) :
            wStim.draw()
            win.flip()
            core.wait(.5)
            win.flip()
            break 
        if ('q' in resp): 
            sys.exit()
    
    if event.getKeys(['q']):
        break