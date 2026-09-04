from dataclasses import dataclass

@dataclass
class Student:
    name:str
    age: int
    marks: float

    def is_passed(self)->bool:
        return self.marks >= 50


students: list[Student]=[]

def add_student() -> None:
    name=input("Enter student name :")
    age=int(input("Enter student age :"))
    marks=float(input("Enter studet marks :"))
    student=Student(name,age,marks)
    students.append(student)
    print("Student add succesfully ")

def show_students() -> None:
    if not students:
        print("Empty student list .")
        return
    count=0
    for student in students:
        count+=1
        print(f"----- Student {count} -----")
        print(student)
        print()

def find_student():
    if not students:
        print("Empty list ")
        return
    
    search_name=input("Enter student name to search :")
    found=False
    for student in students:
        if student.name == search_name:
            print(student)
            found=True
    if not found:
        print("Not found .")

def passed_students() -> None:
    if not students:
        print("Empty student list .")
        return
    
    print("===== Pass Students =====")
    for student in students:
        if student.is_passed():
            
            print(student)

def show_highest_marks() -> None:
    if not students:
        print("Empty list .")
        return
    highest_marks=float("-inf")
    student_name=""
    for student in students:
        if student.marks > highest_marks:
            highest_marks=student.marks
            student_name=student.name
    print("Student name is :",student_name)
    print("Highest Marks :",highest_marks)

def average_marks() -> None:
    if not students:
        print("Empty studnet list .")
        return
    total=0
    for student in students:
        total+=student.marks

    average=total/len(students)

    print("Average Marks :",average)



while True:
    print("------------ Student Managment Systme ------------")
    print("1. Add Student ")
    print("2. Show All Students ")
    print("3. Find Student ")
    print("4. Show Passed Student ")
    print("5. Show Highest Marks ")
    print("6. Show Average Marks ")
    print("7. Exit ")
    print("--------------------------------------------------")
    choice=input("Enter your choice :")
    if choice == '1':
        add_student()

    elif choice == '2':
        show_students()

    elif choice =='3':
        find_student()

    elif choice == '4':
        passed_students()

    elif choice == '5':
        show_highest_marks()

    elif choice == '6':
        average_marks()

    elif choice == '7':
        print("Program ended .")
        break
    else:
        print("Invalid choice . try again ! ")







