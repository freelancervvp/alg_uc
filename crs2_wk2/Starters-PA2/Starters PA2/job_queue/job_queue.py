# python3

def parent(i):
	return int((i - 1) / 2)
	
def leftChild(i):
	return 2 * i + 1

def rightChild(i):
	return 2 * i + 2

class Heap:
	def __init__(self):
		self.id = []
		self.next_free_time = []

	#def isEmpty(self):
	#	return self.items == []

	#def insert(self, item):
	#	#insert item
	#	global size
	#	size += 1
	#	self.items.append(item)
	#	# or self.items[size] = item
	#	self.siftUp(size)

	#def siftUp(self, i):
	#	#siftup i
	#	global swaps
	#	while i > 0 and self.items[parent(i)] > self.items[i]:
	#		self.items[parent(i)], self.items[i] = self.items[i], self.items[parent(i)]
	#		swaps.append((parent(i), i))
	#		i = parent(i)
	
	def siftDown(self, i):
		#siftdown i
		global size
		minIndex = i
		l = leftChild(i)
		if l <= size and (self.next_free_time[l] < self.next_free_time[minIndex] or (self.next_free_time[l] == self.next_free_time[minIndex] and self.id[l] < self.id[minIndex])):
			minIndex = l
		r = rightChild(i)
		if r <= size and (self.next_free_time[r] < self.next_free_time[minIndex] or (self.next_free_time[r] == self.next_free_time[minIndex] and self.id[r] < self.id[minIndex])):
			minIndex = r
		if i != minIndex:
			self.next_free_time[minIndex], self.next_free_time[i] = self.next_free_time[i], self.next_free_time[minIndex]
			self.id[minIndex], self.id[i] = self.id[i], self.id[minIndex]
			#swaps.append((minIndex, i))
			self.siftDown(minIndex)

	#def buildHeap(self, data):
	#	#build heap
	#	global size
	#	global swaps
	#	size = -1
	#	swaps = []
	#	for i in range(len(data)):
	#		self.insert(data[i])
	#	#print(self.items)
	#	return swaps
	
	def changePriority(self, i, job_time):
		self.next_free_time[i] = self.next_free_time[i] + job_time
		self.siftDown(i)
		
	def buildHeapFromArray(self, data):
		#build heap
		global size
		global swaps
		size = len(data) - 1
		#swaps = []
		self.id = data
		self.next_free_time = [0] * len(data)
		#for i in range(int(len(data) / 2), -1 ,-1):
		#	#print(i)
		#	self.siftDown(i)
		#print(self.items)
		#return swaps

class JobQueue:
	def read_data(self):
		self.num_workers, m = map(int, input().split())
		self.jobs = list(map(int, input().split()))
		assert m == len(self.jobs)

	def write_response(self):
		for i in range(len(self.jobs)):
			print(self.assigned_workers[i], self.start_times[i]) 
		  
	def assign_jobs(self):
		# TODO: replace this code with a faster algorithm.
		self.assigned_workers = [None] * len(self.jobs)
		self.start_times = [None] * len(self.jobs)
		next_free_time = [0] * self.num_workers
		#for i in range(len(self.jobs)):
		#  next_worker = 0
		#  for j in range(self.num_workers):
		#    if next_free_time[j] < next_free_time[next_worker]:
		#      next_worker = j
		#  self.assigned_workers[i] = next_worker
		#  self.start_times[i] = next_free_time[next_worker]
		#  next_free_time[next_worker] += self.jobs[i]
		workers = Heap()
		workers.buildHeapFromArray(list(range(self.num_workers)))
		for i in range(len(self.jobs)):
			next_worker = workers.id[0]
			self.assigned_workers[i] = next_worker
			self.start_times[i] = workers.next_free_time[0]
			workers.changePriority(0, self.jobs[i])
			#print('workers.id = ', workers.id)
			#print('workers.next_free_time = ', workers.next_free_time)

	def solve(self):
		self.read_data()
		self.assign_jobs()
		self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

