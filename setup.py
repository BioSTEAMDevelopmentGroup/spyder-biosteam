# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 16:17:00 2017

@author: Yoel Cortes-Pena
"""
from setuptools import setup
#from Cython.Build import cythonize
#import numpy

setup(
    name='spyder_biosteam',
    packages=['spyder_biosteam'],
    license='MIT',
    version='0.1.0',
    description='An interactive plugin to render BioSTEAM flowsheets in the Spyder-IDE',
    long_description=open('README.rst').read(),
    author='Yoel Cortes-Pena',
    install_requires=['biosteam>=2.9.10',
                      'PyQt5>=5.12'],
    python_requires=">=3.6",
    package_data=
        {'spyder_biosteam': ['widgets/*']},
    platforms=['Windows', 'Mac', 'Linux'],
    author_email='yoelcortes@gmail.com',
    url='https://github.com/BioSTEAMDevelopmentGroup/spyder-biosteam',
    download_url='https://github.com/BioSTEAMDevelopmentGroup/spyder-biosteam.git',
    classifiers=['Development Status :: 3 - Alpha',
                 'Environment :: Console',
                 'License :: OSI Approved :: MIT License',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 'Topic :: Scientific/Engineering',
                 'Topic :: Scientific/Engineering :: Chemistry',
                 'Topic :: Scientific/Engineering :: Mathematics'],
    keywords='flowsheet, BioSTEAM, interctive, Spyder',
)