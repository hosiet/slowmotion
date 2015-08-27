#!/usr/bin/env python3
"""
Socket Server.

Now receive line-based instruction. e.g.:
    '1\n'
    '2\n'

Will listen to port such as '9999'

This Socketserver shall act as the main process for the entire project.
"""

import os, sys
import socketserver
import xml.etree.ElementTree as ET

import smglobal
import smlibaction
import keyboardplay

class MyTCPInfoHandler(socketserver.StreamRequestHandler):

    timeout = None;

    def errlog(self, logstr):
        printf(logstr)

    # Override
    def handle(self):
        """
        Handle input TCP data stream.

        Using XML as data format.
        """
        # {{{ Some simple static functions
        @staticmethod
        def is_command_reset_note(xmlroot):
            return xmlroot.tag == 'command' and 'action' in xmlroot.attrib.keys() and xmlroot.attrib['action'] == 'reset note'
        @staticmethod
        def is_command_reset_all(xmlroot):
            return xmlroot.tag == 'command' and 'action' in xmlroot.attrib.keys() and xmlroot.attrib['action'] == 'reset all'
        @staticmethod
        def is_status_standby():
            return smglobal.ROBOT_STATUS in smglobal.ROBOT_STATUS_LIST and smglobal.ROBOT_STATUS == 'STANDBY'
        @staticmethod
        def is_status_userplay():
            return smglobal.ROBOT_STATUS in smglobal.ROBOT_STATUS_LIST and smglobal.ROBOT_STATUS == 'USERPLAY'
        @staticmethod
        def is_status_userplay_transaction():
            return smglobal.ROBOT_STATUS in smglobal.ROBOT_STATUS_LIST and smglobal.ROBOT_STATUS == 'USERPLAY_TRANSACTION'
        @staticmethod
        def is_command_userplay(xmlroot):
            return xmlroot.tag == 'command' and 'action' in xmlroot.attrib.keys() and xmlroot.attrib['action'] == 'state userplay'
        @staticmethod
        def is_command_userplay_transaction(xmlroot):
            return xmlroot.tag == 'command' and 'action' in xmlroot.attrib.keys() and xmlroot.attrib['action'] == 'state userplay_transaction'
        @staticmethod
        def is_command_music(xmlroot):
            return xmlroot.tag == 'command' and 'action' in xmlroot.attrib.keys() and xmlroot.attrib['action'] == 'state music'
        @staticmethod
        def is_command_note_single(xmlroot):
            return xmlroot.tag == 'play' and 'note' in xmlroot.attrib.keys()

        # }}} end of some simple static functions

        while True:

            # {{{ Pre-formatting
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
                print("UnicodeDecodeError happened!")
                continue
            # }}}

            ########################################################
            # Now begin the real parsing!
            ########################################################
            try:
                xmlroot = ET.fromstring(mydata)
            except xml.etree.ElementTree.ParseError:
                print("XML ParseError!")
                continue

            ###### {{{ High-priority commands

            # No.1 action:reset note
            # Won't be run if in state:userplay or state:userplay_transaction
            if is_command_reset_note(xmlroot):
                if smglobal.ROBOT_STATUS != 'USERPLAY' and smglobal.ROBOT_STATUS != 'USERPLAY_TRANSACTION':
                    smlibaction.smActionResetNote()
                continue

            # No.2 action:reset all
            # Will always run
            if is_command_reset_all(xmlroot):
                smlibaction.smActionResetAll()
                continue

            ###### }}}

            ###### {{{ Parse commands according to status

            # No.1 'STANDBY'
            if is_status_standby():
                if is_command_userplay(xmlroot):
                    # TODO ENTER USERPLAY MODE
                    smglobal.ROBOT_STATUS = "USERPLAY"
                    continue
                elif is_command_userplay_transaction(xmlroot):
                    # TODO ENTER USERPLAY_TRANSACTION MODE
                    continue
                elif is_command_music(xmlroot):
                    # TODO ENTER MUSIC MODE
                    continue
                else:
                    self.errlog('NOW IN STANDBY, BUT COMMAND NOT FOUND')

            # No.2 'USERPLAY'
            if is_status_userplay():
                if is_command_note_single():
                    # TODO PLAY THE NOTE
                    keyboardplay.kp_play_note_once(int(xmlroot.attrib['note']))
                else:
                    self.errlog('NOW IN USERPLAY, BUT COMMAND NOT FOUND')
                finally:
                    continue


            # No.3 'USERPLAY_TRANSACTION'
            if is_status_userplay_transaction():
                pass

            # No.4 'MUSIC'

            self.errlog('COMMAND NOT CATCHED, NOT CONTINUEING')

             # 0 Will be omitted as a testing for connectivity

             ###### }}}
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
