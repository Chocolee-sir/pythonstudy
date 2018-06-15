#!/usr/bin/env python
# encoding:utf-8
__author__ = 'Chocolee'

import socket

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost',8088))
    sock.listen(5)

    while True:
        connection, address = sock.accept()
        buf = connection.recv(1024)
        data = open('img.html', 'rb').read()
        connection.sendall(bytes("HTTP/1.1 201 OK\r\n\r\n","utf8"))
        connection.sendall(bytes(data))
        connection.close()

if __name__ == '__main__':

    main()