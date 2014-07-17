#!/usr/bin/env python
#Idea taken from www.wavepot.com

import math

from itertools import *
from AudioPython import *
from AudioPython.dsp import *

def bass_osc(n):
    tri = triangle_wave(frequency=n, amplitude=0.24)
    sine = sine_wave(frequency=n*32, amplitude=0.052)
    for i in count(0):
        yield next(tri) + next(sine)

def sub(gen, amp):
    c = 0
    tau = 2 * math.pi
    for i in count(0):
        c += 0.000014
        yield math.sin(next(gen) * (1 + math.sin(1.1337 * c * tau)) * (2 + (1 +
                math.sin(0.42 * c * tau)) * 15) + tau * c) * amp

n = 44100 / 500

channels = ((sub(bass_osc(n), 0.3),),)
samples = compute_samples(channels)
write_wavefile("temp.wav", samples)
