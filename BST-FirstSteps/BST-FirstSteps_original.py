# -*- coding: utf-8 -*-
"""
Created on Fri Apr 1 16:42:42 2016

@author: Nathalie & Ted for S2
"""

#------------------------------------------------------------------------------
# 0.0 Type

class BinTree:
    pass
    
def newBinTree(key, left, right):
    T = BinTree()
    T.key = key
    T.left = left
    T.right = right
    return T

#------------------------------------------------------------------------------
# 1.1 Search

## q1: minimum and maximum
## --

# Returns the minimum key of a non-empty BST
# Iterative version
def minBST(B):
    while "FIXME":
        B = "FIXME"
    return "FIXME"

# Returns the minimum key of a non-empty BST
# Recursive version
def minBST_rec(B):
    if "FIXME":
        return "FIXME"
    else:
        return "FIXME"
    
# Returns the maximum key of a non-empty BST
# Iterative version
def maxBST(B):
    "FIXME"
    
# Returns the maximum key of a non-empty BST
# Recursive version
def maxBST_rec(B):
    "FIXME"


## q2: search for x in B
## --
    
# Returns the node of BST B containing key x or None if not found
# Recursive version
def searchBST(x, B):
    if "FIXME":
        return "FIXME"
    else:
        if "FIXME":
            return "FIXME"
        else:
            return "FIXME"

# Returns the node of BST B containing key x or None if not found
# Iterative version
def searchBST_iter(x, B):
    while "FIXME":
        if "FIXME":
            B = "FIXME"
        else:
            B = "FIXME"
    return "FIXME"


#------------------------------------------------------------------------------
# 1.2 Insert

# Adds a key to a BST
def addBST(x, B):
    if B == None:
        B = "FIXME"
    else:
        if "FIXME":
            "FIXME"
        else:
            "FIXME"
    return "FIXME"

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
            if "FIXME":
                B.key = "FIXME" # Find a suitable replacement
                B.left = "FIXME" # Resume suppression
            else:
                if "FIXME":
                    "FIXME"
                else:
                    "FIXME"
        else:
            if "FIXME":
                "FIXME"
            else:
                "FIXME"
        return "FIXME"

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
        "FIXME"
        return (G, D)

# Add a new root to a BST. Use "cut" to split the old one.
def addRoot(x, B):
    R = "FIXME"
    R.key = "FIXME"
    (R.left, R.right) = "FIXME"
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
    return "FIXME"


#------------------------------------------------------------------------------
# 2.2

# Check if B is a valid BST
# Hint: consider that comparable value spaces admit a global maximum
#       and a global minimum (ie: floatinf = float('inf'))
def isBST(B):
    return "FIXME"


