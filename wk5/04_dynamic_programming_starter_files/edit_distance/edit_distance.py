# Uses python3
import numpy as np

def edit_distance(s, t):
    #write your code here
	D = np.zeros((len(s) + 1, len(t) + 1))
	for i in range(len(s) + 1):
		D[i, 0] = i
	for j in range(len(t) + 1):
		D[0, j] = j
	for j in range(1, len(t) + 1):
		for i in range(1, len(s) + 1):
			insertion = D[i, j-1] + 1
			deletion = D[i-1, j] + 1
			match = D[i-1, j-1]
			mismatch = D[i-1, j-1] + 1
			if s[i-1] == t[j-1]:
				D[i, j] = min(insertion, deletion, match)
			else:
				D[i, j] = min(insertion, deletion, mismatch)
	#print(D)
	return int(D[len(s), len(t)])

if __name__ == "__main__":
    print(edit_distance(input(), input()))
