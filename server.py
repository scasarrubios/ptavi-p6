#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys


class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.wfile.write(b"Hemos recibido tu peticion")
        line = self.rfile.read().decode('utf-8').split()

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    try:
        serv = socketserver.UDPServer((sys.argv[1], int(sys.argv[2])), EchoHandler)
        print("Lanzando servidor UDP de eco...")
    except IndexError:
        sys.exit("Usage: python server.py IP port audio_file")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("\nFinalizado servidor")
