#-*-coding:utf8;-*-
#qpy:3
#qpy:console
#made by moular_b

def bubbleSortT(l): #bubble sort of a tuple list
    for x in range(len(l)-1, 0, -1):
        for i in range(x):
            if l[i][1] < l[i+1][1]:
                tmp = l[i]
                l[i] = l[i+1]
                l[i+1] = tmp
                
def maxListT(l): #return max(list de tupel)
    res = ("yolo", -1)
    for i in l:
        if i[1] > res[1]:
            res = i
    return res

def dell2(l, pos):
    res, i, deleted, lenL = [], 0, False, len(l)
    if pos > lenL or pos < 0:
        return l
    while i < lenL and not deleted:
        if i == pos:
            deleted = True
        else:
            res.append(l[i])
            i += 1
    while i < lenL:
        res.append(l[i])
        i += 1
    return res

def dell(l, pos): #supprime l element d une liste
    lenL, i, res = len(l), 0, []
    if pos > lenL - 1 or pos < 0:
       return("bad pos to dell")
    while i < lenL:
        #print(i, l[i], pos, lenL, res)
        if i != pos:
            res.append(l[i])
        i += 1
    return res

def nbCar(s):# function to enumerate every char of a string
    res = []
    for elt in s:
        found, i, lenS = False, 0, len(res)
        while i < lenS and not found:
            #print(res)
            if elt == res[i][0]:
                #print(res[i], elt)
                found = not found
                #print(res[i][1])
                tmp = (res[i][0], res[i][1] + 1)
                res = dell(res, i)
                res.append(tmp)
            i += 1
        if not found:
            res.append((elt, 1))
    bubbleSortT(res)
    return(len(res), maxListT(res), res)

def ask():#call fun
    s = str(input("String ? "))
    (lenRes, mAx, l) = nbCar(s)
    print("len(string) =", len(s), "\nNb char diff :", lenRes, "\nMax occurence = ", mAx, "\nEntire list : ", l)
while True:
    ask()