#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 02:55:35 2019

@author: root
"""

from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    return Response("Hello, World!")

if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple("localhost", 5000, application)


# NoFirstUse
