#!/usr/bin/python3 -O
# -*- coding:utf-8 -*-
"""
Slomotion Music Player

A server-side module.
"""

import subprocess
import sqlite3

import smglobal
from smglobal import DEBUG

def smGetMusicPipe()
    """
    Start background mplayer process.

    Should be called when the smserver starts.
    """
    smMusic = subprocess.Popen(['mplayer', '-slave', '-idle'], stdout=subprocess.PIPE,
              stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)
    return smMusic

def smStopMusicPipe()
    """
    Stop background mplayer process.

    Optional. Should be called when the smserver stops.
    """
    smglobal.ROBOT_MUSIC_HANDLER.terminate()
    return

def smPlayMusic(path):
    """
    Play music by given path.

    Should not be called directly.
    """
    return False

def smStopMusic():
    """
    Stop music playing.
    """
    pass

def smPauseMusic():
    pass

def smResumeMusic():
    pass

def smPlayMusicById(intid)
    """
    Begin to play music according to given id.

    Will
    """
    conn = sqlite3.connect(smglobal.PROGRAM_PREFIX + smglobal.ROBOT_MUSIC_DB)
    c = conn.cursor()
    found = False
    for i in c.execute("SELECT filename FROM musicdata WHERE id=?", (intid,)):
        found = True
        break
    if not found:
        return False
    conn.close()     # NOTE: should we make conn a global var?
    return smPlayMusic(smglobal.PROGRAM_PREFIX + smglobal.ROBOT_MUSIC_PATH + i)

#  vim: set ts=8 sw=4 tw=0 et :
