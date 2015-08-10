#!/usr/bin/env python3

"""
FIFO Keeper.

let fifo to be '/tmp/note-playback-fifo'.
"""
import errno
import os

NOTE_PLAYBACK_FIFO = '/tmp/note-playback-fifo'

class FmFifo():
    """
    A fifo-monitor fifo class.

    Used for keeping a fifo object.
    """
    def __init__(self, filepath=NOTE_PLAYBACK_FIFO):
        """
        Class init.

        Will also bring up a FIFO file together.
        """
        os.mkfifo(filepath)
        self.fr = open(filepath, mode='rt')
        self.fw = open(filepath, mode='wt')
        self.filepath = filepath
        pass

    def __del__(self):
        """
        Meanwhile, it will delete the fifo on the disk.
        """
        fw.close()
        fr.close()
        os.remove(filepath)
        pass

    def text_clear(self):
        """
        Read the fifo file until nothing left.
        """
        assert self.fr.readable == True
        BUFFER_SIZE = 1024
        while True:
            try:
                buffer = os.read(f, BUFFER_SIZE)
            except OSError as err:
                if err.errno == errno.EAGAIN or err.errno == errno.EWOULDBLOCK:
                    buffer = None
                    break
                else:
                    raise
            except:
                raise
        assert buffer == None
        return True

