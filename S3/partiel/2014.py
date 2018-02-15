#python3
#made by moular_b

import GraphMat, queue, Stack

#Graph

## Salut Tom, tu parles du partiel 2014? Ca ressemble au partiel de cette année.
## Je vais commenté le code en précisant la question que je suppose que c'est.

## FEEDBACK: Premier exo à revoir pour la détection de cycles. Second bien mais 
## commentaires à relire.

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

## Jusqu'ici tout va bien, ton parcours largeur est bon, 
## il faut que tu sois en mesure par contre de faire aussi 
## des parcours profondeurs.

#exo 4

## Pour verifier si on est un arbre il faut vérifier qu'on ne recontre
## d'arcs retour lors du parcours, cela se fait avec un parcours 
## profondeur pas avec un parcours largeur. Ici, tu ne fais que repérer 
## si tu n'as pas d'arcs supplémentaire vers le père. Tu trouveras un 
## algo qui fait le boulot plus bas en parcours profondeur.

def _isTree(G, x, marque):
  marque[x] = True
  f = Queue()
  f = enqueue((x, None), f)
  while not isEmpty(f):
    y, prec = dequeue(f)
    for i in range(G.adjList[y]):
      if not marque[G.adjList[y][i]]:
        marque[G.adjList[y][i]] = true
        f = enqueue((G.adjList[y][i], y), f)
      else:
	if G.adjList[y][i] != prec and prec != None
          return False

## Tu n'as pas besoin de rappeler ta fonction d'appel car un arbre est connexe 
## si jamais t'as besoin de faire un nouvel appel tu sais déjà que tu ne 
## peux pas être un arbre.
def isTree(G):
	res = []
	q = Queue()
	for x in G.adj:
		q = enqueue(x, q)
	while not isEmpty(q):
		tmp = dequeue(q)
		if tmp in res:
			return False
		else:
			for x in tmp.adj:
				res.append(x)
				q = enqueue(x, q)
	return True
  marque = [False] * G.order
  for x in range(G.order):
    if not marque[x]:
      _isTree(G, x, marque)
  return True

def __isTreeDfs(G, x, fathers, size):
    for v in G.adjLists[x]:
      if not fathers[v]:
          fathers[v] = x
          return __isTreeDfs(G, v, fathers, size + 1) # size compte le nombre de sommets que je rencontre
      else:
          if v != fathers[x]: 
      	# Je teste si par hasard v (qui est deja visite) ne serait pas le père de x, 
      	# au cas ou je serais en train de remonter mon parcours. 		
                    return(False, size)
    return True, size

def isTreeDfs(G):
  fathers = []*G.order
  size = 0
  
  tree, size = __isTreeDFS(G, 0, fathers)
  
  if not tree and size != G.order: # si jamais je n'ai pas parcouru tous les sommets (plus d'une comp connexe)
      return(False)
	return(True)
    
#exo 5
def _rec(G, x, marque, distance):
  distance += 1
  marque[x] = max(distance, marque[x]) # pas nécessaire tu ne rappelles sur x qu'une fois.
  f = Queue()
  f = enqueue(x, f)
  f = enqueue(None, f)
  toAdd = 1
  while not isEmpty(f):
    y = dequeue(f)
    if y = None:
      toAdd += 1
      if not isEmpty(f):
        f = enqueue(None, f)
    else:
      for i in range(G.adjList[y]):
        if marque[i] == -1:
          marque[i] = toAdd + distance
          f = enqueue(i, f)
        
def _diametre(G, x):
  #retourne un tuple, (le point le plus loin de x dans G, sa distance avec x)
  
  ## Le rappelle marche pour une forêt ici mais on te dit qu'on est sur un arbre. 
  ## Un seul appel à partir de 0 suffit pour ton appel. Là tu fais le calcul pour le 
  ## cas d'une forêt.

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
