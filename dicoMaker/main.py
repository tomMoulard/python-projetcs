# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 12:15:54 2016

@author: tomMoulard
"""
import time

bb = [" ","a","b","c","d","e","f",
      "g","h","i","j","k","l","m",
      "n","o","p","q","r","s","t",
      "u","v","w","x","y","z"]
lRes = []

def buildlist(x, prec, bBL, l):
    """
    use like :
        x    : poids (ex: 3 will make 000 to zzz)
        prec : str du debut
        bBL  : len(bb) -> fast :3
    """                        
    for n in range(bBL):
        if x == 1:
            l.append(prec) 
            return 
        else:
            buildlist((x-1), (prec+str(bb[n])), bBL, l)
            
def makeADir(path):
    import os
    if not os.path.exists(path):
        os.mkdir(path)
            
            
def fillFile(fileName, l):
    file = open(fileName,'a')
    file.writelines("Made by tomMoulard\n")
    for x in l:
        file.writelines(x)
    file.close()
    
def generateName():
    return "C:/junk/" + str(time.clock())
    
def main():
    n = generateName()
    makeADir("C:/junk/")
    l = []
    buildlist(26, "", len(bb), l)
    fillFile(n, l)
    