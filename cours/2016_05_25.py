#made by moular_b

class AVLTree():
	pass

def newAVL(key, left, right, bal):
	A       = AVLTree()
	A.key   = key
	A.left  = left
	A.right = right
	A.bal   = bal
	return A

class Stack:
	pass

def newStack():
	return []

def isEmptyStack(s):
	return s == []

def pushStack(e, s):
	s.append(e)
	return s

def popStack(s):
	return s.pop() 

def printLeftSideRec(B, cpt=1):
	if None == B:
		return 0
	elif B.left == None:
		print(B.key)
		return cpt
	else:
		print(B.key)
		return printLeftSide(B.left, cpt+1)

def printLeftSideIte(B):
	if None == B:
		return 0
	cpt = 0
	while B != None:	
		cpt += 1
		print(B.key)
		B = B.left
	return cpt

def print_AVL(A, prec=""):
	print(prec + str(A.key) + " : (" + str(A.bal) + ")\n")
	if None != A.left:
		print_AVL(A.left, prec + " |")
	if None != A.right:
		print_AVL(A.right, prec + "  ")

def insertTMP(e, A):
	if None == A:
		return newAVL(e, None, None, 0), 1
	else:
		if e == A.key:
			return A, 0
		elif e < A.key:
			A.left, deltaH = insertTMP(e, A.left)
			if delatH != 0:
				deltaH -= 1
				if A.bal > 1:
					if A.left.bal < -1:
						A = rotLR(A)
					else:
						A = rotR(A)
				return A, A.bal
			else:
				return A, 0
		else:
			A.right, deltaH = insertTMP(e, A.right)
			if deltaH != 0:
				deltaH += 1
				if A.bal < -1:
					if A.right.bal > 1:
						A = rotRL(A)
					else:
						A = rotL(A)
				return A, A.bal
			else:
				return A, 0

def  parcProfMGIte(b):
	if None == B:
		return
	s = newStack()
	s = pushStack(B, s)

	while not isEmptyStack(s):
		B = popStack(s)
		print(B.key)
		if B.right != None:
			s = pushStack(B.right, s)
		if B.left != None:
			s = pushStack(B.left, s)
		

def  parcProfMGIte(b):
	if None == B:
		return
	s = newStack()
	s = pushStack(B, s)

	while not isEmptyStack(s):
		B = popStack(s)

		if B.right != None:
			s = pushStack(B.right, s)
		print(B.key)
		if B.left != None:
			s = pushStack(B.left, s)
		
