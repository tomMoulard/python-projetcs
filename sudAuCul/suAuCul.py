#-*-coding:utf8;-*-
#qpy:3
#made by moular_b

def loadFile(fA):
    f = open(fA)
    line = f.readline()
    f.close()
    lines = []
    for x in line:
        lines.append(str2int(x.strip().split(" ")))
    return lines

def str2int(l):
    for i in range(len(l)):
        l[i] = int(l[i])
    return l

def printMat(m):
    lenMCol = len(m[0])
    s = "|{:2d}"
    for x in range(lenMcol*3):
        print("~", end="")
    print("")
    for x in range(len(m)):
        for y in range(lenMCol):
            if x%3==0:
                print("~~~~~")
            else:
                print(m[x][y], end=" ")

printMat(loadFile("test"))