#-*-coding:utf8;-*-
# made by moular_d

def parf(n):
    s, act, div = 0, 1, n // 2
    while act <= div:
        if n % act == 0:
            s += act
            #print(act)
        act += 1
    print (n, s==n)
    return s == n

def start(n):
    if n < 1:
        return false
    a = 0
    while n > a:
        if (parf(a)):
            print(a, "True")
        #print(a)
        a += 1
        
def yolo():
    n = int(input("n = "))
    start(n)
    
yolo()