#!/usr/bin/env python3
"""
Socket Server.

Now receive line-based instruction. e.g.:
    '1\n'
    '2\n'
"""

import os, sys
import socketserver

class MyTCPInfoHandler(socketserver.StreamRequestHandler):

    # Override
    def handle(self):
        while True:
            self.data = self.rfile.readline().strip()
            if self.data == b'': # Empty line
                break
            if self.data == b'\x1b': # ESC
                break
            print("From {0}, Received: '{1}'.".format(self.client_address, self.data))
        print('Connection closed by me.')
        return

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create server and Bind to port
    server = socketserver.TCPServer((HOST, PORT), MyTCPInfoHandler)

    # Activate it. Use CTRL+C to interrupt
    server.serve_forever()
    pass
#  vim: set ts=8 sw=4 tw=0 et :
