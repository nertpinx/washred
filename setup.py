#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Build, test and install configuration """


import os
import sys
from glob import glob
from setuptools import setup, find_packages, Command


class CheckPylint(Command):
    """ setup.py command checking code-correctness with pylint and pep8 """
    user_options = []
    description = "Check code using pylint and pep8"

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        files = glob('*.py') + glob('*/*.py')

        output_format = sys.stdout.isatty() and "colorized" or "text"

        cmd = "/usr/bin/pylint "
        cmd += "--output-format=%s " % output_format
        cmd += " ".join(files)
        os.system(cmd + " --rcfile tests/pylint.cfg")

        print("running pep8")
        cmd = "/usr/bin/pep8 "
        cmd += " ".join(files)
        os.system(cmd + " --config tests/pep8.cfg")


setup(
    name='washred',
    version='0.0.1',
    description='Washington Redskins',
    long_description=''.join(open('README.rst').readlines()),
    keywords='git, github, gerrit, gerrithub, tryout',
    author='Martin Kletzander',
    author_email='nert.pinx+github@gmail.com',
    license='GPLv3',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        ],
    scripts=['washred.py'],
    cmdclass={'pylint': CheckPylint},
)
