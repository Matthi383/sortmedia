#!/usr/bin/env python3
# encoding: utf-8

from setuptools import setup, find_packages

setup(
    name="sortmedia",
    version="1.0",
    description="Organizes photos and videos into folders using date/time information",
    author="Matthias Radl",
    packages=find_packages(),
    include_package_data=True,
    license="MIT License",
    entry_points={
        "console_scripts": [
            "sortmedia = src.sortmedia:main",
        ]
    },
)
