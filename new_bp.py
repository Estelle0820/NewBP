import psychopy

from param import *
from utils import *
from training_trial import *


class NewBP:

    def __init__(self):
        self.participant_info = ExperimentManager.show_dialog_box()
        self.group = args.GROUP_NAMES[self.participant_info['Group']]
        self.exp_info = ExperimentManager.get_experiment_info(
            self.participant_info.copy())
        self.this_exp = ExperimentManager.get_experiment_handler(self.exp_info)
        self.chord_manager = ChordManager(self.group)
        self.win = ExperimentManager.get_experiment_window()
        self.default_keyboard = psychopy.hardware.keyboard.Keyboard()

    def welcome(self):
        welcome_text = ExperimentManager.get_experiment_text(self.win,
                                                             'welcome_text',
                                                             'Welcome\n\nHi~\n\n')
        ExperimentManager.run_experiment_routine(
            self.win, self.default_keyboard,
            self.this_exp, args.MAX_WELCOME_SHOW_TIME,
            [welcome_text])

    def train(self):
        result_text = ExperimentManager.get_experiment_text(self.win, 'result_text', '')
        chord_help_text = ExperimentManager.get_experiment_text(self.win, 'result_text', 'Listen to the chord.')

        args.MAX_CHORD_PLAY_TIME
        total_train_trial_count = 0
        correct_continuous_train_trial_count = 0
        continue_training_trial = True
        while continue_training_trial:
            # *Step 1: play music*
            refill = total_train_trial_count > args.AT_LEAST_TRIAL
            chord = self.chord_manager.get_chord(refill)  # select music
            if chord is None:
                # failed test
                logger.info('Training trial failed.')
                result_text.setText('Training trial failed.')
                continue_training_trial = False

    def test(self):
        pass

    def run(self):
        self.welcome()
        self.train()
        self.test()


if __name__ == "__main__":
    new_bp = NewBP()
    new_bp.run()
