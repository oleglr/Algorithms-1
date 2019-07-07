class Node():
	def __init__(self, initdata):
		self.data = initdata
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self, newdata):
		self.data = newdata

	def setNext(self, new_next):
		self.next = new_next	


class UnorderedList():
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def add(self, item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = tmp

	def size(self):
		count = 0
		current = self.head

		while current != None:
			count += 1
			current = current.getNext()

		return count

	def search(self, item):
		current = self.head
		found = False

		while not found and current != None:
			if current.getData() == item:
				found = True

			else:
				current = current.getNext()

		return found
		
	def remove(self, item):
		current = self.head
		previous = None
		found = False

		while not found:
			if current.getData() == item:
				found = True

			else:
				previous = current
				current = self.getNext()

		if previous == None:
			self.head = current.getNext()

		else:
			if current.getNext() is not None:
				previous.setNext(current.getNext())
			else:
				previous.setNext(None)

	def insert(self, index, data):
		cur_index = 0
		current = self.head
		previous = None
		
		temp = Node(data)

		if index == 0:
			temp.setNext(self.head)
			self.head = temp

		else:
			while cur_index != index:
				previous = current
				current = self.getNext()
				cur_index += 1

			
			previous.setNext(temp)
			temp.setNext(current)

	def append(self, data):
		current = self.head

		while current.next is not None:
			current = current.next

		current.setNext(Node(data))

	def pop(self, index=None):
		current = self.head
		previous = None
		cur_index = 0
		
		if index is None:
			while current.next is not None:
				previous = current
				current = current.getNext()
				cur_index += 1
			
			previous.next = None

		return current

	def index(self, data):
		index = 0
		current = self.head

		while current.getData() != data:
			current = current.getNext()
			index += 1

		return index
			
			

