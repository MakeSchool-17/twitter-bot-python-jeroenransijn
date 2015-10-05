import random

def get_book_text():
	return open('book.txt', 'r').read()

def get_sample_text():
	return open('some.txt', 'r').read()

# dictionary based
def histogram_dictionary(source_text):
	hist = {}

	for word in source_text.split():
		if word in hist:
			hist[word] += 1
		else:
			hist[word] = 1
	return hist

def histogram_list_of_tuples(source_text):
	hist = []

	for word in source_text.split():
		is_found = False

		for hist_word in hist:
			if word == hist_word[0]:
				hist_word[1] += 1
				is_found = True

		if not is_found:
			hist.append((word, 1))

	return hist

# Singly linked list

class NodeSinglyLinkedList(object):

	def __init__(self, data = None, next_node = None):
		self.data = data
		self.next_node = next_node

	def set_next(self, next_node):
		self.next_node = next_node

class SinglyLinkedList(object):

	def __init__(self, head = None):
		self.head = None

	def insert(self, data):
		new_node = NodeSinglyLinkedList(data)
		new_node.set_next(self.head) # why is this?
		self.head = new_node

	# Functional style find so we can pass lamdas
	# returns None if not found
	def find(func):
		return self.recursive_find(self.head, func)

	# def frequency():

	@staticmethod
	def recursive_find(node, func):
		if node == None:
			return None
		elif func(node):
			return node
		elif:
			return recursive_find(node.next_node, func)

def histogram_singly_linked_list(source_text):
	singyly_linked_list = SinglyLinkedList()

	for word in source_text.split():
		node = singly_linked_list.find(lambda node: node[0] == word)
		if node != None:
			node[1] += 1
		else:
			singly_linked_list.insert(NodeSinglyLinkedList((word, 1)))

	return singly_linked_list

# Binary search tree

class BSTNode(object):

	def __init__(self, data):
		self.data = data

class BinarySearchTree(object):

	def __init__(self):
		self.root = None

	def insert(self, word):
		if self.root == None:
			self.root = word

		node = self.root
		while node:
			if word == node.data[0]:
				node.data[1] += 1 # increase the frequency
			elif word < node.data[0]:
				if node.left_node == None:
					node.left_node = BSTNode((word, 1))
				else:
					node = node.left_node
			elif word > node.data[0]:
				if node.right_node == None:
					node.right_node = BSTNode((word, 1))
				else:
					node = node.right_node

	def find(self, word):
		return recursive_find(self.root, word)

	def frequency(self, word):
		node = find(word)

		if node == None:
			return 0
		else:
			return node[1]

	@classmethod
	def recursive_find(node, word):
		if word == node.data[0]:
			return node
		if word < node.data[0]:
			recursive_find(node.left_node)
		elif word > node.data[0]:
			recursive_find(node.right_node)
		else:
			return None

def histogram_binary_search_tree(source_text):
	bst = BinarySearchTree()

	for word in source_text.split():
		bst.insert(word)

	return bst


def unique_words(hist):
	return len(hist)

def frequency(hist, word):
	return hist[word]

def get_random_word(hist):
	return random.choice(list(hist.keys()))

def create_sentence(amount_of_words):
	text = get_sample_text()

	hist = histogram(text)

	number_line = create_number_line(hist)

	sentence = ""
	for i in range(amount_of_words): # 40
		sentence += get_random_word_by_frequency(number_line) + " "

	return sentence

def get_random_word_by_frequency(number_line):
	total = number_line[-1][1]
	rand_int = random.randint(1, total)

	for item in number_line:
		if item[1] >= rand_int:
			return item[0]

def create_number_line(hist):
	line = []
	prev = 0

	for word, amount in hist.items():
		prev = prev + amount
		line.append((word, prev))

	return line

# print(get_book_text())
print(create_sentence(40))
# print(my_hist)
# print(unique_words(my_hist))
# print(frequency(my_hist, 'Giles'))
# print(get_random_word(my_hist))

