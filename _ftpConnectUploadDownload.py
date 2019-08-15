#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title - FTP connection, upload and download a file

Created on Tue Aug 13 15:59:36 2019
@author: k as root
"""

from ftplib import FTP

#domain name or server ip:
ftp = FTP('123.server.ip')
ftp.login(user='username', passwd = 'password')
#connection to remote server complete

## change to a specific directory
ftp.cwd('/whyfix/')

##Download a file
def grabFile():

    filename = 'example.txt'

    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024) # retreive binary data. buffer = 1024

    ftp.quit()
    localfile.close()


##Uploading a file
def placeFile():

    filename = 'exampleFile.txt'
    ftp.storbinary('STOR '+filename, open(filename, 'rb'))
    ftp.quit()

placeFile()
    
    
# https://pythonprogramming.net/ftp-transfers-python-ftplib/