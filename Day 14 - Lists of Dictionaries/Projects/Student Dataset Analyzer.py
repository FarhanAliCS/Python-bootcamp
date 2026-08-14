def validate_name(name,students):
    if not name.replace(" ","").isalpha():
        raise ValueError("Integer or special character are not allowed .")
    if len(name) <= 4:
        raise ValueError("Length must be greater then 4 .")

    for student in students:
        if name == student["Name"]:
            raise ValueError("Name already exists .")
def  validate_marks(marks):
    if not 0 <= marks <= 100 :
        raise ValueError("Marks must be between 0 - 100")

def validate_gpa(gpa):
    if not 0<=gpa <= 4 :
        raise ValueError("Gpa must be between 0 - 4")

def details(student):
        print(f"Name         :   {student["Name"]}")
        print(f"Marks         :   {student["Marks"]}")
        print(f"GPA         :   {student["GPA"]}")
        print()
def add_student(students):
    while True:
        try:
            name=input("Enter student name : or enter stop to exist :").strip().title()
            if name.lower() == 'stop':
                break
            validate_name(name,students)
        except ValueError as e:
            print("Error :",e)
            continue

        while True:
            try:
                marks=int(input("Enter marks of student :"))
                validate_marks(marks)
                break
            except ValueError as e:
                print("Error :",e)
                continue

        while True:
            try:
                GPA=float(input("Enter student gpa :"))
                validate_gpa(GPA)
                break
            except ValueError as e:
                print("Error :",e)
                continue

        students.append(
            {
                "Name"   : name,
                "Marks"  : marks,
                "GPA"    : GPA
            }
          )     

def show_all_student(students):
    if not students:
        print("Empty List .")
        return
    count=0
    for student in students:
        count+=1
        print(f"====== Students {count} ======")
        details(student)


def student_above_80_marks(students):
    if not students:
        print("Empty list .")
        return
    for student in students:
        if student["Marks"] > 80 :
            print("==== Student info =====")
            details(student)


def highest_marks(students):
    if not students:
        print("Empty list .")
        return
    highest_marks=float("-inf")
    name=""
    for student in students:
        if student["Marks"] > highest_marks:
            highest_marks=student["Marks"]
            name=student["Name"]

    print("Highest Marks are :",highest_marks)
    print("Student name is :",name)

def lowerst_marks(students):
    if not students:
        print("Empty list .")
        return
    lowest_marks=float("inf")
    name=""
    for student in students:
        if student["Marks"] < lowest_marks:
            lowest_marks=student["Marks"]
            name=student["Name"]

    print("Lowest Marks are :",lowest_marks)
    print("Student name is :",name)

def average_marks(students):
    if not students:
        print("Empty list .")
        return
    total=0
    for student in students:
        total+=student["Marks"]

    average=total/len(students)
    print("Average Marks is :",average)

def average_gpa(students):
    if not students:
        print("Empty list .")
        return
    total=0.0
    name=""
    for student in students:
        total+=student["GPA"]
    average=total/len(students)
    print("Average gpa is :",average)

def top_3_student_by_marks(students):
    if not students:
        print("Empty list .")
        return
    top_students=[]

    remaning_student=students.copy()
    limit=()
    for i in range(3):
        highest_mark=float("-inf")
        name=None
        count=0
        for student in remaning_student:
            if student["Marks"] > highest_mark:
                highest_mark=student["Marks"]
                name=student
        top_students.append(name)
        remaning_student.remove(name)

    for position,student in enumerate(top_students,start=1):
        print(f"position {position} : {student["Name"] , {student["Marks"]}}")

def search_by_name(students):
    if not students:
        print("Empty list .")
        return
    while True:
      try:
        name=input("Enter student name :").strip().lower()
        if not name:
            raise ValueError("Name must not be empty .")
        for student in students:
            if name in student['Name'].lower():
                details(student)
      except ValueError as e:
        print("Error :",e)
        continue
    
    

    
students=[]


while True:
    print("=========== Student Dataset Analyzer ============")
    print("1. Add Students ")
    print("2. Show Students")
    print("3. Students abover 80 marks ")
    print("4. Highest Marks")
    print("5. lowest Marks")
    print("6. Average Marks")
    print("7. Average gpa")
    print("8. Search Students")
    print("9. Top 3 highest students with marks")
    print("10. Exit")
    print("=================================================")

    choice = input("Enter your choice :")

    if choice == '1':
        add_student(students)

    elif choice == '2':
        show_all_student(students)

    elif choice == '3':
        student_above_80_marks(students)

    elif choice == '4':
        highest_marks(students)

    elif choice == '5':
        lowerst_marks(students)

    elif choice == '6':
        average_marks(students)

    elif choice == '7':
        average_gpa(students)

    elif choice == '8':
        search_by_name(students)

    elif choice == '9':
        top_3_student_by_marks(students)

    elif choice == '10':
        print("Program ended .")
        break

    else:
        print("Invalid choice . try again!")
