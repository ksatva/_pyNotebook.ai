#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 19:58:45 2019

@author: k as root
"""

import requests

url = 'http://google.com/favicon.ico'
r = requests.get(url, allow_redirects=True)

##---------------
print(r.headers.get('content-type'))

# 1. code to download the media at http://google.com/favicon.ico and save it as google.ico.
open('google.ico', 'wb').write(r.content)


def isDownloadable(url):
    """
    Does the url contain a downloadable resource
    """
    h = requests.head(url, allow_redirects = True)
    header = h.headers
    contentType = header.get('content-type')
    contentLength = header.get('content-length', None)
    
    if 'text' in contentType.lower():
        return False
    if 'html' in contentType.lower():
        return False
    #restricting download greater than 200mB   
    if contentLength and contentLength > 2e8:  # 200 mb approx
        return False
    return True


print(isDownloadable('https://www.youtube.com/watch?v=9bZkp7q19f0'))
# >> False
print(isDownloadable('http://google.com/favicon.ico'))
# >> True

# Get filename from url
url = 'http://aviaryan.in/images/profile.png'
if url.find('/'):
  print(url.rsplit('/', 1)[1])
"""
This will be give the filename in some cases correctly.
However, there are times when the filename information is not present in the url.
Example, something like "http://url.com/download." In that case, 
the "Content-Disposition" header will contain the filename information.
Here is how to fetch it---->>
"""
import requests
import re

def getFilenameFromCdHeader(cd):
    """
    Get filename from content-disposition
    """
    if not cd:
        return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
        return None
    return fname[0]


url = 'http://google.com/favicon.ico'
r = requests.get(url, allow_redirects=True)
filename = getFilenameFromCdHeader(r.headers.get('content-disposition'))
open(filename, 'wb').write(r.content) # troubleshoot

