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

Coming soon.

Examples
--------

Coming soon.

Contribute
----------

This work is potentially never-ending. DSPs, Sound Effects, Instruments, all of them can
be produced in AudioPython and a few of them will be.

I personally am engaged in a flanger, a delay, a reverb and chorus, because based on that,
a few more instruments are possible. 

Also, many of the functions are basically untested and need to be tested. Sadly, I am not
very creative at the moment, which means I cannot come up with enough ways to break my code.
Please do that for me. Even better if you can fix it afterwards, but if you cannot or do not
want to, just drop me a few lines so I know the problem exists.
