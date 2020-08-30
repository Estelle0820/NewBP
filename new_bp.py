import psychopy

from param import *
from utils import *
from training_trial import *


class NewBP:

    def __init__(self):
        self.participant_info = show_dialog_box()
        self.group = args.GROUP_NAMES[self.participant_info['Group']]
        self.exp_info = get_experiment_info(self.participant_info.copy())
        self.this_exp = get_experiment_handler(self.exp_info)
        self.chord_manager = ChordManager(self.group)
        self.win = get_experiment_window()
        self.defaultKeyboard = psychopy.hardware.keyboard.Keyboard()

    def welcome(self):
        pass

    def train(self):
        pass

    def test(self):
        pass

    def run(self):
        self.welcome()
        self.train()
        self.test()


if __name__ == "__main__":
    new_bp = NewBP()
    new_bp.run()
