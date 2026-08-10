class Student:
    def __init__(self):
        self.students={}
    #Helper
    def validate_name(self,name):
        if not name.replace(" ","").isalpha():
            raise ValueError("digits are special character not allowed in name .")
        
        if len(name) < 4:
            raise ValueError("Name must be greater then 4")
        
    def validate_marks(self,marks):
        if not 0 <= marks <= 100 :
            raise ValueError("Marks must be between 0 - 100 .")
    def validate_gpa(self,gpa):
        if not 0 <= gpa <= 4 :
            raise ValueError("Gpa must be between 0 and 4 .")

    def display(self,name,details):
        print(f"Name    : {name}")
        print(f"Marks   : {details["Marks"]}")
        print(f"GPA     :  {details["GPA"]}")
        print()
        
            
    def add_student(self):
        while True:
            try:
                name=(input("Enter your name : or enter (stop) to exit :")).strip().title()
                if name.lower() == "stop":
                    break
                self.validate_name(name)
            except ValueError as e:
                print("Error :",e)
                continue

            while True:
                try:
                    marks=int(input("Enter student marks ."))
                    self.validate_marks(marks)
                    break
                except ValueError as e:
                    print("Error :",e)
                    continue

            while True :
                    try:
                        gpa=float(input("Enter student gpa :"))
                        self.validate_gpa(gpa)
                        break
                    except ValueError as e:
                        print("Error :",e)
                        continue
            self.students[name]={
                "Marks" : marks,
                "GPA"   : gpa
            }
            
    def search_student(self):
        if not self.students:
            print("Empty student dictionart .")
            return
        while True:
            search_name=input("Enter student name to search :").strip().title()
            found=False
            for name,details in self.students.items():
                if search_name == name:
                    self.display(name,details)
                    found=True
                    break
            if not found:
                print("Student not found .")
                break


    def show_all_student(self):
        if not self.students:
            print("No student found .")
            return
        count=0
        for name,details in self.students.items():
            count+=1
            print(f"===== Student {count+1} ==== ")
            self.display(name,details)

    def highest_marks(self):
        if not self.students:
            print("No student found .")
            return
        high_marks=float("-inf")
        student_name=""
        for name,details in self.students.items():
            if details["Marks"] >high_marks:
                high_marks=details["Marks"]
                student_name=name

        print("Highest Marks are :",high_marks)
        print("Student Name are :",student_name)

    def lowerst_marks(self):
        if not self.students:
            print("No student found .")
            return
        lowest_marks=float("inf")
        student_name=""
        for name,details in self.students.items():
            if details["Marks"] < lowest_marks:
                lowest_marks=details["Marks"]
                student_name=name

        print("Highest Marks are :",lowest_marks)
        print("Student Name are :",student_name)

    def average_marks(self):
        if not self.students:
            print("No student found .")
            return
        sum=0
        count=0
        for name ,details in self.students.items():
            sum+=details["Marks"]
            count+=1

            average=sum/count

        print("Average marks of all students are :",average)




student_info=Student()
while True:
    print("========== Studnet Result Analyzer ==============")
    print("1. Add Student ")
    print("2. Search Studnt")
    print("3. Highest Marks")
    print("4. Lowest Marks ")
    print("5. Average Marks ")
    print("6. Exit ")
    print("==================================================")

    choice = input("Enter your choice :")

    if choice == '1':
        student_info.add_student()

    if choice == '2':
        student_info.search_student()

    elif choice == '3':
        student_info.highest_marks()

    elif choice == '4':
        student_info.lowerst_marks()

    elif choice == '5':
        student_info.average_marks()

    elif choice == '6':
        print("Program ended .")
        break
    else:
        print("Invalid choice . try again !\n")




