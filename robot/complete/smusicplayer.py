#!/usr/bin/python3 -O
# -*- coding:utf-8 -*-
"""
Slomotion Music Player

A server-side module.
"""

import subprocess

import smglobal
from smglobal import DEBUG


def smGetMusicPipe()
    smMusic = subprocess.Popen(['mplayer', '-slave', '-idle'], stdout=subprocess.PIPE,
              stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)
    return smMusic

def smStopMusicPipe()
    smglobal.ROBOT_MUSIC_HANDLER.terminate()
    return

#  vim: set ts=8 sw=4 tw=0 et :
