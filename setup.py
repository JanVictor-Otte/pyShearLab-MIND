"""Setup script for huest.

Installation command::

    pip install [--user] [-e] .
"""

from __future__ import print_function, absolute_import

from setuptools import setup, find_packages
import os

root_path = os.path.dirname(__file__)
requires = open(os.path.join(root_path, 'requirements.txt')).readlines()

setup(
    name='pyShearLab-MIND',

    version='0.0.1',

    description='Fork of the original pyShearLab libarary with minimal alterations specifically for the pyMIND package',

    url='https://github.com/JanVictor-Otte/pyShearLab-MIND',

    author='Stefan Loock',
    maintainer='Minimally Altered by Jan Victor Otte',
    license='GPL-3.0',

    packages=find_packages(exclude=['*test*']),

    install_requires=[r.strip() for r in requires],
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
