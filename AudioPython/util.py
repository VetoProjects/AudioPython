#!/usr/bin/env python
# -*- coding: utf-8 -*-

import operator
import random
from itertools import *

# Experimental python3 compatibility.
try:
    from itertools import izip
except ImportError:
    izip = zip
    imap = map
    izip_longest = zip_longest


"""A note lookup table from C0 to B8"""
note_lookup = {"C0": 16.35, "C#0": 17.32, "D0": 18.35, "D#0": 19.45,
               "E0": 20.60, "F0": 21.83, "F#0": 23.12, "G0": 24.50,
               "G#0": 25.96, "A0": 27.50, "A#0": 29.14, "B0": 30.87,
               "C1": 32.70, "C#1": 34.65, "D1": 36.71, "D#1": 38.89,
               "E1": 41.20, "F1": 43.65, "F#1": 46.25, "G1": 49.00,
               "G#1": 51.91, "A1": 55.00, "A#1": 58.27, "B1": 61.74,
               "C2": 65.41, "C#2": 69.30, "D2": 73.42, "D#2": 77.78,
               "E2": 82.41, "F2": 87.31, "F#2": 92.50, "G2": 98.00,
               "G#2": 103.83, "A2": 110.00, "A#2": 116.54, "B2": 123.47,
               "C3": 130.81, "C#3": 138.59, "D3": 146.83, "D#3": 155.56,
               "E3": 164.81, "F3": 174.61, "F#3": 185.00, "G3": 196.00,
               "G#3": 207.65, "A3": 220.00, "A#3": 233.08, "B3": 246.94,
               "C4": 261.63, "C#4": 277.18, "D4": 293.66, "D#4": 311.13,
               "E4": 329.63, "F4": 349.23, "F#4": 369.99, "G4": 392.00,
               "G#4": 415.30, "A4": 440.00, "A#4": 466.16, "B4": 493.88,
               "C5": 523.25, "C#5": 554.37, "D5": 587.33, "D#5": 622.25,
               "E5": 659.25, "F5": 698.46, "F#5": 739.99, "G5": 783.99,
               "G#5": 830.61, "A5": 880.00, "A#5": 932.33, "B5": 987.77,
               "C6": 1046.50, "C#6": 1108.73, "D6": 1174.66, "D#6": 1244.51,
               "E6": 1318.51, "F6": 1396.91, "F#6": 1479.98, "G6": 1567.98,
               "G#6": 1661.22, "A6": 1760.00, "A#6": 1864.66, "B6": 1975.53,
               "C7": 2093.00, "C#7": 2217.46, "D7": 2349.32, "D#7": 2489.02,
               "E7": 2637.02, "F7": 2793.83, "F#7": 2959.96, "G7": 3135.96,
               "G#7": 3322.44, "A7": 3520.00, "A#7": 3729.31, "B7": 3951.07,
               "C8": 4186.01, "C#8": 4434.92, "D8": 4698.63, "D#8": 4978.03,
               "E8": 5274.04, "F8": 5587.65, "F#8": 5919.91, "G8": 6271.93,
               "G#8": 6644.88, "A8": 7040.00, "A#8": 7458.62, "B8": 7902.13}

"""A lookup table of operations"""
op_codes = {'>': operator.lt, '>=': operator.le, '==': operator.eq,
            '!=': operator.ne, '<=': operator.ge, '<': operator.gt,
            'not': operator.ne, 'is': operator.eq, '+': operator.add,
            '-': operator.sub, '*': operator.mul, '/': operator.truediv,
            '//': operator.floordiv, '%': operator.mod, '<<': operator.lshift,
            '>>': operator.rshift, '|': operator.or_, '&':operator.and_,
            'or': operator.or_, 'and': operator.and_, '**': operator.pow,
            '^': operator.xor, 'xor': operator.xor}

"""
A markov matrix for ratios when which cadence is usually played
(useful for random progressions).
"""
cadence_markov = [[0, 0, 0.25, 0.25, 0.25, 0.35],
                  [0, 0, 0, 0, 0.5, 0, 0.5],
                  [0, 0, 0, 0, 0, 1],
                  [0.25, 0.25, 0, 0, 0.25, 0, 0.25],
                  [0.5, 0, 0, 0, 0, 0.5],
                  [0, 0.5, 0, 0.5],
                  [0.5, 0, 0, 0, 0.5]]

def next_note(current):
    """
    Returns a random next note for the currently played note.
    Formula should work. Maybe.
    TODO: Testing!
    """
    if current < 1:
        current = 1
    if current > 7:
        current = 7
    x = random.random()
    sumx = 0
    for i, prob in enumerate(cadence_markov[current]):
        sumx += prob
        if sumx >= x:
            return i

def grouper(n, iterlist, fillvalue=None):
	"""
	Slices iterlist into sublists of length n
	and groups them if necessary.
	"""
	args = [iter(iterlist)] * n
	return izip_longest(fillvalue=fillvalue, *args)

def ncycles(iterable, n):
    "Returns the sequence elements n times"
    return chain.from_iterable(repeat(tuple(iterable), n))

def note_to_freq(note):
    """Translates a note to a corresponding frequency"""
    try:
        return note_lookup[note]
    except KeyError:
        raise ValueError("No such note. Maybe you chose a flat note?")

def apply_fun(generator, function, args):
	"""Applies a function to a generator"""
	while True:
		yield function(next(generator), *args)

def apply_op(g, h, op):
	"""Applies the operator to two generators"""
	if type(op) is str:
		try:
			op = op_codes[op]
		except KeyError:
			ArithmeticError("No such operation on generators.")
	while True:
		yield op(next(g), next(h))
