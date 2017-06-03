#This is a test on how to use threads in python3
#made by tomMoulard

import threading

def thr(name):
    #This is the actual function used in threads
    global nbs
    for x in range(nbs):
       print(name, "->", x)


threads = []
n = int(input("How many threads ?\n"))
# n = 42000
nbs = int(input("How many loops ?\n"))
# nbs = 42000
try:
    for x in range(n):

        thread = threading.Thread(target=thr, args=(str(x), ))
        thread.daemon = False
        thread.start()

        threads.append(thread)
except:
    print("failed")
print(threads)