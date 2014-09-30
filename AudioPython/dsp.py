#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import random
from itertools import count

from .util import *
from .effects import *


def sine_wave(frequency=440.0, framerate=44100, amplitude=0.5,
              skip_frame=0):
    """
    Generates a sine wave at a given frequency of infinite length.
    """
    if type(frequency) is str:
        frequency = note_to_freq(frequency)

    if amplitude > 1.0:
        amplitude = 1.0
    if amplitude < 0.0:
        amplitude = 0.0
    for i in count(skip_frame):
        sine = math.sin(math.pi * float(frequency) *
                        (float(i) / float(framerate)))
        yield float(amplitude) * sine


def square_wave(frequency=440.0, framerate=44100, amplitude=0.5,
                skipframe=0, rounding=1):
    """
    Generates a square wave at a given frequency of infinite length.
    """
    for s in sine_wave(frequency, framerate, amplitude=1.0,
                       skipframe=skipframe):
        yield amplitude * math.tan(rounding * s)


def damped_wave(frequency=440.0, framerate=44100, amplitude=0.5,
                length=44100, skipframe=0):
    """
    Generates a damped wave at a given frequency of infinite length.
    """
    if amplitude > 1.0:
        amplitude = 1.0
    if amplitude < 0.0:
        amplitude = 0.0
    return (math.exp(-(float(i % length)/float(framerate))) *
            s for i, s in enumerate(sine_wave(frequency,
                                    framerate, amplitude, skipframe)))


def sawtooth_wave(frequency=440.0, framerate=44100, amplitude=0.5,
                  skip_frame=0):
    """
    Generates a sawtooth wave at a given frequency of infinite length.
    """
    if type(frequency) is str:
        frequency = note_to_freq(frequency)
    if amplitude > 1.0:
        amplitude = 1.0
    if amplitude < 0.0:
        amplitude = 0.0
    while True:
        degree = (2.0 * math.pi * float(frequency) *
                  (float(i) / float(framerate)) % 360.0) / 360
        yield (-1 + degree * 2) * float(amplitude)


def leaky_integrator(gen, old=0.0, leak=0.99):
    """
    Sets up a leaky integrator on top of a given generator.
    Could be right. Maybe.
    TODO: Testing!
    """
    for i in gen:
        old = leak * old + i
        yield old


def triangle_wave(frequency=440.0, framerate=44100, amplitude=0.5,
                  skip_frame=100.0):
    """
    Generates a triangle wave at a given frequency of infinite length.
    """
    if type(frequency) is str:
        frequency = note_to_freq(frequency)
    if amplitude > 1.0:
        amplitude = 1.0
    if amplitude < 0.0:
        amplitude = 0.0
    while True:
        skip_frame += 0.0000114  # coefficient i found by playing around
        yield (abs(1 - (2 * skip_frame * frequency) % 2) * 2 - 1) * amplitude


def white_noise(amplitude=0.5):
    """Generates random samples."""
    if amplitude > 1.0:
        amplitude = 1.0
    if amplitude < 0.0:
        amplitude = 0.0
    return (float(amplitude) * random.uniform(-1, 1) for i in count(0))


def pink_noise(amplitude=0.5, ranged=128):
    """Generates pink noise based on Voss' algorithm."""
    if amplitude > 1.0:
        amplitude = 1.0
    if amplitude < 0.0:
        amplitude = 0.0
    max_pos = 0x1f  # five bits set
    pos = 0
    white_values = [0, 0, 0, 0, 0]
    for i in range(5):
        white_values[i] = random.randint(0, ranged//5)
    while True:
        last_pos = pos
        sumd = 0
        pos += 1
        if(pos > max_pos):
            key = 0
        diff = last_pos ^ pos
        for i in range(5):
            if(diff & (1 << i)):
                white_values[i] = random.randint(0, ranged//5)
            sumd += white_values[i]
        yield sumd * amplitude / 10


# def ringbuffer(gen, phase, decay=1.0, old=None):
#  """Generates a ringbuffer-like DSP. Sketch."""
#  old = tee(gen)
#  for index, i in enumerate(gen):
#    if index > phase:
#        gen = old
#        old = tee(gen)
#    yield i * decay
