# -*- coding: utf-8 -*-
import os
import argparse

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
args.MAX_WELCOME_SHOW_TIME = 10.0
args.MAX_CHORD_PLAY_TIME = 3.0
args.MAX_KEY_WAIT_TIME = 2.0
args.MAX_RESULT_SHOW_TIME = 1.0
args.EXPERIMENT_NAME = 'New BP Experiment'
args.GROUP_TYPES = [1, 2, 3, 4]
args.GROUP_NAMES = {
    1: 'unconventional_consonant',
    2: 'unconventional_dissonant',
    3: 'western_consonant',
    4: 'western_dissonant',
}
args.DIALOG_NORMAL_FIELDS = ['Name', 'Student ID', 'Age']
args.DIALOG_CHOICE_FIELDS = {'Group': args.GROUP_TYPES}
args.FRAME_TOLERANCE = 0.001

args.WELCOME_TEXT = 'Welcome\n\nHi~\n\n'
args.CHORD_HELP_TEXT = 'Listen to the chord'
args.ANSWER_HELP_TEXT = 'Press <space> if the chord is the target chord and neglect it if it is not'

logger.info(args)
