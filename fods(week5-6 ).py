"""
Write a program to read a file “students.csv” and print it’s value. The fields to read are name, id,
course, level and section.
"""
"""
import csv

def read_students_csv(file_name):
    try:
        with open(file_name, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row.get('name')
                id = row.get('id')
                course = row.get('course')
                level = row.get('level')
                section = row.get('section')
                
                print(f"Name: {name}, ID: {id}, Course: {course}, Level: {level}, Section: {section}")
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

read_students_csv("student.csv")
"""
"""
Write a program to take the user details as the input from the user and write it to the existing file
“students.csv”. The new record should be added to the end of the file. The fields to take input are
name, id, course, level and section.
"""
import csv

def add_student_record():
    print("Enter student details:")
    name = input("Name: ")
    id = input("ID: ")
    course = input("Course: ")
    level = input("Level: ")
    section = input("Section: ")

    with open('student.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, id, course, level, section])
    
    print("Student record added successfully!")

add_student_record()
"""
Write a program input any list of numbers from the user, calculate the addition, subtraction,
multiplication and division values and write into a file with the current date and time. The program
should allow the user to repeat the operation until they want. When the user choose the option to
exit the program, the user should be displayed with the details in the current file in a proper format.
"""
import datetime

def perform_calculations(numbers):
    total_sum = sum(numbers)
    total_diff = numbers[0]   
    for num in numbers[1:]:
        total_diff -= num

    total_product = 1
    for num in numbers:
        total_product *= num
    
    total_division = numbers[0] 
    for num in numbers[1:]:
        if num != 0: 
            total_division /= num
        else:
            return (total_sum, total_diff, total_product, 'Division by zero error.')

    return (total_sum, total_diff, total_product, total_division)

def write_to_file(results):
    with open("calculations.txt", "a") as file:
        now = datetime.datetime.now()
        file.write(f"Date and Time: {now}\n")
        file.write(f"Results:\n")
        file.write(f"Sum: {results[0]}\n")
        file.write(f"Difference: {results[1]}\n")
        file.write(f"Product: {results[2]}\n")
        file.write(f"Division: {results[3]}\n")
        file.write("\n")

def display_file_contents():
    with open("calculations.txt", "r") as file:
        contents = file.read()
        print(contents)

def main():
    while True:
        user_input = input("Enter a list of numbers separated by spaces: ")
        numbers = list(map(float, user_input.split()))
        
        results = perform_calculations(numbers)
        write_to_file(results)
        
        repeat = input("Do you want to perform another calculation? (yes/no): ")
        if repeat.lower() != 'yes':
            break

    print("Here are the details of the calculations:")
    display_file_contents()

if _name_ == "_main_":
    main()

# Write a program to take read a file and write it into another file. The input and output file names
# should be taken input from the user. Use the concept of try/except to handle the exception. Provide
# the proper error if the file does not exist while reading and also if the file for output exists.
def copy_file():
    input_file = input("Enter the name of the input file: ")
    output_file = input("Enter the name of the output file: ")

    try:
        with open(input_file, 'r') as infile:
            try:
                with open(output_file, 'x') as outfile:
                    content = infile.read()
                    outfile.write(content)
                print(f"Contents of '{input_file}' have been copied to '{output_file}'.")
            except FileExistsError:
                print(f"Error: The file '{output_file}' already exists.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")

if _name_ == "_main_":
    copy_file()
# 5. Create a class Student with the attributes such as id, name, address, admission year, level, section. Instantiate the object of class to take input for all the attributes and display the output. 
class Student:
    def _init_(self, sid, name, address, admission_year, level, section):
        self.id = sid
        self.name = name
        self.address = address
        self.admission_year = admission_year
        self.level = level
        self.section = section

    def display(self):
        print("\n--- Student Details ---")
        print("ID:", self.id)
        print("Name:", self.name)
        print("Address:", self.address)
        print("Admission Year:", self.admission_year)
        print("Level:", self.level)
        print("Section:", self.section)


sid = input("Enter Student ID: ")
name = input("Enter Student Name: ")
address = input("Enter Address: ")
admission_year = input("Enter Admission Year: ")
level = input("Enter Level: ")
section = input("Enter Section: ")

student1 = Student(sid, name, address, admission_year, level, section)

student1.display()

# 6. Write a program to create a class called recipe with the attributes such as id, name, ingredients, descriptions. Create another class called recipe book to manage the collection of recipes.
class Recipe:
    def _init_(self, rid, name, ingredients, description):
        self.id = rid
        self.name = name
        self.ingredients = ingredients
        self.description = description

    def display(self):
        print("\n--- Recipe Details ---")
        print("ID:", self.id)
        print("Name:", self.name)
        print("Ingredients:", self.ingredients)
        print("Description:", self.description)

class RecipeBook:
    def _init_(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)
        print(f"Recipe '{recipe.name}' added successfully.")

    def display_all_recipes(self):
        if not self.recipes:
            print("\nNo recipes in the book.")
        else:
            print("\n=== All Recipes ===")
            for recipe in self.recipes:
                recipe.display()


recipe_book = RecipeBook()

while True:
    print("\n--- Recipe Book Menu ---")
    print("1. Add Recipe")
    print("2. View All Recipes")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        rid = input("Enter Recipe ID: ")
        name = input("Enter Recipe Name: ")
        ingredients = input("Enter Ingredients (comma separated): ")
        description = input("Enter Description: ")
        recipe = Recipe(rid, name, ingredients, description)
        recipe_book.add_recipe(recipe)

    elif choice == '2':
        recipe_book.display_all_recipes()

    elif choice == '3':
        print("Exiting Recipe Book. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")


# 7. Write a program to implement a class called employee with attributes such as empid, name, address, contact_number, spouse_name, number_of_child, salary. Instantiate this class to input the values for multiple employees and write it in a file “employees.csv”. Allow the user of your program to see the list of employees and their details as well. Try to use the concept of try/except too in the program.
import csv

class Employee:
    def _init_(self, empid, name, address, contact_number, spouse_name, number_of_child, salary):
        self.empid = empid
        self.name = name
        self.address = address
        self.contact_number = contact_number
        self.spouse_name = spouse_name
        self.number_of_child = number_of_child
        self.salary = salary

    def to_list(self):
        return [self.empid, self.name, self.address, self.contact_number, self.spouse_name, self.number_of_child, self.salary]

def add_employee():
    empid = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    address = input("Enter Address: ")
    contact_number = input("Enter Contact Number: ")
    spouse_name = input("Enter Spouse Name: ")
    number_of_child = input("Enter Number of Children: ")
    salary = input("Enter Salary: ")
    return Employee(empid, name, address, contact_number, spouse_name, number_of_child, salary)

def write_employees_to_file(employees, filename="employees.csv"):
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            
            writer.writerow(["EmpID", "Name", "Address", "Contact Number", "Spouse Name", "Number of Children", "Salary"])
            for emp in employees:
                writer.writerow(emp.to_list())
        print(f"Successfully saved {len(employees)} employees to '{filename}'.")
    except Exception as e:
        print(f"Error writing to file: {e}")

def read_employees_from_file(filename="employees.csv"):
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)   
            employees = list(reader)
            return employees
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return []
    except Exception as e:
        print(f"Error reading from file: {e}")
        return []

