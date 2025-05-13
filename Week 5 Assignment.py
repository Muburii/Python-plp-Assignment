# Assignment 1: Book 
class Book:
    def __init__(self, title, author, pages, genre):
        self.title = title
        self.author = author
        self._pages = pages       # Encapsulated (protected) attribute
        self.genre = genre

    def description(self):
        return f"'{self.title}' by {self.author} - Genre: {self.genre}, Pages: {self._pages}"

    def read(self):
        print(f"You start reading '{self.title}'... ")

# Inherited class: EBook
class EBook(Book):
    def __init__(self, title, author, pages, genre, file_size_mb):
        super().__init__(title, author, pages, genre)
        self.file_size_mb = file_size_mb

    def download(self):
        print(f"Downloading '{self.title}'... File size: {self.file_size_mb}MB ")

    def read(self):
        print(f"Opening eBook '{self.title}' on your device... ")

book1 = Book("Tumbo LisiloShiba", "alifa Chokocha", 336, "Hekaya")
ebook1 = EBook("Digital Fortress", "Dan Brown", 384, "Tech Thriller", 2.5)

print(book1.description())
print(ebook1.description())

book1.read()
ebook1.download()
ebook1.read()

#Assignment 2

class Animal:
    def move(self):
        print("The animal moves.")

class Dog(Animal):
    def move(self):
        print("The dog runs ")

class Bird(Animal):
    def move(self):
        print("The bird flies ")

class Fish(Animal):
    def move(self):
        print("The fish swims ")

# Polymorphic behavior
def describe_movement(animal):
    animal.move()

# Create instances
dog = Dog()
bird = Bird()
fish = Fish()

# Test polymorphism
animals = [dog, bird, fish]
for animal in animals:
    describe_movement(animal)

