# python3
#from collections import deque
#import queue

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
	_multiplier = 263
	_prime = 1000000007

	def __init__(self, bucket_count):
		self.bucket_count = bucket_count
		# store all strings in one list
		#self.elems = [deque()] * self.bucket_count
		self.elems = [[] for _ in range(self.bucket_count)]
		#print(self.elems[1])
		#self.elems[1] = deque(['wo', 'we'])
		#print(self.elems[1].popleft())
		#print(self.elems[1])
		
	def _hash_func(self, s):
		ans = 0
		for c in reversed(s):
			ans = (ans * self._multiplier + ord(c)) % self._prime
		return ans % self.bucket_count

	def write_search_result(self, was_found):
		print('yes' if was_found else 'no')

	def write_chain(self, chain):
		print(' '.join(chain))

	def read_query(self):
		return Query(input().split())

	def process_query(self, query):
		if query.type == "check":
			# use reverse order, because we append strings to the end
			#self.write_chain(cur for cur in reversed(self.elems)
			#			if self._hash_func(cur) == query.ind)
			#print(self.elems)
			self.write_chain(reversed(self.elems[query.ind]))
		else:
			hash = self._hash_func(query.s)
			#print(hash)
			try:
				ind = self.elems[hash].index(query.s)
			except ValueError:
				ind = -1
			if query.type == 'find':
				self.write_search_result(ind != -1)
			elif query.type == 'add':
				if ind == -1:
					#print(self.elems[hash])
					self.elems[hash].append(query.s)
			else:
				if ind != -1:
					self.elems[hash].remove(query.s)

	def process_queries(self):
		n = int(input())
		for i in range(n):
			self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
