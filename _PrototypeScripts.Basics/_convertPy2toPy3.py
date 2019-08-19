#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title - Converting Python2 code to Python3 code
        *** Python 3 comes with a script called "2to3", 
        which converts quite a bit of common differences between Python 2 and Python 3 code. 
        (LOCATE THIS FILE IN YOUR SYSTEM)

Created on Tue Aug 13 18:51:17 2019
@author: k as root
"""

"""
Some differences between py2 and py3:

py2: print "Hello"
py3: print("Hello")
-------------------------

py2:
try:
    dosomething
except Exception, e:
    return str(e)

py3:
try:
    dosomething
except Exception as e:
    return str(e)
-----------------------

urllib2 module in py2 ---Internet information returned as string data
urllib in py3 -----internet information returned as Bytes
# UPDATE: use "requests" module instead in python3

======================

NOW CONVERSION 2 to 3:
   
EXECUTE IN SHELL:
    $ 2to3.py python2script.py    # To view changes
    $ 2to3.py -w python2script.py # To convert

"""
