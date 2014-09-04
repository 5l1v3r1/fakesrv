#!/usr/bin/env python

import os
import sys
import socket
import signal

def handleUDP(cs, MSG):
    (data, addr) = cs.recvfrom(1024)
    print("%s\n" % data)
    cs.sendto("%s\n" % MSG, addr)

def handleTCP(cs, addr, MSG):
    print("Connection from: %s", addr)
    data = cs.recv(1024)
    print("%s\n" % data)
    cs.sendall("%s\n" % MSG)

def main():
    if len(sys.argv) != 4:
        print('Usage: %s PORT MSG PROTO' % sys.argv[0])
        sys.exit(1)

    PROTO = sys.argv[1]
    PORT = int(sys.argv[2])
    MSG = sys.argv[3]

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
