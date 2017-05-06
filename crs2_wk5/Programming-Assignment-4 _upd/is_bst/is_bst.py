#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def IsBinarySearchTree(tree1):
	# Implement correct algorithm here
	if tree1.n == 0 or tree1.inOrder_bool():
		return True
	else:
		return False

class TreeOrders:
	def read(self, nodes, tree):
		self.n = nodes
		self.key = [0 for i in range(self.n)]
		self.left = [0 for i in range(self.n)]
		self.right = [0 for i in range(self.n)]
		for i in range(self.n):
			[a, b, c] = tree[i]
			self.key[i] = a
			self.left[i] = b
			self.right[i] = c

	def inOrder(self):
		self.result = []
		self.inOrderTraversal(0)
		return self.result

	def inOrderTraversal(self, i):
		if i == -1:
			return
		self.inOrderTraversal(self.left[i])
		self.result.append(self.key[i])
		self.inOrderTraversal(self.right[i])
		
	def inOrder_bool(self):
		self.result = True
		self.list = []
		self.inOrderTraversal_bool(0)
		return self.result

	def inOrderTraversal_bool(self, i):
		if i == -1:
			return
		self.inOrderTraversal_bool(self.left[i])
		#print(" ".join(str(x) for x in self.list))
		if len(self.list) > 0 and self.key[i] <= self.list[len(self.list) - 1]:
			self.result = False
		self.list.append(self.key[i])
		self.inOrderTraversal_bool(self.right[i])

	def preOrder(self):
		self.result = []
		self.preOrderTraversal(0)			
		return self.result
	
	def preOrderTraversal(self, i):
		if i == -1:
			return
		self.result.append(self.key[i])
		self.preOrderTraversal(self.left[i])
		self.preOrderTraversal(self.right[i])

	def postOrder(self):
		self.result = []
		self.postOrderTraversal(0)			
		return self.result
		
	def postOrderTraversal(self, i):
		if i == -1:
			return
		self.postOrderTraversal(self.left[i])
		self.postOrderTraversal(self.right[i])
		self.result.append(self.key[i])

def main():
	nodes = int(sys.stdin.readline().strip())
	tree = []
	for i in range(nodes):
		tree.append(list(map(int, sys.stdin.readline().strip().split())))
	tree1 = TreeOrders()
	tree1.read(nodes, tree)
  
	#print(" ".join(str(x) for x in tree1.inOrder()))
  
	if IsBinarySearchTree(tree1):
		print("CORRECT")
	else:
		print("INCORRECT")

threading.Thread(target=main).start()
