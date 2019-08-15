#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title - Creates a dynamic website with WSGI (Web Server Gateway Interface)

Created on Mon Aug 12 22:07:20 2019
@author: k as root
"""

from wsgiref.simple_server import make_server

def application(environ, start_response):
    start_response("200 OK", [("Content-type", "text/plain")])
    return ["Hello my friend!".encode("utf-8")]


server = make_server('localhost', 8080, application)
server.serve_forever()



"""
# example 2--->>
from wsgiref.simple_server import make_server

def application(environ, start_response):
    start_response("200 OK", [("Content-type", "text/plain")])

    fh = open("ulysses.txt")               # -------< enter file to open >
    lines = [fh.readline().encode("utf-8") for i in range(30)]

    return lines


server = make_server('saturn', 8080, application)
server.serve_forever()


# Check in browser with url "saturn:8080"
"""

# https://www.python-course.eu/dynamic_websites_wsgi.php