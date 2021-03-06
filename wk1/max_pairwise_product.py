# Uses python3
import random
import numpy
import time
random.seed(16)
#n = int(input())
#a = [int(x) for x in input().split()]
#assert(len(a) == n)

def MaxPairwiseProductFast(n, a):
	result = 0
	max_index1 = -1
	for i in range(0, n):
		if max_index1 == -1 or a[i] > a[max_index1]:
			max_index1 = i
	max_index2 = -1		
	for i in range(0, n):
		if (i != max_index1) and (max_index2 == -1 or a[i] > a[max_index2]):
			max_index2 = i
	result = a[max_index1] * a[max_index2]	
	return result

def MaxPairwiseProduct(n, a):
	result = 0
	for i in range(0, n):
		for j in range(i+1, n):
			if a[i]*a[j] > result:
				result = a[i]*a[j]
	return result

while True:
	n = random.randint(2, 10000)
	print(n)
	a = []
	for i in range (0, n):
		a.append(random.randint(1, 100000))
		#print(a[i], ' ', end='')
	print()
	start1 = time.clock()
	res1 = MaxPairwiseProduct(n, a)
	time1 = time.clock() - start1
	start2 = time.clock()
	res2 = MaxPairwiseProductFast(n, a)
	time2 = time.clock() - start2
	print('Exec time: ', time1, ' ', time2)
	if res1 != res2:
		print('Wrong answer: ', res1, ' ', res2)
		break
	else:
		print(' OK')
