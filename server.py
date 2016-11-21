#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
import os


class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        line = self.rfile.read().decode('utf-8').split()
        my_methods = ['INVITE', 'ACK', 'BYE']
        if line[0] not in my_methods:
            self.wfile.write(b'SIP/2.0 405 Method Not Allowed\r\n\r\n')
        elif len(line) != 3:
            self.wfile.write(b'SIP/2.0 400 Bad Request\r\n\r\n')
        else:
            if line[0] == 'INVITE':
                template = ('SIP/2.0 100 Trying\r\n\r\n'
                            'SIP/2.0 180 Ring\r\n\r\n'
                            'SIP/2.0 200 OK\r\n\r\n')
                self.wfile.write(bytes(template, 'utf-8'))
            elif line[0] == 'ACK':
                os.system('./mp32rtp -i 127.0.0.1 -p 23032 < ' +
                          archivo_audio)
            elif line[0] == 'BYE':
                self.wfile.write(b'SIP/2.0 200 OK\r\n\r\n')

if __name__ == "__main__":
    try:
        serv = socketserver.UDPServer((sys.argv[1],
                                       int(sys.argv[2])), EchoHandler)
        archivo_audio = sys.argv[3]
        print("Listening...")
    except IndexError:
        sys.exit("Usage: python server.py IP port audio_file")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("\nFinalizado servidor")
