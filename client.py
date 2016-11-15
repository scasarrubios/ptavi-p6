#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

try:
    SERVER = sys.argv[2].split('@')[-1].split(':')[0]
    PORT = int(sys.argv[2].split(':')[-1])
    RECEIVER = sys.argv[2].split('@')[0]
    method = sys.argv[1].upper()
except:
    sys.exit('Usage: client.py method receiver@ip:SIPport')

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((SERVER, PORT))

line = method + ' sip:' + RECEIVER + '@' + SERVER + ' SIP/2.0'
print("Enviando: " + line)
my_socket.send(bytes(line, 'utf-8') + b'\r\n\r\n')
answer = my_socket.recv(1024)
template = ('SIP/2.0 100 Trying\r\n\r\n'
            'SIP/2.0 180 Ring\r\n\r\n'
            'SIP/2.0 200 OK\r\n\r\n')
if answer == template:
    method = 'ACK'
    line = method + ' sip:' + RECEIVER + '@' + SERVER + ' SIP/2.0'
    my_socket.send(bytes(line, 'utf-8') + b'\r\n\r\n')
print('Recibido -- ', data.decode('utf-8'))
print("Terminando socket...")

# Cerramos todo
my_socket.close()
print("Fin.")
