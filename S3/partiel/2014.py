#python3
#made by moular_b
#Graph
class Graph:
	def __init__(self, order, directed = False):
		self.order = order
		self.directed = directed
		self.adjLists = []
		for i in range(order):
		    self.adjLists.append([])
        
        
#Queue
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


def parc_lag(G, x):
  marque = [False] * G.order
  for x in range(G.order):
    if not marque[x]:
      largeur(x, G, marque)

def largeur(x, G, marque):
  marque[x] = True
  f = Queue()
  f = enqueue(x, f)
  while not isEmpty(f):
    y = dequeue(f)
    #rencontre de chaques noeuds
    for i in range(G.adjlist[y]): # i = adj de y
      #arc y -> x
      if not marque[i]:
        marque[i] = True:
        f = Q.enqueue(i, f)

#exo 5
def _rec(G, x, marque, distance):
  distance ++
  marque[x] = max(distance, marque[x])
  f = Queue()
  f = enqueue(x, f)
  f = enqueue(None, f)
  toAdd = 1
  while not isEmpty(f):
    y = dequeue(f)
    if y = None:
      toAdd ++
      if not isEmpty(f):
        f = enqueue(None, f)
    else:
      for i in range(G.adjList[y]):
        if marque[i] == -1:
          marque[i] = toAdd + distance
          f = enqueue(i, f)
        
def _diametre(G, x):
  #retourne un tuple, (le point le plus loin de x dans G, sa distance avec x)
  marque = [-1] * G.order
  for y in range(G.order):
    if marque[y] == -1:
      _rec(G, y, marque, 0)
  res = (0, marque[0])
  for i in range(G.order):
    if marque[i] > res[1]:
      res = (i, marque[i])
  return res

def diametre(G):
  S0 = G[0]
  S1 = _diametre(G, S0)[0]
  return _diametre(G, S1)[1] #return S2
  
