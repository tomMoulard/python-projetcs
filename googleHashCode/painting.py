# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 14:10:41 2016

@author: epita-student
"""

import random

#1 is painted
#0 is eraised

class Painting():
    def paint_plain(n):
        res = []
        for x in range(n):
            tmp =[]
            for y in range(n):
                tmp.append(random.randint(0,1))
            res.append(tmp)
        return res
    def paint_pl(n):
        res = []
        for x in range(n):
            res.append([0]*n)
        return res 
        
    def paint_print(l):
        '''To print the grid'''
        for x in l:
            for y in x:
                print(y , end=' ')
            print()
            
    def paint_square(r, c, s, l):
        '''to paint a square centered in (r, c) with a s radius'''
        minX, minY, maxX, maxY = r - s, c - s, r + s, c + s        
        if s == 0:
            l[r][c] == 1
        else:
            for x in range(minX, maxX):
                Painting.paint_line(x, minY, x, maxY, l)
        return l
    
    def paint_line(r1, c1, r2, c2, l):
        '''use to draw a line'''
        print("c1", c1, "c2", c2 )
        if r1 == r2 and c1 == c2:
            l[r1][c1] = 1
            return l
        elif r1 == r2:
            for x in range(c1, c2):
                l[r1][x] = 1
            return l
        elif c1 == c2:
            for x in range(r1, r2):
                l[x][c1] = 1            
            return l
        else:
            raise Exception ("Bad Input")
    
    def erase_cell(r, c, l):
        '''Used to erase a place'''
        l[r][c] = 0
    
pict = Painting()
pict.tmp = []
pict.tmp = Painting.paint_pl(10)
#pict.tmp = Painting.paint_line(1 ,1 ,8 ,1 , pict.tmp)
#pict.tmp = Painting.paint_line(1 ,1 ,1 ,8 , pict.tmp)
#pict.tmp = Painting.paint_line(0 ,4 ,3 ,4 , pict.tmp)
pict.tmp = Painting.paint_square(5, 5, 5, pict.tmp)
Painting.paint_print(pict.tmp)























(pict.tmp)