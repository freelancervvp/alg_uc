# Uses python3
import sys
import numpy as np

def get_fibonacci_last_digit(n):
    # write your code here
	if (n <= 1):
		return n	
	a = np.zeros(n + 1, dtype = np.int)
	#a[0] = 0
	a[1] = 1
	for i in range(2, n + 1):
		a[i] = (a[i-1] + a[i-2]) % 10
		# a[i] = a[i] % 10
	return a[n]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))
