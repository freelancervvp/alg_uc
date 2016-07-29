# Uses python3
import sys
import numpy

def get_change(m):
	#write your code here
	#print(next(coins))
	coin = next(coins)
	#print(m)
	res = m // coin
	#print(res)
	change.append(res)
	m = m % coin
	if m == 0:
		return None
	get_change(m)
	return None
	
if __name__ == '__main__':
	m = int(sys.stdin.read())
	coins = iter([10, 5, 1])
	change = list()
	get_change(m)
	#print(change)
	print(sum(change))
