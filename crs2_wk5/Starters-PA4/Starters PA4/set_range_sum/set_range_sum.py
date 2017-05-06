# python3

from sys import stdin

# Splay tree implementation

# Vertex of a splay tree
class Vertex:
  def __init__(self, key, sum, left, right, parent):
    (self.key, self.sum, self.left, self.right, self.parent) = (key, sum, left, right, parent)

def update(v):
  if v == None:
    return
  v.sum = v.key + (v.left.sum if v.left != None else 0) + (v.right.sum if v.right != None else 0)
  if v.left != None:
    v.left.parent = v
  if v.right != None:
    v.right.parent = v

def smallRotation(v):
  parent = v.parent
  if parent == None:
    return
  grandparent = v.parent.parent
  if parent.left == v:
    m = v.right
    v.right = parent
    parent.left = m
  else:
    m = v.left
    v.left = parent
    parent.right = m
  update(parent)
  update(v)
  v.parent = grandparent
  if grandparent != None:
    if grandparent.left == parent:
      grandparent.left = v
    else: 
      grandparent.right = v

def bigRotation(v):
  if v.parent.left == v and v.parent.parent.left == v.parent:
    # Zig-zig
    smallRotation(v.parent)
    smallRotation(v)
  elif v.parent.right == v and v.parent.parent.right == v.parent:
    # Zig-zig
    smallRotation(v.parent)
    smallRotation(v)    
  else: 
    # Zig-zag
    smallRotation(v);
    smallRotation(v);

# Makes splay of the given vertex and makes
# it the new root.
def splay(v):
  if v == None:
    return None
  while v.parent != None:
    if v.parent.parent == None:
      smallRotation(v)
      break
    bigRotation(v)
  return v

# Searches for the given key in the tree with the given root
# and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key.
# Otherwise, result is a pointer to the node with the smallest
# bigger key (next value in the order).
# If the key is bigger than all keys in the tree,
# then result is None.
def find(root, key): 
	v = root
	last = root
	next = None
	#if v != None:
		#print('v.key, key', v.key, key)
	while v != None:
		if v.key >= key and (next == None or v.key < next.key):
			next = v    
			last = v
		if v.key == key:
			break    
		if v.key < key:
			v = v.right
		else: 
			v = v.left
	#if root != None:
	#	print('root.key=', root.key)
	#if last != None:
	#	print('last.key=', last.key)
	#if next != None:
	#	print('next.key=', next.key)
	root = splay(last)
	#if root != None:
	#	print('root.key=', root.key)
	#if last != None:
	#	print('last.key=', last.key)
	#if next != None:
	#	print('next.key=', next.key)
	#update(root)
	return (next, root)

def split(root, key):  
  (result, root) = find(root, key)  
  if result == None:    
    return (root, None)  
  right = splay(result)
  left = right.left
  right.left = None
  if left != None:
    left.parent = None
  update(left)
  update(right)
  return (left, right)

  
def merge(left, right):
  if left == None:
    return right
  if right == None:
    return left
  while right.left != None:
    right = right.left
  right = splay(right)
  right.left = left
  update(right)
  return right

  
# Code that uses splay tree to solve the problem
                                    
root = None

def insert(x):
	global root
	(left, right) = split(root, x)
	if left != None:
		print('[module:insert] left.key = ', left.key)
	if right != None:
		print('[module:insert] right.key = ', right.key)
	new_vertex = None
	if right == None or right.key != x:
		new_vertex = Vertex(x, x, None, None, None)  
	root = merge(merge(left, new_vertex), right)
	if root != None:
		print('[module:insert] root.key = ', root.key)
	print_tree(root)
	
def erase(x): 
	global root
	# Implement erase yourself
	if root != None:
		print('[module:erase] root.key before find_without_splay = ', root.key)
	if x != None:
		print('[module:erase] x = ', x)
	N = find_without_splay(root, x)
	if N != None:
		print('[module:erase] N.key = ', N.key)
	if N == None:
		return
	if next_node(N) != None:
		print('[module:erase] next_node(N).key = ', next_node(N).key)
	if root != None:
		print('[module:erase] root.key before splay(next_node(N)) = ', root.key)
	splay(next_node(N))
	if root != None:
		print('[module:erase] root.key before splay(N) = ', root.key)
	splay(N)
	if root != None:
		print('[module:erase] root.key before delete(N) = ', root.key)
	delete(N)
	if root != None:
		print('[module:erase] root.key after delete(N) = ', root.key)
	#pass
  
def next_node(v):
	#print('v.key', v.key)
	if v.right != None:
		#print('leftDescendant(v.right)', leftDescendant(v.right).key)
		return leftDescendant(v.right)
	else:
		#print('rightAncestor(v)', rightAncestor(v).key)
		return rightAncestor(v)
		
def leftDescendant(v):
	if v.left == None:
		return v
	else:
		return leftDescendant(v.left)
	
def rightAncestor(v):
	if v.parent == None:
		return None
	elif v.key < v.parent.key:
		return v.parent
	else:
		return rightAncestor(v.parent)
  
def find_without_splay(root, key): 
  v = root
  last = root
  next = None
  while v != None:
    if v.key >= key and (next == None or v.key < next.key):
      next = v    
    last = v
    if v.key == key:
      break    
    if v.key < key:
      v = v.right
    else: 
      v = v.left      
  #root = splay(last)
  return (next)
 
def delete(v):
	global root
	if v.right == None:
		#remove v, promote v.left
		if v.left != None:
			v.left.parent = None
			root = v.left
		else:
			root = None
	else:
		X = next_node(v)
		#print('X', X.key)
		#Replace v by X
		v.key = X.key
		#print(X.key, X.parent.key)
		#Promote X.right
		if X.right != None:
			if X.parent.left == X:
				X.parent.left = X.right
				X.right.parent = X.parent
			elif X.parent.right == X:
				X.parent.right = X.right
				X.right.parent = X.parent
		#update(X)
	update(root)
	print_tree(root)
	#def promote_left_node(v):
	
def search(x): 
	global root
	# Implement find yourself
	(v, root) = find(root, x)
	if v != None:
		return v.key == x
	else:
		return False
  
def sum(fr, to): 
	global root
	(left, middle) = split(root, fr)
	(middle, right) = split(middle, to + 1)
	ans = 0
	# Complete the implementation of sum
	if middle != None:
		ans = middle.sum
	#return ans
	if root != None:
		print('[module:sum] root.key before merge = ', root.key)
	root = merge(merge(left, middle), right)
	if root != None:
		print('[module:sum] root.key after merge = ', root.key)
	return ans

def print_tree(root1):
	if root1 != None:
		print_tree(root1.left)
		print_tree(root1.right)
		print(root1.key)
	
MODULO = 1000000001
n = int(stdin.readline())
last_sum_result = 0
for i in range(n):
  line = stdin.readline().split()
  if line[0] == '+':
    x = int(line[1])
    insert((x + last_sum_result) % MODULO)
  elif line[0] == '-':
    x = int(line[1])
    erase((x + last_sum_result) % MODULO)
  elif line[0] == '?':
    x = int(line[1])
    print('Found' if search((x + last_sum_result) % MODULO) else 'Not found')
  elif line[0] == 's':
    l = int(line[1])
    r = int(line[2])
    res = sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
    print(res)
    last_sum_result = res % MODULO