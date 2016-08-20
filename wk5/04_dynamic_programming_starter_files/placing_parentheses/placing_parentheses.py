# Uses python3
import numpy as np

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False
		
def MinAndMax(i, j, M, m, ops):
	mini = 99999
	maxi = -99999
	for k in range(i, j):
		a = evalt(M[i,k], M[k+1, j], ops[k])
		b = evalt(M[i,k], m[k+1, j], ops[k])
		c = evalt(m[i,k], M[k+1, j], ops[k])
		d = evalt(m[i,k], m[k+1, j], ops[k])
		mini = min(mini, a, b, c, d)
		maxi = max(maxi, a, b, c, d)
		#print(mini, maxi)
	return((mini, maxi))

def get_maximum_value(dataset):
    #write your code here
	#print(dataset)
	digits = []
	ops = []
	for i in range(len(dataset)):
		if i % 2 == 0:
			digits.append(dataset[i])
		else:
			ops.append(dataset[i])
	#print(digits)
	#print(ops)
	M = np.zeros((len(digits),len(digits)))
	m = np.zeros((len(digits),len(digits)))
	for i in range(len(digits)):
		M[i,i] = digits[i]
		m[i,i] = digits[i]
	for s in range(1, len(digits)):
		for i in range(0, len(digits) - s):
			j = i + s
			m[i,j], M[i,j] = MinAndMax(i,j, M, m, ops)
	#print(m)
	#print(M)
	return int(M[0, len(digits) - 1])

if __name__ == "__main__":
    print(get_maximum_value(input()))
