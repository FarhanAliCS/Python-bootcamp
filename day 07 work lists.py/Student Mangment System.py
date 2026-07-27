#Add student
def add_student(student_names,father_names,ages):
    while True:
        name=input(" Enter name of student or enter 'stop' to exit :")
        if name.lower()=='stop':
            break
        if name in student_names:
             print("name already exists")
             continue
       
        father_name=input("Enter father name :")
        while True:
             age=input("Enter student age :") 
             if age.isdigit():
                 break
             else:
                 print("Invalid age format only digit are allowed .")       
        student_names.append(name)
        father_names.append(father_name)
        ages.append(age)
        print("Contact add succesfully .\n")
        

#search for student
def search_student (student_names,father_names,ages):
    search_name=input("Enter your search :")
    for i in range(len(student_names)):
        if student_names[i].lower()==search_name.lower():
            print(student_names[i],":",father_names[i],":",ages[i])
    if search_name not in student_names:
        print("Contact does not exit .") 

#display all student
def student_display(student_names,father_names,ages):
    print("======== Student list =======")
    if not student_names:
        print("list is empty")
    for i in range(len(student_names)):
        print(student_names[i],":",father_names[i],":",ages[i])

#Delete speciefic contact 
def delete_contact(names,father_names,ages):
    name=input("Enter student name to delete :")
    if not names:
        print("List is already empty")
    if name not in names:
        print("Name does not exist ")
        return
    while True:
         for i in range(len(names)):
             if names[i].lower()==name:
                 ask=input("Are you sure you want to delete y/n :")
                 if ask.lower()=='y':
                     names.pop(i)
                     father_names.pop(i)
                     ages.pop(i)
                     print("delete succesfully")
         break


    #+===============================================      
    #+              MAIN MENUE
    #+===============================================
names=[]
father_names=[]
ages=[]
while True:
    print("================== MENUE =======================")
    print("1. Add student ")
    print("2. Search student data")
    print("3. Show all student data ")
    print("4. Delete student ")
    print("5. Exit ")
    print("+====+==============+==============+===========+\n")
    choice=input("Enter your choice :")
    print("\n")
    if choice == '1':
        add_student(names,father_names,ages)

    elif choice == '2':
        search_student(names,father_names,ages)

    elif choice == '3':
        student_display(names,father_names,ages)

    elif choice == '4':
        delete_contact(names,father_names,ages)

    elif choice == '5':
        print("program exit ....")
        break
    else:
        print("Invalid choice ")
        
         