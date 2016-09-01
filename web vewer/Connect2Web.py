# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 17:39:59 2016

@author: moular_b
"""

import urllib.request
opener = urllib.request.FancyURLopener({})
 
def cut2url(src, begin="du=", end="&"):
    '''To extract url from the responce'''
    res = []
    tmp = src.split(begin)    
    for x in tmp:
        pos, ll, resTmp = 0, len(x), "http://"
        while pos < ll and x[pos] != end:
            resTmp += x[pos]
            pos +=1
        res.append(resTmp)
    return res

def printList(l):
    '''To printthe list'''
    for x in l:
        print("", x, "", sep="")

def rmDoublons(l):
    '''To remove excedent urls''' 
    res = []
    pos, ll = 1, len(l)
    while pos < ll:
        if  not pos == ll - 1 and not l[pos] == l[pos + 1]:
            res.append(l[pos])
        pos += 1
    return res

def generateUrl(keyWord):
    '''easier to generate 1st url'''
    return ("http://www.dogpile.com/search/web?fcoid=417&fcop=topnav&fpid=2&q="
            + keyWord) 

url = generateUrl("science")
#url = "http://www.science-et-vie.com/"       
responce = str(opener.open(url).read())
urls = rmDoublons(cut2url(responce))
printList(urls)

#print(responce)

    