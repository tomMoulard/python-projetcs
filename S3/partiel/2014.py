#python3
#made by moular_b
import GraphMat, queue, Stack


# exo4

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