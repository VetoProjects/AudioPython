AudioPython
===========

An audio module for Python that is included in a Live Coding Environment I currently work on;
it is based on [wavebender](https://github.com/zacharydenton/wavebender/) and relies heavily
on such constructs as itertools, generators and lambdas. Note that it is in development and
not really usable up until now although you can create really neat sounds if you work really
hard.

The idea is that in the end you will only have to fill the channels with generators(waves or
samples) and the environment will iterate through it endlessly(calling `yield_wavefile()`). 
You will be able to add to them and update to them on the fly as the encoding is done in 
8kb chunks, so the next 8kb will be the updated melody/beat(if you specify a speed, I will
even be able to compute where the next bar begins and update there instead of in the middle
of the beat, which will make it sound more natural).

If you wait a few weeks, it might become something useful. :)
