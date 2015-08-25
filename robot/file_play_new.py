#!/usr/bin/env python3

import sys, os
import keyboardplay
import time, sched
import xml.dom
import xml.etree.ElementTree as ET

debug = False
#debug = True

class PlayableNote():
    def __init__(self, orig_str):
        """
        Parse the orig_str for the convinence of playing.

        playplan should be an iterable for both note and the play time.
        """
        self.playplan = [];
        # First Step: determine input to be a valid XML
        root = ET.fromstring(orig_str)
        if not root.tag == 'transaction': # only begin with a transaction
            print('BAD FILE DETECTED')
            sys.exit(1)
        for child in root:
            if not child.tag == 'play': # IGNORE non-play tag
                continue
            self.playplan.append(child.attrib.copy())
        return

    def play(self):
        """
        Play song using new format.

        Now considering use multithreading way.
        """
        s = sched.scheduler(time.time, time.sleep)
        print("Now I have {}.".format(self.playplan))
        last_time = 0;
        for i in self.playplan:
            if eval(i["time"]) == 0.0:
                s.enter(0, 1, self.mydelaytime)
                last_time = eval(i["time"])
            else:
                s.enter(eval(i["time"])-last_time, 1, keyboardplay.kp_play_note_once(eval(i["note"])))
            #keyboardplay.kp_play_note_once(i["note"])
            #time.sleep(i["time"])
        s.run()
        return

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
