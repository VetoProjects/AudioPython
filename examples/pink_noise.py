#!/usr/bin/env python
from AudioPython import *
from AudioPython.dsp import *
import sys

channels = ((pink_noise(amplitude=0.01),),)

samples = compute_samples(channels)
write_wavefile("temp.wav", samples)
