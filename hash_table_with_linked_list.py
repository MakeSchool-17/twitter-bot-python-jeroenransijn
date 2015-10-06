from linked_list import LinkedList

# Hash table using a linked list for the buckets
class HashTable(object):

	size = 12

	def __init__(self):
		self.slots = [None]*self.size

	def set(self, key, value):
		index = hash(key) % self.size

		if self.slots[index] == None:
			bucket = LinkedList()
			bucket.append([key, value])
			self.slots[index] = bucket
		else:
			self.slots[index].append((key, value))

	def get_node(self, bucket, key):
		return bucket.find(lambda data: data[0] == key)

	def get(self, key):
		index = hash(key) % self.size
		bucket = self.slots[index]

		if bucket == None:
			return None

		return self.get_node(bucket, key)[1]

	def update(self, key, value):
		index = hash(key) % self.size
		bucket = self.slots[index]

		if bucket == None:
			return None

		node = self.get_node(bucket, key)

		if node != None:
			node[1] = value

	def keys(self):
		keys_list = []

		for bucket in self.slots:
			if bucket != None:
				# Could possibly be done by a map
				bucket.each(lambda node: keys_list.append(node.data[0]))

		return keys_list

	def values(self):
		values_list = []

		for bucket in self.slots:
			if bucket != None:
				# Could possibly be done by a map
				bucket.each(lambda node: values_list.append(node.data[1]))

		return values_list


roman = HashTable()
roman.set('I', 1)
print(roman.get('I'))          # => 1
roman.set('V', 5)
roman.set('X', 9)
print(roman.update('X', 10)   )# Oops, let's fix that.
print(roman.get('X')          )# => 10
print(roman.keys()            )# => ['I', 'V', 'X']
print(roman.values()          )# => [1, 5, 10]