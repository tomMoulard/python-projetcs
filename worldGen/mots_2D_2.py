#a -*- coding: utf-8 -*-

import numpy as np
from numpy.random import choice, seed
import sys
import time
import codecs

if len(sys.argv) < 2:
    seed(int(time.time()))
else:
    seed(int(sys.argv[1]))
CODEC = "ISO-8859-1"
filepath = "__wordsFR.txt"
outfile = "output.txt"
probafile = "count2D_EN.bin"

dico = []
with codecs.open(filepath, "r", "ISO-8859-1") as lines:
    for l in  lines:
        dico.append(l[:-1])

count          = np.fromfile(probafile,dtype="int32").reshape(256,256,256)
s              = count.sum(axis=2)
st             = np.tile(s.T,(256,1,1)).T
p              = count.astype('float')/st
p[np.isnan(p)] = 0
f              = codecs.open(outfile,"w",CODEC)
K              = 100
col            = 0
for TGT in range(3,13):
#K = 100
#for TGT in range(4,11):
    total = 0
    while total<6:
        i=0
        j=0
        res = u''
        while not j==10:
            k   = choice(range(256),1,p=p[i,j,:])[0]
            res = res + chr(k)
            i   = j
            j   = k
        if len(res) == 1+TGT:
            x=res[:-1]
            if res[:-1] in dico:
                x = res[:-1]+"*"
            total += 1
            if col == 0:
                col = 1
            else:
                col = 0
            print(x)
            f.write(x+"\n")
f.close()