#!/usr/bin/env python

import time
import sys
import random
from psychopy import visual,event,core,gui
import csv

"""

11. Do something new. 
Compare response times to first and last names, 
measure effect of font face, etc.
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
    fixationStim.draw()
    win.flip()
    core.wait(.5)
    win.flip()
    # random.choice takes a list as an argument
    nameShown = random.choice(Names)
    NameStim.setText(nameShown)
    NameStim.draw()
    win.flip()

    while True :
        resp = event.waitKeys(maxWait = 1)
        print(resp)
        if not resp :
            wStim.draw()
            win.flip()
            core.wait(.5)
            win.flip()
            break 
        # First names
        if nameShown in firstNames : 
            firstLast = 'f'
            if ( ('f' in resp) ) : 
                cStim.draw()
                win.flip()
                core.wait(.5)
                win.flip()
                ACC = 1
                break
            else:
                wStim.draw()
                win.flip()
                core.wait(.5)
                win.flip()
                ACC = 0
                break 

        if nameShown in lastNames : 
            firstLast = 'f'
            if ( ('f' in resp) ) : 
                cStim.draw()
                win.flip()
                core.wait(.5)
                win.flip()
                ACC = 1
                break
            else:
                wStim.draw()
                win.flip()
                core.wait(.5)
                win.flip()
                ACC = 0
                break 
    # Write the file 
    outfile = "output.txt" 
    openfile = open(outfile, 'a')
    csvout = csv.writer(openfile, delimiter='\t')
    write_me = [trialNum, firstLast, nameShown, ACC, RT]
    csvout.writerow(write_me)
    openfile.close()

    core.wait(.5)
    win.flip()


