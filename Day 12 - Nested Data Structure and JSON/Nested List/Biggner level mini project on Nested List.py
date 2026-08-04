class Studentmarks:
    #Default constructor
    def __init__(self):
        self.students = [
    ["Ali", 90, 93, 86],
    ["Ahmed", 45, 67, 78],
    ["Sara", 78, 89, 54]
                        ]
#All student display
    def show_details(self):
        count=0
        for row in self.students:
            count +=1
            print("student",count,row)
        print()
#Search for a student on name 
    def search_student(self):
        while True:
            
            name=input("Enter student name :")
            found=False
            for i in range(len(self.students)):
                if name.lower()== self.students[i][0].lower():
                    print(self.students[i])
                    found=True
                    break
            else:
                if not found:
                   print("Not found .")
            break
#highest marks in all student in one stubject and his/her name .
    def highest_marks(self):
        highest_score=self.students[0][1]
        name=self.students[0][0]
        for row in self.students:
            for data in row[1:]:
                if data > highest_score:
                    highest_score=data
                    name=row[0]           
        print(f"Name is :{name}.Highest marks is :{highest_score} .")

#Highest scoring student and marks
    def highest_scoring_student(self):

        highest=sum(self.students[0][1:])
        student_name=self.students[0][0]
        for row in self.students:
            current=sum(row[1:])
            if current > highest :
                highest = current
                student_name=row[0]
        print(f"Name is : {student_name}. Marks is {highest} .")

    def count_Of_all_student(self):
        count=0
        for row in self.students:
            count+=1
        print("Total student are :",count)
#Average marks and Pass/Fail
    def average_marks(self):
       for row in self.students:
           total=0
           count=0
           for mark in row[1:]:
               total+=mark
               count+=1
           average=total/count
           status=""
           if average >= 50:
               status ="Pass"
           else:
               status="Fail"
           print(f"{row[0]} average marks is : {average:.2f}. {status}")
            
            
student=Studentmarks()
#===============
#   MAIN
#===============

while True:
    print("\n======== MAIN MENU ==========")
    print("1. Show all marks ")
    print("2. Show one student marks ")
    print("3. Print highes of the marks ")
    print("4. Highest scoring student")
    print("5. Count of all students")
    print("6. Average marks off all students")
    print("7. Exit")
    print("==============================")
    choice=input("Enter your choice :")
    print("\n====================================")
    if choice == '1':
        student.show_details()
    elif choice == '2':
       student.search_student()
    elif choice == '3':
       student.highest_marks()
    elif choice == '4':
       student.highest_scoring_student()
    elif choice == '5':
          student.count_Of_all_student()
    elif choice == '6':
        student.average_marks()
    elif choice =='7':
        print("Program ended .")
        break
    else:
        print("Invalid choice .")
   


        
    
