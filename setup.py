#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs

from setuptools import setup, find_packages

setup(
    name='activity',
    version='2.3.0',
    description='Activity feeds backed by Redis',
    long_description=codecs.open('readme.md', "r", "utf-8").read(),
    author='Simon Zimmermann',
    author_email='simon@insmo.com',
    url='http://github.com/simonz05/activity-feed',
    license='MIT',
    keywords="redis",
    packages=find_packages(exclude=['tests']),
    install_requires=['redis', 'leaderboard'],
    zip_safe=True,
    test_suite="nose.collector",
    tests_require=['nose'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
    ],
)
