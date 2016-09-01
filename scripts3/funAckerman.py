#made by moular_b
print("yolo")
a = 0
def acker(m,n):
    print("m =", m, "n =", n)
    
    if m == 0:
        return (n + 1)
    elif n == 0:
        return acker((m - 1), 1)
    else :
        return acker((m - 1), acker(m, (n-1)))

def sart():
    m = int(input("m = "))
    n = int(input("n = "))
    print(acker(m, n))
    #print("a =", a)

sart()
