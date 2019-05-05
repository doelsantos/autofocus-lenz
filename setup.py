# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "af_lenz"
VERSION = "1.2.6"

#REQUIRES = ["autofocus"]
REQUIRES = [""]

setup(
    name=NAME,
    version=VERSION,
    description="Autofocus Lenz",
    author_email="jwhite@paloaltonetworks.com",
    url="",
    keywords=["autofocus", "af_lenz"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="A tool for interfacing with the PANW autofocus api",
    entry_points = {
        'console_scripts': ['af_lenz=af_lenz:main']
    }
)
