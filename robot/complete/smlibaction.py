#!/usr/bin/python3 -O

"""
Library functions for Slowmotion robots.

**IMPORTANT**

  To use properly, you need to do the 'from librobotaction import *'.

"""
import os, sys
import smglobal
from smglobal import DEBUG
import xml.etree.ElementTree as ET
from keyboardplay import keyboard_data

def smActionResetNote():
    """
    Reset 8 notes of the robot.
    """
    if DEBUG == True:
        print('smActionResetNote(): Will reset note, passing.', file=sys.stderr)
        return
    for i in range(1, 9):
        os.system('echo {0}={1} >> /dev/pi-blaster'.format(keyboard_data[i]['gpio'], keyboard_data[i]['high']))
        time.sleep(0.2)

def smActionResetAll():
    """
    Reset all subprocesses.

    However, this will not reset notes.
    """
    # First Step: Check current running status
    if smglobal.ROBOT_STATUS == None:
        raise Exception('ROBOT_STATUS_NULL')
    elif smglobal.ROBOT_STATUS == "STANDBY" and smglobal.ROBOT_STATUS in smglobal.ROBOT_STATUS_LIST:
        return False
    else:
        # Second Step: Stop and clear the USERPLAY_TRANSACTION handler, if exists
        if smglobal.ROBOT_USERPLAY_TRANSACTION_HANDLER != None:
            smglobal.ROBOT_USERPLAY_TRANSACTION_HANDLER.stop()

        smglobal.ROBOT_USERPLAY_TRANSACTION_HANDLER = None

    # Third Step: Stop and clear the MUSIC handler, if exists
    if smglobal.ROBOT_MUSIC_HANDLER != None:
        smusicplayer.smStopMusicPipe()
        smglobal.ROBOT_MUSIC_HANDLER = None

    # Finally we switch the status to standby
    smglobal.ROBOT_STATUS = "STANDBY"

    return True


def smPowerOff():
    """
    Power off the robot.
    """
    import os
    #assert os.getenv('USER') == 'root'
    os.system('poweroff')
    return

def smReboot():
    """
    Reboot with default value.
    """
    import os
    #assert os.getenv('USER') == 'root'
    os.system('reboot')
    return

#  vim: set ts=8 sw=4 tw=0 et :