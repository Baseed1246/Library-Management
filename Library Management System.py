class Book:
    def __init__(self, title, author, isbn, quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.quantity = quantity

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Quantity: {self.quantity}"

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author, isbn, quantity):
        if isbn in self.books:
            self.books[isbn].quantity += quantity
        else:
            self.books[isbn] = Book(title, author, isbn, quantity)
        print(f"Added {quantity} copies of '{title}'.")

    def update_book(self, isbn, title=None, author=None, quantity=None):
        if isbn in self.books:
            if title:
                self.books[isbn].title = title
            if author:
                self.books[isbn].author = author
            if quantity is not None:
                self.books[isbn].quantity = quantity
            print(f"Updated book with ISBN {isbn}.")
        else:
            print(f"Book with ISBN {isbn} does not exist.")

    def delete_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]
            print(f"Deleted book with ISBN {isbn}.")
        else:
            print(f"Book with ISBN {isbn} does not exist.")

    def view_books(self):
        if not self.books:
            print("Library is empty.")
        else:
            for book in self.books.values():
                print(book)

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. View Books")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            quantity = int(input("Enter number of copies: "))
            library.add_book(title, author, isbn, quantity)

        elif choice == '2':
            isbn = input("Enter book ISBN to update: ")
            title = input("Enter new book title (or leave blank to keep current): ")
            author = input("Enter new book author (or leave blank to keep current): ")
            quantity = input("Enter new quantity (or leave blank to keep current): ")
            quantity = int(quantity) if quantity else None
            library.update_book(isbn, title if title else None, author if author else None, quantity)

        elif choice == '3':
            isbn = input("Enter book ISBN to delete: ")
            library.delete_book(isbn)

        elif choice == '4':
            library.view_books()

        elif choice == '5':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
