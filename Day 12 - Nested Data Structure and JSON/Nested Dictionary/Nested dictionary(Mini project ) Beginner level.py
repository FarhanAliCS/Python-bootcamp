class Students:
    def __init__(self):
        self.students={}
    def add_students(self):
        while True:
            try:
                name=input("Enter  name : or enter (stop) to exist :").strip().title()
                if name.lower()=='stop':
                    break
                if not name.replace(" ","").isalpha():
                    raise ValueError("Only alphabet allowed in name . Try again !")
                if name in self.students:
                    print("Name already exists .")
                    continue
            except ValueError as e :
                print("Error :",e)
                continue
            while True:
                try:
                    age=int(input("Enter age  :"))
                    if 5 <= age <= 30:
                        break
                    else:
                        raise ValueError("Age must be between 5 - 30 .")
                except ValueError as e:
                    print("Error :",e)
                    continue
            while True:
                try:
                    semester=int(input("Enter semester :"))
                    if 1<= semester <=8:
                        break
                    else:
                        raise ValueError("semester must be a digit. and between 1 - 8 .")
                    
                except ValueError as e:
                    print("Error :",e)
                    continue
            while True:
                try:
                    marks=int(input("Enter student marks :"))
                    if 0 <= marks <= 100:
                        break
                    else:
                        raise ValueError("Marks must be between 0 and 100 .")
                except ValueError as e:
                    print("Error :",e)
            self.students[name]={
                "Age" : age,
                "Semester" : semester,
                "Marks" : marks
                }
            print("Student add succesfully .\n")

    def show_students(self):
        if not self.students:
            print("Empty dictionary .")
            return
        print("===========: Student Details :=============")
        for name, details in self.students.items():
             print(f"\nName      : {name}")
             print(f"Age       : {details['Age']}")
             print(f"Semester  : {details['Semester']}")
             print(f"Marks     : {details['Marks']}")

    def search_student(self):
        if not self.students:
            print("Empt dectionary .")
            return
        search=input("Enter name to search :").strip().title()
        found=False
        if search not in self.students:
            print("Not found .")
            return
        details=self.students[search]
        print(f"\nName      : {search}")
        print(f"Age       : {details['Age']}")
        print(f"Semester  : {details['Semester']}")
        print(f"Marks     : {details['Marks']}")

    def delete_student(self):
        if not self.students:
            print("Empty dictionary .")
            return
        
        delete=input("Enter name to delete :").strip().title()

        if delete not in self.students:
            print("Student no found .")
            return
        del self.students[delete]
        print("Student delete succesfully .\n")

    def update_marks(self):
        if not self.students:
            print("Empty dictionary")
            return
        update=input("Enter name of student :").strip().title()
        if not update in self.students:
            print("Student not found .")
            return
        while True:
            try:  
              new_marks=int(input("Enter new marks :"))
              if 0 <= new_marks <= 100:
                  break
              else:
                  raise ValueError("Marks must be between 1 to 100 .")
            except ValueError as e:
              print("Error :",e)
              continue
        self.students[update]['Marks']=new_marks
        print("Marks update succesfully .")
            


                          #=======================#
                          #          MENU         #
                          #=======================#
                          
  
students_info=Students()
while True:
    print("================: Student Mangment System :===============")  
    print("1. Add Student ")
    print("2. Show Student")
    print("3. Search Student")
    print("4. Delete Student ")
    print("5. update marks ")
    print("6. Exit ")
    print("=========================")
    choice=input("Enter your choice :")
    if choice == '1':
        students_info.add_students()
    elif choice == '2':
        students_info.show_students()
    elif choice == '3':
        students_info.search_student()
    elif choice == '4':
        students_info.delete_student()
    elif choice =='5':
        students_info.update_marks()
    elif choice == '6':
        print("Program ended .")
        break
    else:
        print("Invalid input .")
    print()
                              




            

            
                