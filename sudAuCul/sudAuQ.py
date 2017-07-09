#-*-coding:utf8;-*-
"""
Made by tomMoulard
The goal is to create a new sudoku and being able to display the solution
NOT FINISHED
"""

import random

DIFF = 80

def newTable():
    return [[0]*9 for x in range(9)]
    
def printTable(T):
    line = "+~~~~~~~~~~~~~~~~~~~~~~~+"
    for w in range(3):
        print(line)
        for x in range(w * 3, (w * 3)+3, 1):
            print("| ", end="")
            for y in range(9):
                if T[x][y] == 0:
                    print(" ", end=" ")
                else:
                    print(T[x][y], end=" ")
                if y % 3 == 2:
                    print("| ", end="")
            print()
    print(line)

def possiblesNumbers(T,x,y):
    """
    return an array of all possibles numbers
    in the (x,y) pos of T
    """
    res = [1,2,3,4,5,6,7,8,9]
    tmp = []
    #cols
    for number in range(9):
        if T[number][y] != 0:
            tmp.append(T[number][y])
    #line
    for number in range(9):
        if T[x][number] != 0 and not T[x][number] in tmp: 
            tmp.append(T[x][number])
    #square
    xC = x
    while xC % 3 != 0:
        xC -= 1
    yC = y
    while yC % 3 != 0:
        yC -= 1
    for col in range(xC, xC + 3):
        for line in range (yC, yC + 3):
            if not T[col][line] in tmp:
                tmp.append(T[col][line])       
    # removing numbers from res
    for num in tmp:
        try:
            res.remove(num)
        except:
            pass
    return res
    
def getNext(x,y):
    """
    this return the tupple of the next pos to pick a number
    """
    x += 1
    if x > 8:
        x = 0
        y += 1
    if y > 8:
        y = 0
    return (x,y)

def pickAPlace():
    """
    return a random place to start and a random number to start with
    """
    return(random.randint(0,8), random.randint(0,8), random.randint(1,9))

def appRec(T, x, y, casePos):
    """
    WARNING EXPLICIT FUNCTION NAME
    recursive function to get all numbers in place for the sudoku
    """
    #printTable(T)
    possibleVal = possiblesNumbers(T, x, y)
    #print(x, y, casePos, possibleVal)
    if len(possibleVal) == 1 and casePos > 79:
        T[x][y] = possibleVal[0]
        return (T, 1)
    if len(possibleVal) == 0 and casePos < 80:
        return (T, 0)
    xn, yn = getNext(x,y)
    for num in possibleVal:
        T[x][y] = num
        tmp, code = appRec(T, xn, yn, casePos + 1)
        if code == 1:
            return (tmp, 1)
    T[x][y] = 0
    return (T, 0)
                    
def generateGrid(nb):
    res = newTable()
    x,y,val = pickAPlace()
    res[x][y] = val
    xn, yn = getNext(x, y)
    res, code = appRec(res, xn, yn, 0)
    #printTable(res)
    hollow = []
    for lines in res:
        tmp = []
        for cols in lines:
            tmp.append(cols)
        hollow.append(tmp)
    for diff in range(nb):
        xt, yt, val = pickAPlace()
        hollow[xt][yt] = 0
    printTable(hollow)
    input("Do you want the response ?")
    printTable(res)
    return res
generateGrid(DIFF)