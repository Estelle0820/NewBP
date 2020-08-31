from __future__ import absolute_import, division

import psychopy
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np
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


def read_all_files_in_directory(directory_path):
    """
    Return a list contains all files in the directory.
    """
    files = []
    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)
        if os.path.isfile(file_path):
            files.append(file_name)
    return files


class ExperimentManager():
    """
    Util class for experiment
    """

    @staticmethod
    def quit_experiment():
        """
        Quit experiment and release all resources.
        """
        core.quit()

    @staticmethod
    def show_dialog_box():
        """
        Show a dialog box with PsychoPy library and collect participant info
        """
        new_bp_dlg = gui.Dlg(title=args.EXPERIMENT_NAME)
        for field in args.DIALOG_NORMAL_FIELDS:
            new_bp_dlg.addField(field)
        for field, choice in args.DIALOG_CHOICE_FIELDS.items():
            new_bp_dlg.addField(field, choices=choice)
        dlg_results = new_bp_dlg.show()
        if new_bp_dlg.OK:
            for result in dlg_results:
                if isinstance(result, str) and not bool(result):
                    logger.info('Invalid input.')
                    quit_experiment()
            participant_info_fields = args.DIALOG_NORMAL_FIELDS + \
                list(args.DIALOG_CHOICE_FIELDS.keys())
            participant_info = dict(zip(participant_info_fields, dlg_results))
            logger.info(participant_info)
            return participant_info
        else:
            logger.info('Participant cancelled.')
            quit_experiment()

    @staticmethod
    def get_experiment_info(exp_info={}):
        """
        Return an dict of experiment info.
        """
        exp_info['ExperimentName'] = args.EXPERIMENT_NAME
        expInfo['Date'] = data.getDateStr()
        exp_info['PsychoPyVersion'] = psychopy.__version__
        return exp_info

    @staticmethod
   def get_experiment_handler(exp_info):
        """
        An ExperimentHandler isn't essential but helps with data saving.
        """
        data_save_directory = os.path.join(
            args.DATA_PATH, '%s_%s' % (exp_info['Student ID'], exp_info['Name']))
        data_save_path = os.path.join(
            data_save_directory, '%s' % exp_info['Date'])
        this_exp = data.ExperimentHandler(name=exp_info['ExperimentName'],
                                          version=exp_info['PsychoPyVersion'],
                                          extraInfo=exp_info,
                                          runtimeInfo=None,
                                          savePickle=True,
                                          saveWideText=True,
                                          dataFileName=data_save_path)
        return this_exp

    @staticmethod
    def get_experiment_window(size=(1024, 768), fullscr=False,
                              screen=0, winType='pyglet'):
        win = visual.Window(
            size=size, fullscr=fullscr, screen=screen,
            winType=winType, allowGUI=False, allowStencil=False,
            monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
            blendMode='avg', useFBO=True,
            units='height')
        return win

    @staticmethod
    def get_experiment_clock():
        clock = core.Clock()
        return clock

    @staticmethod
    def get_experiment_text(win, name, text, pos=(0, 0), height=0.1):
        text = visual.TextStim(win=win, name=name,
                               text=text,
                               font='Arial',
                               pos=pos, height=height, wrapWidth=None, ori=0,
                               color='white', colorSpace='rgb', opacity=1,
                               languageStyle='LTR',
                               depth=0.0)
        return text

    @staticmethod
    def run_experiment_routine(win, default_keyboard, this_exp, count_down,
                               components=[], key_resp=None):
        """
        Run a experiment routine with given components.
        Component type must be visual.TextStim/sound.Sound.
        """

        # *init*
        clock = get_experiment_clock()
        timer = core.CountdownTimer()
        timer.add(count_down)
        continueRoutine = True
        # update component parameters for each repeat
        if key_resp is not None:
            key_resp.keys = []
            key_resp.rt = []
            _key_resp_allKeys = []
            key_responsed = False   # has got key response of the participant?
        # keep track of which components have finished
        for component in components if key_resp is None else components + [key_resp]:
            component.tStart = None
            component.tStop = None
            component.tStartRefresh = None
            component.tStopRefresh = None
            if hasattr(component, 'status'):
                component.status = NOT_STARTED
        t = 0 # reset timers
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # *run routine*
        while continueRoutine and timer.getTime() > 0:
            # get current time
            t = clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            # number of completed frames (so 0 is the first frame)
            frameN = frameN + 1
            # update/draw components on each frame
            for component in components:
                if component.status == NOT_STARTED and tThisFlip >= 0.0 - args.FRAME_TOLERANCE:
                    # keep track of start time/frame for later
                    component.frameNStart = frameN  # exact frame index
                    component.tStart = t  # local t and not account for scr refresh
                    component.tStartRefresh = tThisFlipGlobal  # on global time
                    if isinstance(component, visual.TextStim):
                        # time at next scr refresh
                        win.timeOnFlip(component, 'tStartRefresh')
                        component.setAutoDraw(True)
                    elif isinstance(component, sound.Sound):
                        component.play(when=win)  # sync with win flip
                    else:
                        pass
                if component.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > component.tStartRefresh + count_down - args.FRAME_TOLERANCE:
                        # keep track of stop time/frame for later
                        component.tStop = t  # not accounting for scr refresh
                        component.frameNStop = frameN  # exact frame index
                    if isinstance(component, visual.TextStim):
                        # time at next scr refresh
                        win.timeOnFlip(component, 'tStopRefresh')
                        component.setAutoDraw(False)
                    elif isinstance(component, sound.Sound):
                        # time at next scr refresh
                        win.timeOnFlip(component, 'tStopRefresh')
                        component.stop()
                    else:
                        pass
            # update key response if exists
            if key_resp is not None:
                waitOnFlip = False
                if key_resp.status == NOT_STARTED and tThisFlip >= 0.0 - args.FRAME_TOLERANCE:
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
                    if tThisFlipGlobal > key_resp.tStartRefresh + count_down - args.FRAME_TOLERANCE:
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
                        # if a response ends the routine, uncomment:
                        # continueRoutine = False
            # check for quit (typically the Esc key)
            if default_keyboard.getKeys(keyList=["escape"]):
                quit_experiment()
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for component in components:
                if hasattr(component, "status") and component.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # *end routine*
        if key_resp is not None:
            # check responses
            if key_resp.keys in ['', [], None]:  # No response was made
                key_resp.keys = None
            this_exp.addData('key_resp.keys', key_resp.keys)
            if key_resp.keys != None:  # we had a response
                this_exp.addData('key_resp.rt', key_resp.rt)
                key_responsed = True
        for component in components if key_resp is None else components + [key_resp]:
            if hasattr(component, "setAutoDraw"):
                component.setAutoDraw(False)
            if isinstance(component, sound.Sound):
                component.stop()
            this_exp.addData('%s.started' % component.name, component.tStartRefresh)
            this_exp.addData('%s.stopped' % component.name, component.tStopRefresh)
