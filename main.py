from books import display_books, load_books, save_books
from dotenv import load_dotenv
import os

load_dotenv()

name = input("Enter your name: ")
print("welcome", name)

admin_mode = input("do you want to unlock the admin mode? (yes / no)")
if admin_mode == "yes":
    password = input("enter the password admin : ")
    if password == os.getenv("admin_pass"):
        print("admin mode actived!")
    else :

        print("wrong in the active the admin mode!")

print(f"Hello {name}, welcome to Personal Book Manager!")

books = load_books()

book_count = int(input("How many books do you want to enter? "))

for i in range(book_count):
    book = input(f"Enter the title of book #{i + 1}: ")
    books.append(book)

save_books(books)

display_books(books)

print("please follow me!")