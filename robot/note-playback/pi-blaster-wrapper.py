#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
pi-blaster-wrapper.py -- A pi-blaster wrapper

Used to wrap pi-blaster use.
"""

## CONFIG FOR PI-BLASTER USE

PI_BLASTER_NOTE =  \
        {'1': '17',\
         '2': '18',\
         '3': '19',\
         '4': '20',\
         '5': '21',\
         '6': '22',\
         '7': '23',\
         '8': '24' \
        };

## MAIN FUNCTIONS

def note_playback_hard(number):
    if not number in PI_BLASTER_NOTE.keys():
        # FIXME
        raise Exception('BAD_NOTE_KEY')
    # 控制 /dev/pi-blaster 进行一次敲击
    # FIXME

if __name__ == "__main__":
    print('This file won\'t run directly.')

#  vim: set ts=8 sw=4 tw=0 et :
