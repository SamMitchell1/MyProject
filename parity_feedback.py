#! /usr/bin/env python
# Time-stamp: <2021-03-24 14:41:36 christophe@pallier.org>
"""Three digit number comparison

At each trial, a number between 100 and 999 is presented at the center of the
screen and the participant must press the key 'f' if the number is larger, 'j' if
it is small.

"""

import random
from expyriment import design, control, stimuli, misc

MAX_RESPONSE_DELAY = 2000
LRG_RESPONSE_KEY = misc.constants.K_f
SML_RESPONSE_KEY = misc.constants.K_j
BUZZER = 'wrong-answer.ogg'

exp = design.Experiment(name="Three Digit Number Comparison", text_size=40)

control.initialize(exp)
#need to include some cue number 555 
cue = stimuli.FixCross(size=(50, 50), line_width=4)
blankscreen = stimuli.BlankScreen()

block = design.Block()
targets = expyriment.design.randomize.rand_int(100, 999) 
random.shuffle(targets)
for number in targets:
    t = design.Trial()
    t.set_factor('number', number)
    t.set_factor('is_even', number % 2 == 0)
    t.add_stimulus(stimuli.TextLine(str(number)))
    block.add_trial(t)

negative_feedback = stimuli.Audio(BUZZER)

instructions = stimuli.TextScreen("Instructions",
    f"""When you'll see a number, your task to decide, as quickly as possible, whether it is larger or smaller.

    if it is larger, press '{chr(LRG_RESPONSE_KEY)}'

    if it is smaller, press '{chr(SML_RESPONSE_KEY)}'

    There will be {len(targets)} trials in total.

    Press the space bar to start.""")


exp.add_data_variable_names(['number', 'is_larger', 'respkey', 'RT', 'is_correct'])

control.start(skip_ready_screen=True)
instructions.present()
exp.keyboard.wait()

for trial in block.trials:
    blankscreen.present()
    exp.clock.wait(1000)
    cue.present()
    exp.clock.wait(500)
    trial.stimuli[0].present()
    key, rt = exp.keyboard.wait([EVEN_RESPONSE_KEY, ODD_RESPONSE_KEY], duration=MAX_RESPONSE_DELAY)

    is_correct_answer = (trial.get_factor('is_larger') and key == LRG_RESPONSE_KEY) or \
                        (not trial.get_factor('is_smaller') and key ==  SML_RESPONSE_KEY)
    if not is_correct_answer:
            negative_feedback.play()

    exp.data.add([trial.get_factor('number'), trial.get_factor('is_larger'), key, rt, is_correct_answer])

control.end()
