#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 04:52:29 2019

@author: root
"""

"""MarkupSafe implements a text object that escapes characters so it is safe 
to use in HTML and XML. Characters that have special meanings are replaced 
so that they display as the actual characters. 

This mitigates injection attacks, meaning untrusted user input can safely be 
displayed on a page. Escaping is implemented in C so it is as efficient as possible."""


from markupsafe import Markup, escape
# escape replaces special characters and wraps in Markup
escape('<script>alert(document.cookie);</script>')
# op: Markup(u'&lt;script&gt;alert(document.cookie);&lt;/script&gt;')

#>>> # wrap in Markup to mark text "safe" and prevent escaping
Markup('<strong>Hello</strong>')
# op: Markup('<strong>hello</strong>')

escape(Markup('<strong>Hello</strong>'))
# op: Markup('<strong>hello</strong>')

#>>> # Markup is a text subclass (str on Python 3, unicode on Python 2)
#>>> # methods and operators escape their arguments

template = Markup("Hello <em>%s</em>")
template % '"World"'
# op: Markup('Hello <em>&#34;World&#34;</em>')




# NoFirstUse
