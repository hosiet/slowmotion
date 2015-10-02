#!/usr/bin/env python3

import sqlite3
import sched, time
import threading

import keyboardplay
import smglobal
from smglobal import DEBUG

class StrikeThread(threading.Thread):
    def __init__(self):
        super().__init__(self)
        self.conn = sqlite3.connect("smusic/new.db")

    def _strike(self):
        c = self.conn.cursor()
        for x in c.execute("SELECT time, note FROM music;"):
            break
        t = x[0].split()
        w = x[1].split()
        self.conn.close()
        s = sched.scheduler(time.time, time.sleep)
        count = -1
        for i in t:
            count += 1
            floatnumber = float(t[count])
            s.enter(floatnumber, 1, keyboardplay.kp_play_note_once, argument=(w[count], ))
        s.run()

    def run(self):
        self._strike()

def test():
    thread1 = StrikeThread()
    thread1.start()
    thread1.join()

if __name__ == '__main__':
    test()
