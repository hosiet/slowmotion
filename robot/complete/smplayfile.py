#!/usr/bin/python3 -O
"""

Yes. Playback *must* be in a separate thread.

Let's use threading module.
"""

import sys, os
import time, sched
import xml.etree.ElementTree as ET
import threading

import smglobal
from smglobal import DEBUG
import keyboardplay

class PlayableNote():
    """
    Special class for USERPLAY_TRANSACTION.

    Workflow
    --------
    1. call __init__(), setup self.playplan --> sched task --> threading.Thread object
    2. call play(), will run Thread.run()
    3. (optional) call stop(), will set self.stop_flag = True. Then running thread
    may detect and stop. fin.
    """
    # TODO PROPER TESTING

    def __init__(self, orig_str):
        """
        Parse the orig_str for the convinence of playing.

        playplan should be an iterable for both note and the play time.
        """
        self.mThread = None
        self.stop_flag = False
        self.playplan = [];

        def _playWrapper(self, playplan_fragment, schedule):
            """
            A Wrapper to play notes.

            Will check for stop_flag and cancel all jobs if flag is set.
            """
            keyboardplay.kp_play_note_once(eval(playplan_fragment["note"]))
            if self.stop_flag == True:
                # Cancel future jobs
                for i in schedule.queue:
                    schedule.cancel(i)

        # First Step: determine input to be a valid XML
        root = ET.fromstring(orig_str)
        if not root.tag == 'transaction': # only begin with a transaction
            print('BAD FILE DETECTED', file=sys.stderr)
            sys.exit(1)
        for child in root:
            if not child.tag == 'play': # IGNORE non-play tag
                continue
            self.playplan.append(child.attrib.copy())

        # Second Step: build the schedule object
        s = sched.scheduler(time.time, time.sleep)
        last_time = 0
        for i in self.playplan:
            if eval(i["time"]) == 0.0:
                s.enter(0, 1, self.mydelaytime)
                last_time = eval(i["time"])
            else:
                s.enter(eval(i["time"])-last_time, 1, _playWrapper(self, i, s))

        # Third Step: assign target function to Thread Object
        self.mThread = threading.Thread(target=lambda x:x.run(), args=(s,))

        return

    def play(self):
        """
        Play song.

        In fact, we only need to start the thread.
        """
        self.mThread.start()
        return

    def stop(self):
        """
        Stop playing.

        In fact, we only(?) need to stop the thread.
        """
        self.stop_flag = True

def playFile(filename):
    """ Parse file.

    Example is shown in song3.song.

    Note: 0 is empty and shall accept.

    """
    try:
        f = open(filename, "r")
    except FileNotFoundError:
        print('No such file.')
        sys.exit(2)
    except Exception as e:
        print(e)
        sys.exit(3)
    # Now begin to parse file.
    #
    # Example:
    s = f.read()
    playObject = PlayableNote(s)
    playObject.play()

if __name__ == "__main__":
    try:
        a = sys.argv[1]
    except IndexError:
        print('Bad arguments.')
        sys.exit(1)
    playFile(sys.argv[1])
