# python3

import sys, threading, random
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
	def read(self):
		self.n = int(sys.stdin.readline())
		self.parent = list(map(int, sys.stdin.readline().split()))
		#self.n = 100000
		#self.parent = []
		#self.parent.append(-1)
		#for i in range(self.n - 1):
		#	self.parent.append(random.randint(0, 1000))
		#print(self.parent)
		self._max_depth = -1
		self.depths = [None] * self.n

	def max_depth(self):
		if self._max_depth == -1:
			for idx, parent in enumerate(self.parent):
				depth = self.get_depth(idx)
				if self._max_depth < depth:
					self._max_depth = depth
		return self._max_depth

	def get_depth(self, idx):
		depth = self.depths[idx]
		if depth is not None:
			return depth
		parent = self.parent[idx]
		if parent == -1:
			depth = 1
		else:
			depth = self.get_depth(parent) + 1
		self.depths[idx] = depth
		return depth
			
	#def compute_height(self):
			# Replace this code with a faster implementation
			# maxHeight = 0
			# for vertex in range(self.n):
					# height = 0
					# i = vertex
					# while i != -1:
							# height += 1
							# i = self.parent[i]
					# maxHeight = max(maxHeight, height);
			# return maxHeight;

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.max_depth())

threading.Thread(target=main).start()
