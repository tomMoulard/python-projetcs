# -*- coding: utf-8 -*-
"""
Created on Thu Fev 15 2018

@author: tomMoulard

My anwsers to the question of the YT video:
https://www.youtube.com/watch?v=XKu_SEDAykw
"""

"""
The question:
There is an array of numbers and we must find the pair that sums into the
argument give.
Should return True or false depending if the pair as been found.
"""

def tests(arraysOfFunctions):
    import timeit
    for funct in arraysOfFunctions:
        print("For the function:", str(funct.__name__))
        print("[1,2,3,9] and 8 -> {} (Supposed to be False)".\
                format(str(funct([1,2,3,9], 8))))
        print(timeit.timeit(funct.__name__ + "([1,2,3,9], 8)", setup="from __main__ import " + funct.__name__))
        print("[1,2,4,4] and 8 -> {} (Supposed to be True)".\
                format(str(funct([1,2,4,4], 8))))
        print(timeit.timeit(funct.__name__ + "([1,2,4,4], 8)", setup="from __main__ import " + funct.__name__))

def simplestOne(array, sum):
    for x in range(len(array)):
        for y in array[x+1:]:
            if array[x] + y == sum:
                return True
    return False

def notSoSimpleOne(array, sum):
    comp = {}
    for x in range(len(array)):
        if sum - array[x] in comp:
            return True
        else:
            comp[sum - array[x]] = x
    return False

if __name__ == "__main__":
    arraysOfFunctions = [
        simplestOne,
        notSoSimpleOne,
    ]
    tests(arraysOfFunctions)