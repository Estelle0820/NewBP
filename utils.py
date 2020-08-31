from __future__ import absolute_import, division

import os  # handy system and path functions
import random
import psychopy
from enum import Enum
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, clock
from psychopy.hardware import keyboard
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

from param import args


class ChordType(Enum):
    """
    Defines types of chord.
    """
    AAB = 0
    ABC = 1


class ChordManager:
    """
    For chord picking and checking.
    """

    def __init__(self, participant_group, is_training=True):
        self.current_AAB_count = 0
        self.current_ABC_count = 0
        self.chord_AAB_list = []
        self.chord_ABC_list = []
        self.participant_group = participant_group
        self.chord_path = os.path.join(
            args.MUSIC_PATH, participant_group, 'training' if is_training else 'test')
        self.chord_AAB_path = os.path.join(self.chord_path, 'AAB')
        self.chord_ABC_path = os.path.join(self.chord_path, 'ABC')
        self.fill_chord_lists()
        self.current_cord_type = None

    def clear_chord_lists(self):
        self.chord_AAB_list = []
        self.chord_ABC_list = []

    def fill_chord_lists(self):
        for file_name in ExperimentManager.read_all_files_in_directory(self.chord_AAB_path):
            chord_path = os.path.join(self.chord_AAB_path, file_name)
            chord = sound.Sound(chord_path, secs=-1,
                                stereo=True, hamming=True, name='chord_AAB_%s' % file_name, volume=1.0)
            self.chord_AAB_list.append(chord)
        for file_name in ExperimentManager.read_all_files_in_directory(self.chord_ABC_path):
            chord_path = os.path.join(self.chord_ABC_path, file_name)
            chord = sound.Sound(chord_path, secs=-1,
                                stereo=True, hamming=True, name='chord_ABC_%s' % file_name, volume=1.0)
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
            self.clear_chord_lists()
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


class ExperimentManager():
    """
    Util class for experiment
    """

    @staticmethod
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

    @staticmethod
    def quit_experiment():
        """
        Quit the experiment and end the process.
        """
        core.quit()

    @staticmethod
    def stop_experiment(win, this_exp, exp_info):
        """
        Stop the experiment and release all resources.
        """
        # Flip one final time so any remaining win.callOnFlip()
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()

        # these shouldn't be strictly necessary (should auto-save)
        data_save_path = ExperimentManager.get_data_save_path(exp_info)
        this_exp.saveAsWideText(data_save_path + '.csv')
        this_exp.saveAsPickle(data_save_path)
        this_exp.abort()  # or data files will save again on exit
        win.close()
        ExperimentManager.quit_experiment()

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
                    ExperimentManager.quit_experiment()
            participant_info_fields = args.DIALOG_NORMAL_FIELDS + \
                list(args.DIALOG_CHOICE_FIELDS.keys())
            participant_info = dict(zip(participant_info_fields, dlg_results))
            return participant_info
        else:
            ExperimentManager.quit_experiment()

    @staticmethod
    def get_experiment_info(exp_info):
        """
        Return an dict of experiment info.
        """
        exp_info['ExperimentName'] = args.EXPERIMENT_NAME
        exp_info['Date'] = data.getDateStr()
        exp_info['PsychoPyVersion'] = psychopy.__version__
        return exp_info

    @staticmethod
    def get_data_save_path(exp_info):
        """
        Return the path for data saving.
        """
        data_save_directory = os.path.join(
            args.DATA_PATH, '%s_%s' % (exp_info['Student ID'], exp_info['Name']))
        data_save_path = os.path.join(
            data_save_directory, '%s' % exp_info['Date'])
        return data_save_path

    @staticmethod
    def get_experiment_handler(exp_info):
        """
        An ExperimentHandler isn't essential but helps with data saving.
        """
        data_save_path = ExperimentManager.get_data_save_path(exp_info)
        this_exp = data.ExperimentHandler(name=exp_info['ExperimentName'],
                                          version=exp_info['PsychoPyVersion'],
                                          extraInfo=exp_info,
                                          runtimeInfo=None,
                                          originPath=os.path.abspath(__file__),
                                          savePickle=True,
                                          saveWideText=True,
                                          dataFileName=data_save_path)
        return this_exp

    @staticmethod
    def get_experiment_window(size=(1024, 768), fullscr=args.FULL_SCREEN,
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
        """
        Return a clock.
        """
        return core.Clock()

    @staticmethod
    def get_experiment_keyboard():
        """
        Return a keyboard.
        """
        return keyboard.Keyboard()

    @staticmethod
    def get_experiment_timer():
        """
        Return a countdown timer.
        """
        return core.CountdownTimer()

    @staticmethod
    def get_experiment_text(win, name, text, pos=(0, 0), height=0.1):
        """
        Return a text stim.
        """
        text = visual.TextStim(win=win, name=name,
                               text=text,
                               font='Arial',
                               pos=pos, height=height, wrapWidth=None, ori=0,
                               color='white', colorSpace='rgb', opacity=1,
                               languageStyle='LTR',
                               depth=0.0)
        return text
