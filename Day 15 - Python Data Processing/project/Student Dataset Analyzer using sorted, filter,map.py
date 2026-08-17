def validate_name(name):
    if not name.replace(" ","").isalpha():
        raise ValueError("Integer and special character not allowed in name .")
    if len(name) < 4:
        raise ValueError("Name must be atleast 4 character .")
    for student in Students:
        if name== student["Name"]:
            raise ValueError("Name must be unique .")

def validate_marks(marks):
    if not 0 <= marks <=100:
        raise ValueError("Mark must be between 0 - 100 .")

def validate_gpa(gpa):
    if not 0 <= gpa <= 4:
        raise ValueError("Gpa must be between 0 - 4")

def empty_list(Students):
    if not Students:
        print("Empty dictionary .")
        return

def display(student):
    print(f"Name       : {student['Name']}")
    print(f"Marks      : {student['Marks']}")
    print(f"GPA        : {student['GPA']}")

def add_student(Students):
    while True:
        try:
            name=input("Enter student name : or enter (stop) to exit :").strip().title()
            if name.lower() == 'stop':
                break
            validate_name(name)
        except ValueError as e:
            print("Error :",e)
            continue

        while True:
            try:
                marks=int(input("Enter your marks :"))
                validate_marks(marks)
                break
            except ValueError as e:
                print("Error :",e)
                continue

        while True:
            try:
                GPA=float(input("Enter your gpa :"))
                validate_gpa(GPA)
                break
            except ValueError as e:
                print ("Error :",e)
                continue

        Students.append(
            {
                "Name" : name,
                "Marks" : marks,
                "GPA" : GPA
            }
        )
        print("Student add succesfully .\n")

def show_students(Students):
    empty_list(Students)
    count=0
    for student in Students:
        count+=1
        print(f"----- Student  {count} -----")
        display(student)
        print()

def search_student(Students):
    empty_list(Students)
    while True:
        try:
            name=input("Enter student name to search :").strip().title()
        except ValueError as e:
            print("Error",e)
            continue
        else:
            found=False
            for student in Students:
                if name == student["Name"]:
                   display(student)
                   found=True
                   return

            if not found:
                print("Not found .")
                break

def highest_marks(Students):
    empty_list(Students)
    highest=sorted(
        Students, key=lambda student:student["Marks"],
        reverse=True
    )

    print(highest[0])

def lowest_marks(Students):
    empty_list(Students)
    lowest=sorted(
        Students,key=lambda student:student["Marks"]
    )
    for student in lowest[0:1]:
        display(student)

def student_above_80(Student):
    empty_list(Students)
    data=filter(
       lambda student:student["Marks"] > 80,Students
    )
    for student in data:
        display(student)
        print()

def top_3_student(Student):
    empty_list(Students)
    result=sorted(
        Students,key=lambda student:student["Marks"],
        reverse=True
    )
    count=0
    for student in result[:3]:
       count+=1
       print(f"------ Position {count} -------")
       display(student)
       print()


def student_names(Students):
    empty_list(Students)
    name=map(
        lambda student:student["Name"],Students
    )
    for n in name:
      print(n)

def student_marks(Students):
    empty_list(Students)
    marks=map(
        lambda student : student["Marks"],Students
    )
    for m in marks:
        print(m)

def student_name_marks_above_80(Students):
    empty_list(Students)
    data=filter(
        lambda student: student["Marks"] > 80 ,Students
    )
    name=map(
        lambda student:student["Name"],data
    )
    for n in name:
        print("Name :",n)


Students=[
    {"Name": "Farhan", "Marks": 85,"GPA" : 3.2},
    {"Name": "Ahmed", "Marks": 70,"GPA" : 3.6},
    {"Name": "Ashraf", "Marks": 90,"GPA" : 3.1},
    {"Name": "Ali", "Marks": 60,"GPA" : 2.2}
]

while True:
    print("========== Student Data Analyzer ===============")
    print("1. Add student")
    print("2. Show student ")
    print("3. Search student ")
    print("4. Highest marks ")
    print("5. Lowest marks ")
    print("6. Student above 80 ")
    print("7. Top 3 student")
    print("8. Student name marks above 80")
    print("9. All student name ")
    print("10. All student marks ")
    print("========================================")
    choice =input("Enter your choice :")

    if choice == '1':
        add_student(Students)

    elif choice == '2':
        show_students(Students)

    elif choice == '3':
        search_student(Students)

    elif choice == '4':
        highest_marks(Students)

    elif choice == '5':
        lowest_marks(Students)

    elif choice == '6':
        student_above_80(Students)

    elif choice == '7':
        top_3_student(Students)

    elif choice == '8':
        student_name_marks_above_80(Students)

    elif choice == '9':
        student_names(Students)

    elif choice == '10':
        student_marks(Students)

    elif choice == '11':
        print("Program ended .")
        break

    else:
        print("Invalid choice .")
    