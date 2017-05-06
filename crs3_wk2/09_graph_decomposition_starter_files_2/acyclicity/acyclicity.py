#Uses python3

import sys


def acyclic(adj):
	cycled = 0
	for v in range(n):
		for w in adj[v]:
			visited = [0]*n
			explore(v, visited)
			if visited[v] == 2:
				cycled = 1
	return cycled

def explore(v, visited):
	visited[v] = 1
	for w in adj[v]:
		if not visited[w]:
			#print(w)
			#print(visited)
			explore(w, visited)
		else:
			visited[w] += 1

if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	n, m = data[0:2]
	data = data[2:]
	edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
	adj = [[] for _ in range(n)]
	for (a, b) in edges:
		adj[a - 1].append(b - 1)
	print(acyclic(adj))
