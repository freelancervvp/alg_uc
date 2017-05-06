#Uses python3

import sys
import queue

def ReconstructPath(s,t,prev):
	path = []
	while t != s:
		path.append(t)
		t = prev[t]
	path.append(s)
	#print(path)
	return path[::-1]

def distance(adj, s, t):
    #write your code here
	dist = [-1]*n
	prev = [-1]*n
	#for u in range(n):
	#	dist[u] = -1
	dist[s] = 0
	q = queue.Queue()
	q.put(s)
	while q.qsize() != 0:
		u = q.get()
		for v in adj[u]:
			if dist[v] == -1:
				q.put(v)
				dist[v] = dist[u] + 1
				prev[v] = u
	#print(prev, s, t)
	return len(ReconstructPath(s,t,prev)) - 1 if prev[t] != -1 else -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
