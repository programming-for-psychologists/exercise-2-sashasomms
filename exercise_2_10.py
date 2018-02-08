#!/usr/bin/env python

import time
import sys
import random
from psychopy import visual,event,core,gui
import csv

"""

10. Output the response times (in ms, e.g., 453 for 453 ms) 
and accuracy (1 for correct, 0 for incorrect) to a file output.txt. 
Output one line per trial: each line should contain the accuracy 
(1 or 0) and the response time (in milliseconds). 
See the python documentation for examples of how to write to a file. 
Ask for help if you are stuck.
"""

names = open('names.txt', 'r').readlines()
firstNames = [name.split(' ')[0] for name in names]
lastNames = [name.split(' ')[1].rstrip() for name in names]
Names = firstNames
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
# feedback wrong
NameNoExistStim = visual.TextStim(win,text="Name does not exist", height=40, color="red",pos=[0,0])
NameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
fixationStim = visual.TextStim(win,text="+", height=40, color="white",pos=[0,0])
# feedback correct
cStim = visual.TextStim(win,text="0", height=40, color="green",pos=[0,0])
# feedback wrong
wStim = visual.TextStim(win,text="X", height=40, color="red",pos=[0,0])

resp = prompt.show()
if len(resp) and resp[0] in firstNames:
    NameStim.setText("Proceeding...")
    NameStim.draw()
else:
    NameNoExistStim.draw()

win.flip()
core.wait(2)

trialNum = 1
while True:
    trialNum += 1
    fixationStim.draw()
    win.flip()
    core.wait(.5)
    win.flip()
    # random.choice takes a list as an argument
    nameShown = random.choice(Names)
    NameStim.setText(nameShown)
    NameStim.draw()
    win.flip()
    timer = core.Clock()
    hitspace = event.waitKeys(keyList='space', maxWait = .5)
    ACC = 1
    RT = 'NA'
    if hitspace :
        RT = timer.getTime()
        print(RT)
        if nameShown == resp[0] :
            cStim.draw()
            win.flip()
            core.wait(.5)
            win.flip()
            ACC = 1
        else:
            wStim.draw()
            win.flip()
            core.wait(.5)
            win.flip()
            ACC = 0
    if (nameShown == resp[0]) & (not hitspace) : 
        wStim.draw()
        win.flip()
        core.wait(.5)
        win.flip()
        ACC = 0
        RT = 'NA'
    # Write the file 
    outfile = "output.txt" 
    openfile = open(outfile, 'a')
    csvout = csv.writer(openfile, delimiter='\t')
    write_me = [trialNum, nameShown, ACC, RT]
    csvout.writerow(write_me)
    openfile.close()

    core.wait(.5)
    win.flip()


