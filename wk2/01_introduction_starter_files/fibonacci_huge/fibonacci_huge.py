# Uses python3
import sys
import numpy as np

def get_fibonaccihuge(n, m):
    # write your code here
	print (n % (m**2 - 1))
	return get_fibonacci_remainder(n % (m**2 - 1), m)
	
def get_fibonacci_remainder(n, m):
    # write your code here
	if (n <= 1):
		return n	
	a = np.zeros(n + 1, dtype = np.int)
	#a[0] = 0
	a[1] = 1
	for i in range(2, n + 1):
		a[i] = (a[i-1] + a[i-2]) % m
		# a[i] = a[i] % 10
	return a[n]

# def calc_fib_fast(n):
	# if (n <= 1):
		# return n	
	# a = np.zeros(n + 1, dtype = np.uint64)
	# #a[0] = 0
	# a[1] = 1
	# for i in range(2, n + 1):
		# a[i] = a[i-1] + a[i-2]
	# return a[n]

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonaccihuge(n, m))