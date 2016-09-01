#-*-coding:utf8;-*-
#qpy:3
#qpy:console
#made by moular_b

def modulo(a, n): #trouve x tq a congru à x[n]
    x = a
    while x >= n:
        #print(x, n)
        x -= n
    return x
    
def isDiv(a, b): #verifie si a|b, retourne i tq ia = b
    i = -b
    res = false
    while i <= b and not res:
        if i * a == b:
            res = true
        i += 1
    return (res, i)
    
def isDiv2(a, b): #reste div eucl a/b==0
    




def yolo():
    a = int(input("a = "))
    n = int(input("n = "))
    print(a, "congru à", modulo(a, n), "[", n, "]")

yolo()