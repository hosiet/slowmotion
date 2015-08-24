#!/usr/bin/env python3

import sys, os
import keyboardplay
import time

debug = False
#debug = True

class PlayableNote():
    def __init__(self, orig_str):
        """
        Parse the orig_str for the convinence of playing.
        """
        self.playplan = [];
        onenote = {"note":None, "time":None}
        for i in orig_str.splitlines():
            #print('Now i is {}.'.format(i))
            if i.isdigit():
                # Consider it to be note(1-8) or empty(0)
                if not (int(i) >= 1 and int(i) <= 8):
                    raise Exception('Bad note number')
                onenote["note"] = int(i)
            elif i[-1] == 's':
                # Consider it to be seconds
                onenote["time"] = eval(i[:-1])
            if onenote["note"] != None and onenote["time"] != None:
                #print('Now onenote is {}.'.format(onenote))
                self.playplan.append(onenote.copy())                    # 惊天大坑
                #print('Now self.playplan is {}.'.format(self.playplan))
                onenote["note"], onenote["time"] = None, None
        return

    def play(self):
        print("Now i have {}.".format(self.playplan))
        for i in self.playplan:
            keyboardplay.kp_play_note_once(i["note"])
            time.sleep(i["time"])
        return

def playFile(filename):
    """ Parse file.

Example:

1
0.2s
2
0.3s
3
0.5s


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
