class User(object):
	def __init__(self, name, email):
		self.name = name
		self.email = email
		self.books = {}
		
	def get_email(self):
		return self.email

	def change_email(self, address):
		self.email = address
		print("The email of " + self.name + " is updated")

	def __repr__(self):
		return "User {user_name}, email: {user_email}, books read: {books_read}".format(user_name = self.name, user_email = self.email, books_read = len(self.books))

	def __eq__(self, other_user):
		if (self.name == other_user.name) and (self.email == other_user.email):
			return True
		else:
			return False

	def read_book(self, book, rating = None):
		self.books[book] = rating
		
	def get_average_rating(self):
		total_rating = 0
		for rating in self.books.values():
			if rating is not None:
				total_rating += rating
		return total_rating / len(self.books)
	
	def  get_books_read(self):
		return len(self.books)

	def __hash__(self):
		return hash((self.name, self.email))

class Book(object):
	def __init__(self, title, isbn):
		self.title = title
		self.isbn = isbn
		self.ratings = []

	def get_title(self):
		return self.tilte

	def get_isbn(self):
		return self.isbn

	def set_isbn(self, new_isbn):
		self.isbn = new_isbn
		print("The ISBN is updated")

	def add_rating(self, rating):
		if rating == None:
			return
		if rating >= 0 and rating <= 4:
			self.ratings.append(rating)
		else:
			print("Invalid Rating")

	def get_average_rating(self):
		total_rating = 0
		for rating in self.ratings:
			total_rating += rating
		return total_rating / len(self.ratings)
			
	def __eq__(self, other_book):
		if (self.title == other_book.title) and (self.isbn == other_book.isbn):
			return True
		else:
			return False

	def __hash__(self):
		return hash((self.title, self.isbn))
	
	def __repr__(self):
		return "Book: {book}, with ISBN: {isbn}".format(book = self.title, isbn = self.isbn)

class Fiction(Book):
	def __init__(self, title, author, isbn):
		super().__init__(title, isbn)
		self.author = author

	def get_author(self):
		return self.author

	def __repr__(self):
		return "{title} by {author}".format(title = self.title, author = self.author)

class Non_Fiction(Book):
	def __init__(self, title, subject, level, isbn):
		super().__init__(title, isbn)
		self.subject = subject
		self.level = level

	def get_subject(self):
		return self.subject

	def get_level(self):
		return self.level

	def __repr__(self):
		return "{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)

class TomeRater(object):
	def __init__(self):
		self.users = {}
		self.books = {}

	def create_book(self, title, isbn):
		new_book = Book(title, isbn)
		return	new_book

	def create_novel(self, title, author, isbn):
		new_novel = Fiction(title, author, isbn)
		return new_novel

	def create_non_fiction(self, title, subject, level, isbn):
		new_non_fiction = Non_Fiction(title, subject, level, isbn)
		return new_non_fiction

	def add_book_to_user(self, book, email, rating = None):
		if email not in self.users.keys():
			print("No user with email {email}!".format(email = email))	
		else:
			user = self.users.get(email)
			user.read_book(book, rating)
			book.add_rating(rating)
			known_book = self.books.get(book, None)
			if known_book == None:
				self.books[book] = 1
			else:
				value = self.books.get(book)
				self.books[book] = value + 1

	def add_user(self, name, email, user_books = None):
		new_user = User(name, email)
		self.users[email] = new_user
		if not user_books == None:
			for book in user_books:
				self.add_book_to_user(book, email)

	def print_catalog(self):
		for book in self.books.keys():
			print(book)

	def print_users(self):
		for user in self.users.values():
			print(user)
	
	def most_read_book(self):
		most_read_book = None
		highest_times_read = 0
		for book in self.books.keys():
			if self.books.get(book) > highest_times_read:
				highest_times_read = self.books.get(book)
				most_read_book = book
		return most_read_book
		
	def highest_rated_book(self):
		highest_rated_book = None
		highest_average_rating = 0
		for book in self.books.keys():
			if book.get_average_rating() > highest_average_rating:
				highest_avarage_rating = book.get_average_rating()
				highest_rated_book = book
		return highest_rated_book

	def most_positive_user(self):
		most_positive_user = None
		highest_average_rating = 0
		for user in self.users.values():
			if user.get_average_rating() > highest_average_rating:
				highest_average_rating = user.get_average_rating()
				most_positive_user = user
		return most_positive_user
		
	def get_n_most_read_books(self, n):
		if n > len(self.books):
			n = len(self.books)
		most_read_books_list = []
		copy_self_books = self.books
		for i in range(n):
			times_read = 0
			most_read = None
			for book in copy_self_books:
				if copy_self_books.get(book) > times_read:
					most_read = book
					times_read = copy_self_books.get(book)
			most_read_books_list.append(most_read)
			copy_self_books.pop(most_read)
		return most_read_books_list
					
	def get_n_most_prolific_readers(self, n):
		if n > len(self.users):
			n = len(self.users)
		most_prolific_readers_list = []
		copy_self_users = self.users
		for i in range(n):
			books_read = 0
			most_prolific_reader = None
			for user in copy_self_users.values():
				if user.get_books_read() > books_read:
					most_prolific_reader = user
					books_read = user.get_books_read()
			most_prolific_readers_list.append(user)
			copy_self_users.pop(most_prolific_reader.get_email())
		return most_prolific_readers_list

		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		