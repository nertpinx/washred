#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Main script to run """

import sys
from redwash import greetings


def main(argv=None):
    """ This function has so many things it can do! """
    if argv:
        greetings.greet(''.join(argv))
    else:
        greetings.greet()
    return 0

if __name__ == '__main__':
    exit(main(sys.argv))
