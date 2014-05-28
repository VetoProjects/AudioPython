#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from dsp import *
from itertools import *
from util import *

def make_melody(note_list, length_list, amplitude_list,
                bar_length=11025, default_length=0.25,
                default_amplitude=0.5):
    """
    Returns a melody of notes specified in not_list
    that is mapped to length.
    """
    tones = []
    second_length = len(length_list)
    third_length = len(amplitude_list)
    for note, index in enumerate(note_list):
        if type(note) is str:
            note = note_to_freq(note)
        if index < second_length:
            length = length_list[index]
        else:
            length = default_length
        if index < third_length:
            amp = amplitude_list[index]
        else:
            length = default_amplitde
        tones.append(islice(damped_wave(frequency=note, amplitude=amp,
                                        length=length),
                            bar_length))
    return cycle(chain(*tones))

def concat_melodies(melodylist):
    """
    Concatenates two or melodies and returns a
    cycle of those.
    """
    return cycle(chain(*melodylist))

def hammond(frequency, drawbar_positions):
    """Returns a hammond organ-like sound."""
    freq_ratio = [0.5, 1.5, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 8.0]
    drawbars = ()
    for i in range(8):
        drawbars + (sine_wave(frequency=freq_ratio[i]*frequency,
                              amplitude=drawbar_positions[i]/9),)
    return leslie(gen)

def leslie(gen, flan=[1.0, 0.0, 0.6, 1.0], nchannels=1, channel=1, frame=0,
            wet=0.5, feedback=0.5, t_amp=0.1, t_freq=0.0):
    """Emulates a leslie flanger."""
    flange = flanger(*flan)
    if nchannels == 2:
        left, right = izip(*gen)
        return (leslie(left), leslie(right, channel=2))
    elif nchannels == 1:
        tf = t_freq if channel == 1 else t_freq*1.1
        for i in count(frame):
            ret = 0
            for sound in gen:
                ret += next(flange(sound, wet, feedback)) *
                       next(tremolo(t_amp, tf) + 1.0
            yield ret

def random_progression(scale, start=1, gen=damped_wave, args):
    """
    Yields a random progression.
    Formula should work. Maybe.
    TODO: Testing!
    """
    for i in scale:
        if type(i) is str:
            i = note_to_freq(i)
    if start < 1:
        start = 1
    if start > 7:
        start = 7
    current = scale[start-1]
    while True:
        current = scale[next_note(current)]
        if args:
            yield gen(current, *args)
        else:
            yield gen(current)

def flanger():
    """Emulates a flanger"""
    yield 1

def chorus():
    """Emulates a chorus"""
    yield 1

def delay(gen, delay, frame=0, _n=0, _y=0.0):
    """Emulates a delay"""
#    for i, x in count(frame), next(gen):
#        _n = time-1 % delay
#        _y = x gen (pref?)



#(bind-func delay_c
#  (lambda (max_delay:i64)
#    (let ((delay max_delay)
#          (line:SAMPLE* (zalloc delay))
#(time 0)
#          (n 0)
#          (y 0.0))
#      (lambda (x:SAMPLE wet feedback)
#        (set! n (modulo time delay))
#        (set! y (pref line n))
#        (set! time (+ time 1))
#        (pset! line n (* feedback (+ x y)))
#        (+ x (* y wet))))))


def make_instrument(suffix, directory_name, path="./instruments/"):
    """Creates a dict of samples that can be played by the instrument"""
    search = re.compile(".*" + suffix)
    resuffix = re.compile(suffix)
    matches = filter(lambda x: search.match(x),
                os.listdir(path + directory_name))
    names = [resuffix.split(i)[0] for i in matches]
    sampledict = {}
    for name in names:
        search = re.compile(name + suffix)
        sampledict[name] = filter(lambda x: search.match(x),
                                os.listdir(path + directory_name))
    return sampledict

def get_sample(name, sampledict, loudness=0.5):
    """Gets a sample for a note of the instrument at a given loudness"""
    if loudness > 1.0:
        loudness = 1.0
    if loudness < 0.0:
        loudness = 0.0
    samples = sampledict[name]
    if len(samples) != 0:
        comp = 1.0/len(samples)
    else:
        raise ValueError("No such key.")
    i = 0
    while comp < loudness:
        comp += 1.0/len(samples)
        i += 1
    return samples[i]
