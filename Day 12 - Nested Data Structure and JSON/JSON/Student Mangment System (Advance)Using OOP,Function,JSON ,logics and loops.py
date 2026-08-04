import json
class Student:
    def __init__(self):
        self.data="student_data.json"
        try:
          with open(self.data,'r') as file:
            self.students=json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
               self.students={}

    def save_to_file(self):
       with open(self.data,'w') as file:
          json.dump(self.students,file,indent=4)

    def add_students(self):
       while True:
          try:
             name =input("Enter student name : or enter (stop) to exit :").strip().title()
             if name.lower()== 'stop':
                break
             if not name.replace(" ","").isalpha():
                raise ValueError ("Only alphabet allowed in name.")
             if name in self.students:
                print("Name already exists .")
                continue
          except ValueError as e :
             print("Error :",e)
             continue
          while True:
             try:
                age= int(input("Enter student age :"))
                if 17 <= age <= 30:
                   break
                else:
                   raise ValueError ("Age must be between 17 and 30 .")
             except ValueError as e:
                print("Error :",e)
                continue
          while True:
             try:
                department=input("Enter student department name :").strip().title()
                if not department.replace(" ","").isalpha():
                   raise ValueError("depatemnt name must be alphabet .")
             except ValueError as e:
                print("Error :",e)
                continue
             else:
                break
          while True:
             try:
                semester=int(input("Enter student semester :"))
                if 1 <= semester <= 8:
                   break
                else:
                   raise ValueError ("semester must be between 1 to 8")
             except ValueError as e:
                print("Error :",e)
                continue
          while True:
             try:
                marks=int(input("Enter student marks :"))
                if 0 <= marks <= 100:
                   break
                else:
                   raise ValueError ("Marks must be between 0 to 100 .")
             except ValueError as e:
                print("Error :",e)
                continue
          self.students[name]={
             "Age":age,
             "Department" : department,
             "Semester" : semester,
             "Marks" : marks
          }
          self.save_to_file()
          print('student add succesfully .')
          print()

    def search_student(self):
       if not self.students:
          print("Empty dictonary .")
          return
       while True:
          try:
             search=input("Enter student name to search :").strip().title()
             if not search.replace(" ","").isalpha():
                raise ValueError("Only alphabet allowed in name .")
          except ValueError as e:
             print("Error :",e)
             continue
          else:
             if search not in self.students:
                print("Name not found .")
                break
             print("\n======== Student details ==========")
             details=self.students[search]
             print(f"Name          :     {search}")
             print(f"Age           :     {details["Age"]}")
             print(f"Department    :     {details["Department"]}")
             print(f"Semester      :     {details["Semester"]}")
             print(f"Marks         :     {details["Marks"]}")
             print()
             break
          

    def show_students(self):
       if not self.students:
          print("Empty dictionary .")
          return
       count=0
       for name,details in self.students.items():
            count+=1
            print(f"====== Student {count} ======== ")
            print(f"\nName          :     {name}")
            print(f"Age           :     {details["Age"]}")
            print(f"Department    :     {details["Department"]}")
            print(f"Semester      :     {details["Semester"]}")
            print(f"Marks         :     {details["Marks"]}")

    def delete_student(self):
       if not self.students:
          print("Empty dictionary .")
          return
       while True:
          try:
             delete=input("Enter name to delete a student :").strip().title()
             if not delete.replace(" ","").isalpha():
                raise ValueError("only string allowed in name .")
          except ValueError as e:
             print("Error :",e)
             continue
          if delete not in self.students:
             print("Student not found .")
             break
          del self.students[delete]
          self.save_to_file()
          print("delete succesfully")
          break

    def update_marks(self):
       if not self.students:
          print("Empty dictionary .")
          return
       while True:
          try:
             name=input("Enter student name :").strip().title()
             if not name.replace(" ","").isalpha():
                raise ValueError("Only alphabet allowed .")
          except ValueError as e :
             print("Error :",e)
             continue
          if not name in self.students:
             print("student not found .")
             break
          while True:
             try:
                new_marks=int (input("Enter new marks :"))
                if 0 <= new_marks <= 100:
                    break
                else:
                   raise ValueError("Marks must be between 0 and 100 .")
             except ValueError as e:
                print("Error :",e)
                continue
          self.students[name]["Marks"]=new_marks
          self.save_to_file()
          print("Marks update succesfully .")
          break

    def total_students(self):
       if not self.students:
          print("Empty dectionary")
          return
       count=0
       for key in self.students:
          count+=1
       print("Total students are ",count)

    def highest_marks(self):
       if not self.students:
          print("Empty dictionary .")
          return
       mix_marks=-1
       student_name=""
       for name ,details in self.students.items():
          if details["Marks"] > mix_marks:
             mix_marks=details["Marks"]
             student_name=name
       print(f"Student name is {student_name} marks is {mix_marks}")

    def lowest_marks(self):
       if not self.students:
          print("Empty dictionary .")
          return
       min_marks=102
       student_name=''
       for name , details in self.students.items():
          if details["Marks"] < min_marks:
             min_marks=details["Marks"] 
             student_name=name
       print(f"Student name is {student_name} marks is {min_marks} .")
          
#==============#
#    MAIN      #
#==============#

studentinfo=Student()
while True:
   print("=========: STUDENT MANAGMENT SYSTEM :==========")
   print("1. Add Student ")
   print("2. Show Student")
   print("3. Search Student ")
   print("4. Delete Student ")
   print("5. Update Marks ")
   print("6. Total Students ")  
   print("7. Highest Marks")   
   print("8. Lowest Marks")
   print("9. Exit ")
   print("===============================================")
   choice=input("Enter your choice :")
   if choice == "1":
      studentinfo.add_students()
   elif choice == '2':
      studentinfo.show_students()
   elif choice == '3':
      studentinfo.search_student()
   elif choice == '4':
      studentinfo.delete_student()
   elif choice == '5':
      studentinfo.update_marks()
   elif choice == '6':
      studentinfo.total_students()
   elif choice == '7':
      studentinfo.highest_marks()
   elif choice == '8':
      studentinfo.lowest_marks()
   elif choice == '9':
      print("Program Ended .")
      break
   else:
      print("Invalid input . try again")    
             
       
        
        
        