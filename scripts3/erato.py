#-*-coding:utf8;-*-
#qpy:3
#qpy:console
#made by moular_b 

def buildList(n): 	
    if n < 2:
        e = "Fail"
        print(e)
        raise Exception(e)
    res = [1]
    for x in range(2, n):
        res.append(x) 
    return res 
   	
def suppr(l, pos):
    ll, i, lenL = [], 0, len(l)
    while i < lenL: 	
        if i != pos: 			
            ll.append(l[i]) 		
        i += 1 	
    return ll 
    
def erato(n): 	
    if n < 2: 		
        e = "Fail" 		
        print(e) 		
        raise Exception(e) 	
    l = buildList(n + 1) 	
    lenL = n 	
    x = 1 	
    while x < lenL: 		
        i = x 		
        lX = l[x] 		
        #print(lX) 		
        while i < lenL: 			
            if l[i] % lX == 0 and l[i] != lX: 				
                l = suppr(l, i) 				
                lenL -= 1 			
            i += 1 		
        x += 1 	
    return l 
    
def main(): 	
    print("This was made by moular_b") 	
    n = int(input("n =? ")) 
    for x in range(2, n + 1):
        print(x, erato(x))

while True: 	
    main()