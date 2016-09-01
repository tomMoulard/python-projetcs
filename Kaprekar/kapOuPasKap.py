def sortMax (n): #FixMePlz
	return n

def sortMin (n): #FixMePlz
	return n

def test (n):
	res = True	
	l = []
	for x in str(n):
		l.append(x)
	old = l[0]
	#print("list",l)
	notTwoDiffNum = True
	lenL = len(l)
	y = 1
	while twoDiffNum and y < lenL :
		if l[y] != l[y - 1]
			notTwoDiffNum = False
		y += 1
	return notTwoDiffNum

res = []

def kap (n):
	for x in res:
		if x == n:
			print(x)
			return x
	res.append(n)
	if test(n):
		raise Exception("Bad Input,", n ," is not a valid number :(")
	p = len(str(n))
	a = sortMax(n)
	b = sortMin(n)
	aMb = a - b
	#print("a", a, "b", b, "p", p, "aMb", aMb)
	if aMb < 10**(p-1):
		aMb = a * 10 - b
	print(aMb)
	return kap(aMb) 

kap(42)