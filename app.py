import json
import os
import requests

def get_book_summary(title):
    """Fetch a book summary from Google Books API based on title."""
    url = f"https://www.googleapis.com/books/v1/volumes?q=intitle:{title}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if "items" in data:
            summary = data["items"][0]["volumeInfo"].get("description", "No summary available.")
            return summary
        else:
            return "❌ No summary found for this book."
    else:
        return "❌ Error fetching summary."

def display_menu():
    print("\nWelcome to your Personal Library Manager!")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Get Book Summary")
    print("7. Exit")

def add_book(library):
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
    
    library.append({"title": title, "author": author, "year": year, "genre": genre, "read": read_status})
    save_library(library)  # ✅ Save immediately after adding a book
    print("Book added successfully!")

def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            save_library(library)  # ✅ Save immediately after removing a book
            print("Book removed successfully!")
            return
    print("Book not found!")

def search_book(library):
    choice = input("Search by (1) Title or (2) Author? Enter 1 or 2: ")
    query = input("Enter your search query: ")
    
    results = [book for book in library if (book["title"].lower() if choice == "1" else book["author"].lower()) == query.lower()]
    
    if results:
        print("Matching Books:")
        for book in results:
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    else:
        print("No matching books found.")

def display_books(library):
    if library:
        print("Your Library:")
        for book in library:
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    else:
        print("Library is empty!")

def display_statistics(library):
    total_books = len(library)
    if total_books == 0:
        print("No books in the library yet.")
        return
    read_books = sum(1 for book in library if book["read"])
    percentage_read = (read_books / total_books) * 100
    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.2f}%")

def get_book_summary_option():
    title = input("Enter the book title for summary: ")
    summary = get_book_summary(title)
    print(f"\n📖 Summary for '{title}':\n{summary}\n")

def save_library(library, filename="library.txt"):
    """Library ko JSON format mein save karega taake wapas load kar sakein."""
    with open(filename, "w") as file:
        json.dump(library, file, indent=4)  # Pretty formatting for better readability

def load_library(filename="library.txt"):
    """Library ko file se load karega. Agar file exist nahi karti to empty list return karega."""
    if os.path.exists(filename) and os.path.getsize(filename) > 0:  # File khali na ho
        with open(filename, "r") as file:
            return json.load(file)
    return []  # Agar file exist nahi karti ya empty hai to empty list return karega

def main():
    library = load_library()  # ✅ Load library when the program starts
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            get_book_summary_option()
        elif choice == "7":
            save_library(library)  # ✅ Save on exit
            print("Library saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
