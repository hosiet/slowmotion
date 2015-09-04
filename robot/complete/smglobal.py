#!/usr/bin/python3 -O

##########################################################

##
# Global variables
#
# To record current running status.

## Robot status tuple
ROBOT_STATUS_LIST=("STANDBY", "USERPLAY", "USERPLAY_TRANSACTION", "MUSIC",)

## Robot status
ROBOT_STATUS=None

## Subprocess list
ROBOT_SUBPROCESSES=[]

## Music pipe
ROBOT_MUSIC_HANDLER=None

## Set if it is debug
DEBUG=True

## END OF GLOBAL VARIABLES
##########################################################

## Import static functions
from smstaticfunc import *

#  vim: set ts=8 sw=4 tw=0 et :
