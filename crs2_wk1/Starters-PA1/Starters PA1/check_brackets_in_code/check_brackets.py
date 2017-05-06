# python3

import sys

class Stack:
	 def __init__(self):
		 self.items = []

	 def isEmpty(self):
		 return self.items == []

	 def push(self, item):
		 self.items.append(item)

	 def pop(self):
		 return self.items.pop()

	 def peek(self):
		 return self.items[len(self.items)-1]

	 def size(self):
		 return len(self.items)

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
	text = sys.stdin.read()

	opening_brackets_stack = []
	isBalanced = -1 # -1 means balanced, otherwise the 0-based index of a faulty bracket
	for i, next in enumerate(text):
		if next == '(' or next == '[' or next == '{':
			bracket = Bracket(next, i)
			opening_brackets_stack.append(bracket)
		elif next == ')' or next == ']' or next == '}':
			if not opening_brackets_stack: # if stack is empty
				isBalanced = i
				break
			top = opening_brackets_stack.pop()
			if not top.Match(next):
				isBalanced = i
				break
	if opening_brackets_stack and isBalanced == -1:
		top = opening_brackets_stack[0]
		isBalanced = top.position
	# Printing answer, write your code here
	if isBalanced == -1:
		print("Success")
	else:
		print(isBalanced + 1)