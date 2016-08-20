# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

def calc_all_opt(C, i):
	if i*2 <= n or i*3 <= n or i+1 <= n:
		C[i*2] = min(C[i] + 1, C[i*2])
		C[i*3] = min(C[i] + 1, C[i*3])
		C[i+1] = min(C[i] + 1, C[i+1])
		calc_all_opt(C, i*2)
		calc_all_opt(C, i*3)
		calc_all_opt(C, i+1)
	return C	
	
def dyn_prog_sequence(n):
	#sequence = []
	C = {}
	#for i in range(n*3):
	#	C[i] = 999999
	i = 1
	C[i] = 0
	#print(C)
	#C = calc_all_opt(C, i)
	for i in range(2, n + 1):
		if i % 2 == 0 and i % 3 == 0:
			C[i] = min(C[i/2], C[i/3], C[i-1]) + 1
		if i % 2 == 0 and not i % 3 == 0:
			C[i] = min(C[i/2], C[i-1]) + 1
		if not i % 2 == 0 and i % 3 == 0:
			C[i] = min(C[i/3], C[i-1]) + 1
		if not i % 2 == 0 and not i % 3 == 0:	
			C[i] = C[i-1] + 1
	#print(C)
	sequence = [None] * (C[n] + 1)
	j = C[n]
	sequence[j] = n
	sequence[0] = 1
	while j > 1:
		if sequence[j] % 2 == 0 and C[sequence[j] / 2] == C[sequence[j]] - 1:
			sequence[j - 1] = round(sequence[j] / 2)
		if sequence[j] % 3 == 0 and C[sequence[j] / 3] == C[sequence[j]] - 1:
			sequence[j - 1] = round(sequence[j] / 3)
		if C[sequence[j] - 1] == C[sequence[j]] - 1:
			sequence[j - 1] = sequence[j] - 1
		j -= 1
	return sequence

input = sys.stdin.read()
n = int(input)
sequence = list(dyn_prog_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
