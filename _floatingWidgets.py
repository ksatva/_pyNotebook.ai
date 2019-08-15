#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title - Floating widgets with text "tkinter"

Created on Sun Aug 11 22:34:58 2019
@author: k as root
"""

import tkinter as tk

root = tk.Tk()
root.attributes('-type','dialog') # For floating windows in i3-windowmanager
T = tk.Text(root, height=2, width = 30)
T.pack()
T.insert(tk.END, "Just a text Widget\nin two lines\n" )
tk.mainloop()


"""
Explore tkinter for more
"""