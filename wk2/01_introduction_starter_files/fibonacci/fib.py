# Uses python3
import numpy as np
import random
import time

def calc_fib(n):
    if (n <= 1):
        return n
    return calc_fib(n - 1) + calc_fib(n - 2)
	
def calc_fib_fast(n):
	if (n <= 1):
		return n	
	a = np.zeros(n + 1, dtype = np.int)
	#a[0] = 0
	a[1] = 1
	for i in range(2, n + 1):
		a[i] = a[i-1] + a[i-2]
	return a[n]
	
n = int(input())
print(calc_fib_fast(n))
	
# while True:
	# n = random.randint(0, 25)
	# print(n)
	# start1 = time.clock()
	# res1 = calc_fib(n)
	# time1 = time.clock() - start1
	# start2 = time.clock()
	# res2 = calc_fib_fast(n)
	# time2 = time.clock() - start2
	# print('Exec time: ', time1, ' ', time2)
	# if res1 != res2:
		# print('Wrong answer: ', res1, ' ', res2)
		# break
	# else:
		# print('Right answer: ', res1, ' ', res2)
		# print(' OK')


