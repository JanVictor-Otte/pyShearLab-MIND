"""Setup script for huest.

Installation command::

    pip install [--user] [-e] .
"""

from __future__ import print_function, absolute_import

from setuptools import setup, find_packages
import os

root_path = os.path.dirname(__file__)

setup(
    name='pyShearLab-MIND',

    version='0.0.2',

    description='Fork of the original pyShearLab libarary with minimal alterations specifically for the pyMIND package',

    url='https://github.com/JanVictor-Otte/pyShearLab-MIND',

    author='Stefan Loock',
    maintainer='Minimally Altered by Jan Victor Otte',
    license='GPL-3.0',

    packages=find_packages(where="src", exclude=['*test*']),
    package_dir={"": "src"},
    python_requires='>=3.6',
    install_requires=[
        "numpy",
        "scipy",
        "matplotlib",
        "Pillow"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
