#!/usr/bin/env python
#Idea taken from www.wavepot.com
import math

from AudioPython import *

transpose = 2.0
bpm = 240   # Beats per minute
spb = 60.0/bpm    # Second per beat

def note(n, octave):
    n += transpose
    return pow(2, (n - 33 + (12 * (octave or 0))) / 12) * 440

melodies = [
  [note(3,2), note(7,2), note(10,2), note(2,3), note(3,3), note(7,3), note(3,3), note(2,3)],
  [note(0,2), note(3,2), note(7,2), note(10,2), note(0,3), note(7,2), note(3,2), note(7,2)],
  [note(8,1), note(0,2), note(3,2), note(7,2), note(8,2), note(7,2), note(8,2), note(7,2)],
  [note(5,1), note(10,2), note(2,2), note(5,2), note(10,3), note(2,3), note(5,3), note(2,3)]
]

bassline = [
  [note(3,1),note(3,1),note(3,1),note(3,1),note(3,1),note(3,1),note(3,1),note(2,1)],
  [note(0,1),note(0,1),note(0,1),note(0,1),note(0,1),note(0,1),note(0,1),note(-2,1)],
  [note(8,0),note(8,0),note(8,0),note(8,0),note(8,0),note(8,0),note(8,0),note(7,0)],
  [note(5,0),note(5,0),note(5,0),note(5,0),note(8,0),note(5,0),note(8,0),note(2,1)]
]


def melody(t = 0):
    counter = 0
    while True:
        t += 0.000013 # try setting that to 1. its... interesting
        counter = math.floor(t/spb) #How many beats have passed
        #Changes note every 8beat, alter chord every 16 beats
        yield (sqr(t, melodies[int(math.floor(counter/16)%4)][int(counter%8)], 0.11)
            + sqr(t, bassline[int(math.floor(counter/16)%4)][int(counter%8)], 0.11))

def sin(t, f, a):
  return a * math.sin(2 * math.pi *  t * f)

def sqr(t,f,a):
  return  ((sin(t, f, a) > 0) * 2 - 1) * a

def test_complex():
    channels = ((melody(1),),)
    samples = compute_samples(channels)
    for i in range(1000):
        yield_raw(samples)

if __name__ == "__main__":
    test_complex()
