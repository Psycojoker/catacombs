#!/usr/bin/python
# -*- coding:Utf-8 -*-

from setuptools import setup

setup(name='catacombs',
      version='git',
      author='Laurent Peuch',
      # long_description=open("README").read(),
      author_email='cortex@worlddomination.be',
      install_requires=['pymongo', 'selector'],
      packages=['catacombs'],
      license= 'aGPLv3+',
      scripts=['bin/catacombs'],
     )

# vim:set shiftwidth=4 tabstop=4 expandtab:
