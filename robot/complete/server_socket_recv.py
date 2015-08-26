#!/usr/bin/env python3
"""
Socket Server.

Now receive line-based instruction. e.g.:
    '1\n'
    '2\n'

Will listen to port such as '9999'
"""

import os, sys
import socketserver
import keyboardplay

class MyTCPInfoHandler(socketserver.StreamRequestHandler):

    timeout = None;

    # Override
    def handle(self):
        while True:
            self.data = self.rfile.readline()                   # DO NOT REMOVE '\n'
            print("Data is {}.".format(self.data))
            if self.data == b'':                                # Connection reset by peer
                print('Connection reset by peer.')
                return
            self.data = self.data.strip(b'\n')                  # REMOVE '\n'
            if self.data == b'':                                # Empty Line
                break
            if self.data == b'\x1b':                            # ESC
                break
            print("From {0}, Received: '{1}'.".format(self.client_address, self.data))
            try:
                mydata = self.data.decode('UTF-8') # 1-8
            except UnicodeDecodeError:                          # Not valid unicode(utf-8) input
                continue
            try:
                intdata = int(mydata)
            except ValueError:                                  # Not valid value
                continue
            if intdata >= 1 and intdata <= 9:                   # valid playing data
                keyboardplay.kp_play_note_once(intdata)
            if intdata == 0:                                    # 0 Will be omitted as a testing for connectivity
                print('Testing 9 received, ignoring...')
        print('Connection closed by me.')
        return

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 9999

    # Create server and Bind to port
    server = socketserver.TCPServer((HOST, PORT), MyTCPInfoHandler)

    # Activate it. Use CTRL+C to interrupt
    server.serve_forever()
    pass

#  vim: set ts=8 sw=4 tw=0 et :
