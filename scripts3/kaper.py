#-*-coding:utf8;-*-
#qpy:3
#qpy:console
#made by moular_b

def bubbleSortmax(alist):
    #res = ""
    for x in range(len(alist)-1,0,-1):
        for i in range(x):
            if alist[i]>alist[i+1]:
                #print("Swapp", alist[i], alist[i+1])
                #res = res + "\nSwapp "+str(alist[i])+" et "+str(alist[i+1])
                temp = alist[i];
                alist[i] = alist[i+1];
                alist[i+1] = temp;
    print(alist)
                
def bubbleSortmin(alist):
    #res = ""
    for x in range(len(alist)-1,0,-1):
        for i in range(x):
            if alist[i]<alist[i+1]:
                #print("Swapp", alist[i], alist[i+1])
                #res = res + "\nSwapp "+str(alist[i])+" et "+str(alist[i+1])
                temp = alist[i];
                alist[i] = alist[i+1];
                alist[i+1] = temp;

def intToList(n):
    strN = str(n)
    res = []
    for x in strN:
        res.append(x)
    return res
    
def listToInt(l):
    res = 0
    ll = len(l)
    pos = 0
    while pos < ll:
        #print("res ", res,"pos ", pos)
        res += int(l[pos]) * 10 ** (pos)
        pos += 1
    return res

def sortMax (n): 
    l = intToList(n)
    bubbleSortmax(l)
    return listToInt(l)

def sortMin (n): #FixMePlz
    l = intToList(n)
    bubbleSortmin(l)
    return listToInt(l)

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
	while notTwoDiffNum and y < lenL :
		if l[y] != l[y-1]:
			notTwoDiffNum = False
		y += 1
	return notTwoDiffNum

res = []

def kap (n):
	#print(n, end='->')
	for x in res:
		if x == n:
			#print(x)
			return x
	res.append(n)
	if test(n):
		print("Bad Input,", n ,"is not a valid number :(")
		return n
		#raise Exception("Bad Input,", n ," is not a valid number :(")
	p = len(str(n))
	a = sortMax(n)
	b = sortMin(n) #b = reverse(a)
	#print(n, "Max :", a, "Min", b)
	aMb = a - b
	#print("a", a, "b", b, "p", p, "aMb", aMb)
	if aMb < 10**(p-1):
		aMb = a * 10 - b
	#print(aMb)
	return kap(aMb) 

def yolo():
    n = int(input("kap de : "))
    print("kap de", n, "=",kap(n))

def yolo2():
    n = int(input("kap de 1 à : "))
    for x in range(12, n + 1):
        print("kap(",x,") = ", kap(x))
while True:
   yolo2()