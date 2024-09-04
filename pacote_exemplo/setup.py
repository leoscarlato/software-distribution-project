#!/usr/bin/env python3

from setuptools import setup

setup(name='dev_aberto_leonardo_scarlato',
      version='0.1',
      packages=['dev_aberto'],
      author="Leonardo Scarlato",
      author_email="leonardos15@al.insper.edu.br",
      install_requires=['requests==2.31.0'],
      scripts=['scripts/hello.py'],
    )