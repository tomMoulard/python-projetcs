#-*-coding:utf8;-*-
#qpy:3
#qpy:console
#made by moular_b
#just another recursive and iterative function :3

bb = [0,1]
#bb = ['0','1','2','3','4','5','6','7','8','9','b','c','d','e','f','g', 'h','j','k','m','n','p','q','r','s','t','u','v','w','x','y','z']
bb = [0,1,2,3,4,5,6,7,8,9]
#bb = ['a','b','c']
#bb = ["yolo "]
def test2(x, prec, bBL):
    """
    use like :
        x    : poids (ex: 3 will make 000 to zzz)
        prec : str du debut
        bBL  : len(bb) -> fast :3
    """                        
    for n in range(bBL):
        if x == 1:
            #print("->", prec)
            print(chr(int(prec)), end=' ')
            #can use prec here
            #no incidence in the futur 4 the function
            return
        else:
            test2((x-1), (prec+str(bb[n])), bBL)

def main():
    n = int(input("poids = "))
    test2(n+1, "", len(bb),)

while True:
    main ()