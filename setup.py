#!/usr/bin/env python
import os
from setuptools import find_packages, setup

PROJECT_DIR = os.path.dirname(__file__)

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="wagtailsvg",
    version="0.2.0",
    url="https://github.com/Aleksi44/wagtailsvg",
    author="Alexis Le Baron (Original), Modified for Wagtail 6 compatibility",
    author_email="alexis@stationspatiale.com",
    description="Wagtail SVG - Modified for Wagtail 6 Compatibility",
    long_description=long_description,
    keywords="wagtail svg",
    license="GPL-3.0",
    install_requires=[
        "wagtail>=6.0,<7.0",
        "django>=4.2,<6.0",
    ],
    platforms=["linux"],
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
    ],
)
