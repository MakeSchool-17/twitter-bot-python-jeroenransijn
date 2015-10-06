from linked_list_node import LinkedListNode

# Singly linked
class LinkedList(object):

	def __init__(self):
		self.list = []
		self.head = None

	def append(self, data):
		node = LinkedListNode(data)

		if self.head == None:
			self.head = node
		else:
			node.next_node = self.tail

		self.tail = node

		self.list.append(node)

	# Functional style find so we can pass lambdas
	# returns None if not found
	def find(self, func):
		return self.recursive_find_on_data(self.tail, func)

	@staticmethod
	def recursive_find_on_data(node, func):
		if node == None:
			return None
		elif func(node.data):
			return node.data
		else:
			return LinkedList.recursive_find_on_data(node.next_node, func)

	def each(self, func):
		return self.recursive_each(self.tail, func)

	@staticmethod
	def recursive_each(node, func):
		if node == None:
			return
		else:
			func(node)
			LinkedList.recursive_each(node.next_node, func)

	# Returns nodes[0] = prev_node, nodes[1] = node instead of node.data
	@staticmethod
	def recursive_find(prev_node, node, func):
		if node == None:
			return None
		elif func(node):
			return (prev_node, node)
		else:
			return LinkedList.recursive_find(node, node.next_node, func)

	# Returns bool indicating success
	def delete(self, data):
		nodes = self.recursive_find(None, self.tail, lambda node: node.data == data)

		if nodes == None:
			return False

		prev_node = nodes[0]
		current_node = nodes[1]

		if current_node != None:
			# A node is found with the data

			if current_node == self.head:
				# The head is removed, the previous node becomes the head
				prev_node.next_node = None
				self.head = prev_node
			else:
				# Remove the current node from the chain
				prev_node.next_node = current_node.next_node

			if current_node == self.tail:
				# the current node is the tail and gets removed, tail becomes the next node
				self.tail = current_node.next_node

			return True
		else:
			return False


# Test code

# mylist = LinkedList()

# mylist.append('a')
# mylist.append('b')
# mylist.append('c')

# print(mylist.head.data) # => 'a'
# print(mylist.tail.data) # => 'c'
# print(mylist.find(lambda data: data > 'b')) # => 'c'
# print(mylist.delete('a'))
# print(mylist.head.data)  # => 'b')