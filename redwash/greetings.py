#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Compilation of various greetings """


def greet(text=None):
    """ Default greeting without any specialities """
    if text is None:
        print("Hello World!")
    else:
        print(text)
