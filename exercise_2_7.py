#!/usr/bin/env python

import time
import sys
import random
from psychopy import visual,event,core,gui

"""
7. Pop up a box that accepts a first name, 
and check to make sure that the name exists. 
If it doesn't, pop-up a 'Name does not exist' error box
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
prompt = "Please enter a name\n >"

prompt = gui.Dlg(title="Please enter a name:\n")
prompt.addField('Name')
win = visual.Window([800,600],color="black", units='pix')
cStim = visual.TextStim(win,text="Got 'em", height=40, color="green",pos=[0,0])
# feedback wrong
wStim = visual.TextStim(win,text="Name does not exist", height=40, color="red",pos=[0,0])

while True:
    res = prompt.show()
    if res and len(res) and res[0] in firstNames:
        cStim.draw()
    else:
        wStim.draw()

    win.flip()
    core.wait(2)


 