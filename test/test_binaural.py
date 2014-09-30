#!/usr/bin/env python
from AudioPython import *


def test_sine():
    channels = ((sine_wave(440.0, amplitude=0.1),),
                (sine_wave("C5", amplitude=0.1),))

    samples = compute_samples(channels)
    for i in range(1000):
        yield_raw(samples)


if __name__ == "__main__":
    test_sine()
