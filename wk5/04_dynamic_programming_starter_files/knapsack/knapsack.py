# Uses python3
import sys
import numpy as np

def optimal_weight(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result

def optimal_weight_dyn_prog(W, w):
	value = np.zeros((W + 1, len(w) + 1))
	for i in range(1, len(w) + 1):
		for weight in range(1, W + 1):
			value[weight, i] = value[weight, i - 1]
			if w[i-1] <= weight:
				val = value[weight - w[i-1], i - 1] + w[i-1]
				if value[weight, i] < val:
					value[weight, i] = val
		#print(value)
	#print(value)
	return int(value[W, len(w)])
	
if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight_dyn_prog(W, w))
