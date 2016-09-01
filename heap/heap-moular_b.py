#-*-coding:utf8;-*-

#qpy:3

#qpy:console

#made by Tom Moulard B1


#binTree
class BinTree():

    pass



def nBT(key, left, right):

    B = BinTree()

    B.key = key

    B.left = left

    B.right = right

    return B

    

def printBinTree(B, prec=""):

    if None != B:

        print(prec, "-", B.key)

        printBinTree(B.left, prec + " |")

        printBinTree(B.right, prec + "  ")

        

def etcBinTree():

    return nBT(1,
 
    	        nBT(2,

    	        	    nBT(4, None, None),

    	        	    nBT(5, None, None)),

    	        	nBT(3,

    	        		    nBT(6, None, None),

    	        		    None))


#printBinTree(etcBinTree())



#Exercice 1:

#question 1:


# [None,(,'A'),(,'C'),(,'B'),(,'I'),(,'E'),(,'D'),(,'F'),(,'L'),(,'J'),(,'G'),(,'M'),(,'K'),(,'H')]


#question 2

#A


#root is on index 1


#B


#if node is on index i, his sons are on index 2 * i and 2 * i + 1


#C


#if node is on index i, and his father exist, he is on index i // 2


#D


#if node is on index i, and this node is a leaf, then 2 * i > len(V)



def newHeap():

    return [None]

def isEmpty(H):

    return len(H) == 1



#exercice 2

#question 1

#A


#to add an element in the tree you need to use an add2root technic

#B

nH= nBT 
