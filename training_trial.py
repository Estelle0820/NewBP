
# -*- coding: utf-8 -*-

import random

from psychopy.sound import Sound

from param import *
from utils import *
import log
logger = log.Logging.getLogger()


class ChordManager:
    """
    For chord picking and checking.
    """

    def __init__(self, participant_group):
        self.current_AAB_count = 0
        self.current_ABC_count = 0
        self.chord_AAB_list = []
        self.chord_ABC_list = []
        self.participant_group = participant_group
        self.chord_path = os.path.join(args.MUSIC_PATH, participant_group)
        self.chord_AAB_path = os.path.join(self.chord_path, 'AAB')
        self.chord_ABC_path = os.path.join(self.chord_path, 'ABC')
        self.fill_chord_lists()
        self.current_cord_type = None

    def fill_chord_lists(self):
        for file_name in read_all_files_in_directory(self.chord_AAB_path):
            chord_path = os.path.join(self.chord_AAB_path, file_name)
            chord = Sound(chord_path, secs=-1,
                          stereo=True, hamming=True, name='chord_AAB_%d' % file_name, volume=1.0)
            self.chord_AAB_list.append(chord)
        for file_name in read_all_files_in_directory(self.chord_ABC_path):
            chord_path = os.path.join(self.chord_ABC_path, file_name)
            chord = Sound(chord_path, secs=-1,
                          stereo=True, hamming=True, name='chord_ABC_%d' % file_name, volume=1.0)
            self.chord_ABC_list.append(chord)
        random.shuffle(self.chord_AAB_list)
        random.shuffle(self.chord_ABC_list)

    def choose_chord_type(self):
        """
        Randomly pick a chord type.
        """
        chord_type = ChordType.AAB if (
            random.random() > 0.5) else ChordType.ABC
        if chord_type == ChordType.AAB and self.current_AAB_count < 2:
            # AAB occurs less than 2 times, return AAB
            self.current_AAB_count += 1
            self.current_ABC_count = 0
            return ChordType.AAB
        elif chord_type == ChordType.AAB and self.current_AAB_count >= 2:
            # AAB occurs more than 2 times, returen ABC
            self.current_AAB_count = 0
            self.current_ABC_count += 1
            return ChordType.ABC
        elif chord_type == ChordType.ABC and self.current_ABC_count < 2:
            # ABC occurs less than 2 times, return ABC
            self.current_AAB_count = 0
            self.current_ABC_count += 1
            return ChordType.ABC
        elif chord_type == ChordType.ABC and self.current_ABC_count >= 2:
            # ABC occurs more than 2 times, return AAB
            self.current_AAB_count += 1
            self.current_ABC_count = 0
            return ChordType.AAB
        else:
            raise Exception

    def get_chord(self, refill):
        """
        Get a chord and return None if failed.
        """
        self.current_cord_type = self.choose_chord_type()
        # check if the chord lists is empty
        if (len(self.chord_AAB_list) == 0 or len(self.chord_ABC_list) == 0) and refill:
            self.fill_chord_lists()
        try:
            chord = self.chord_AAB_list.pop(
            ) if self.current_cord_type == ChordType.AAB else self.chord_ABC_list.pop()
        except IndexError:
            chord = None
        finally:
            return chord

    def check_chord(self, chord_type):
        """
        Check the chord type.
        """
        if self.current_cord_type is None or chord_type is None:
            raise Exception
        else:
            return chord_type == self.current_cord_type
