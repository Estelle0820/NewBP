# -*- coding: utf-8 -*-

import os

import log
logger = log.Logging.getLogger()

# parameters
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
ASSETS_PATH = os.path.join(ROOT_PATH, 'assets')
CHORD_AAB_PATH = os.path.join(ASSETS_PATH, 'music/AAB')
CHORD_ABC_PATH = os.path.join(ASSETS_PATH, 'music/ABC')
CHORD_AAB_COUNT = 7
CHORD_ABC_COUNT = 7
AT_LEAST_TRIAL = 5
ACCEPT_CORRECT_TRIAL = 3
MAX_CHORD_PLAY_TIME = 3.0
MAX_KEY_WAIT_TIME = 2.0
MAX_RESULT_PLAY_TIME = 1.0
