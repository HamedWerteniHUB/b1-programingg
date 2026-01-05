
# Lab Task 1: School Management System


class Person:
    """Base class representing a person"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."


class Student(Person):
    """Student class inheriting from Person"""
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        return f"Hi, I'm {self.name}, a student. My ID is {self.student_id} and I'm {self.age} years old."


class Teacher(Person):
    """Teacher class inheriting from Person"""
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        return f"Hello, I'm {self.name}, a teacher. I teach {self.subject} and I'm {self.age} years old."


# Testing Task 1
student = Student("Alice", 16, "S001")
teacher = Teacher("Mr. Smith", 35, "Mathematics")

print("=== School Management System ===")
print(student.introduce())
print(teacher.introduce())
print(f"Student age: {student.age}")
print(f"Teacher subject: {teacher.subject}")



# Lab Task 2: Library System with Composition


class Book:
    """Represents a single book"""
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn})"


class Library:
    """Library class that contains Book objects (composition)"""
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        return f"Added: {book.display_info()}"

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                return f"Removed: {book.display_info()}"
        return f"Book '{title}' not found."

    def list_books(self):
        if not self.books:
            return f"{self.name} has no books."
        result = f"\n=== Books in {self.name} ===\n"
        for i, book in enumerate(self.books, 1):
            result += f"{i}. {book.display_info()}\n"
        return result

    def search_by_title(self, search_term):
        found = [book for book in self.books if search_term.lower() in book.title.lower()]
        if found:
            result = f"\nFound {len(found)} book(s):\n"
            for book in found:
                result += f"- {book.display_info()}\n"
            return result
        return f"No books found matching '{search_term}'"


# Testing Task 2
library = Library("City Library")
book1 = Book("Python Crash Course", "Eric Matthes", "978-1593279288")
book2 = Book("Clean Code", "Robert Martin", "978-0132350884")
book3 = Book("The Pragmatic Programmer", "Hunt & Thomas", "978-0201616224")

print("\n=== Library System ===")
print(library.add_book(book1))
print(library.add_book(book2))
print(library.add_book(book3))
print(library.list_books())
print(library.search_by_title("Python"))
print(library.remove_book("Clean Code"))
print(library.list_books())


# ===============================
# Lab Task 3: File Manager with os Module


import os

def file_manager_demo():
    """Demonstrates file and directory operations using os module"""

    # 1. Display current working directory
    current_dir = os.getcwd()
    print(f"\nCurrent Directory: {current_dir}\n")

    # 2. Create a new folder
    folder_name = "lab_files"
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print(f"Created folder: {folder_name}")
    else:
        print(f"Folder '{folder_name}' already exists")

    # 3. Create three text files
    file_names = ["file1.txt", "file2.txt", "file3.txt"]
    for file_name in file_names:
        file_path = os.path.join(folder_name, file_name)
        with open(file_path, 'w') as f:
            f.write(f"This is {file_name}")
        print(f"Created file: {file_name}")

    # 4. List all files
    print(f"\n=== Files in {folder_name} ===")
    for file in os.listdir(folder_name):
        print(f"- {file}")

    # 5. Rename a file
    old_path = os.path.join(folder_name, "file2.txt")
    new_path = os.path.join(folder_name, "renamed_file.txt")
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"\nRenamed 'file2.txt' to 'renamed_file.txt'")

    print(f"\n=== Files after rename ===")
    for file in os.listdir(folder_name):
        print(f"- {file}")

    # 6. Cleanup
    print(f"\n=== Cleaning up ===")
    for file in os.listdir(folder_name):
        file_path = os.path.join(folder_name, file)
        os.remove(file_path)
        print(f"Deleted: {file}")
    os.rmdir(folder_name)
    print(f"Removed folder: {folder_name}")
    print("\nAll cleanup completed successfully!")


# Run Task 3
file_manager_demo()

