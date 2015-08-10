#!/usr/bin/env python3

import os
import time
import socket
import multiprocessing

def sendMyMessage(connection=None):
    if connection == None:
        return
    conn = connection[0];
    address = connection[1];
    conn.send(b'abc')
    print(address)
    return


if __name__ == "__main__":
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0, fileno=None)
    s.bind(('127.0.0.1', 4399))
    print('Begin listen...')
    s.listen(5) # Maximum background waiting queue
    while True:
        connection = s.accept()
        print('accepted')
        sendMyMessage(connection)
        time.sleep(1800)
        #s.close()

#  vim: set ts=8 sw=4 tw=0 et :
