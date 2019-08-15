#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title - Sockets (HTTPS)

Created on Tue Aug 13 16:43:07 2019
@author: k as root
"""

import socket
import ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = True
context.load_default_certs()

server = "pythonprogramming.net" #-------------< server name > 
port = 443
server_ip = socket.gethostbyname(server)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = context.wrap_socket(s, server_hostname=server)

request = "GET / HTTP/1.1\nHost: "+server+"\n\n" #--------< GET request >

s.connect((server,port))
s.send(request.encode())
result = s.recv(4096)

while (len(result) > 0):
    print(result)
    result = s.recv(4096)
    
    
# https://pythonprogramming.net/python-sockets/?completed=/ftp-transfers-python-ftplib/