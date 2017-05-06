# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))
	
def hash_func(s):
	_multiplier = 263
	_prime = 1000000007
	ans = 0
	for c in reversed(s):
		ans = (ans * _multiplier + ord(c)) % _prime
	return ans
	
def hash_precompute(text, pattern):
	_multiplier = 263
	_prime = 1000000007
	text_length = len(text)
	pattern_length = len(pattern)
	H = [[] for _ in range(text_length - pattern_length + 1)]
	S = text[text_length - pattern_length : text_length]
	#print("S=", S)
	H[text_length - pattern_length] = hash_func(S)
	#print('H=', H)
	y = 1
	for i in range(pattern_length):
		y = (y * _multiplier) % _prime
	for i in range(text_length - pattern_length - 1, -1, -1):
		#print(i)
		H[i] = (_multiplier * H[i + 1] + ord(text[i]) - y * ord(text[i + pattern_length])) % _prime
	return H	
	
def rabin_karp(text, pattern):
	result = []
	pHash = hash_func(pattern)
	#print(pHash)
	H = hash_precompute(text, pattern)
	#print(H)
	for i in range(len(text) - len(pattern) + 1):
		#print(i)
		#tHash = hash_func(text[i:i + len(pattern)])
		if pHash != H[i]:
			continue
		if text[i:i + len(pattern)] == pattern:
			result.append(i)
	return result

def get_occurrences(pattern, text):
    #return [
    #    i 
    #    for i in range(len(text) - len(pattern) + 1) 
    #    if text[i:i + len(pattern)] == pattern
    #]
	return rabin_karp(text, pattern)

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

