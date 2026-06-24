# Project: Student Management System
# Problem Statement

# Create a Student Management System using Python and Object-Oriented Programming (OOP).

# The system should allow the user to:

# Add a new student.
# View all students.
# Search for a student using Student ID.
# Update a student's marks.
# Delete a student record.
# Display the student with the highest marks.
# Exit the application.
# Student Details

# Each student should have:

# Student ID
# Student Name
# Age
# Marks
class Student:
    def __init__(self, student_id, name, age, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.marks = marks

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Marks: {self.marks}"


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        if any(s.student_id == student.student_id for s in self.students):
            print("Student ID already exists.")
            return
        self.students.append(student)
        print("Student added successfully.")

    def view_students(self):
        if not self.students:
            print("No student records found.")
            return
        for student in self.students:
            print(student)

    def search_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                print("Student found:")
                print(student)
                return student
        print("Student not found.")
        return None

    def update_marks(self, student_id, new_marks):
        student = self.search_student(student_id)
        if student:
            student.marks = new_marks
            print("Marks updated successfully.")

    def delete_student(self, student_id):
        for i, student in enumerate(self.students):
            if student.student_id == student_id:
                del self.students[i]
                print("Student deleted successfully.")
                return
        print("Student not found.")

    def highest_marks_student(self):
        if not self.students:
            print("No student records found.")
            return
        top_student = max(self.students, key=lambda s: s.marks)
        print("Student with highest marks:")
        print(top_student)


def main():
    sms = StudentManagementSystem()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add a new student")
        print("2. View all students")
        print("3. Search for a student using Student ID")
        print("4. Update a student's marks")
        print("5. Delete a student record")
        print("6. Display the student with the highest marks")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            age = int(input("Enter Age: "))
            marks = float(input("Enter Marks: "))
            sms.add_student(Student(student_id, name, age, marks))
        elif choice == "2":
            sms.view_students()
        elif choice == "3":
            student_id = input("Enter Student ID to search: ")
            sms.search_student(student_id)
        elif choice == "4":
            student_id = input("Enter Student ID to update marks: ")
            new_marks = float(input("Enter new marks: "))
            sms.update_marks(student_id, new_marks)
        elif choice == "5":
            student_id = input("Enter Student ID to delete: ")
            sms.delete_student(student_id)
        elif choice == "6":
            sms.highest_marks_student()
        elif choice == "7":
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()