def display_employees(employees):
    if not employees:
        print("No employee records found.")
        return
    print("\n--- Employee List ---")
    for emp in employees:
        print(f"ID: {emp[0]}, Name: {emp[1]}, Address: {emp[2]}, Contact: {emp[3]}, Spouse: {emp[4]}, Children: {emp[5]}, Salary: {emp[6]}")

def main():
    employees = []
    while True:
        print("\nEmployee Management Menu:")
        print("1. Add Employee")
        print("2. Save Employees to File")
        print("3. View Employees from File")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            emp = add_employee()
            employees.append(emp)
            print("Employee added.")

        elif choice == '2':
            if employees:
                write_employees_to_file(employees)
            else:
                print("No employees to save. Add employees first.")

        elif choice == '3':
            emps = read_employees_from_file()
            display_employees(emps)

        elif choice == '4':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()

import csv

class Employee:
    def _init_(self, empid, name, address, contact_number, spouse_name, number_of_child, salary):
        self.empid = empid
        self.name = name
        self.address = address
        self.contact_number = contact_number
        self.spouse_name = spouse_name
        self.number_of_child = number_of_child
        self.salary = salary

    def to_list(self):
        return [self.empid, self.name, self.address, self.contact_number, self.spouse_name, self.number_of_child, self.salary]

def add_employee():
    empid = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    address = input("Enter Address: ")
    contact_number = input("Enter Contact Number: ")
    spouse_name = input("Enter Spouse Name: ")
    number_of_child = input("Enter Number of Children: ")
    salary = input("Enter Salary: ")
    return Employee(empid, name, address, contact_number, spouse_name, number_of_child, salary)

