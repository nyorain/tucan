#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from os import path
from setuptools import setup


setup(
    name="tucan",
    version="0.9",
    description="New Grades Notification Script for TuCaN",
    long_description=open(path.join(path.dirname(__file__), "README.rst")).read(),
    url="http://github.com/fhirschmann/tucan",
    author="Fabian Hirschmann",
    author_email="fabian@hirschmann.email",
    license="MIT",
    platforms="any",
    install_requires=[
        "lxml",
        "mechanize",
    ],
    keywords="tucan tu darmstadt technische universität",
    scripts=["tucan"],
)
