import random
from psychopy import sound

# parameters
CHORD_AAB_COUNT = 7
CHORD_ABC_COUNT = 7
AT_LEAST_TRIAL = 5
ACCEPT_CORRECT_TRIAL = 3


# variables
chord_AAB_list = []s
chord_ABC_list = []


for i in range(CHORD_AAB_COUNT):
    chord = sound.Sound('./assets/music/AAB/%d.wav' % i, secs=-1, stereo=True, hamming=True, name='chord_AAB_%d' % i, volume=1.0)
for i in range(CHORD_ABC_COUNT):
    chord = sound.Sound('./assets/music/ABC/%d.wav' % i, secs=-1, stereo=True, hamming=True, name='chord_ABC_%d' % i, volume=1.0)
