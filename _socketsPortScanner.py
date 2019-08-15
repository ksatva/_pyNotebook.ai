#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title - Port scanner with sockets

WARNING: 
    It should be noted that port scanning can be seen as, or construed as, a crime.
    You should never execute a port scanner against any website or IP address 
    without explicit, written, permission from the owner of the server or computer 
    that you are targeting. Port scanning is akin to going to someones house and 
    checking out all of their doors and windows. There is really only reason why 
    anyone would do this, and it is to assess securities and vulnerabilities. 
    Thus, if you have no good reason to be testing these things, it can be assumed 
    you are a criminal.

TO BE SAFE:
    For the target, you could enter website that allows you to do this. 
    Check out "https://www.hackthissite.org/", or 
    you can always target your own servers.


Created on Tue Aug 13 16:45:37 2019
@author: k as root
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

target = input('What website to scan?: ')
# Enter: https://www.hackthissite.org/

def pscan(port):
    try:
        con = s.connect((target,port))
        return True
    except:
        return False


for x in range(100):
    if pscan(x):
        print('Port',x,'is open')	    
	  
# Troubleshoot
# https://pythonprogramming.net/python-port-scanner-sockets/?completed=/python-sockets/       