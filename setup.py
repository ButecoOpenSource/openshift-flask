#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='OpenShift Flask Example',
    version='0.0.1',
    author='Alexandre Vicenzi',
    author_email='vicenzi.alexandre@gmail.com',
    install_requires=['Flask'],
)
