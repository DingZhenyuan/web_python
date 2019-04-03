#!/user/bin/env python

# TCP Server
from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print("Watiting for connection...")
    tcpCliSock, addr = tcpSerSock.accept()
    print('...Connected from:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send('[%s] %s'.encode(encoding='utf_8') % (bytes(ctime(), 'utf-8'), data))
    tcpCliSock.close()

tcpSerSock.close()

