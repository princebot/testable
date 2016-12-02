#!/usr/bin/env python
"""
demo - importable script

This is a script that can be unit tested: It can be invoked as a script or
imported as a module, where its functions may be tested.
"""

def say_hello(name):
    print('hello, {}.'.format(name))


def say_goodbye(name):
    print('goodbye, {}.'.format(name))


if __name__ == '__main__':
    say_hello('mark rosewater')
    say_goodbye('john finkel')
