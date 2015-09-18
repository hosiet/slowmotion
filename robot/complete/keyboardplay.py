#!/usr/bin/python3 -O
# -*- coding: utf-8 -*-

# 仅为了测试与检查所用。
# 
# 在键盘上按动字符1-8，使得实体的八个舵机分别敲击。

import sys, os
import select
import tty
import termios
import time
import multiprocessing
try:
    from smglobal import DEBUG
except ImportError:
    DEBUG = False
    print('no smglobal found, passing.', file=sys.stderr)

# 键值数值标记
keyboard_data = {\
        "=": {"low":0.23, "high":0.21, "gpio":21, "time":0.14},\
        "-": {"low":0.23, "high":0.21, "gpio":18, "time":0.14},\
        '0': {"low":0.22, "high":0.20, "gpio":17, "time":0.14},\
        '9': {"low":0.23, 'high':0.20, 'gpio':4, 'time':0.12},\
        '8': {'low':0.165, 'high':0.21, 'gpio':25, 'time':0.14},\
        '7': {'low':0.18, 'high':0.21, 'gpio':24, 'time':0.14},\
        '6': {'low':0.23, 'high':0.26, 'gpio':23, 'time':0.14},\
        '5': {'low':0.18, 'high':0.20, 'gpio':22, 'time':0.14},\
        '4': {'low':0.19, 'high':0.21, 'gpio':21, 'time':0.14},\
        '3': {'low':0.19, 'high':0.21, 'gpio':18, 'time':0.14},\
        '2': {'low':0.18, 'high':0.20, 'gpio':17, 'time':0.14},\
        '1': {'low':0.18, 'high':0.20, 'gpio':4,  'time':0.12}}


# 确认是树莓派平台
#is_under_pi = False
is_under_pi = True

def kp_play_note_once(inputnote):
    """
    Play a note once a time.
    """
    print('{0} pressed; Will play: {1}.'.format(inputnote, keyboard_data[inputnote]))
    if DEBUG:
        print('kp_play_note_once(): Will play note, passing.', file=sys.stderr)
        return
    os.system('echo {0}={1} >> /dev/pi-blaster'.format(keyboard_data[inputnote]['gpio'], keyboard_data[inputnote]['low']))
    time.sleep(keyboard_data[inputnote]['time'])
    os.system('echo {0}={1} >> /dev/pi-blaster'.format(keyboard_data[inputnote]['gpio'], keyboard_data[inputnote]['high']))
    # May be improved later? Don't use os.system (TODO)
    return

def kp_start_playing():
    """
    Non-stop play the note using keyboard.

    Use ESC to stop.
    """
    def isData():
        return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

    old_settings = termios.tcgetattr(sys.stdin)

    try:
        tty.setcbreak(sys.stdin.fileno())
        while True:
            if not isData():
                c = sys.stdin.read(1)
                if c >= '0' and c <= '9' or c == '-' or c == '=':
                    # Valid input, use multiprocessing to prevent problem?
                    # 0 means release
                    p = multiprocessing.Process(target=kp_play_note_once, args=(c,))
                    p.start()
                    # Never join!
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
