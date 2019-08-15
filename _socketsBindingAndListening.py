#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title - Binding and listening with sockets

Created on Tue Aug 13 18:39:30 2019
@author: k as root
"""

import socket
import sys

HOST = ''
PORT = 5555

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

## Binding
try:
    s.bind((HOST, PORT))
    
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
	
print('Socket bind complete')

## Listening
s.listen(10)

conn, addr = s.accept()

print('Connected with ' + addr[0] + ':' + str(addr[1]))

"""
Now you can run your script. 
Once you've done that, you should be able to make a connection. 
You will likely get a security notifcation that you must accept in order to 
continue with the tutorial. You are getting this notification because the 
program is trying to open and listen for incoming connections on your behalf. 
As you might imagine, people might attempt to give you malicious software 
to do just this.

Accept the warning if you get one, and now you should be able to telnet localhost 
on the port you chose, which was 5555 for me. 
So, opening bash, a shell, or cmd.exe, type:

    telnet localhost 5555

For now, nothing much will happen, but you should see a black window and your 
running python script should update with the incoming connection address.
"""
#https://pythonprogramming.net/python-binding-listening-sockets/?completed=/python-threaded-port-scanner/