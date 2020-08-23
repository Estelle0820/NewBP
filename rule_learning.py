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
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

from param import *
from training_trial import *
import log
logger = log.Logging.getLogger()


def run():

    # Ensure that relative paths start from the same directory as this script
    os.chdir(ROOT_PATH)

    # Store info about the experiment session
    psychopyVersion = '2020.1.2'
    expName = 'RuleLearning'  # from the Builder filename that created this script
    expInfo = {'participant': '', 'session': '001'}
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    expInfo['date'] = data.getDateStr()  # add a simple timestamp
    expInfo['expName'] = expName
    expInfo['psychopyVersion'] = psychopyVersion

    # Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    filename = ROOT_PATH + os.sep + \
        u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

    # An ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(name=expName, version='',
                                     extraInfo=expInfo, runtimeInfo=None,
                                     originPath=os.path.abspath(__file__),
                                     savePickle=True, saveWideText=True,
                                     dataFileName=filename)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.WARNING)

    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    frameTolerance = 0.001  # how close to onset before 'same' frame

    # Start Code - component code to be run before the window creation

    # Setup the Window
    win = visual.Window(
        size=(1024, 768), fullscr=False, screen=0,
        winType='pyglet', allowGUI=False, allowStencil=False,
        monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
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

    # Initialize components for Routine "welcome"
    welcomeClock = core.Clock()
    welcome_text = visual.TextStim(win=win, name='welcome_text',
                                   text='Welcome\n\nHi~\n\n',
                                   font='Arial',
                                   pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
                                   color='white', colorSpace='rgb', opacity=1,
                                   languageStyle='LTR',
                                   depth=0.0)

    # Initialize components for Routine "training_trial_chord_playing"
    training_trial_chord_playingClock = core.Clock()
    chord_manager = ChordManager()
    chord_help_text = visual.TextStim(win=win, name='chord_help_text',
                                      text='Listen to the chord.',
                                      font='Arial',
                                      pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
                                      color='white', colorSpace='rgb', opacity=1,
                                      languageStyle='LTR',
                                      depth=0.0)

    # Initialize components for Routine "training_trial_answer"
    training_trial_answerClock = core.Clock()
    text = visual.TextStim(win=win, name='text',
                           text='Press <space> if the chord is the target chord.\nNeglect it if it is not.',
                           font='Arial',
                           pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
                           color='white', colorSpace='rgb', opacity=1,
                           languageStyle='LTR',
                           depth=0.0)
    key_resp = keyboard.Keyboard()

    # Initialize components for Routine "training_trial_result"
    training_trial_resultClock = core.Clock()
    result_text = visual.TextStim(win=win, name='result_text',
                                  text='Show result',
                                  font='Arial',
                                  pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
                                  color='white', colorSpace='rgb', opacity=1,
                                  languageStyle='LTR',
                                  depth=0.0)

    # Create some handy timers
    globalClock = core.Clock()  # to track the time since experiment started
    # to track time remaining of each (non-slip) routine
    routineTimer = core.CountdownTimer()

    # ------Prepare to start Routine "welcome"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    welcomeComponents = [welcome_text]
    for thisComponent in welcomeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    welcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "welcome"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = welcomeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=welcomeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        # number of completed frames (so 0 is the first frame)
        frameN = frameN + 1
        # update/draw components on each frame

        # *welcome_text* updates
        if welcome_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            welcome_text.frameNStart = frameN  # exact frame index
            welcome_text.tStart = t  # local t and not account for scr refresh
            welcome_text.tStartRefresh = tThisFlipGlobal  # on global time
            # time at next scr refresh
            win.timeOnFlip(welcome_text, 'tStartRefresh')
            welcome_text.setAutoDraw(True)
        if welcome_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > welcome_text.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                welcome_text.tStop = t  # not accounting for scr refresh
                welcome_text.frameNStop = frameN  # exact frame index
                # time at next scr refresh
                win.timeOnFlip(welcome_text, 'tStopRefresh')
                welcome_text.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in welcomeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "welcome"-------
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('welcome_text.started', welcome_text.tStartRefresh)
    thisExp.addData('welcome_text.stopped', welcome_text.tStopRefresh)

    # ------Prepare to start Routine "training_Trial"-------
    total_train_trial_count = 0
    correct_continuous_train_trial_count = 0
    continue_training_trial = True

    # -------Start Routine Loop "training_Trial"-------
    while continue_training_trial:

        """
        Step 1: play music
        """

        # ------Prepare to start Routine "training_trial_chord_playing"-------
        continueRoutine = True
        routineTimer.add(MAX_CHORD_PLAY_TIME)
        # update component parameters for each repeat
        chord = chord_manager.get_chord()  # select music
        if chord is None:
            # failed test
            logger.info('Training trial failed!')
            result_text.setText('Training trial failed')
            continue_training_trial = False
        if continue_training_trial:
            logger.info('Training %d:' % total_train_trial_count)
            logger.info('Chord: ' + chord.name)
            # keep track of which components have finished
            training_trial_chord_playingComponents = [chord_help_text, chord]
            for thisComponent in training_trial_chord_playingComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            # t0 is time of first possible flip
            training_trial_chord_playingClock.reset(-_timeToFirstFrame)
            frameN = -1

            # -------Run Routine "training_trial_chord_playing"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = training_trial_chord_playingClock.getTime()
                tThisFlip = win.getFutureFlipTime(
                    clock=training_trial_chord_playingClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                # number of completed frames (so 0 is the first frame)
                frameN = frameN + 1
                # update/draw components on each frame
                # start/stop chord
                if chord.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    chord.frameNStart = frameN  # exact frame index
                    chord.tStart = t  # local t and not account for scr refresh
                    chord.tStartRefresh = tThisFlipGlobal  # on global time
                    chord.play(when=win)  # sync with win flip
                if chord.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > chord.tStartRefresh + MAX_CHORD_PLAY_TIME - frameTolerance:
                        # keep track of stop time/frame for later
                        chord.tStop = t  # not accounting for scr refresh
                        chord.frameNStop = frameN  # exact frame index
                        # time at next scr refresh
                        win.timeOnFlip(chord, 'tStopRefresh')
                        chord.stop()
                if chord_help_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    chord_help_text.frameNStart = frameN  # exact frame index
                    chord_help_text.tStart = t  # local t and not account for scr refresh
                    chord_help_text.tStartRefresh = tThisFlipGlobal  # on global time
                    # time at next scr refresh
                    win.timeOnFlip(chord_help_text, 'tStartRefresh')
                    chord_help_text.setAutoDraw(True)
                if chord_help_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > chord_help_text.tStartRefresh + MAX_CHORD_PLAY_TIME - frameTolerance:
                        # keep track of stop time/frame for later
                        chord_help_text.tStop = t  # not accounting for scr refresh
                        chord_help_text.frameNStop = frameN  # exact frame index
                        # time at next scr refresh
                        win.timeOnFlip(chord_help_text, 'tStopRefresh')
                        chord_help_text.setAutoDraw(False)

                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()

                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in training_trial_chord_playingComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished

                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()

            # -------Ending Routine "training_trial_chord_playing"-------
            for thisComponent in training_trial_chord_playingComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('chord_help_text.started',
                            chord_help_text.tStartRefresh)
            thisExp.addData('chord_help_text.stopped',
                            chord_help_text.tStopRefresh)
            chord.stop()  # ensure sound has stopped at end of routine
            thisExp.addData('%s.started' % chord.name, chord.tStartRefresh)
            thisExp.addData('%s.stopped' % chord.name, chord.tStopRefresh)

            """
            Step 2: wait for key response
            """

            # ------Prepare to start Routine "training_trial_answer"-------
            continueRoutine = True
            routineTimer.add(MAX_KEY_WAIT_TIME)
            # update component parameters for each repeat
            key_resp.keys = []
            key_resp.rt = []
            _key_resp_allKeys = []
            current_trial_key_responsed = False  # has got key response of the participant?
            # keep track of which components have finished
            training_trial_answerComponents = [text, key_resp]
            for thisComponent in training_trial_answerComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            # t0 is time of first possible flip
            training_trial_answerClock.reset(-_timeToFirstFrame)
            frameN = -1

            # -------Run Routine "training_trial_answer"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = training_trial_answerClock.getTime()
                tThisFlip = win.getFutureFlipTime(
                    clock=training_trial_answerClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                # number of completed frames (so 0 is the first frame)
                frameN = frameN + 1
                # update/draw components on each frame

                # *text* updates
                if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text.frameNStart = frameN  # exact frame index
                    text.tStart = t  # local t and not account for scr refresh
                    text.tStartRefresh = tThisFlipGlobal  # on global time
                    # time at next scr refresh
                    win.timeOnFlip(text, 'tStartRefresh')
                    text.setAutoDraw(True)
                if text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text.tStartRefresh + MAX_KEY_WAIT_TIME - frameTolerance:
                        # keep track of stop time/frame for later
                        text.tStop = t  # not accounting for scr refresh
                        text.frameNStop = frameN  # exact frame index
                        # time at next scr refresh
                        win.timeOnFlip(text, 'tStopRefresh')
                        text.setAutoDraw(False)

                # *key_resp* updates
                waitOnFlip = False
                if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp.frameNStart = frameN  # exact frame index
                    key_resp.tStart = t  # local t and not account for scr refresh
                    key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    # time at next scr refresh
                    win.timeOnFlip(key_resp, 'tStartRefresh')
                    key_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    # t=0 on next screen flip
                    win.callOnFlip(key_resp.clock.reset)
                    # clear events on next screen flip
                    win.callOnFlip(key_resp.clearEvents, eventType='keyboard')
                if key_resp.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp.tStartRefresh + MAX_KEY_WAIT_TIME - frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp.tStop = t  # not accounting for scr refresh
                        key_resp.frameNStop = frameN  # exact frame index
                        # time at next scr refresh
                        win.timeOnFlip(key_resp, 'tStopRefresh')
                        key_resp.status = FINISHED
                if key_resp.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp.getKeys(
                        keyList=['space'], waitRelease=False)
                    _key_resp_allKeys.extend(theseKeys)
                    if len(_key_resp_allKeys):
                        # just the first key pressed
                        key_resp.keys = _key_resp_allKeys[0].name
                        key_resp.rt = _key_resp_allKeys[0].rt
                        # a response ends the routine
                        # continueRoutine = False

                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()

                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in training_trial_answerComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished

                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()

            # -------Ending Routine "training_trial_answer"-------
            for thisComponent in training_trial_answerComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('text.started', text.tStartRefresh)
            thisExp.addData('text.stopped', text.tStopRefresh)
            # check responses
            if key_resp.keys in ['', [], None]:  # No response was made
                key_resp.keys = None
            thisExp.addData('key_resp.keys', key_resp.keys)
            if key_resp.keys != None:  # we had a response
                thisExp.addData('key_resp.rt', key_resp.rt)
                current_trial_key_responsed = True
                logger.info('Key response recived.')
            thisExp.addData('key_resp.started', key_resp.tStartRefresh)
            thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
            thisExp.nextEntry()

            """
            Step 3: Check answer
            """
            total_train_trial_count += 1
            input_chord_type = ChordType.AAB if current_trial_key_responsed else ChordType.ABC
            answer = chord_manager.check_chord(input_chord_type)
            logger.info('Correct: ' + str(answer))
            if answer:
                correct_continuous_train_trial_count += 1
                result_text.setText('Correct')
            else:
                correct_continuous_train_trial_count = 0
                result_text.setText('Incorrect')
            logger.info('Correct count: %d' %
                        correct_continuous_train_trial_count)
            if (correct_continuous_train_trial_count >= ACCEPT_CORRECT_TRIAL and total_train_trial_count > AT_LEAST_TRIAL):
                # pass test
                logger.info('Training trial succeed!')
                result_text.setText('Training trial succeed')
                continue_training_trial = False

        """
        Step 4: Show result
        """

        # ------Prepare to start Routine "training_trial_result"-------
        continueRoutine = True
        routineTimer.add(MAX_RESULT_PLAY_TIME)
        # update component parameters for each repeat
        # keep track of which components have finished
        training_trial_resultComponents = [result_text]
        for thisComponent in training_trial_resultComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        # t0 is time of first possible flip
        training_trial_resultClock.reset(-_timeToFirstFrame)
        frameN = -1

        # -------Run Routine "training_trial_result"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = training_trial_resultClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=training_trial_resultClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            # number of completed frames (so 0 is the first frame)
            frameN = frameN + 1
            # update/draw components on each frame

            # *result_text* updates
            if result_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                result_text.frameNStart = frameN  # exact frame index
                result_text.tStart = t  # local t and not account for scr refresh
                result_text.tStartRefresh = tThisFlipGlobal  # on global time
                # time at next scr refresh
                win.timeOnFlip(result_text, 'tStartRefresh')
                result_text.setAutoDraw(True)
            if result_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > result_text.tStartRefresh + MAX_RESULT_PLAY_TIME - frameTolerance:
                    # keep track of stop time/frame for later
                    result_text.tStop = t  # not accounting for scr refresh
                    result_text.frameNStop = frameN  # exact frame index
                    # time at next scr refresh
                    win.timeOnFlip(result_text, 'tStopRefresh')
                    result_text.setAutoDraw(False)

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in training_trial_resultComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "training_trial_result"-------
        for thisComponent in training_trial_resultComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('result_text.started', result_text.tStartRefresh)
        thisExp.addData('result_text.stopped', result_text.tStopRefresh)

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


if __name__ == "__main__":
    run()
