#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 02:40:31 2019

@author: root
"""

# googlesearh: conda install flup
def myapp(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['Hello World!\n']

"""
if __name__ == '__main__':
    from flup.server.fcgi import WSGIServer
    WSGIServer(myapp).run()
   """ 
# wsgi from wiki official     
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    yield b'Hello, World\n'

#Example: calling an wsgi example
from io import BytesIO

def call_application(app, environ):
    status = None
    headers = None
    body = BytesIO()
    
    def start_response(rstatus, rheaders):
        nonlocal status, headers
        status, headers = rstatus, rheaders
        
    app_iter = app(environ, start_response)
    try:
        for data in app_iter:
            assert status is not None and headers is not None, \
                "start_response() was not called"
            body.write(data)
    finally:
        if hasattr(app_iter, 'close'):
            app_iter.close()
    return status, headers, body.getvalue()

environ = {...}  # "environ" dict
status, headers, body = call_application(app, environ)

"""Example: Publisher middleware
from flup.middleware.session import MemorySessionStore, SessionMiddleware
from flup.middleware.gzip import GzipMiddleware
from flup.middleware.error import ErrorMiddleware

def myapp(environ, start_response):
    session = environ['com.saddi.service.session'].session
    count = session.get('count', 0) + 1
    session['count'] = count
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['You have been here %d times!\n' % count]

sessionStore = MemorySessionStore()
app = SessionMiddleware(sessionStore, myapp)

app = GzipMiddleware(app)

app = ErrorMiddleware(app, 'wsgi-admin@example.com')

if __name__ == '__main__':
    from flup.server.ajp import WSGIServer
    WSGIServer(app).run()
"""


# NoFirstUse
