import math

from . import util

def leslie(gen, flan=[1.0, 0.0, 0.6, 1.0], nchannels=1, channel=1, frame=0,
            wet=0.5, feedback=0.5, t_amp=0.1, t_freq=0.0):
    """
    Emulates a leslie flanger.
    NOTE: This will not work until I have coded a flanger.
    """
    flange = flanger(*flan)
    if nchannels == 2:
        left, right = izip(*gen)
        for soundl, soundr in leslie(left), leslie(right, channel=2):
            yield (soundl, soundr)
    elif nchannels == 1:
        tf = t_freq if channel == 1 else t_freq*1.1
        for i in count(frame):
            ret = 0
            for sound in gen:
                ret += (next(flange(sound, wet, feedback)) *
                       next(tremolo(t_amp, tf)) + 1.0)
                yield ret

def chorus(gen, dry=0.5, wet=0.5, depth=1.0, delay=25.0, samplerate=44100,
    last=0.0):
  """Emulates a chorus."""
  adjust = float(samplerate) / 1000
  delay *= adjust
  depth *= adjust
  for i in gen:
    x = last
    last = i
    i = (i / 2 + 0.5) * depth + delay
    yield i * dry + x * wet

def flanger(gen, dry=0.5, wet=0.5, depth=25.0, delay=1.0, samplerate=44100,
    last=0.0):
  """Emulates a flanger."""
  adjust = float(rate) / 1000
  delay *= mil
  depth *= mil
  for i in gen:
    x = last
    last = i
    i = (i / 2 + 0.5) * depth + delay
    yield feedback_modulated_delay(data, modwave, dry, wet)

def tremolo(gen, dry=0.5, wet=0.5):
  """Emulates a tremolo."""
  for i in gen:
    mod = i / 2 + 0.5
    yield (mod / 2 + 0.5)  * dry + (i * mod) * wet

def modulated_delay(gen, dry, wet, last=0.0):
  """Emulates a modulated delay."""
  for i in gen:
    x = last
    last = i
    yield i * dry + x * wet

def lowpass(gen, cutoff, samplerate=44100):
    """Emulates a lowpass filter(butterworth)."""
    coeff = 1.0 / math.tan(math.pi * cutoff / samplerate)
    b0 = 1.0 / ( 1.0 + math.sqrt(2.0) * coeff + coeff * coeff)
    b1 = 2.0 * b0
    b2 = b0
    a1 = 2.0 * b0 * (1.0 - coeff * coeff)
    a2 = b0 * (1.0 - math.sqrt(2.0) * coeff + coeff * coeff)
    for i in biquad_filter(gen, b0, b1, b2, a1, a2): yield i

def highpass(gen, cutoff, samplerate=44100):
    """Emulates a highpass filter(butterworth)."""
    coeff = math.tan(math.pi * cutoff / samplerate)
    b0 = 1.0 / ( 1.0 + math.sqrt(2.0) * coeff + coeff * coeff)
    b1 = -2.0 * b0
    b2 = b0
    a1 = 2.0 * b0 * (coeff * coeff -1.0)
    a2 = b0 * (1.0 - math.sqrt(2.0) * coeff + coeff * coeff)
    for i in biquad_filter(gen, b0, b1, b2, a1, a2): yield i

def biquad_filter(gen, b0=0.0, b1=0.0, b2=0.0, a1=0.0, a2=0.0,
    y = 0.0, y1=0.0, y2=0.0, x1=0.0, x2=0.0):
    """
    Emulates a biquad filter. Ugly variable names, but if you know biquad,
    they should look familiar to you, as they are mostly named the same
    in examples.
    """
    for x in gen:
        y = b0 * x + b1 * x1 + b2 * x2 - a1 * y1 - a2 * y2
        y1, y2 = y, y1
        x1, x2 = x, x1
        yield y
