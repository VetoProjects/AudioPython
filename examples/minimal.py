#!/usr/bin/env python
# That's some obfuscated shit, I know
import math
from AudioPython import *
from AudioPython import util

s = math.sin


def minimal():
    t = 0
    while 1:
        t += 0.000013
        q = 1 - (t * 2.15 % 1)
        yield clamp(s(27*q**24)*0.9 + 3*s(((q*4) % 1)**5*3) *
                    min(0.1, max(-0.1, 9*s(60*(1+q)*s(690+q*3)))), -1, 1)


channels = ((minimal(),),)
samples = compute_samples(channels)
write_wavefile("temp.wav", samples)
