#! /usr/bin/python
'''
@author: mahsan
'''

# Recommendation - Utilities for item recommendation
# Copyright (C) 2015 Muhammad Ahsan

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

"""setup.py: setuptools control."""

import os
import re
from setuptools import setup

this_dir = os.path.dirname(os.path.abspath(__file__))
pkg_dir = os.path.join(this_dir, "recommendation")

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('recommendation/__init__.py').read(),
    re.M
    ).group(1)


with open(os.path.join(this_dir, "README.md")) as f:
    long_description = f.read()

setup(
    name='Recommendation',
    version=version,
    description='Python CLI for items recommendation',
    long_description=long_description,
    author='Muhammad Ahsan',
    author_email='muhammad.ahsann@gmail.com',
    packages=['recommendation', 'recommendation.tests'],
    package_data={
        'recommendation': ['data/*.json'],
    },
    entry_points={
        'console_scripts': ['recommendation=recommendation.recommendation:main'],
        },
    classifiers=(
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
    )
)
