#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 02:55:35 2019

@author: root
"""

# Example: webapplication that prints "Hello, World!"
from werkzeug.wrappers import Request, Response
import webbrowser as wb


@Request.application
def application(request):
    return Response("Hello, World!")

if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple("localhost", 5000, application)

# open a browser and type url: http://localhost:5000/
#                   OR
    url="http://localhost:5000/";
    wb.open_new_tab(url)
    




# NoFirstUse
