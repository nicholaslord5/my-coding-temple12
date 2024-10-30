#

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book(library, new_book):
    if new_book in library:
        print(f"The book '{new_book[0]}' by {new_book[1]} is already in the library.")
    else:
        library.append(new_book)
        print(f"Added '{new_book[0]}' by {new_book[1]} to the library.")

def user_input_add_books(library):
    while True:
        title = input("Enter the book title you wish to add (or type 'quit' to end program): ")
        if title.lower() == 'quit':
            print("Program ended. Happy reading!")
            break
        author = input("Enter the author's name: ")
        add_book(library, (title, author))
        print()

print("Welcome to Ye Olde Library System!")
user_input_add_books(library)

print("\nUpdated Library:")
for book in library:
    print(f"'{book[0]}' by {book[1]}")