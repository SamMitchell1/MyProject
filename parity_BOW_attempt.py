#! /usr/bin/env python
# Time-stamp: <2021-03-24 08:15:54 christophe@pallier.org>
"""This is a simple decision experiment.

At each trial, a number between 0 and 9 is presented at the center of the
screen and the participant must press the key 'f' if the number is even, 'j' if
it is odd.

"""

import random
from expyriment import design, control, stimuli

MAX_RESPONSE_DELAY = 10000
TARGETS = []#insert strings from BOW
CAT1_RESPONSE = '1'
CAT2_RESPONSE = '2'
CAT3_RESPONSE = '3'
CAT4_RESPONSE = '4'
CAT5_RESPONSE = '5'
exp = design.Experiment(name="Parity Decision", text_size=10)
control.initialize(exp)

cue = stimuli.FixCross(size=(50, 50), line_width=4)
blankscreen = stimuli.BlankScreen()
instructions = stimuli.TextScreen("Instructions",
    f"""When you'll see a para, your task to decide, as quickly as possible, which category it belongs to.

if it is [CAT1] press '{KEY_1}'

if it is [CAT2] press '{KEY_2}''

if it is [CAT3] press '{KEY_3}'

if it is [CAT4] press '{KEY_4}'

if it is [CAT5] press '{KEY_5}'

    There will be {len(TARGETS)} trials in total.

    Press the space bar to start.""")

# prepare the stimuli
trials = []
for number in TARGETS:
    trials.append((number, stimuli.TextLine(str))


exp.add_data_variable_names(['text', 'respkey', 'RT'])

control.start(skip_ready_screen=True)
instructions.present()
exp.keyboard.wait()

for t in trials:
    blankscreen.present()
    exp.clock.wait(1000)
    cue.present()
    exp.clock.wait(10000)
    t[1].present()
    key, rt = exp.keyboard.wait(CAT1_RESPONSE + CAT2_RESPONSE + CAT3_RESPONSE + CAT4_RESPONSE + CAT5_RESPONSE, duration=MAX_RESPONSE_DELAY)
    exp.data.add([t[0],  key, rt])

control.end()
