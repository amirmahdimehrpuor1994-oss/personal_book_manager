import json


def display_books(books):
    print("\nYour books:")

    for book in books:
        print(f"- {book}")


def load_books():
    try:
        with open("books.json", "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

def save_books(books):
    with open("books.json", "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)