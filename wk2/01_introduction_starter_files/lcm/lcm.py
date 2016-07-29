# Uses python3
import sys
import numpy as np

def lcm(a, b):
    #write your code here
	gcd = gcd_fast(b, a % b)
	# print(gcd)
	gcd = b // gcd
	# print(gcd)
	gcd = a * gcd
	# print(gcd)
	return gcd

def gcd_fast(a, b):
	if b == 0:
		return a
	return gcd_fast(b, a % b)

if __name__ == '__main__':
	input = sys.stdin.read()
	a, b = map(int, input.split())
	# print(a, b)
	print(lcm(a, b))

