# Uses python3
import sys
import numpy as np

def get_optimal_value(capacity, weights, values):
	value = 0.
	# write your code here
	n = len(weights)
	items = np.zeros(n)
	weights = np.array(weights)
	values = np.array(values)
	v2w = values / weights
	id_sort = np.argsort(v2w)[::-1]
	#print('id_sort: ', id_sort)
	for i in id_sort:
		if capacity == 0:
			return value, items
		vol = min(weights[i], capacity)
		value += vol * v2w[i]
		weights[i] -= vol
		items[i] += vol
		capacity -= vol
	return value, items


if __name__ == "__main__":
	data = list(map(int, sys.stdin.read().split()))
	n, capacity = data[0:2]
	values = data[2:(2 * n + 2):2]
	weights = data[3:(2 * n + 2):2]
	#print(type(values))
	opt_value, opt_items = get_optimal_value(capacity, weights, values)
	#opt_value = round(opt_value, 4)
	print("{:.10f}".format(opt_value))
	#print(opt_items)
