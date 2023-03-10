class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		
class Stack:
	def __init__(self):
		self.head = None
		self.size = 0

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
		self.size += 1

	# Remove element that is the current head (start of the stack)
	def pop(self):

		if self.isempty():
			return None

		else:
			poppednode = self.head
			self.head = self.head.next
			poppednode.next = None
			self.size -=1
			return poppednode.data
		
			
	def length(self):
        return self.size

	# Returns the head node data
	def peek(self):

		if self.isempty():
			return None

		else:
			return self.head.data

	# Prints out the stack
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


class Solution:
    def leftSmaller(self, n, a):
        s = Stack()
        arr=[]
        for i in a:
            if s.isempty():
                s.push(i)
                arr.append(-1)
                
            elif i > s.peek():
                arr.append(s.peek())
                s.push(i)
                
            else:
                while s.length()>0 and i<=s.peek():
                    s.pop()
                if s.length() == 0:
                    s.push(i)
                    arr.append(-1)
                else:
                    arr.append(s.peek())
                    s.push(i)
                    
        return  arr
 
