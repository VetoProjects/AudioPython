AudioPython
===========

An audio module for Python that is included in a Live Coding Environment I currently work on;
it is based on [wavebender](https://github.com/zacharydenton/wavebender/) and relies heavily
on such constructs as itertools, generators and lambdas, all in all it is based on the
functional parts of Python - Guido would hate it. Note that it is in development and
not really usable up until now although you can create really neat sounds if you work really
hard.

Table of Contents
-----------------
1. **[Requirements](#requirements)**
2. **[Usage](#usage)**
3. **[Examples](#examples)**
3. **[Contribute](#contribute)**

Requirements
------------

The library is based on Python2.7. Even though I work on support for Python3.x, it is not
working, because I have problems with Pythons `struct` module. So at the moment all you need
is a working installation of Python. 

I have not yet concocted setuptools integration, because it really is a subproject for 
[a live coding editor](https://github.com/hellerve/Veto-LiveCoding) I am currently working on. 
The module is very well integrated there and should work pretty good. Try it out!

Usage
-----

To use the library, first do your usual

```python
from AudioPython import *
```

If you are already familiar with wavebender, the transition should be mostly smooth.
The thing that might confuse at first is that there are several submodules to AudioPython
that were not present in wavebender. A short list to what is there and how to use it:

**dsp**:

This submodule contains the basic waveform: sine, square, sawtooth, triangle, damped, 
white noise and a leaky integrator.

**instruments**:

This submodule contains more "high level" interfaces, such as make_melody(which creates a melody
from frequencies), concat_melodies, a hammond organ, a leslie flanger, a regular one, a delay,
a chorus, a random progression function if you want to get freaky, and a make_instrument function
which creates an instrument from a directory of samples. You can get those samples with the function
get_sample afterwards.

**util**:

This submodule contains mostly internal functions.

**wave**:

This submodule also contains mostly internal functions for encoding sound as wave files.
This is largely based on wavebender, only experimental Python 3 support is my work. And that
is not functional yet. So, basically, I did nothing to it.

Examples
--------

I included a examples directory where some of the most basic features are shown. You can tweak them
and experiment with them, they should be a little introduction.

You might also have a look at [wavebenders test files](https://github.com/zacharydenton/wavebender), 
they should be compatible.

Contribute
----------

This work is potentially never-ending. DSPs, Sound Effects, Instruments, all of them can
be produced in AudioPython and a few of them will be.

I personally am engaged in a reverb, a ringbuffer, pink noise and a bi-quad-filter.

Also, many of the functions are basically untested and need to be tested. Sadly, I am not
very creative at the moment, which means I cannot come up with enough ways to break my code.
Please do that for me. Even better if you can fix it afterwards, but if you cannot or do not
want to, just drop me a few lines so I know the problem exists.
