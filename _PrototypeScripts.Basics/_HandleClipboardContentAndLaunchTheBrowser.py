#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Handle the clipboard content and launch the browser

Created on Sun Aug 11 21:53:25 2019
@author: k as root
"""

#! python3
# mapIt.py - launch a map in the browser using an address from the
# command line or clipboard

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from the command line
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()

mapheaderurl = 'https://www.google.com/maps/place/'
webbrowser.open(mapheaderurl + address)
        
