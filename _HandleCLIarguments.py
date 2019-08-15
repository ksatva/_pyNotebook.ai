#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title - Handle command line arguments

Created on Sun Aug 11 22:04:55 2019
@author: k as root
"""

#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard

import webbrowser, sys

if len(sys.argv) > 1:
    # Get address from command line
    address = ' '.join(sys.argv[1:])
    
# TODO: Get address from the clipboard