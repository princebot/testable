#!/usr/bin/env python
"""unit tests for importable.py"""

import importable as main


def test_say_hello(capsys):
    main.say_hello('foo')
    out, err = capsys.readouterr()
    assert out == 'hello, foo.\n'
    assert err == ''

def test_say_goodbye(capsys):
    main.say_goodbye('bar') == 'goodbye, bar.'
    out, err = capsys.readouterr()
    assert out == 'goodbye, bar.\n'
    assert err == ''
