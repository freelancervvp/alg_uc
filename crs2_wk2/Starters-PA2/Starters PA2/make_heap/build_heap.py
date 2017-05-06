# python3

def parent(i):
	return int((i - 1) / 2)
	
def leftChild(i):
	return 2 * i + 1

def rightChild(i):
	return 2 * i + 2

class Heap:
	def __init__(self):
		self.items = []

	#def isEmpty(self):
	#	return self.items == []

	def insert(self, item):
		#insert item
		global size
		size += 1
		self.items.append(item)
		# or self.items[size] = item
		self.siftUp(size)

	def siftUp(self, i):
		#siftup i
		global swaps
		while i > 0 and self.items[parent(i)] > self.items[i]:
			self.items[parent(i)], self.items[i] = self.items[i], self.items[parent(i)]
			swaps.append((parent(i), i))
			i = parent(i)
	
	def siftDown(self, i):
		#siftdown i
		global size
		minIndex = i
		l = leftChild(i)
		if l <= size and self.items[l] < self.items[minIndex]:
			minIndex = l
		r = rightChild(i)
		if r <= size and self.items[r] < self.items[minIndex]:
			minIndex = r
		if i != minIndex:
			self.items[minIndex], self.items[i] = self.items[i], self.items[minIndex]
			swaps.append((minIndex, i))
			self.siftDown(minIndex)

	def buildHeap(self, data):
		#build heap
		global size
		global swaps
		size = -1
		swaps = []
		for i in range(len(data)):
			self.insert(data[i])
		#print(self.items)
		return swaps
		
	def buildHeapFromArray(self, data):
		#build heap
		global size
		global swaps
		size = len(data) - 1
		swaps = []
		self.items = data
		for i in range(int(len(data) / 2), -1 ,-1):
			#print(i)
			self.siftDown(i)
		#print(self.items)
		return swaps
		
	#def size(self):
	#	 return len(self.items)

class HeapBuilder:
	def __init__(self):
		self._swaps = []
		self._data = []

	def ReadData(self):
		n = int(input())
		self._data = [int(s) for s in input().split()]
		assert n == len(self._data)

	def WriteResponse(self):
		print(len(self._swaps))
		for swap in self._swaps:
			print(swap[0], swap[1])

	def GenerateSwaps(self):
		# The following naive implementation just sorts 
		# the given sequence using selection sort algorithm
		# and saves the resulting sequence of swaps.
		# This turns the given array into a heap, 
		# but in the worst case gives a quadratic number of swaps.
		
		# TODO: replace by a more efficient implementation
		#for i in range(len(self._data)):
		#  for j in range(i + 1, len(self._data)):
		#    if self._data[i] > self._data[j]:
		#      self._swaps.append((i, j))
		#      self._data[i], self._data[j] = self._data[j], self._data[i]
		
		heap = Heap()
		# This is to build heap from scratch
		#self._swaps = heap.buildHeap(self._data)
		# This is to build heap from array
		self._swaps = heap.buildHeapFromArray(self._data)

	def Solve(self):
		self.ReadData()
		self.GenerateSwaps()
		self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()