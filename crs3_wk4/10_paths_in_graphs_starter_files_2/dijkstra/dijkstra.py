#Uses python3

import sys
import queue
import numpy as np

def extract_min(h, dist, visited):
	min = 1e5
	min_idx = -1
	for i in range(len(h)):
		if (dist[i] < min) and (visited[i] == False):
			min = dist[i]
			min_idx = i
			#print(min)
	#print('min=',min)
	if min_idx != -1:
		u = h[min_idx]
		visited[min_idx] = True
	else:
		u = -1
	#print('dist=', dist)
	#print('visited=',visited)
	#print('u=',u)
	return u

def distance(adj, cost, s, t):
    #write your code here
	dist = [1e4]*n
	prev = [None]*n
	dist[s] = 0
	h = list(range(n))
	visited = [False]*n
	#print(prev)
	#i = 0
	while False in visited:
		#i += 1
		#if i == 15:
		#	break
		u = extract_min(h, dist, visited)
		#print(visited)
		#print('u=',u)
		if u == -1:
			break
		for v in adj[u]:
			#print('v=',v)
			#print(cost[u][adj[u].index(v)])
			if dist[v] > dist[u] + cost[u][adj[u].index(v)]:
				dist[v] = dist[u] + cost[u][adj[u].index(v)]
				prev[v] = u
			#print('dist=', dist)
			#print('prev=', prev)
	#print(visited)
	#print(cost[3][adj[3].index(0)])
	#print(dist)
	return dist[t] if dist[t] != 1e4 else -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
