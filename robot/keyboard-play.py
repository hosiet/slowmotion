#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 仅为了测试与检查所用。
# 
# 在键盘上按动字符1-8，使得实体的八个舵机分别敲击。

import sys, os
import select
import tty
import termios

# 键值数值标记
keyboard_data = {\
        8: {'low':0.15, 'high':0.24, 'gpio':25, 'time':0.14},\
        7: {'low':0.15, 'high':0.24, 'gpio':24, 'time':0.14},\
        6: {'low':0.19, 'high':0.25, 'gpio':23, 'time':0.14},\
        5: {'low':0.18, 'high':0.25, 'gpio':22, 'time':0.14},\
        4: {'low':0.19, 'high':0.24, 'gpio':21, 'time':0.14},\
        3: {'low':0.16, 'high':0.24, 'gpio':18, 'time':0.14},\
        2: {'low':0.19, 'high':0.24, 'gpio':17, 'time':0.14},\
        1: {'low':0.18, 'high':0.22, 'gpio':4,  'time':0.12}}


def kp_play_note_once(inputnote):
    """
    Play a note once a time.
    """
    print('{0} pressed; Will play: {1}.'.format(inputnote, keyboard_data[inputnote]))
    pass

def kp_start_playing():
    """
    Non-stop play the note using keyboard.

    Use 'c' to stop.
    """
    def isData():
        return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

    old_settings = termios.tcgetattr(sys.stdin)

    try:
        tty.setcbreak(sys.stdin.fileno())
        while True:
            if not isData():
                c = sys.stdin.read(1)
                if c >= '1' and c <= '8':
                    # Valid input
                    kp_play_note_once(int(c))
                    #kp_play_note((int(c),))
                    continue
                elif c == '\x1b': # ESC
                    break
                print('Not valid input.') # Invalid input
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

if __name__ == "__main__":
    # 读取键盘输入的1-8，转换成音乐播放
    kp_start_playing()

#  vim: set ts=8 sw=4 tw=0 et :
