# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 12:26:05 2016

@author: tm
"""

#import webbrowser
url = "http://tom.moulard.org"
#webbrowser.open(url)
#for x in range(10):    
#    webbrowser.open(url, new=0, autoraise=False)
 
import re
import mechanize

br = mechanize.Browser()
br.open("http://www.example.com/")