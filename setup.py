#!/usr/bin/env python
"""
An installation script for AudioPython using distutils.
"""

from distutils.core import setup
import AudioPython

setup(
    name='AudioPython',
    description='An audio live coding library in Python',
    author=AudioPython.__author__,
    author_email=AudioPython.__author_mail__,
    version=AudioPython.__version__,
    url=AudioPython.__url__,
    long_description=AudioPython.__longdescr__,
    classifiers=AudioPython.__classifiers__,
    keywords=AudioPython.__keywords__,
    packages=['AudioPython'],
    license="MIT",
    platforms=['Linux', 'OS X', 'Windows']
)


