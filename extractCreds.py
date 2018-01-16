#!/usr/bin/env python

import sys
import struct
import hexdump

__version__ = "0.0"
__author__ = "@ret5et"


def _print(s):
    print "%s:%s" % (s[0], s[1])

logreqmark = 'SCertReq'
creds = set()
with open(sys.argv[1],"rb") as fd:
    data = fd.read()

while True:

    idx = data.find(logreqmark)
    if idx == -1:
        break

    idx += len(logreqmark)

    login_len = struct.unpack('b', data[idx])[0]
    idx += 1

    login = data[idx: idx+login_len]
    login = login.decode('utf-16be')
    idx += login_len


    pwd_len = struct.unpack('b', data[idx])[0]
    idx += 1

    password = data[idx: idx+pwd_len]
    password = password.decode('utf-16be')
    idx +=  pwd_len

    creds.add((login, password))

    data = data[idx:]

map(_print, creds)





