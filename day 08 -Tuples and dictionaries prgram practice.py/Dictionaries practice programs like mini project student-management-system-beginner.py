# Add new student
def add_student(students):
    name = input("Enter name :")
    roll_no = input("Enter roll no :")
    department = input("Enter department :")
    cgpa = input("Enter cgpa :")

    students['name'] = name
    students['roll_no'] = roll_no
    students['department'] = department
    students['cgpa'] = cgpa

    print("Student added successfully.\n")


# Update student
def Update_data(students):

    if not students:
        print("No student record found.\n")
        return

    print("Available keys:")
    for i in students.keys():
        print(i)

    while True:
        key = input("Enter key to update :")

        if key not in students:
            print("Key does not exist.")
            continue

        if key == 'cgpa':
            value = float(input("Enter value :"))

        elif key == 'roll_no':
            value = input("Enter value :")

        else:
            value = input("Enter value :")

        students[key] = value
        print(key, "updated successfully.\n")
        break


# Delete student
def delete_student(student):

    if not student:
        print("No student record found.\n")
        return

    key = input("Enter key to delete :")

    if key in student:
        del student[key]
        print("Deleted successfully.\n")
    else:
        print("Key does not exist.\n")


# Show student data
def show_data(student):

    if not student:
        print("No student record found.\n")
        return

    print("\n======= Student Data =======")
    for key, value in student.items():
        print(f"{key:13} : {value}")
    print()


# Search student
def search_for_student(student):

    if not student:
        print("No student record found.\n")
        return

    value = input("Enter value to search : ")

    if value in map(str, student.values()):
        print("\nValue found.")
        print(student)
    else:
        print("Value not found.")


# Count student
def count_of_student(student):

    if student:
        print("Count of student is : 1")
    else:
        print("Count of student is : 0")


# ==============================
#          MAIN MENU
# ==============================

students = {}

while True:

    print("================ Task Menu =====================")
    print("1. Add student")
    print("2. Update student")
    print("3. Delete student")
    print("4. Search for student")
    print("5. Count of student")
    print("6. Show all student")
    print("7. Exit")
    print("================================================")

    choice = input("Enter your choice : ")

    if choice == '1':
        add_student(students)

    elif choice == '2':
        Update_data(students)

    elif choice == '3':
        delete_student(students)

    elif choice == '4':
        search_for_student(students)

    elif choice == '5':
        count_of_student(students)

    elif choice == '6':
        show_data(students)

    elif choice == '7':
        print("Program ended.")
        break

    else:
        print("Invalid choice.\n")