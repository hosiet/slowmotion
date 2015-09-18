#!/usr/bin/python3 -O
# -*- coding:utf-8 -*-
# {{{ docstring and instruction
"""
Slomotion Music Player

A server-side module.

## Example mlayer grammar

* [pause]               do pause and unpause
* [loadfile <filename>] load music file and play instantly
* [stop]                stop playing
* [mute]                mute and unmute

For more information, see https://www.mplayerhq.hu/DOCS/tech/slave.txt
"""
# }}}

import subprocess
import sqlite3
import xml.etree.ElementTree as ET

import smglobal
from smglobal import DEBUG

def smGetMusicPipe():
    """
    Start background mplayer process.

    Should be called when the smserver starts.
    """
    smMusic = subprocess.Popen(['mplayer', '-slave', '-idle'], stdout=subprocess.PIPE,
              stdin=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    smglobal.ROBOT_MUSIC_HANDLER = smMusic # NOT NECESSARY
    return smMusic

def smStopMusicPipe():
    """
    Stop background mplayer process.

    Optional. Should be called when the smserver stops.
    """
    smglobal.ROBOT_MUSIC_HANDLER.terminate()
    return

def _smSendCommand(str):
    print(str, file=smglobal.ROBOT_MUSIC_HANDLER.stdin, flush=True)

def smPlayMusic(path):
    """
    Play music by given path.

    Should not be called directly.
    """
    _smSendCommand('loadfile {}'.format(str))
    return True

def smStopMusic():
    """
    Stop music playing.
    """
    _smSendCommand('stop')
    return

def smPauseMusic():
    _smSendCommand('pause')
    return

def smResumeMusic():
    _smSendCommand('pause')
    return

def smPlayMusicById(intid):
    """
    Begin to play music according to given id.
    """
    conn = sqlite3.connect(smglobal.ROBOT_MUSIC_DB)
    c = conn.cursor()
    found = False
    for i in c.execute("SELECT filename FROM musicdata WHERE id=?", (intid,)):
        found = True
        break
    if not found:
        return False
    conn.close()     # NOTE: should we make conn a global var?
    return smPlayMusic(smglobal.ROBOT_MUSIC_PATH + i)

def smGetMusicList():
    """
    Return all valid music list as XML data str.
    """
    xmlroot = ET.Element('musiclist')
    conn = sqlite3.connect(smglobal.ROBOT_MUSIC_DB)
    c = conn.cursor()
    for row in c.execute("SELECT * FROM musicdata ORDER BY id"):
        subelement = ET.SubElement(xmlroot, 'music')
        subelement.set('id', row[0])
        subelement.set('filename', row[1])
        subelement.set('havenote', row[2])
    conn.close()
    return ET.dump(xmlroot)

#  vim: set ts=8 sw=4 tw=0 et :
