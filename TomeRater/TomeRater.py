class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("Your email address has been updated.")

    def __repr__(self):
        return "User: {}, Email: {}, Books Read: {}".format(self.name, self.email, len(self.books)) # Books Read might change to Books Reviewed

    def __eq__(self, other_user):
        return (self.name == other_user.name) and (self.email == other_user.email)

    def read_book(self, book, rating = None):
        self.books[book] = rating
    
    def get_average_rating(self):
        return sum([x for x in self.books.values() if x != None])/len(self.books.keys())

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
    
    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("This book's ISBN has been updated.")

    def add_rating(self, rating):
        self.ratings = []
        if rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def __eq__(self, other_book):
        return (self.title == other_book.title) and (self.isbn == other_book.isbn)

    def get_average_rating(self):
        return sum(self.ratings)/len(self.ratings)

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __repr__(self):
        return "{}".format(self.title)

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author      

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{} by {}".format(self.title, self.author)

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
        return "{}, a {} manual on {}".format(self.title, self.level, self.subject)

class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def __repr__(self):
        return "The usernames and corresponding emails that are currently in the system: {}".format(self.users), "The books and the number of users who have read the book: {}".format(self.books)

    def __eq__(self, otherTomeRater):
        return (self.users == otherTomeRater.get_users_emails()) and (self.books == otherTomeRater.get_books_readers())

    def get_users_emails(self):
        return self.users

    def get_books_readers(self):
        return self.books

    def create_book(self, title, isbn): # Creates new book? 
        return Book(title, isbn)

    def create_novel(self, title, author, isbn): # Creates new novel?
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn): # Creates new non fic?
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating = None):
        if email not in self.users.keys():
            print("No user with email: {}".format(email))
        else:
            print(self.users[email])
            self.users[email].read_book(book, rating)
            if rating != None:
                book.add_rating(rating)
            if book in self.books.keys():
                self.books[book] += 1
            else:
                self.books[book] = 1

    def add_user(self, name, email, books = []):
        self.users[email] = User(name, email)
        if len(books) > 0:
            for x in books:
                self.add_book_to_user(x, email) # Self might be x

    def print_catalog(self):
        for key in self.books.keys():
            print(key)

    def print_users(self):
        for value in self.users.values():
            print(value)

    def most_read_book(self):
        mx = max(self.books.values())
        for key, value in list(zip(self.books.keys(), self.books.values())):
            if value == mx: return key
            
    def highest_rated_book(self):
        mx = 0
        mx_book = None
        for book, rating in list(zip(self.books.keys(), [x.get_average_rating() for x in self.books.keys()])):
            if rating > mx:
                mx = rating
                mx_book = book
        return mx_book
        
    def most_positive_user(self):
        mx = 0
        mx_user = None
        for user, rating in list(zip(self.users.values(), [x.get_average_rating() for x in self.users.values()])):
            if rating > mx:
                mx = rating
                mx_user = user
        return mx_user
        
    
Tome_Rater = TomeRater()

#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)

#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")

#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", books=[book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)


#Uncomment these to test your functions:
Tome_Rater.print_catalog()
Tome_Rater.print_users()

print("Most positive user:")
print(Tome_Rater.most_positive_user())
print("Highest rated book:")
print(Tome_Rater.highest_rated_book())
print("Most read book:")
print(Tome_Rater.most_read_book())

paul = User("dominatingdonut", "dominatingdonutgmail.com")


           
