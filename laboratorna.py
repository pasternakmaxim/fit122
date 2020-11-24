class HomeLibrary:

	def __init__(self):
		self.bookshelf = []

	def home_add(self,data):
		data = data.split()
		self.bookshelf.append(data)

	def search_author(self,author):
		for data in self.bookshelf:
			if ' '.join(data[:2]) == author:
				return ' '.join(data)

	def search_genre(self, genre):
		for data in self.bookshelf:
			if data[3].split(':')[1].strip() == genre:
				return ' '.join(data)


if __name__ == '__main__':
	
	data = '''Мишель Ульбэк "Серотонин" жанр: роман
			  Тамара Габриель "Уроборос" жанр:киберпанк
			  Владмир Кощеев "Ультиматум" жанр:фантастика'''

	home = HomeLibrary()
	for line in data.split('\n'):
		home.home_add(line)


	print(home.search_author('Мишель Ульбэк'))
	print(home.search_genre('Фантастика'))


