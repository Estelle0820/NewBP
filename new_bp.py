from param import args
from utils import *

import log
logger = log.Logging.getLogger()


class NewBP:

    def __init__(self):
        self.participant_info = ExperimentManager.show_dialog_box()
        self.group = args.GROUP_NAMES[self.participant_info['Group']]
        self.exp_info = ExperimentManager.get_experiment_info(
            self.participant_info.copy())
        self.this_exp = ExperimentManager.get_experiment_handler(self.exp_info)
        self.win = ExperimentManager.get_experiment_window()
        self.chord_manager = ChordManager(self.group)
        self.timer = ExperimentManager.get_experiment_timer()
        self.default_keyboard = ExperimentManager.get_experiment_keyboard()
        # init components
        self.welcome_text = ExperimentManager.get_experiment_text(self.win,
                                                                  'welcome_text',
                                                                  args.WELCOME_TEXT)
        self.result_text = ExperimentManager.get_experiment_text(
            self.win, 'result_text', '')
        self.chord_help_text = ExperimentManager.get_experiment_text(
            self.win, 'chord_help_text', args.CHORD_HELP_TEXT)
        self.answer_help_text = ExperimentManager.get_experiment_text(
            self.win, 'answer_help_text',
            args.ANSWER_HELP_TEXT)
        self.key_resp = ExperimentManager.get_experiment_keyboard()

    def welcome(self):
        self.run_experiment_routine(
            args.MAX_WELCOME_SHOW_TIME, [self.welcome_text])

    def train(self):
        # init training loop
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
                self.result_text.setText('Training trial failed.')
                continue_training_trial = False
            if continue_training_trial:
                logger.info('Training %d:' % total_train_trial_count)
                logger.info('Chord: ' + chord.name)
                self.run_experiment_routine(
                    args.MAX_CHORD_PLAY_TIME, [self.chord_help_text, chord])
            # *Step 2: wait for key response*
                key_responsed = self.run_experiment_routine(args.MAX_KEY_WAIT_TIME,
                                                            [self.answer_help_text], self.key_resp)
            # *Step 3: check answer*
                total_train_trial_count += 1
                input_chord_type = ChordType.AAB if key_responsed else ChordType.ABC
                answer = self.chord_manager.check_chord(input_chord_type)
                logger.info('Correct: ' + str(answer))
                if answer:
                    correct_continuous_train_trial_count += 1
                    self.result_text.setText('Correct')
                else:
                    correct_continuous_train_trial_count = 0
                    self.result_text.setText('Incorrect')
                logger.info('Correct count: %d' %
                            correct_continuous_train_trial_count)
                if (correct_continuous_train_trial_count >= args.ACCEPT_CORRECT_TRIAL and total_train_trial_count > args.AT_LEAST_TRIAL):
                    # pass test
                    logger.info('Training trial succeed!')
                    self.result_text.setText('Training trial succeed')
                    continue_training_trial = False
            # *Step 4: Show result*
            self.run_experiment_routine(
                args.MAX_WELCOME_SHOW_TIME, [self.result_text])

    def test(self):
        pass

    def stop(self):
        ExperimentManager.stop_experiment(
            self.win, self.this_exp, self.exp_info)

    def run(self):
        self.welcome()
        self.train()
        self.test()

    def run_experiment_routine(self, count_down, components=[], key_resp=None):
        """
        Run a experiment routine with given components.
        Component type must be visual.TextStim/sound.Sound.
        """

        # *init*
        continueRoutine = True
        self.clock = ExperimentManager.get_experiment_clock()
        self.timer.add(count_down)
        key_responsed = None
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
        t = 0  # reset timers
        _timeToFirstFrame = self.win.getFutureFlipTime(clock="now")
        # t0 is time of first possible flip
        self.clock.reset(-_timeToFirstFrame)
        frameN = -1

        # *run routine*
        while continueRoutine and self.timer.getTime() > 0:
            # get current time
            t = self.clock.getTime()
            tThisFlip = self.win.getFutureFlipTime(clock=self.clock)
            tThisFlipGlobal = self.win.getFutureFlipTime(clock=None)
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
                        self.win.timeOnFlip(component, 'tStartRefresh')
                        component.setAutoDraw(True)
                    elif isinstance(component, sound.Sound):
                        component.play(when=self.win)  # sync with win flip
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
                        self.win.timeOnFlip(component, 'tStopRefresh')
                        component.setAutoDraw(False)
                    elif isinstance(component, sound.Sound):
                        # time at next scr refresh
                        self.win.timeOnFlip(component, 'tStopRefresh')
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
                    self.win.timeOnFlip(key_resp, 'tStartRefresh')
                    key_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    # t=0 on next screen flip
                    self.win.callOnFlip(key_resp.clock.reset)
                    # clear events on next screen flip
                    self.win.callOnFlip(
                        key_resp.clearEvents, eventType='keyboard')
                if key_resp.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp.tStartRefresh + count_down - args.FRAME_TOLERANCE:
                        # keep track of stop time/frame for later
                        key_resp.tStop = t  # not accounting for scr refresh
                        key_resp.frameNStop = frameN  # exact frame index
                        # time at next scr refresh
                        self.win.timeOnFlip(key_resp, 'tStopRefresh')
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
            if self.default_keyboard.getKeys(keyList=["escape"]):
                ExperimentManager.quit_experiment()
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for component in components if key_resp is None else components + [key_resp]:
                if hasattr(component, "status") and component.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                self.win.flip()

        # *end routine*
        if key_resp is not None:
            # check responses
            if key_resp.keys in ['', [], None]:  # No response was made
                key_resp.keys = None
            self.this_exp.addData('key_resp.keys', key_resp.keys)
            if key_resp.keys != None:  # we had a response
                self.this_exp.addData('key_resp.rt', key_resp.rt)
                key_responsed = True
        for component in components if key_resp is None else components + [key_resp]:
            if hasattr(component, "setAutoDraw"):
                component.setAutoDraw(False)
            if isinstance(component, sound.Sound):
                component.stop()
            if hasattr(component, "name"):
                self.this_exp.addData('%s.started' %
                                      component.name, component.tStartRefresh)
                self.this_exp.addData('%s.stopped' %
                                      component.name, component.tStopRefresh)

        return key_responsed


if __name__ == "__main__":
    new_bp = NewBP()
    new_bp.welcome()
