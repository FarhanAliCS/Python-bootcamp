

class Student:

    def __init__(self):
        self.name = ""
        self.age = 0
        self.department = ""
        self.cgpa = 0.0

    # Add Student
    def addstudent(self):
        self.name = input("Enter name : ")

        while True:
            age = input("Enter age : ")
            if age.isdigit():
                self.age = int(age)
                break
            print("Age must be an integer.")

        self.department = input("Enter department : ")

        while True:
            try:
                self.cgpa = float(input("Enter CGPA : "))
                if 0 <= self.cgpa <= 4:
                   break
                print("CGPA must be between 0 and 4.")
            except ValueError:
                print("Invalid CGPA.")

        print("Student added successfully.\n")

    # Display Student
    def display(self):

        if self.name == "":
            print("No student data available.\n")
            return

        print("\n======= Student Info =======\n")
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Department :", self.department)
        print("CGPA       :", self.cgpa)
        print()


# =============================
#           MAIN
# =============================

student1 = Student()

while True:

    print("========== MENU ==========")
    print("1. Add Student")
    print("2. Display Student")
    print("3. Exit")
    print("==========================")

    choice = input("Enter your choice : ")

    if choice == "1":
        student1.addstudent()

    elif choice == "2":
        student1.display()

    elif choice == "3":
        print("Program ended.")
        break

    else:
        print("Invalid choice.\n")
    
