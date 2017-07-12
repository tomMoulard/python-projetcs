#-*-coding:utf8;-*-
"""
Made by tomMoulard
The goal is to create a new sudoku and being able to display the solution
The sudoku is renewed each hours therfore it is useless to run it twice in one hour
"""

import random
import time

DIFF = 150

def newTable():
    return [[0]*9 for x in range(9)]
    
def printTable(T):
    line = "+~~~~~~~+~~~~~~~+~~~~~~~+"
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

def suffle(l):
    """
    suffle a list in place
    need random
    And is very slow
    """
    #print(l, end=" -> ")
    pos = 0
    ll = len(l)
    while pos < ll:
        newPos = random.randint(pos, ll-1)
        l[pos], l[newPos] = l[newPos], l[pos]
        pos += 1
    #print(l)

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
    if len(possibleVal) == 1 and casePos > 79:
        T[x][y] = possibleVal[0]
        return (T, 1)
    if len(possibleVal) == 0 and casePos < 80:
        return (T, 0)
    xn, yn = getNext(x,y)
    suffle(possibleVal)
    for num in possibleVal:
        #print("({},{}) {} {} -> {}".format(x, y, casePos, possibleVal, num))
        T[x][y] = num
        tmp, code = appRec(T, xn, yn, casePos + 1)
        if code == 1:
            return (tmp, 1)
    T[x][y] = 0
    return (T, 0)

def cpyTable(T):
    """
    return a hard copy of the table
    """
    res = []
    for lines in T:
        tmp = []
        for col in lines:
            tmp.append(col)
        res.append(tmp)
    return res

def nbZeros(T):
    """
    return the number of zero(s) in the table
    """
    zeros = 0
    for x in T:
        for y in x:
            if y == 0:
                zeros += 1
    return zeros

def getE(H, T):
    """
    This get the errors / fails between two Tables
    And does not count empty cases
    """
    res = 0
    for l in range(9):
        for c in range (9):
            if H[l][c] != 0 and H[l][c] != T[l][c]:
                res += 1
    return res

def play(h, T):
    """
    Big loop to play with the sudoku
    """
    H = cpyTable(h)
    t = time.time()
    wtp = """
    So you want to play ?
    here is the input :
        - X Y     : Put cursor in position (x, y) in the table and display possbles numbers to put
        - X Y VAL : Put VAL in position (x, y) in the table
        - verify  : Display numbers
        - help    : Print easy fill in
        - q       : Quit
    """
    print(wtp) #Way to play
    quit = False
    while not quit:
        n = input(">>> ")
        if n == "q":
            quit = True
        else:
            n = n.split(" ")
            if len(n) == 2:
                n = [int(x) for x in n]
                printTable(H)
                print(possiblesNumbers(H, n[0], n[1]))
            elif len(n) == 3:
                n = [int(x) for x in n]
                H[n[0]][n[1]] = n[2]
                printTable(H)
            elif n == ["help"]:
                xt, yt = 0, 0
                for x in range(81):
                    pN = possiblesNumbers(H, xt, yt)
                    if H[xt][yt] == 0 and len(pN) == 1:
                        print("({}, {}) -> {}".format(xt, yt, pN[0]))
                    xt, yt = getNext(xt, yt)           
            else:
                zeros = nbZeros(H)
                err = getE(H, T)
                if zeros == 0:
                    print("You filled every holes in {} and made {} errors, Congratulations !".format(time.time() - t, err))
                else:
                    print("There is still {} hole(s) to fill and there is {} errors ({})".format(zeros, err, time.time() - t))
                
def generateGrid():
    """
    This is the hat function to create a Table
    return a 2D array containing a new grid
    """
    res = newTable()
    x,y,val = pickAPlace()
    res[x][y] = val
    xn, yn = getNext(x, y)
    res, code = appRec(res, xn, yn, 0)
    return res

def main(nb):
    """
    This is the main function:
        it create a table and put holes regarding nb
        then ask the user if he wants to play
        and makes him play of he want to
    """
    random.seed(str([x for x in time.gmtime()[:4]]))
    res = generateGrid()
    hollow = cpyTable(res)
    for diff in range(int(nb * random.random())):
        xt, yt, val = pickAPlace()
        hollow[xt][yt] = 0
    printTable(hollow)
    n = input(\
        "Do you want the response or do you want to play ?\n(\"R\" or \"P\") ")
    if n == "P":
        play(hollow, res)
    printTable(res)
    return res
    
main(DIFF)
