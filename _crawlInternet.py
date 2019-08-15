#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A prototype that crawls internet. It crawls a site looks for internal and 
external links (The external link part is internet crawling)

Created on Thu Aug  8 05:44:21 2019
@author: k as root
"""


import requests
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

# Retreives a list of all Internal links found on a page
def getInternalLinks(bsO, includeUrl):
    internalLinks = []
    # Finds all links that begin with a "/"
    for link in bsO.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks

# Retreives a list of all External links found on a page
def getExternalLinks(bsO,excludeUrl):
    externalLinks = []
    # Finds all links that start with "http" or "www" that donot contain the current url
    for link in bsO.findAll("a", href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    addressParts = address.replace("http://","").split("/")
    return addressParts

def getRandomExternalLink(startingPage):
    r = requests.get(startingPage)
    bsO = BeautifulSoup(r.text,'html.parser')
    externalLinks = getExternalLinks(bsO, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(startingPage) # Troubleshoot: only one positional argument
        #return getNextExternalLinks(internalLinks[random.randint(0,len(internalLinks)-1)])
        return getExternalLinks(internalLinks[random.randint(0,len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0,len(externalLinks)-1)]
    
def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print("Random external link is: "+externalLink)
    followExternalOnly(externalLink)
    
followExternalOnly("http://oreilly.com")