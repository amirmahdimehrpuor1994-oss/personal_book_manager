from books import display_books

name = input("Enter your name: ")

print(f"Hello {name}, welcome to Personal Book Manager!")

book_count = int(input("How many books do you want to enter? "))

books = []

for i in range(book_count):
    book = input(f"Enter the title of book #{i + 1}: ")
    books.append(book)

display_books(books)