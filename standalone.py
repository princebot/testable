#!/usr/bin/env python
"""
demo - standalone script

This is a standalone script that cannot be unit tested: It just executes.
"""

def say_hello(name):
    print('hello, {}.'.format(name))


def say_goodbye(name):
    print('goodbye, {}.'.format(name))


say_hello('mark rosewater')
say_goodbye('john finkel')
