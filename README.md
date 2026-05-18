# library_Management-PYTHON
Library Management System
A simple console-based Library Management System developed in Python. This project allows users to manage books and students efficiently using file handling. The system stores data permanently in text files and provides basic library operations such as adding books, viewing books, issuing books, and returning books.
Features
Add new books to the library
View all available and issued books
Add student records
Issue books to students
Return issued books
File handling using text files for data storage
Simple menu-driven interface
Technologies Used
Python
File Handling
Object-Oriented Programming (OOP)
Files Used
books.txt → Stores book details
students.txt → Stores student details
main.py → Main Python program
Book Details Format
Each book is stored in the following format:
Plain text
BookID,Title,Author,Availability
Example:
Plain text
101,Python Basics,John,1
1 → Available
0 → Issued
Student Details Format
Each student is stored in the following format:
Plain text
StudentID,Name,IssuedBooks
Example:
Plain text
S101,Rahul,101|102
How to Run
Install Python on your system.
Save the program as main.py.
Open terminal or command prompt.
Run the following command:
Bash
python main.py
Menu Options
Plain text
1. Add Book
2. View Books
3. Add Student
4. Issue Book
5. Return Book
6. Exit
Concepts Used
Classes and Objects
File Handling
Lists
String Manipulation
Conditional Statements
Loops
Future Improvements
Add login system
Search books by title or author
Delete books and students
Fine calculation for late returns
GUI version using Tkinter
