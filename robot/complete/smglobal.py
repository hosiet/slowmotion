#!/usr/bin/python3 -O

##########################################################

##
# Global variables
#
# To record current running status.

## Working dir prefix
PROGRAM_PREFIX='/home/pi/src/slowmotion/robot/complete/'


## Robot status tuple
ROBOT_STATUS_LIST=("STANDBY", "USERPLAY", "USERPLAY_TRANSACTION", "MUSIC",)

## Robot status
ROBOT_STATUS=None

## Subprocess list
ROBOT_SUBPROCESSES=[]


## Music pipe
ROBOT_MUSIC_HANDLER=None

## Music database path
ROBOT_MUSIC_DB='./smusic/musiclist.db'

## Music mp3 path
ROBOT_MUSIC_PATH='./smusic/music/'

## Note song file path
ROBOT_SONG_PATH='./smusic/song/'


## USERPLAY_TRANSACTION PlayableNote Handler
ROBOT_USERPLAY_TRANSACTION_HANDLER=None

## Set if it is debug
DEBUG=True
DEBUG=False

## END OF GLOBAL VARIABLES
##########################################################

## Import static functions
from smstaticfunc import *

#  vim: set ts=8 sw=4 tw=0 et :
