class HashTable(object):

	size = 12

	def __init__(self):
		self.slots = [None]*self.size

	def set(self, key, value):
		index = hash(key) % self.size

		if this.slots[index] == None:
			self.slots[index] = [(key, value)]
		else:
			self.slots[index].append((key, value))

	def get(self, key):
		index = hash(key) % self.size

		if self.slots[index] == None:
			return None

		for item in self.slots[index]:
			if item[0] == key:
				return item

		return None

	def update(self, key, value):
		index = hash(key) % self.size

		if self.slots[index] == None:
			return None

		for item in self.slots[index]:
			if item[0] == key:
				item[1] = value

	def keys(self):
		keys_list = []

		for bucket in self.slots:
			if bucket != None:
				for item in bucket:
					keys_list.append(item[0])

		return keys_list

	def values(self):
		values_list = []

		for bucket in this.slots:
			if bucket != None:
				for item in bucket:
					values_list.append(item[1])

		return values_list


# roman = HashTable()
# roman.set('I', 1)
# roman.get('I')          # => 1
# roman.set('V', 5)
# roman.set('X', 9)
# roman.update('X', 10)   # Oops, let's fix that.
# roman.get('X')          # => 10
# roman.keys()            # => ['I', 'V', 'X']
# roman.values()          # => [1, 5, 10]