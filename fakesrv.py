#!/usr/bin/env python

import os
import sys
import socket
import signal

def handleUDP(cs, MSG):
    data, addr = cs.recvfrom(1024)
    print("Connection from {0:s}:{1:s}".format(addr[0], addr[1]))
    print("{0:s}:{1:s}: {2:s}".format(addr[0], addr[1], data.rstrip('\n')))
    if MSG:
        cs.sendto("{0:s}".format(MSG), addr)

def handleTCP(cs, addr, MSG):
    print("Connection from: {0:s}:{1:s}".format(addr[0], addr[1]))
    try:
        data = cs.recv(1024)
        print("{0:s}:{1:s}: {2:s}".format(addr[0], addr[1], data.rstrip('\n')))
        if MSG:
            cs.sendall("{0:s}".format(MSG))
        cs.close()
    except:
        print("Some error, killing connection")
        cs.close()

def main():
    if len(sys.argv) != 4:
        print("Usage: {0:s} PROTO PORT FILE/MSG".format(sys.argv[0]))
        sys.exit(1)

    PROTO = sys.argv[1]
    PORT = int(sys.argv[2])
    FILE = sys.argv[3]
    MSG = ""

    try:
        with open(FILE, "r") as f:
            MSG = f.read()
    except:
        print("File {0:s} does not exist. Using input as message to send.".format(FILE))
        MSG = FILE

    signal.signal(signal.SIGCHLD, signal.SIG_IGN)

    if PROTO.upper() == 'TCP':
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('0.0.0.0', PORT))
        s.listen(100)
        while 1:
            (cs, addr) = s.accept()
            pid = os.fork()
            if pid == 0:
                s.close()
                handleTCP(cs, addr, MSG)
                sys.exit(0)
            cs.close()

    elif PROTO.upper() == 'UDP':
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(('0.0.0.0', PORT))
        while 1:
            handleUDP(s, MSG)

    else:
        print('PROTO is either TCP or UDP')
        sys.exit(1)
    return 0

if __name__ == '__main__':
    sys.exit(main())
