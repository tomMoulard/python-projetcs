#python3
#made by moular_b
import GraphMat
import queue as Q


# exo4

def parc_lag(G, x):
  marque = [False] * G.order
  for x in range(G.order):
    if not marque[x]:
      largeur(x, G, marque)

def largeur(x, G, marque):
  marque[x] = True
  f = Q.Queue()
  f = Q.enqueue(x, f)
  while not isEmpty(f):
    y = Q.dequeue(f)
    #rencontre de chaques noeuds
    for i in range(G.adjlist[y]): # i = adj de y
      #arc y -> x
      if not marque[i]:
        marque[i] = True:
        f = Q.enqueue(i, f)

def _diametre(G, x, marque, goal):
  
