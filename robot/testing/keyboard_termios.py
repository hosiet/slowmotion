#!/usr/bin/env python3
#

"""
测试 Python3 的 TTY 与 Termios 的基于字符的东西

应该有按下按键即时生效的效果
"""

import sys, os
import select
import tty
import termios

def isData():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

old_settings = termios.tcgetattr(sys.stdin)

try:
    tty.setcbreak(sys.stdin.fileno())

    i = 0
    while True:
        print(i)
        i += 1

        if not isData():
            c = sys.stdin.read(1)
            if c.isprintable():
                print('We have {}.'.format(c))
            else:
                print('We have a Non-printable character.')
            if c == '\x1b': # ESC
                break
finally:
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

#  vim: set ts=8 sw=4 tw=0 et :
