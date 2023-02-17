class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		
class Stack:
	def __init__(self):
		self.head = None

	# Checks if stack is empty
	def isempty(self):
		if self.head == None:
			return True
		else:
			return False

	# Method to add data to the stack
	# adds to the start of the stack
	def push(self, data):

		if self.head == None:
			self.head = Node(data)

		else:
			newnode = Node(data)
			newnode.next = self.head
			self.head = newnode

	# Remove element that is the current head (start of the stack)
	def pop(self):

		if self.isempty():
			return None

		else:
			# Removes the head node and makes
			# the preceding one the new head
			poppednode = self.head
			self.head = self.head.next
			poppednode.next = None
			return poppednode.data

	# Returns the head node data
	def display(self):

		iternode = self.head
		if self.isempty():
			print("Stack Underflow")

		else:

			while(iternode != None):

				print(iternode.data, end = "")
				iternode = iternode.next
				if(iternode != None):
					print(" -> ", end = "")
			return
def undoOperation():
    temp = undo.pop()
    redo.push(temp)
def redoOperation():
    temp = redo.pop()
    undo.push(temp)

redo = Stack()
undo = Stack()
arr = "my name is shruti"
for i in arr:
    undo.push(i)
print("og")
undo.display()
undoOperation()
print("after undo")
undo.display()
print("\n")
print("after undo in redo")
redo.display()
print("\n")
redoOperation()
print("after redo")
undo.display()
print("\n")
print("after undo in redo")
redo.display()
print("\n")
