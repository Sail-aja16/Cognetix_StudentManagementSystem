import csv
import os

FILE_NAME = "students.csv"

def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Course", "Email"])

def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    email = input("Enter Email: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([sid, name, course, email])

    print("Student added successfully!")

def view_students():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def search_student():
    sid = input("Enter Student ID to search: ")

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == sid:
                print("Student Found:", row)
                return

    print("Student not found")

def delete_student():
    sid = input("Enter Student ID to delete: ")

    rows = []
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != sid:
                rows.append(row)

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("Student deleted")

initialize_file()

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        break
    else:
        print("Invalid choice")
