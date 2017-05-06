#Uses python3

import sys


def negative_cycle(adj, cost):
    #write your code here
	dist = [1e4]*n
	prev = [None]*n
	contains_cycles = False
	#last_relaxed_node = None
	#x = None
	#for s in range(n):
		#dist[s] = 0
	for i in range(n):
		for u in range(n):
			for v in adj[u]:
				#print('u,v: ', u , v)
				if dist[v] > dist[u] + cost[u][adj[u].index(v)]:
					dist[v] = dist[u] + cost[u][adj[u].index(v)]
					prev[v] = u
					if i == n-1:
						contains_cycles = True
					#last_relaxed_node = v
	#for i in range(n):
	#	x = prev[last_relaxed_node]
	return 1 if contains_cycles else 0


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
    print(negative_cycle(adj, cost))
