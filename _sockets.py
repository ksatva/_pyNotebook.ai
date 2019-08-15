#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title - Sockets
"Sockets are used in networking. The idea of a socket is to aid in the communication 
between two entities. When you view a website, you are opening a port and connecting 
to that website via sockets. In this, you are the client, and the website is the server. 
Quite literally, you are served data."

Q. What are Ports and what are Sockets?
Ans. A natural point of confusion here is the difference between sockets and ports. 
     You can think of a port much like a shipping port, where boats dock at the port and unload goods. 
     Then, you can think of the ship itself as the socket. 

     The ocean is the internet. 
     Much like shipping ports, a socket (our ship in this metaphor), 
     is bound by a specific port. Docking at a different port is not allowed, 
     for ships or sockets!


Created on Tue Aug 13 16:06:07 2019
@author: k as root
"""

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket descriptor
print(s)

# -----< eg. >
server = 'reddit.com'   # website name
port = 80               # HTTP port
"""
port = 22  # SSH port
port = 20  # FTP
port = 21  # FTP
port = 443 # HTTPS

# all websites have open ports, 
# but each port is expecting a specific socket (ship in our metaphor from before), 
# and that specific socket's type of payload of data (ship's cargo) is also known 
# and expected before-hand.
# If the expected payload differs 'The socket / ship can be denied'

# TODO: Make a port scanner (scan open ports of an website/app/service)
"""

# retreiving "Server ip from donain name" ----< 1 >
server_ip = socket.gethostbyname(server)
print(server_ip)


## making an HTTP request --------------< 2 >
# Update: do with "requests" module
# 1. defining HTTP request: GET data from host "PythonProgramming.net"
request = "GET / HTTP/1.1\nHost: "+server+"\n\n"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #defining socket (ship)
s.connect(("reddit.com", 80)) # connecting to server
s.send(request.encode())      # sending request
result = s.recv(4096)         # receiving data - buffer: 4096 bytes

print(result) # Do not use this. Instead use the following code
"""
With Python 3, one of the major changes from Python 2 was the differing 
treatment of strings and bytes. If you want to make a request that is a string,
you need to encode it. You will also need to decode any return that you wish 
to treat like a string. You should just get into the habit mentally that 
everything you send out over the internet needs to be encoded, and all that 
you receive needs a .decode, every time! Python 2 implicitly handled this for us. 
Python 3 requires us to be explicit, which is more Pythonic anyways.

One of the main pillars of Python is that "explicit is better than implicit. 
If you have not yet, open a console, and do the following import: 
"""
import this #????????
while (len(result) > 0):
    print(result)
    result = s.recv(4096) #----------------< 2 end >
    

