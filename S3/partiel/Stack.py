from collections import deque

class Stack:
    def __init__(self):
        self.elements = deque()

def push(e, s):
    s.elements.append(e)
    return s

def top(s):
    return s.elements[-1]
    
def pop(s):
    return s.elements.pop()

def isEmpty(s): # empty ?
    return len(s.elements) == 0