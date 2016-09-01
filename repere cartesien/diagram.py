# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 16:55:23 2016

@author: tm
"""

dots = []
    
from tkinter import *
root = Tk()
frame = Frame(root)
frame.pack()
label = Label(frame, text="Hey there.")
label.pack()
quitButton = Button(frame, text="Quit", command=frame.quit)
quitButton.pack()