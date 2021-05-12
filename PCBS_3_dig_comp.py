#! /usr/bin/env python
# Time-stamp: <2021-03-24 08:15:54 christophe@pallier.org>
"""This is a simple decision experiment.
At each trial, a number between 0 and 9 is presented at the center of the
screen and the participant must press the key 'f' if the number is even, 'j' if         
it is odd.
"""

import random
from expyriment import design, control, stimuli, misc
from random import sample

#generate random numbers 

all_numbers = list(random.sample(range(100, 999), 20))

#exclude cue number
exclude_set = {555} 

numbers = list(num for num in all_numbers if num not in exclude_set)

MAX_RESPONSE_DELAY = 2000
LRG_RESPONSE_KEY = 'f'
SML_RESPONSE_KEY = 'j'

exp = design.Experiment(name="3 Digit Comparison task", text_size=40)
control.initialize(exp)

cue = stimuli.TextLine("555")
blankscreen = stimuli.BlankScreen()

block = design.Block()
TARGETS = numbers
random.shuffle(TARGETS)
for number in TARGETS:
    t = design.Trial()
    t.set_factor('number', number)
    t.set_factor('is_larger', number > 555)
    t.set_factor('is_smaller', number < 555)
    t.add_stimulus(stimuli.TextLine(str(number)))
    block.add_(t) #error here: 'Block' has not attribute 'add'

instructions = stimuli.TextScreen("Instructions",
    f"""When you'll see a number, your task to decide, as quickly as possible, whether it is larger or smaller.
    if it is larger, press '{LRG_RESPONSE_KEY}'
    if it is smaller, press '{SML_RESPONSE_KEY}'
    There will be {len(TARGETS)} trials in total. 
    Press the space bar to start.""")

# prepare the stimuli
trials = []
for number in TARGETS:
    trials.append((number, stimuli.TextLine(str(number))))


exp.add_data_variable_names(['number', 'is_even', 'respkey', 'RT', 'is_correct'])

control.start(skip_ready_screen=True)
instructions.present()
exp.keyboard.wait()

for trial in block.trials:
    blankscreen.present()
    exp.clock.wait(1000)
    cue.present()
    exp.clock.wait(500)
    trial[1].present()
    key, rt = exp.keyboard.wait([LRG_RESPONSE_KEY, SML_RESPONSE_KEY], duration=MAX_RESPONSE_DELAY)
##error here: 'trial' has not attribute 'get_factor'
    is_correct_answer = (trial.get_factor('is_larger') and key == LGR_RESPONSE_KEY) or \
                        (trial.get_factor('is_smaller') and key ==  SML_RESPONSE_KEY)
    exp.data.add([trial.get_factor('number'), trial.get_factor('is_larger'), key, rt, is_correct_answer])

control.end()
