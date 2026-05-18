# Library Management System in Python

class Book:   
    def __init__(self, book_id, title, author, available=True):
        self.id = book_id
        self.title = title
        self.author = author
        self.available = available

    def to_string(self):
        return f"{self.id},{self.title},{self.author},{1 if self.available else 0}"


class Student:   # Student class
    def __init__(self, student_id, name, issued_books=""):
        self.id = student_id
        self.name = name
        self.issued_books = issued_books

    def to_string(self):
        return f"{self.id},{self.name},{self.issued_books}"


class Library:   # Library class

    # Add Book
    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Title: ")
        author = input("Enter Author: ")

        with open("books.txt", "a") as file:
            file.write(f"{book_id},{title},{author},1\n")

        print("Book added successfully!")

    
    def view_books(self):
        try:
            with open("books.txt", "r") as file:
                for line in file:
                    data = line.strip().split(",")

                    if len(data) >= 4:
                        book_id, title, author, available = data

                        status = "Available" if available == "1" else "Issued"

                        print(f"{book_id}\t| {title}\t| {author}\t| {status}")

        except FileNotFoundError:
            print("No books found!")

    
    def add_student(self):
        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")

        with open("students.txt", "a") as file:
            file.write(f"{student_id},{name},\n")

        print("Student added successfully!")

    
    def issue_book(self):
        book_id = input("Enter Book ID: ")
        student_id = input("Enter Student ID: ")

        books = []
        found = False

        Availability
        try:
            with open("books.txt", "r") as file:
                for line in file:
                    data = line.strip().split(",")

                    if len(data) >= 4:
                        bid, title, author, available = data

                        if bid == book_id and available == "1":
                            available = "0"
                            found = True

                        books.append(f"{bid},{title},{author},{available}")

            if not found:
                print("Book not available!")
                return

            with open("books.txt", "w") as file:
                for book in books:
                    file.write(book + "\n")

        except FileNotFoundError:
            print("Books file not found!")
            return

        
        students = []

        try:
            with open("students.txt", "r") as sfile:
                for line in sfile:
                    data = line.strip().split(",")

                    if len(data) >= 3:
                        sid, name, issued = data

                        if sid == student_id:
                            if issued == "":
                                issued = book_id
                            else:
                                issued += "|" + book_id

                        students.append(f"{sid},{name},{issued}")

            with open("students.txt", "w") as sfile:
                for student in students:
                    sfile.write(student + "\n")

            print("Book issued successfully!")

        except FileNotFoundError:
            print("Students file not found!")

    
    def return_book(self):
        book_id = input("Enter Book ID: ")
        student_id = input("Enter Student ID: ")

        books = []

        try:
            with open("books.txt", "r") as file:
                for line in file:
                    data = line.strip().split(",")

                    if len(data) >= 4:
                        bid, title, author, available = data

                        if bid == book_id:
                            available = "1"

                        books.append(f"{bid},{title},{author},{available}")

            with open("books.txt", "w") as file:
                for book in books:
                    file.write(book + "\n")

            print("Book returned successfully!")

        except FileNotFoundError:
            print("Books file not found!")


def main():
    lib = Library()

    while True:
        print("\n==== LIBRARY MENU ====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Add Student")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            lib.add_book()

        elif choice == 2:
            lib.view_books()

        elif choice == 3:
            lib.add_student()

        elif choice == 4:
            lib.issue_book()

        elif choice == 5:
            lib.return_book()

        elif choice == 6:
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


# Run Program
if __name__ == "__main__":
    main()
