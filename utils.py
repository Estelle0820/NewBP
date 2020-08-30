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


def quit_experiment():
    """
    Quit experiment and release all resources.
    """
    core.quit()


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


def get_experiment_info(exp_info={}):
    """
    Return an dict of experiment info.
    """
    exp_info['ExperimentName'] = args.EXPERIMENT_NAME
    expInfo['Date'] = data.getDateStr()
    exp_info['PsychoPyVersion'] = psychopy.__version__
    return exp_info


def get_experiment_handler(exp_info):
    """
    An ExperimentHandler isn't essential but helps with data saving.
    """
    data_save_directory = os.path.join(
        args.DATA_PATH, '%s_%s' % (exp_info['Student ID'], exp_info['Name']))
    data_save_path = os.path.join(data_save_directory, '%s' % exp_info['Date'])
    this_exp = data.ExperimentHandler(name=exp_info['ExperimentName'],
                                      version=exp_info['PsychoPyVersion'],
                                      extraInfo=exp_info,
                                      runtimeInfo=None,
                                      savePickle=True,
                                      saveWideText=True,
                                      dataFileName=data_save_path)
    return this_exp


def get_experiment_window(size=(1024, 768),
                          fullscr=False,
                          screen=0,
                          winType='pyglet'):
    win = visual.Window(
        size=size, fullscr=fullscr, screen=screen,
        winType=winType, allowGUI=False, allowStencil=False,
        monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
        blendMode='avg', useFBO=True,
        units='height')
    return win
