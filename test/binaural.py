#!/usr/bin/env python
from AudioPython import *

channels = ((sine_wave(440.0, amplitude=0.1),),
            (sine_wave("C5", amplitude=0.1),))

samples = compute_samples(channels)
for i in range(10):
    yield_raw(samples)
