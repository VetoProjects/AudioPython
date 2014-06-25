#!/usr/bin/env python
from AudioPython import *
from AudioPython import instruments, dsp

def waves():
    l = int(44100*0.4) # each note lasts 0.4 seconds
    return instruments.make_melody([440.0, 261.63, 329.63, 440.0, 293.66, 261.63, 293.66],
            [l/4, l/4, l/2, l, l/4, l/4, l/2],
            default_amplitude=0.5, bar_length=l)

channels = ((waves(),), (waves(), dsp.white_noise(amplitude=0.001),))

samples = compute_samples(channels, None)
write_wavefile("temp.wav", samples, None)
