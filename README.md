# Personal Library Manager

## 📚 Overview
The **Personal Library Manager** is a command-line Python application that allows users to manage their book collection. Users can add, remove, search, and view books, as well as track their reading progress. The program also integrates with the Google Books API to fetch book summaries.

## 🎯 Features
- **Add a Book**: Enter book details (title, author, year, genre, and read status).
- **Remove a Book**: Remove a book by title.
- **Search for a Book**: Search by title or author.
- **Display All Books**: View all books in the collection.
- **Display Statistics**: View total books and percentage of books read.
- **Fetch Book Summary**: Get book summaries using the Google Books API.
- **Persistent Storage**: Books are saved to a file (`library.txt`) and loaded automatically on restart.

## 🛠️ Installation & Usage
### Prerequisites
- Python 3.x installed
- Required Python libraries: `requests`

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/personal-library-manager.git
   cd personal-library-manager
   ```
2. Install dependencies:
   ```bash
   pip install requests
   ```
3. Run the program:
   ```bash
   python library_manager.py
   ```

## 📌 How It Works
1. When the program starts, it **loads the library** from `library.txt`.
2. Users interact with the **menu system** to perform operations.
3. Changes (adding/removing books) are **automatically saved**.
4. When exiting, the program ensures the latest library state is stored.

## 📝 Example Usage
### Adding a Book:
```
Enter the book title: The Alchemist
Enter the author: Paulo Coelho
Enter the publication year: 1988
Enter the genre: Fiction
Have you read this book? (yes/no): yes
Book added successfully!
```
### Fetching Book Summary:
```
Enter the book title for summary: The Alchemist
📖 Summary: A novel about a young shepherd's journey to fulfill his personal legend...
```
### Removing a Book:
```
Enter the title of the book to remove: The Alchemist
Book removed successfully!
```

## 🔥 Future Enhancements
- Export library to CSV/JSON format.
- GUI version using Tkinter or PyQt.
- More API integrations for book details.


## 📄 License
This project is open-source and available under the [MIT License](LICENSE).

