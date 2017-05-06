#Uses python3
import sys
import math

def make_set(i):
	parent[i] = i
	rank[i] = 0
	
def find(i):
	while i != parent[i]:
		i = parent[i]
	return i
	
def union(i,j):
	i_id = find(i)
	j_id = find(j)
	if i_id == j_id:
		return
	if rank[i_id]>rank[j_id]:
		parent[j_id] = i_id
	else:
		parent[i_id] = j_id
		if rank[i_id] == rank[j_id]:
			rank[j_id] = rank[j_id] + 1
	
def minimum_distance(x, y):
	result = 0.
	#write your code here
	global parent 
	global rank
	
	parent = [None]*n
	rank = [None]*n
	e = [] #full set of edges
	e_id = [] #IDs for e
	
	#make_set(1)
	#print(parent, rank)
	for i in range(n):
		make_set(i)
	X = []
	
	for i in range(n):
		j = 0
		while j in range(n) and j != i:
			e.append(((x[i]-x[j])**2 + (y[i]-y[j])**2)**(1/2))
			e_id.append([i,j])
			j+=1
	#print('e=', e, 'e_id=', e_id)

	e_sorted = [s for (t,s) in sorted(zip(e,e_id))]
	#print('e_sorted=',e_sorted)
	
	for uv in e_sorted:
		#print('uv=', uv)
		#print('X=', X)
		if find(uv[0]) != find(uv[1]):
			X.append(uv)
			union(uv[0],uv[1])
			
	#print(X)
	
	for uv in X:
		result += ((x[uv[0]]-x[uv[1]])**2 + (y[uv[0]]-y[uv[1]])**2)**(1/2)
	#result = X
	
	return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
