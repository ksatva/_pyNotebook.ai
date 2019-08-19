#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 04:25:21 2019

@author: root
"""

from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'









# cite: 'Werkzeug' (a comprehensive WSGI web application library)
# Flask wraps 'Werkzeug' using it to handle the details of WSGI while 
# providing more structure and patterns for defining powerful applications.

# https://palletsprojects.com/p/flask/


# NoFirstUse
