# -*- coding: utf-8 -*-
"""
Created on Fri Apr 1 16:42:42 2016

@author: Nathalie & Ted for S2
"""

#------------------------------------------------------------------------------
# 0.0 Type

class BinTree:
    pass
    
def nBT(key, left, right):
    T = BinTree()
    T.key = key
    T.left = left
    T.right = right
    return T
    
def bTEx():
    return (nBT(1, nBT(2, 
                       nBT(4, None, None), 
                       nBT(5, None, None)), 
                   nBT(3, None, 
                       nBT(7, 
                           nBT(15, None, None), 
                           None))))
                           
def printBinTree(B):
    print(pBTR(B))
    
def pBTR(B):    
    if None != B:
        return "< "+str(B.key)+', '+str(pBTR(B.left))+', '+str(pBTR(B.right))+'>'

#------------------------------------------------------------------------------
# 1.1 Search

## q1: minimum and maximum
## --

# Returns the minimum key of a non-empty BST
# Iterative version
def minBST(B):
    while B.left != None:
        B = B.left
    return B.key

# Returns the minimum key of a non-empty BST
# Recursive version
def minBST_rec(B):
    if B.left != None:
        return minBST_rec(B.left)
    else:
        return B.key
    
# Returns the maximum key of a non-empty BST
# Iterative version
def maxBST(B):
    while B.right != None:
        B = B.right
    return B.key
    
# Returns the maximum key of a non-empty BST
# Recursive version
def maxBST_rec(B):
    if None == B.right:
        return maxBST_rec(B.right)
    else:
        return B.key


## q2: search for x in B
## --
    
# Returns the node of BST B containing key x or None if not found
# Recursive version
def searchBST(x, B):
    if x = B.key:
        return B
    if B.right == B.left:
        return None
    else:
        if x < B.key:
            return searchBST(x, B.left)
        else:
            return searchBST(x, B.right)

# Returns the node of BST B containing key x or None if not found
# Iterative version
def searchBST_iter(x, B):
    while x != B.key:
        if x < B.key:
            B = B.left
        else:
            B = B.right
    return B


#------------------------------------------------------------------------------
# 1.2 Insert

# Adds a key to a BST
def addBST(x, B):
    if B == None:
        B = nBT(x, None, None)
    else:
        if x < B.key:
            #B = nBT(B.key, addBST(x, B.left), B.right)
            B.left = addBST(x, B.left)
        else:
            #B = nBT(B.key, B.left, addBST(x, B.right))
            B.right = addBST(x, B.right)
    return b

# Build a BST from successive key insertions into an empty BST
def list2BST(L):
    T = None
    for e in L:
        T = addBST(e, T)
    return T

# L = [13, 20, 5, 1, 15, 10, 18, 25, 4, 21, 27, 7, 12]
# B_tuto = list2BST(L)


#------------------------------------------------------------------------------
# 1.3 Delete

# Removes a key from a BST if present.
# Returns the modified tree
# Hint: when the key is found, replace it by one from a leaf and continue
def delBST(x, B):
    if B == None:
        return None
    else:
        if x == B.key:
            if None != B.left and None != B.right:
                B.key = maxBST(B.left) # Find a suitable replacement
                B.left = delBST(B.key, B.left) # Resume suppression
            else:
                if B.left:
                    B = B.right
                else:
                    B = B.left
        else:
            if x < B.key:
                B.left = delBST(x, B.key)
            else:
                B.right = delBST(x, B.right)
        return B

# Bonus, optimized version:
#   1/ Add a function directly suppressing/returning the key replacement.
#   2/ Use it to change the key when found


#----------------------------------------------------------------------------
# 1.4 Insert as new root (bonus)

# Hint: draw a BST, put the new key above (new root), and draw a line
#       "cutting" the BST from top to bottom. Keys lower or equal to the new
#       root go left, keys higher go right.
#       The final function must create the new root, then call "cut" on the
#       previous BST to build the new left and right sub trees
#       Do NOT use the previous addBST to insert all keys into new trees

# Cut a BST into to BSTs, using x as pivot
def cut(B, x):
    if B == None:
        return (None, None)
    else:
        if x >= B.key:
            G = B
            G.right, D = cut(B.right, x) 
        else:
            D = B
            G, D.left = cut(B.left, x)
        return (G, D)

# Add a new root to a BST. Use "cut" to split the old one.
def addRoot(x, B):
    R = nBT(x, None, None)
    (R.left, R.right) = cut(B, x)
    return R
    
# Build a BST from a list using the "addRoot" method
def list2BST_root(L):
    T = None
    for e in L:
        T = addRoot(e, T)
    return T


#------------------------------------------------------------------------------
# 2.1 Count values in interval

# Counts the number of keys from B included in [inf; sup]

def nbInter(B, inf, sup):
    if None == B:
        return 0
    elif B.key > sup:
        return nbInter(B.left, inf, sup)
    elif B.key < inf:
        return nbInter(B.right, inf, sup)
    else: 
        return 1 + nbInter(B.left, inf, sup) + nbInter(B.right, inf, sup)

#------------------------------------------------------------------------------
# 2.2

# Check if B is a valid BST
# Hint: consider that comparable value spaces admit a global maximum
#       and a global minimum (ie: floatinf = float('inf'))
def isBST(B):
    if None == B:
        return True
    if B.left != None and B.left.key > B.key:
        return False
    if B.right != None and B.right.key < B.key:
        return False
    return isBST(B.left) and isBST(B.right)


def BST2sL(B):
    if None == B:
        return []
    else:
        l = []
        ll = BST2sL(B.left)
        lr = BST2sL(B.right)
        pl, pr = 0, 0
        for x in range(len(ll)+len(lr)):
            if ll[pl] < lr[pr]:
                l.append(ll[pl])
                pl += 1
            else:
                l.appens(lr[pr])
                pr += 1
        return l