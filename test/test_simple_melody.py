#!/usr/bin/env python
import pickle
import codecs

from AudioPython import *
from AudioPython import instruments, dsp, effects


def waves():
    l = int(44100*0.4)  # each note lasts 0.4 seconds
    return instruments.make_melody(note_list=[440.0, 261.63, 329.63, "A4",
                                              293.66, 261.63, 293.66],
                                   length_list=[l/4, l/4, l/2, l, l/4, l/4,
                                                l/2],
                                   default_amplitude=1.0, bar_length=l)


def test_lowpass_make_melody():
    dump = make_check()

    channels = ((effects.lowpass(waves(), 90),),
                (effects.lowpass(waves(), 90),),)

    samples = compute_samples(channels)

    for i, sample in enumerate(yield_raw(samples)):
        if dump[i] != sample:
            raise ValueError("%s yielded wrong value on %s call." %
                             (__file__, i))
        if i == 1000:
            break


def make_check():
    channels = ((effects.lowpass(waves(), 90),),
                (effects.lowpass(waves(), 90),),)

    samples = compute_samples(channels)

    dump = []

    for i, sample in enumerate(yield_raw(samples)):
        dump.append(sample)
        if i == 1000:
            break
    return dump

if __name__ == "__main__":
    test_lowpass_make_melody()
