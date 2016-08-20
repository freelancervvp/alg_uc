# Uses python3
import sys

def get_majority_element(a, left, right):
	if left == right:
		return -1
	#if left + 1 == right:
	#	return a[left]
	#write your code here
	mid = round(left + (right - left) / 2)
	#print(left, mid, right)
	#if x == a[mid]:
	#	return mid
	if get_majority_element(a, left, mid) != -1:
		return 1
	else:
		return get_majority_element(a, mid + 1, right)
	return -1

def find_majority(k, left, right):
	myMap = {}
	maximum = ( '', 0 ) # (occurring element, occurrences)
	for n in k:
		if n in myMap: 
			myMap[n] += 1
		else: myMap[n] = 1
		# Keep track of maximum on the go
		if myMap[n] > maximum[1]: 
			maximum = (n,myMap[n])
	if maximum[1] > len(k) / 2:
		return maximum[0]
	else:
		return -1
	
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if find_majority(a, 0, n) != -1:
        print(1)
    else:
        print(0)
