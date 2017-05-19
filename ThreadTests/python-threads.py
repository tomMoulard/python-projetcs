#This is a test on how to use threads in python3
#made by tomMoulard

import threading

def thr(name, nbs):
    #This is the actual function used in threads
    for x in range(nbs):
       print(name, "->", x)


threads = []
n = int(input("How many threads ?\n"))
# n = 42000
nbs = int(input("How many loops ?\n"))
# nbs = 42000

for x in range(n):

    thread = threading.Thread(target=thr, args=(str(x), nbs, ))
    thread.daemon = False
    thread.start()

    threads.append(thread)

print(threads)