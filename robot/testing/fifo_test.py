#!/usr/bin/env python3

"""
Test for FIFO reading.
"""
import os, time
import multiprocessing

FM_FILEPATH = '/tmp/myfifo'

def mf_keeper(filepath=FM_FILEPATH):
    """
    Open it. Don't close it.
    """
    f2 = open(filepath, 'w')
    while True:
        time.sleep(60)
    pass

if __name__ == "__main__":
    p = multiprocessing.Process(target=mf_keeper)
    p.start() # never join
    f = open(FM_FILEPATH, 'r')
    while True:
        line = f.readline()
        print("I have \"{}\"".format(line))

#  vim: set ts=8 sw=4 tw=0 et :
