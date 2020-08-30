# -*- coding: utf-8 -*-
import os
import argparse
from enum import Enum
from psychopy import gui

import log
logger = log.Logging.getLogger()


class Parameter():

    def __init__(self):
        self.parser = argparse.ArgumentParser(description="")
        self.args = self.parser.parse_args()


parameter = Parameter()
args = parameter.args

args.ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
args.DATA_PATH = os.path.join(args.ROOT_PATH, 'data')
args.ASSETS_PATH = os.path.join(args.ROOT_PATH, 'assets')
args.MUSIC_PATH = os.path.join(args.ASSETS_PATH, 'music')
args.AT_LEAST_TRIAL = 30
args.ACCEPT_CORRECT_TRIAL = 3
args.MAX_CHORD_PLAY_TIME = 3.0
args.MAX_KEY_WAIT_TIME = 2.0
args.MAX_RESULT_PLAY_TIME = 1.0
args.EXPERIMENT_NAME = 'New BP Experiment'
args.GROUP_TYPES = [1, 2, 3, 4]
args.GROUP_NAMES = {
    '1': 'unconventional_consonant',
    '2': 'unconventional_dissonant',
    '3': 'western_consonant',
    '4': 'western_dissonant',
}
args.DIALOG_NORMAL_FIELDS = ['Name', 'Student ID', 'Age']
args.DIALOG_CHOICE_FIELDS = {'Group': args.GROUP_TYPES}
args.FRAME_TOLERANCE = 0.001


class ChordType(Enum):
    """
    Defines types of chord.
    """
    AAB = 0
    ABC = 1


logger.info(args)
