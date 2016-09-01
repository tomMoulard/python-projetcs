#-*-coding:utf8;-*-
#qpy:3
#qpy:console
#made by moular_b

import timeit, functools

#b32 = ['0', '2', '3', '4', '5', '6', '7', '1', '8', '9', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
b32 = ['0','1','2','3','4','5','6','7','8','9','b','c','d','e','f','g', 'h','j','k','m','n','p','q','r','s','t','u','v','w','x','y','z']
def geoHashToIntList(s):
    res = []
    for x in s:
        for i in range(len(b32)):
            if b32[i] == x:
                res.append(i)
    return res

def intToBList(n):
    res = []
    for x in range(5):
        res.append(n % 2)
        n = n // 2
    return res

def reverseImp(l):
    lenL = len(l)
    for x in range(lenL//2):
        tmp = l[x]
        l[x] = l[lenL - x -1]
        l[lenL-x-1] = tmp

def intListToBList(i):
    res = []
    for x in i:
        l = intToBList(x)
        reverseImp(l)
        for w in l:
            res.append(w)
    return res

#print(geoHashToIntList("mvp"))
#print(intListToBList(geoHashToIntList("mvp")))

def separate(l):
    lat, longi, pos, ll = [], [], 0, len(l)
    while pos < ll:
        if pos % 2 == 0:
            longi.append(l[pos])
        else:
            lat.append(l[pos])
        pos += 1
    return (longi, lat)

def bListToReel(l, bSup, bInf, res):
    #bSup, bInf, res = -180, 180, 0
    #print(l, "bSup", bSup, "bInf", bInf, "res", res)
    for x in range(len(l)):
        if l[x] == 1:
            bInf = res
            res = (bSup + res) / 2
        elif l[x] == 0:
            bSup = res
            res = (bInf + res) / 2
        #print(l, "bSup", bSup, "bInf", bInf, "res", res)
    return res

def main():
    h = input("Hash = ")
    longi, lat = separate(intListToBList(geoHashToIntList(h)))
    print("Longitude :", longi, "\nLatitude :", lat, "\nReal longitude :", bListToReel(longi, 180, -180, 0), "\nReal Latitude :", bListToReel(lat, 90, -90, 0))
    print(timeit.timeit(functools.partial(bListToReel,longi, 180, -180, 0), number=1000))
#while True:
   #main()

def test(x, prec):
    for i in range(x*32):
        res = prec + b32[i%32]
        #use "res" here <3
        print(res)
        test((x-1), res)

#test(4, "")

tmp = ""

def unTrucMarrant(x, prec):
    for i in range(x*32):
        res = prec + b32[i%32]
        longi, lat = separate(intListToBList(geoHashToIntList(res)))
        #tmp = tmp + "\ngeoHash : " + str(res) + "\nlongi "+str(bListToReel(longi,180,-180,0))+" lat "+str(bListToReel(lat,90,-90,0))
        
        print("geoHash :", res)
        print("longi", bListToReel(longi, 180, -180, 0), "lat", bListToReel(lat, 90, -90, 0))
        unTrucMarrant((x-1), res)
unTrucMarrant(5, "")