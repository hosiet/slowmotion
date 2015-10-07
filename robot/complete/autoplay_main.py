#!/usr/bin/env python3

import sqlite3
import sched, time
import threading

import keyboardplay
import smglobal
from smglobal import DEBUG

class StrikeThread(threading.Thread):
    """
    StrikeThread, for the strike of autoplay.

    When init, should take one argument: the id of which we need to play.

    NOTE: id start with 1.
    """
    def __init__(self, autoplay_id):
        super().__init__(self)
        self.conn = sqlite3.connect("smusic/musiclist.db")
        self.autoplay_id = autoplay_id;

    def _strike(self):
        """
        Actually do the strike work.
        """
        c = self.conn.cursor()
        found = False
        for x in c.execute("SELECT time, note FROM music WHERE id=?;", (self.autoplay_id, )):
            found = True
            break
        if not found:
            # Given number not found.
            # TODO ERROR LOGGING
            print('ID not found! not doing anything.')
            return
        t = x[0].split()
        w = x[1].split()
        self.conn.close()
        s = sched.scheduler(time.time, time.sleep)
        count = 0
        for i in t:
            floatnumber = float(t[count])
            s.enter(floatnumber, 1, keyboardplay.kp_play_note_once, argument=(w[count], ))
            count += 1
        s.run()

    def run(self):
        self._strike()


def sm_autoplay_test():
    thread1 = StrikeThread(1)
    thread1.start()
    thread1.join()

if __name__ == '__main__':
    sm_autoplay_test()
