import json
#Main Class
class StudentManager:

    #Constructor
    def __init__(self):
        self.data='Students.json'
        try:
            with open(self.data,'r') as file:
                self.students= json.load(file)
        except (FileNotFoundError,json.JSONDecodeError):
            self.students=[]


#Save data to JSON file
    def save_to_json(self):
        with open(self.data,'w') as file:
            json.dump(self.students,file,indent=4)

#Helper
    def validate_name(self,name):
        if not name.replace(" ","").isalpha():
            raise ValueError("Integer and special character not allowed in name .")
        
        if len(name) < 4:
            raise ValueError("Name must be atleast 4 character .")
        
        for student in self.students:
            if name== student["Name"]:
                raise ValueError("Name must be unique .")


#Helper
    def validate_marks(self,marks):
        if not 0 <= marks <=100:
            raise ValueError("Mark must be between 0 - 100 .")


#Helper
    def validate_gpa(self,gpa):
        if not 0 <= gpa <= 4:
            raise ValueError("Gpa must be between 0 - 4")


#Helper
    def empty_list(self):
        if not self.students:
            print("Empty dictionary .")
            return


#Helper display students
    def display(self,student):
        print(f"Name       : {student['Name']}")
        print(f"Marks      : {student['Marks']}")
        print(f"GPA        : {student['GPA']}")
        print()


#Add students
    def add_students(self):
            while True:
                try:
                    name=input("Enter student name : or enter (stop) to exit :").strip().title()
                    if name.lower() == 'stop':
                        break
                    self.validate_name(name)
                except ValueError as e:
                    print("Error :",e)
                    continue

                while True:
                    try:
                        marks=int(input("Enter your marks :"))
                        self.validate_marks(marks)
                        break
                    except ValueError as e:
                        print("Error :",e)
                        continue

                while True:
                    try:
                        GPA=float(input("Enter your gpa :"))
                        self.validate_gpa(GPA)
                        break
                    except ValueError as e:
                        print ("Error :",e)
                        continue

                self.students.append(
                    {
                        "Name" : name,
                        "Marks" : marks,
                        "GPA" : GPA
                    }
                )
                self.save_to_json()
                print("Student add succesfully .\n")


#Update name
    def update_name(self):
        self.empty_list()
        name=input("Enter name to update :").strip().title()
        found=False
        for student in self.students:
            if name == student["Name"]:
                while True:
                    try:
                        new_name=input("Enter new name :")
                        self.validate_name(new_name)
                        found=True
                    except ValueError as e:
                        print("Error :",e)
                        continue
                    else:
                        student["Name"]=new_name
                        self.save_to_json()
                        print("Name update succesfully .")
                        break
        if not found:
            print("Not found .")


#Update GPA
    def update_gpa(self):
        self.empty_list()
        name=input("Enter student name :").strip().title()
        found=False
        for student in self.students:
            if name == student["Name"]:
                while True:
                    try:
                        new_gpa=float(input("Enter new GPA :"))
                        self.validate_gpa(new_gpa)
                    except ValueError as e:
                        print("Error :",e)
                        continue
                    else:
                        student["GPA"]=new_gpa
                        self.save_to_json()
                        print("GPA update succesfully .")
                        found=True
                        break
        if not found:
            print("Not found .")


#Update marks
    def update_marks(self):
        self.empty_list()
        name=input("Enter student name :").strip().title()
        found=False
        for student in self.students:
            if name== student["Name"]:
                while True:
                    try:
                        new_marks=int(input("Enter new marks :"))
                        self.validate_marks(new_marks)
                    except ValueError as e:
                        print("Error :",e)
                        continue
                    else:
                        student["Marks"]=new_marks
                        self.save_to_json()
                        print("Marks update succesfully .")
                        found=True
                        break
        if not found:
            print("Not found .")


#Update main function
    def update_student(self):
        while True:
            print("--------- Update Student -------------")
            print("1. Update Name")
            print("2. Update Marks")
            print("3. Update GPA ")
            print("4. Exit ")
            print("----------------------------------")
            choice=input("Enter your choice :")
            if choice == '1':
                self.update_name()

            elif choice == '2':
                self.update_marks()

            elif choice == '3':
                self.update_gpa()

            elif choice == '4':
                print("Exit .")
                break
            else:
                print("Invalid choice .try again")

#Search students
    def search_students(self):
        self.empty_list()
        name=input("Enter student name to search :").strip().title()
        found=False
        for student in self.students:
            if name == student["Name"]:
                print("------ Student Info ------")
                self.display(student)
                found=True
                break
        if not found:
           print("Not found .")


#Shwo all students
    def show_all_students(self):
        self.empty_list()
        count=0
        for student in self.students:
            count+=1
            print(f"----- Student {count} ------")
            self.display(student)


#Delete students
    def delete_student(self):
        self.empty_list()
        delete=input("Enter student name :").strip().title()
        found=False
        for student in self.students:
            if delete == student["Name"]:
                self.students.remove(student)
                self.save_to_json()
                print("Student delete succesfully .")
                found=True
                return
            
        if not found:
            print("Student not found .")
                


    def top_3_students_by_marks(self):
        self.empty_list()
        result=sorted(
            self.students,key= lambda student : student["Marks"],
            reverse=True
        )
        count=0
        for student in result[:3]:
            count+=1
            print(f"------ position {count} ------")
            self.display(student)

    def total_students(self):
        self.empty_list()
        print("Total students : ",len(self.students))

student=StudentManager()
while True:
    print("------------------ Student Mangment System ---------------------")
    print("1. Add Student ")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete student ")
    print("5. Top 3 studets by marks ")
    print("6. Show all student ")
    print("7. Count of total students")
    print("6. Exit ")
    print("-----------------------------------------------------------------")
    choice=input("Enter your choice :")
    if choice == '1':
        student.add_students()

    elif choice == '2':
        student.search_students()

    elif choice == '3':
        student.update_student()

    elif choice == '4':
        student.delete_student()

    elif choice == '5':
        student.top_3_students_by_marks()

    elif choice == '6':
        student.show_all_students()

    elif choice == '7':
        student.total_students()

    elif choice == '8':
        print("Program ended .")

    else:
        print("Invalid choice : try again !")
        continue

        



