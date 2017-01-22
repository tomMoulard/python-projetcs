from collections import deque

class Queue:
    def __init__(self):
        self.elements = deque()

def enqueue(e, q):
    q.elements.append(e)
    return q

def dequeue(q):
    return q.elements.popleft()

def isEmpty(q): # empty ?
    return len(q.elements) == 0