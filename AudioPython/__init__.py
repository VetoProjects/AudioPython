#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import struct
import argparse
from itertools import *

import wave
from util import *
from dsp import *

# Experimental python3 compatibility.
try:
    from itertools import izip
except ImportError:
    izip = zip
    imap = map
    izip_longest = zip_longest

__author__ = 'Veit Heller'
__author_mail__ = 's0539501@htw-berlin.de'
__version__ = '0.1'
__url__ = 'http://github.com/hellerve/AudioPython'
__longdescr__ = """
                An audio library based on wave-bender
                (https://github.com/zacharydenton/wavebender)
                for live coding music.
                """
__classifiers__ = [
            'Topic :: Multimedia :: Sound/Audio',
            'Topic :: Multimedia :: Sound/Audio :: Sound Synthesis'
            ]
__keywords__ = ['audio', 'live coding', 'music']

def compute_samples(channels, nsamples=None):
    """
    Creates a generator which computes the samples.

    essentially it creates a sequence of the sum of each function in the channel
    at each sample in the file for each channel.
    """
    return islice(izip(*(imap(sum, izip(*channel)) for channel in channels)), nsamples)

def write_wavefile(w, samples, nframes=None, nchannels=2, sampwidth=2, framerate=44100, bufsize=2048):
    """Write samples to a wavefile."""
    if nframes is None:
        nframes = -1

    if type(w) is str:
        w = wave.open(w, 'w')

    w.setparams((nchannels, sampwidth, framerate, nframes, 'NONE', 'not compressed'))

    max_amplitude = float(int((2 ** (sampwidth * 8)) / 2) - 1)

    # split the samples into chunks (to reduce memory consumption and improve performance)
    for chunk in grouper(bufsize, samples):
        frames = ''.join(''.join(str(struct.pack('h', int(max_amplitude * sample))) for sample in channels) for channels in chunk if channels is not None)
        w.writeframesraw(frames)

    w.close()

def yield_wavefile(samples, nframes=None, nchannels=2, sampwidth=2, framerate=44100, bufsize=2048):
    """Yield Samples."""
    if nframes is None:
        nframes = -1

    max_amplitude = float(int((2 ** (sampwidth * 8)) / 2) - 1)

    # split the samples into chunks (to reduce memory consumption and improve performance)
    for chunk in grouper(bufsize, samples):
        frames = ''.join(''.join(struct.pack('h', int(max_amplitude * sample)) for sample in channels) for channels in chunk if channels is not None)
        yield frames

def write_pcm(f, samples, sampwidth=2, framerate=44100, bufsize=2048):
    """Write samples as raw PCM data."""
    max_amplitude = float(int((2 ** (sampwidth * 8)) / 2) - 1)

    if type(f) is str:
        f = open(f, 'w')

    # split the samples into chunks (to reduce memory consumption and improve performance)
    for chunk in grouper(bufsize, samples):
        frames = ''.join(''.join(struct.pack('h', int(max_amplitude * sample)) for sample in channels) for channels in chunk if channels is not None)
        f.write(frames)

    f.close()

def main():
    parser = argparse.ArgumentParser(prog="AudioPython")
    parser.add_argument('-c', '--channels', help="Number of channels to produce", default=2, type=int)
    parser.add_argument('-b', '--bits', help="Number of bits in each sample", choices=(16,), default=16, type=int)
    parser.add_argument('-r', '--rate', help="Sample rate in Hz", default=44100, type=int)
    parser.add_argument('-t', '--time', help="Duration of the wave in seconds.", default=60, type=int)
    parser.add_argument('-a', '--amplitude', help="Amplitude of the wave on a scale of 0.0-1.0.", default=0.5, type=float)
    parser.add_argument('-f', '--frequency', help="Frequency of the wave in Hz", default=440.0, type=float)
    parser.add_argument('filename', help="The file to generate.")
    args = parser.parse_args()

    # each channel is defined by infinite functions which are added to produce a sample.
    channels = ((sine_wave(args.frequency, args.rate, args.amplitude),) for i in range(args.channels))

    # convert the channel functions into waveforms
    samples = compute_samples(channels, args.rate * args.time)

    # write the samples to a file
    if args.filename == '-':
        filename = sys.stdout
    else:
        filename = args.filename
    write_wavefile(filename, samples, args.rate * args.time, args.channels, args.bits / 8, args.rate)

if __name__ == "__main__":
    main()
