# -*- coding: utf-8 -*-

import sys

A = [
"   ##  ",
"  #  # ",
" #    #",
" ######",
" #    #",
" #    #",
]
B = [
" ##### ",
" #    #",
" ##### ",
" #    #",
" #    #",
" ##### ",
]
C = [
"  #### ",
" #    #",
" #     ",
" #     ",
" #    #",
"  #### ",
]
D = [
" ##### ",
" #    #",
" #    #",
" #    #",
" #    #",
" ##### ",
]
E = [
" ######",
" #     ",
" ##### ",
" #     ",
" #     ",
" ######",
]
F = [
" ######",
" #     ",
" ##### ",
" #     ",
" #     ",
" #     ",
]
G = [
"  #### ",
" #    #",
" #     ",
" #  ###",
" #    #",
"  #### ",
]
H = [
" #    #",
" #    #",
" ######",
" #    #",
" #    #",
" #    #",
]
I = [
"    #  ",
"    #  ",
"    #  ",
"    #  ",
"    #  ",
"    #  ",
]
J = [
"      #",
"      #",
"      #",
"      #",
" #    #",
"  #### ",
]
K = [
" #    #",
" #   # ",
" ####  ",
" #  #  ",
" #   # ",
" #    #",
]
L = [
" #     ",
" #     ",
" #     ",
" #     ",
" #     ",
" ######",
]
M = [
" #    #",
" ##  ##",
" # ## #",
" #    #",
" #    #",
" #    #",
]
N = [
" #    #",
" ##   #",
" # #  #",
" #  # #",
" #   ##",
" #    #",
]
O = [
"  #### ",
" #    #",
" #    #",
" #    #",
" #    #",
"  #### ",
]
P = [
" ##### ",
" #    #",
" #    #",
" ##### ",
" #     ",
" #     ",
]
Q = [
"  #### ",
" #    #",
" #    #",
" #  # #",
" #   # ",
"  ### #",
]
R = [
" ##### ",
" #    #",
" #    #",
" ##### ",
" #   # ",
" #    #",
]
S = [
"  #### ",
" #     ",
"  #### ",
"      #",
" #    #",
"  #### ",
]
T = [
"  #####",
"    #  ",
"    #  ",
"    #  ",
"    #  ",
"    #  ",
]
U = [
" #    #",
" #    #",
" #    #",
" #    #",
" #    #",
"  #### ",
]
V = [
" #    #",
" #    #",
" #    #",
" #    #",
"  #  # ",
"   ##  ",
]
W = [
" #    #",
" #    #",
" #    #",
" # ## #",
" ##  ##",
" #    #",
]
X = [
" #    #",
"  #  # ",
"   ##  ",
"   ##  ",
"  #  # ",
" #    #",
]
Y = [
"  #   #",
"   # # ",
"    #  ",
"    #  ",
"    #  ",
"    #  ",
]
Z = [
" ######",
"     # ",
"    #  ",
"   #   ",
"  #    ",
" ######",
]
SPACE = [
" ",
" ",
" ",
" ",
" ",
" ",
]

def l2b(l):
    if l in ['a', 'A']:
        return A
    elif l in ['b', 'B']:
        return B
    elif l in ['c', 'C']:
        return C 
    elif l in ['d', 'D']:
        return D 
    elif l in ['e', 'E']:
        return E 
    elif l in ['f', 'F']:
        return F 
    elif l in ['g', 'G']:
        return G 
    elif l in ['h', 'H']:
        return H 
    elif l in ['i', 'I']:
        return I 
    elif l in ['j', 'J']:
        return J 
    elif l in ['k', 'K']:
        return K 
    elif l in ['l', 'L']:
        return L 
    elif l in ['m', 'M']:
        return M 
    elif l in ['n', 'N']:
        return N 
    elif l in ['o', 'O']:
        return O 
    elif l in ['p', 'P']:
        return P 
    elif l in ['q', 'Q']:
        return Q 
    elif l in ['r', 'R']:
        return R 
    elif l in ['s', 'S']:
        return S 
    elif l in ['t', 'T']:
        return T 
    elif l in ['u', 'U']:
        return U 
    elif l in ['v', 'V']:
        return V 
    elif l in ['w', 'W']:
        return W 
    elif l in ['x', 'X']:
        return X 
    elif l in ['y', 'Y']:
        return Y 
    elif l in ['z', 'Z']:
        return Z 
    elif l in [' ']:
        return SPACE
    else:
        return []

def main():
    res = ["", "", "", "", "", ""]
    alllettres = ""
    for x in range(1, len(sys.argv), 1):
        alllettres += sys.argv[x] + " "
    for l in alllettres:
        tmp = l2b(l)
        for x in range(len(res)):
            res[x] += tmp[x]
    #printing
    for x in res:
        print(x)

if __name__ == '__main__':
    main()