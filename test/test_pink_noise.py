#!/usr/bin/env python
from AudioPython import *
from AudioPython.dsp import *
import sys

def test_pink_noise():
    channels = ((pink_noise(amplitude=0.01),),)

    samples = compute_samples(channels)
    for i in range(10):
        yield_raw(samples)

if __name__ == "__main__":
    test_pink_noise()
