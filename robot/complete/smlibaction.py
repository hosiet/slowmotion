#!/usr/bin/env python3

"""
Library functions for Slowmotion robots.

**IMPORTANT**

  To use properly, you need to do the 'from librobotaction import *'.

"""
import os
import smglobal
import xml.etree.ElementTree as ET
from keyboardplay import keyboard_data

def smActionResetNote():
    """
    Reset 8 notes of the robot.
    """
    for i in range(1, 9):
        os.system('echo {0}={1} >> /dev/pi-blaster'.format(keyboard_data[i]['gpio'], keyboard_data[i]['high']))
        time.sleep(0.2)

def smActionResetAll():
    """
    Reset all subprocesses.
    """
    # First Step: Check current running status
    if smglobal.ROBOT_STATUS == None:
        raise Exception('ROBOT_STATUS_NULL')
    elif smglobal.ROBOT_STATUS == "STANDBY" and smglobal.ROBOT_STATUS in smglobal.ROBOT_STATUS_LIST:
        return False
    else:
        # Second Step: send SIGUSR1 to all subprocesses
        # TODO
        pass
    finally:
        # Finally we switch the status to standby
        smglobal.ROBOT_STATUS = "STANDBY"

    return True




#  vim: set ts=8 sw=4 tw=0 et :
