#!/usr/bin/env python
from AudioPython import *
from AudioPython import instruments, dsp, effects


def waves():
    l = int(44100*0.8)  # each note lasts 0.8 seconds
    return instruments.make_melody(note_list=[440.0, 261.63, 329.63, "A4",
                                              293.66, 261.63, 293.66],
                                   length_list=[l/4, l/4, l/2, l, l/4, l/4,
                                                l/2],
                                   default_amplitude=1.0, bar_length=l)


channels = ((effects.lowpass(waves(), 90),),
            (effects.lowpass(waves(), 90),),)

samples = compute_samples(channels)
write_wavefile("temp.wav", samples)
