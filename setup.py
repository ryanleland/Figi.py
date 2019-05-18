#!/usr/bin/env python

from setuptools import setup

import figi


extras = {
    "develop": []
}

setup(
    name="figi",
    version=figi.__version__,
    description=figi.__doc__,
    url="https://github.com/ryanleland/Figi.py",
    author="Ryan Leland",
    packages=[
        "figi"
    ],
    package_data={"": ["LICENSE"]},
    include_package_data=True,
    license=open("LICENSE").read(),
    classifiers=(
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ),
    install_requires=[
        "requests"
    ],
    extras_require=extras
)
