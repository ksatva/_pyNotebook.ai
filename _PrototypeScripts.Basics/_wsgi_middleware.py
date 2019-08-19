#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 03:07:31 2019

@author: root
"""


def simple_app(environ, start_response):
    """Simplest possible application object"""
    status = '200 OK'
    response_headers = [('Content-type','text/plain')]
    start_response(status, response_headers)
    return ['Hello world!\n']

#https://be.groovie.org/2005/10/07/wsgi_and_wsgi_middleware_is_easy.html
#https://wsgi.readthedocs.io/en/latest/learn.html




# NoFirstUse
