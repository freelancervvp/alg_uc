#Uses python3

import sys

def dfs(adj, used, order, v):
	#write your code here
	explore(v, used)
	pass

def toposort(adj):
	used = [0]*n
	order = []
	#write your code here
	for v in range(n):
		if not used[v]:
			dfs(adj, used, order, v)
	#print(used)
	order = [x for (y,x) in sorted(zip(post,range(n)), reverse=True)]
	return order

def explore(v, used):
	#print("v=\n",v)
	visited[v] = 1
	previsit(v)
	# if len(adj[v]) == 0:
		# for i in range(n):
			# if v in adj[i]:
				# adj[i].remove(v)
				
	for w in adj[v]:
		if (not visited[w]) and (not used[w]):
			explore(w, used)
	
	#check if all descendants are used
	all_desc_used = 1
	for i in adj[v]:
		if used[i] == 0:
			all_desc_used = 0
			
	if (len(adj[v]) == 0) or (all_desc_used == 1):
		used[v] = 1
		
	postvisit(v)
	#print("used[v]=\n",used[v])

def previsit(v):
	global clk
	#print("clk=\n",clk)
	pre[v] = clk
	clk += 1

def postvisit(v):
	global clk
	#print("clk=\n",clk)
	post[v] = clk
	clk += 1

if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	n, m = data[0:2]
	data = data[2:]
	edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
	adj = [[] for _ in range(n)]
	for (a, b) in edges:
		adj[a - 1].append(b - 1)
	visited = [0]*n
	pre = [0]*n
	post = [0]*n
	clk = 1
	order = toposort(adj)
	for x in order:
		print(x + 1, end=' ')
	#print(pre)
	#print(post)

