#!/usr/bin/env python

import time
import sys
import random
from psychopy import visual,event,core,gui

"""
4. On each presentation of a name, wait for a response 
('f' for first name, 'l' for last-name) and 
only proceed to the next name if the response is correct. 
Hint: if you've done steps 2-3 properly, this should be really easy. 
Refer to the psychopy documentation of event.waitKeys() if you have trouble.
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
        if ('f' in resp) and (nameShown in firstNames): 
            break
        elif ('l' in resp) and (nameShown in lastNames): 
            break 
        elif ('q' in resp): 
            sys.exit()
    
    if event.getKeys(['q']):
        break