class Cell:

	def __init__(self, value = None, prev_c = None, next_c = None):

		self.prev_c = prev_c
		self.next_c = next_c
		self.value = value

class List:

	def __init__(self):

		self.l_size = 0
		self.header = Cell()
		self.header.prev_c = self.header
		self.header.next_c = self.header
		self.header.value = 'header'

	def __iter__(self):

		return ListIterator(self)

	def front(self):

		return self.header.next_c

	def push_front(self, value):

		cell = Cell(value, self.header, self.header.next_c)

		self.header.next_c.prev_c = cell
		self.header.next_c = cell
		self.l_size += 1

	def pop_front(self):

		self.header.next_c = self.header.next_c.next_c
		del self.header.next_c.prev_c
		self.header.next_c.prev_c = self.header
		self.l_size -= 1

	def back(self):

		return self.header.prev_c

	def push_back(self, value):

		cell = Cell(value)

		cell.prev_c = self.header.prev_c
		cell.next_c = self.header
		self.header.prev_c.next_c = cell
		self.header.prev_c = cell
		self.l_size += 1

	def pop_back(self):

		self.header.prev_c = self.header.prev_c.prev_c
		del self.header.prev_c.next_c
		self.header.prev_c.next_c = self.header
		self.l_size -= 1

	def find(self, value):

		item = self.header.next_c

		while item.value != 'header':

			if item.value == value:

				return item

			item = item.next_c

		return self.header

	def insert(self, iterator, value):

		cell = Cell(value)
		iterator.element.prev_c.next_c = cell
		cell.prev_c = iterator.element.prev_c
		iterator.element.prev_c = cell
		cell.next_c = iterator.element
		self.l_size += 1
		iterator.element = cell

	def erase(self, iterator):

		iterator.element.prev_c.next_c = iterator.element.next_c
		iterator.element.next_c.prev_c = iterator.element.prev_c
		current = iterator.element.next_c
		del iterator.element
		iterator.element = current
		self.l_size -= 1

	def remove(self, value):

		it = iter(self)

		while it.element.value != 'header':

			if it.element.value == value:

				self.erase(it)

			else:

				it.next()

	def clear(self):

		while self.l_size > 0:

			self.pop_back()

	def size(self):

		return self.l_size

	def empty(self):

		return not self.l_size

class ListIterator:

	def __init__(self, list):

		self.list = list
		self.element = list.header.next_c

	def __iter__(self):

		return self

	def next(self):

		if self.element.value == 'header':

			raise StopIteration

		else:

			current = self.element
			self.element = self.element.next_c
			return current