def write_employees_to_file(employees, filename="employees.csv"):
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            
            writer.writerow(["EmpID", "Name", "Address", "Contact Number", "Spouse Name", "Number of Children", "Salary"])
            for emp in employees:
                writer.writerow(emp.to_list())
        print(f"Successfully saved {len(employees)} employees to '{filename}'.")
    except Exception as e:
        print(f"Error writing to file: {e}")

def read_employees_from_file(filename="employees.csv"):
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)   
            employees = list(reader)
            return employees
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return []
    except Exception as e:
        print(f"Error reading from file: {e}")
        return []

def display_employees(employees):
    if not employees:
        print("No employee records found.")
        return
    print("\n--- Employee List ---")
    for emp in employees:
        print(f"ID: {emp[0]}, Name: {emp[1]}, Address: {emp[2]}, Contact: {emp[3]}, Spouse: {emp[4]}, Children: {emp[5]}, Salary: {emp[6]}")

def main():
    employees = []
    while True:
        print("\nEmployee Management Menu:")
        print("1. Add Employee")
        print("2. Save Employees to File")
        print("3. View Employees from File")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            emp = add_employee()
            employees.append(emp)
            print("Employee added.")

        elif choice == '2':
            if employees:
                write_employees_to_file(employees)
            else:
                print("No employees to save. Add employees first.")

        elif choice == '3':
            emps = read_employees_from_file()
            display_employees(emps)

        elif choice == '4':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()

# 8. Write a program to implement a basic library book management with the functionalities such as issue the book, return the book and search the book. Use the concept of OOP to create the necessary classes on your own and implement the concept of other OOP features. For the storage of book details, use the file handling along with the exception handling. 
import os

class Book:
    def _init_(self, book_id, title, author, is_issued=False):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = is_issued  # True or False

    def display(self):
        status = "Issued" if self.is_issued else "Available"
        print(f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Status: {status}")

    def to_line(self):
        return f"{self.book_id}|{self.title}|{self.author}|{self.is_issued}\n"

    @staticmethod
    def from_line(line):
        parts = line.strip().split('|')
        book_id = parts[0]
        title = parts[1]
        author = parts[2]
        is_issued = parts[3] == 'True'
        return Book(book_id, title, author, is_issued)


class Library:
    def _init_(self, filename="books.txt"):
        self.filename = filename
        self.books = []
        self.load_books()

    def load_books(self):
        self.books = []
        if not os.path.exists(self.filename):
            return
        try:
            with open(self.filename, 'r') as f:
                for line in f:
                    if line.strip():
                        book = Book.from_line(line)
                        self.books.append(book)
        except Exception as e:
            print(f"Error loading books from file: {e}")

    def save_books(self):
        try:
            with open(self.filename, 'w') as f:
                for book in self.books:
                    f.write(book.to_line())
        except Exception as e:
            print(f"Error saving books to file: {e}")

    def add_book(self, book):
        self.books.append(book)
        self.save_books()
        print(f"Book '{book.title}' added to library.")

    def find_book_by_id(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def issue_book(self, book_id):
        book = self.find_book_by_id(book_id)
        if book:
            if book.is_issued:
                print(f"Book '{book.title}' is already issued.")
            else:
                book.is_issued = True
                self.save_books()
                print(f"Book '{book.title}' has been issued.")
        else:
            print("Book not found.")

    def return_book(self, book_id):
        book = self.find_book_by_id(book_id)
        if book:
            if not book.is_issued:
                print(f"Book '{book.title}' is not issued currently.")
            else:
                book.is_issued = False
                self.save_books()
                print(f"Book '{book.title}' has been returned.")
        else:
            print("Book not found.")

    def search_books(self, search_term):
        found = [book for book in self.books if search_term.lower() in book.title.lower() or search_term.lower() in book.book_id.lower()]
        if not found:
            print("No books found matching your search.")
        else:
            print(f"\nFound {len(found)} book(s):")
            for book in found:
                book.display()

    def display_all_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\n--- Library Books ---")
            for book in self.books:
                book.display()

def main():
    library = Library()

    while True:
        print("\nLibrary Management Menu:")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Search Book")
        print("5. Display All Books")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Book Author: ")
            new_book = Book(book_id, title, author)
            library.add_book(new_book)

        elif choice == '2':
            book_id = input("Enter Book ID to issue: ")
            library.issue_book(book_id)

        elif choice == '3':
            book_id = input("Enter Book ID to return: ")
            library.return_book(book_id)

        elif choice == '4':
            search_term = input("Enter Book Title or ID to search: ")
            library.search_books(search_term)

        elif choice == '5':
            library.display_all_books()

        elif choice == '6':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if _name_ == "_main_":
    main()