class Student:
    def __init__(self, name, roll_number, Year_of_graduation,College_name):
        self.name = name
        self.roll_number = roll_number
        self.Year_of_graduation = Year_of_graduation
        self.College_name = College_name
class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self):
        name = input("Enter student name: ")
        roll_number = input("Enter student roll number: ")
        Year_of_graduation = input("Enter student Year_of_graduation: ")
        College_name = input("Enter student College_name: ")
        student = Student(name, roll_number, Year_of_graduation, College_name)
        self.students.append(student)
        print(f"Student '{name}' added successfully!")

    def search_student(self):
        roll_number = input("Enter student roll number: ")
        for student in self.students:
            if student.roll_number == roll_number:
                print("Student found:")
                print(f"Name: {student.name}")
                print(f"Roll Number: {student.roll_number}")
                print(f"Year_of_graduation: {student.Year_of_graduation}")
                print(f"College_name: {student.College_name}")
                return
        print(f"Student with roll number '{roll_number}' not found.")

    def remove_student(self):
        roll_number = input("Enter student roll number: ")
        for student in self.students:
            if student.roll_number == roll_number:
                self.students.remove(student)
                print(f"Student with roll number '{roll_number}' removed successfully!")
                return
        print(f"Student with roll number '{roll_number}' not found.")

    def update_student(self):
        roll_number = input("Enter student roll number: ")
        for student in self.students:
            if student.roll_number == roll_number:
                print("Enter new student details:")
                name = input("Name: ")
                Year_of_graduation = input("Year_of_graduation: ")
                College_name = input("College_name: ")
                student.name = name
                student.Year_of_graduation = Year_of_graduation
                student.College_name = College_name
                print(f"Student with roll number '{roll_number}' updated successfully!")
                return
        print(f"Student with roll number '{roll_number}' not found.")

    def display_students(self):
        if not self.students:
            print("No students found.")
            return

        print("Student List:")
        print("--------------")
        for student in self.students:
            print(f"Name: {student.name}")
            print(f"Roll Number: {student.roll_number}")
            print(f"Year_of_graduation: {student.Year_of_graduation}")
            print(f"College_name: {student.College_name}")
            print("--------------")


obj = StudentManagementSystem()

while True:
    print("\nSTUDENT MANAGEMENT SYSTEM")
    print("------------------------")
    print("1. Add Student ")
    print("2. Search Student")
    print("3. Remove Student")
    print("4. Update Student")
    print("5. Display Students")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        obj.add_student()
    elif choice == "2":
        obj.search_student()
    elif choice == "3":
        obj.remove_student()
    elif choice == "4":
        obj.update_student()
    elif choice == "5":
        obj.display_students()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
