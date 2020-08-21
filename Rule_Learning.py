#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.2),
    on Fri Aug 21 16:44:47 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
# from numpy./andom import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.2'
expName = 'Rule_Learning'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/estellesong/Documents/Ph.D/Research/New BP/Rule_Learning/Rule_Learning.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Welcome"
WelcomeClock = core.Clock()
welcome_text = visual.TextStim(win=win, name='welcome_text',
    text='Welcome\n\nHi~\n\n',
    font='Arial',
    pos=(0,0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Training_Trial"
Training_TrialClock = core.Clock()
train_key_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Welcome"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
WelcomeComponents = [welcome_text]
for thisComponent in WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Welcome"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = WelcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome_text* updates
    if welcome_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_text.frameNStart = frameN  # exact frame index
        welcome_text.tStart = t  # local t and not account for scr refresh
        welcome_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_text, 'tStartRefresh')  # time at next scr refresh
        welcome_text.setAutoDraw(True)
    if welcome_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > welcome_text.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            welcome_text.tStop = t  # not accounting for scr refresh
            welcome_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(welcome_text, 'tStopRefresh')  # time at next scr refresh
            welcome_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome"-------
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('welcome_text.started', welcome_text.tStartRefresh)
thisExp.addData('welcome_text.stopped', welcome_text.tStopRefresh)

# ------Prepare to start Routine "Training_Trial"-------
continueRoutine = True
# routineTimer.add(30.000000)
# update component parameters for each repeat
train_key_resp.keys = []
train_key_resp.rt = []
_train_key_resp_allKeys = []
# keep track of which components have finished
Training_TrialComponents = [train_key_resp] + chord_AAB_list  + chord_ABC_list
for thisComponent in Training_TrialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Training_TrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# init auxiliary variables and functions
current_AAB_count = 0
current_ABC_count = 0

stopped_chord = []
random.shuffle(chord_AAB_list)
random.shuffle(chord_ABC_list)

def choose_chord_is_AAB():
    global current_AAB_count
    global current_ABC_count
    print(current_AAB_count)
    print(current_ABC_count)
    isAAB = random.random() > 0.5
    if isAAB and current_AAB_count < 2:
        # AAB occurs less than 2 times, return AAB
        current_AAB_count += 1
        current_ABC_count = 0
        return True
    elif isAAB and current_AAB_count >= 2:
        # AAB occurs more than 2 times, returen ABC
        current_AAB_count = 0
        current_ABC_count +=1
        return False
    elif not isAAB and current_ABC_count < 2:
        # ABC occurs less than 2 times, return ABC
        current_AAB_count = 0
        current_ABC_count += 1
        return False
    elif not isAAB and current_ABC_count >= 2:
        # ABC occurs more than 2 times, return AAB
        current_AAB_count += 1
        current_ABC_count = 0
        return True
    else:
        raise Exception

# -------Run Routine "Training_Trial"-------
# while continueRoutine and routineTimer.getTime() > 0:
while continueRoutine:
    # get current time
    t = Training_TrialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Training_TrialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)

    # update/draw components on each frame
    total_train_trial_count = 0
    correct_count = 0
    while True:
        # Step 1: play music
        # select music
        isAAB = choose_chord_is_AAB()
        chord = chord_AAB_list.pop() if isAAB else chord_ABC_list.pop()
        # start/stop sound
        if chord.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            chord.frameNStart = frameN  # exact frame index
            chord.tStart = t  # local t and not account for scr refresh
            chord.tStartRefresh = tThisFlipGlobal  # on global time
            chord.play(when=win)  # sync with win flip
        if chord.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > chord.tStartRefresh + 30.0-frameTolerance:
                # keep track of stop time/frame for later
                chord.tStop = t  # not accounting for scr refresh
                chord.frameNStop = frameN  # exact frame index
                win.timeOnFlip(chord, 'tStopRefresh')  # time at next scr refresh
                chord.stop()

        stopped_chord.append(chord)
        # Step 2: wait for key response
        # Step 3: check answer

        answer = singe_train_trial()
        if answer:
            correct_count += 1
        else:
            correct_count = 0
        if (correct_count >= 3 and total_train_trial_count > AT_LEAST_TRIAL)
            # pass test
            break
        elif (len(chord_AAB_list) == 0 or len(chord_ABC_list) == 0)
            # failed test
            break
        else:
            raise Exception
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Training_TrialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Training_Trial"-------
for thisComponent in Training_TrialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
for chord in stopped_chord:
    chord.stop()  # ensure sound has stopped at end of routine
    thisExp.addData('%s.started' % chord.name, chord.tStartRefresh)
    thisExp.addData('%s.stopped' % chord.name, chord.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
