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

def biquad_filter(gen, last=0.0, lastmixed=0.0, beforelast=0.0,
        beforelastmixed=0.0):
    """Emulates a biquad filter."""
    for i in gen:
        beforelast = last
        last = i
        beforelastmixed = lastmixed
        lastmixed = i +last + lastmixed + beforelast + beforelastmixed
        return lastmixed
