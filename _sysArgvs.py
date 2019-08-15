#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title - Command line arguments (sys.argv)

Created on Sun Aug 11 22:26:15 2019
@author: k as root
"""

"""
import sys
programName = sys.argv[0]
arguments = sys.argv[1:]
count = len(arguments)
"""

import sys

def main():
    if len(sys.argv) == 4:
        if sys.argv[1] == 'add':
            print(int(sys.argv[2]) + int(sys.argv[3]))
        elif sys.argv[1] == 'sub':
            print(int(sys.argv[2]) - int(sys.argv[3]))
    else:
        print("Invalid Arguments")

if __name__ == '__main__':
    main()

# Run using following command
#    python _sysArgvs.py add 5 3
#    python _sysArgvs.py sub 5 3