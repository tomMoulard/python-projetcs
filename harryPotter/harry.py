#made by moular_b

import random

def printMat(m):
    s = "|{:2d}"
    for x in m:
        for y in x:
            print (s.format(y), end='')
        print("|")

def makeARoom(h, w):
    res = []
    for x in range(h):
        tmp = []
        for y in range(w):
            tmp.append(random.randint(1,10))
        res.append(tmp)
    return res

a = makeARoom(6,5)
#print(a)
printMat(a)

def getMaxPos(l):
    posM, pos, lenL = 0, 0, len(l)
    while pos < lenL:
        if l[pos] > l[posM]:
            posM = pos
        pos += 1
    print(posM)
    return posM

def harryPotter(m):
    posInM, posInL, lenM, res = 0, getMaxPos(m[0]), len(m), 0
    while posInM < lenM-1:
        res += m[posInM][posInL]
        print("posInM", posInM, "posInL", posInL, "lenM", lenM, "res", res, "actual", m[posInM][posInL])
        tmp = []
        tmpdiff = posInL
        if posInL == 0:
            tmp.append(m[posInM+1][0])
            tmp.append(m[posInM+1][1])
        elif posInL == len(m[posInM])-1:
            tmp.append(m[posInM+1][len(m[posInM])-2])
            tmp.append(m[posInM+1][len(m[posInM])-1])
        else:
            tmp.append(m[posInM+1][posInL-1])
            tmp.append(m[posInM+1][posInL])
            tmp.append(m[posInM+1][posInL+1])
        print(tmp)
        posInL = getMaxPos(tmp) + tmpdiff
        print("posInL", posInL)
        posInM += 1
    return res

#print(a)
print(harryPotter(a))
		