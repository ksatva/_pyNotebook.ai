#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title - Executing shell scripts with os.system()

Created on Mon Aug 12 23:15:51 2019
@author: k as root
"""
"""
# In linux 
import os
def getch():
    os.system("bash -c \"read -n 1\"")

getch() """


"""
# for Windows
from msvcrt import getch"""

# Independent of OS (LINUX/Windows)
import os, platform
if platform.system() == "Windows":
    import msvcrt
def getch():
    if platform.system() == "Linux":
        os.system("bash -c \"read -n 1\"")
    else:
        msvcrt.getch()

print("Type a key!")
getch()
print("Okay")

"""
# The Bash command "read -n 1 waits for a key (any key) to be typed.
# If you import os, it's easy to write a script providing getch() 
# by using os.system() and the Bash shell. 
# getch() waits just for one character to be typed without a return
# Following code overcomes this (TODO: convert in python3)

import os

command = " "
while (command != "exit"):
    command = raw_input("Command: ")
    handle = os.popen(command)
    line = " "
    while line:
        line = handle.read()
        print line
    handle.close()

print "Ciao that's it!"

"""


# https://www.python-course.eu/os_module_shell.php