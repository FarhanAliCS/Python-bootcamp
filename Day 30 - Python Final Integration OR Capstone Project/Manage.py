from Student import Student,students
from colorama import Fore,init
from dataclasses import asdict
from validate_function import (
    validate_name,
    validate_age,
    validate_semester,
    validate_department,
    validate_marks,
    display_student_info
)
import json
import logging
init(autoreset=True)

file = logging.FileHandler("Student.log")
terminal = logging.StreamHandler()

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file.setFormatter(formatter)

file.setLevel(logging.DEBUG)
terminal.setLevel(logging.INFO)

logging.basicConfig(handlers=[file, terminal], level=logging.DEBUG)
logger = logging.getLogger(__name__)



class StudentManager:
    student_file = "students.json"

    def __init__(self):
        try:
            with open(self.student_file, "r") as file:
               self.data=json.load(file)
               students.extend(Student(**item)
                for item in self.data)

        except FileNotFoundError:
            logger.warning(Fore.RED+"JSON file not found, continuing with empty student list.")

        except json.JSONDecodeError:
            logger.warning(Fore.RED+"JSON is empty or contains invalid data.")

    def validate_roll_no(self,roll_no):

            if not len(roll_no) == 4:
               logger.debug(Fore.RED+"Len must be 4 character ")
               raise ValueError("Roll NO must be atlease 4 digit .")
            
            for student in students:
               if student.roll_no == roll_no:
                   logger.debug(Fore.RED+"Roll No already exist .")
                   raise ValueError(f"Roll No {roll_no} already exist please enter another Roll No .")
                   
            





  ################### -------: Save Data To Fle :-------- #####################

    def save_to_file(self):
        data=[asdict(student) for student in students]
        try:
            with open(self.student_file, "w") as file:
                json.dump(data, file, indent=4)

            logger.info("Data saved to file successfully.")

        except OSError:
            logger.exception(Fore.RED+"Failed to save data to student file.")




 ################## -------: For Adding New Student :------ #######################           

    def add_student(self):
        while True:
            try:
                name = input(
                    "Enter student name or enter (stop) to exit: "
                ).strip().title()

                if name.lower() == "stop":
                    logger.info(Fore.GREEN+"Student adding stopped successfully.")
                    break

                validate_name(name)

            except ValueError as e:
                print("Error:", e)
                continue

            while True:
                try:
                    roll_no = input("Enter student Roll No: ")
                    self.validate_roll_no(roll_no)
                    break
                except ValueError as e:
                    print("Error:", e)
                    continue

            while True:
                try:
                    age = int(input("Enter student age: "))
                    validate_age(age)
                    break
                except ValueError as e:
                    print("Error:", e)
                    continue


            while True:
                try:
                    semester = int(input("Enter student semester: "))
                    validate_semester(semester)
                    break
                except ValueError as e:
                    print("Error:", e)
                    continue

            while True:
                try:
                    department = input(
                        "Enter student department: "
                    ).strip().title()

                    validate_department(department)
                    break

                except ValueError as e:
                    print("Error:", e)
                    continue

            ### Validate Subject Marks :-------######
            while True:
                try:
                    software_engineering=float(input("Enter marks of Software Engineering :"))
                    validate_marks(software_engineering)
                    break
                except ValueError as e:
                    print("Error :",e)
                    continue

            while True:
                try:
                    artificial_intaligence=float(input("Enter marks of Artificial Intelligence :"))
                    validate_marks(artificial_intaligence)
                    break
                except ValueError as e:
                    print("Error :",e)
                    continue

            while True:
                try:
                    information_secuity=float(input("Enter marks of  Information Secuity :"))
                    validate_marks(information_secuity)
                    break
                except ValueError as e:
                    print("Error :",e)
                    continue

            while True:
                try:
                    computer_architecture=float(input("Enter marks of Computer Architecture And Organization :"))
                    validate_marks(computer_architecture)
                    break
                except ValueError as e:
                    print("Error :",e)
                    continue

            while True:
                try:
                    probability_and_statistics=float(input("Enter marks of Probability And Statistics :"))
                    validate_marks(probability_and_statistics)
                    break
                except ValueError as e:
                    print("Error :",e)
                    continue

            while True:
                try:
                    theory_of_atomata=float(input("Enter marks of Theory of Atomata :"))
                    validate_marks(theory_of_atomata)
                    break
                except ValueError as e:
                    print("Error :",e)
                    continue

            while True:
                try:
                    Teaching_of_holy_quran=float(input("Enter marks of Teaching Of Holy Quran :"))
                    validate_marks(Teaching_of_holy_quran)
                    break
                except ValueError as e:
                    print("Error :",e)
                    continue


            student=Student(
                name,
                roll_no,
                age,
                semester,
                department,
                subjects={"Software Engineering":software_engineering,
                          "Artificial Intelligence" : artificial_intaligence,
                          "Information Secuity" : information_secuity,
                          "Computer Architecture And Organization":computer_architecture,
                          "Probability And Statistics":probability_and_statistics,
                          "Theory of Atomata":theory_of_atomata,
                          "Teaching Of Holy Quran":Teaching_of_holy_quran
                }

            )
            students.append(student)
            logger.info(Fore.GREEN+"Student Add Succesfully ."+Fore.RESET)
            

            self.save_to_file()

    
        



############ --------------: For Displaying All Student Info :------------ ############

    def show_students(self):
        if not students:
            logger.warning(Fore.RED+"No students added to list.")
            logger.info(Fore.GREEN+"Student.json is empty .")
            return

        count = 0

        for student in students:
            count += 1
            print(f"========= {count} Student Info ============")
            display_student_info(student)





########### ------: Search For Student :---------############
    def search_student(self):
        if not students:
            logger.warning(Fore.RED+"Student List is Empty ."+Fore.RESET)
            return
        
        while True:
            
            logger.info(Fore.GREEN+"Enter Roll No Or Name to search Student .")
            search=input("Enter Student Roll No or Enter name  :").strip().lower()
               
        
            found=False
            for student in students:
                if search == student.roll_no.lower() or search in student.name.lower():
                    found=True
                    print("---------------- Student Info --------------")
                    display_student_info(student)

            if not found:
                logger.info(Fore.GREEN+"Student Not Found .")

            print()
            again=input("Are You want to search another student . (Y/N) :")
            if not again.lower() == "y":
                logger.info(Fore.GREEN+"Operation exit .")
                return



################ --------: Delete Student :------------ ###############
#It Delete One student at a time .

    def delete_student(self):
        if not students:
            logger.warning(Fore.RED+"Student List is Empty .")
            return
        
        while True:
            logger.info(Fore.GREEN+"Enter student Name OR Enter Student Roll No to delete Student .\n")
            delete=input("Enter Student Roll No  OR Enter Name to Delete Student :")

            found=False
            for student in students:
                if delete == student.roll_no or delete == student.name:

                    conform=input("Are you sure (y/n)")
                    if not conform.lower() =='y':
                        return

                    students.remove(student)
                    logger.info(Fore.GREEN+"Student delete succesfully .")

                    self.save_to_file()
                    found=True
                    

            if not found:
                logger.info(Fore.GREEN+"Student not found .")

            print()
            again=input("Are You want to delete another student . (Y/N) :")
            if not again.lower() == "y":
                logger.info(Fore.GREEN+"Operation exit .")
                return






# ############################# -----------: Update Student :-----------#########################################

#          ##### ------: Update Name :----------####
    def validate_roll_no_for_update_student(self,roll_no):
        if not roll_no.isdigit():
                raise ValueError("Roll No must be digit ")
        
        if not (len(roll_no)) == 4:
               logger.debug(Fore.RED+"Len must be 4 character ")
               raise ValueError("Roll NO must be atlease 4 digit .")

##### ------: Update Name :----------####
    def update_name(self):
        while True:
            try:
                roll_no=input("Enter student Roll No  :")
                self.validate_roll_no_for_update_student(roll_no)

            except ValueError as e:
                print("Error :",e)
                continue
            found=False
            for student in students:
                if roll_no == student.roll_no:
                    logger.info(Fore.GREEN+f"Student found on Roll No {roll_no} His Name is {student.name} .")
                    while True:
                        try:
                            new_name=input("Enter new name for student  :").strip().title()
                            validate_name(new_name)
    
                        except ValueError as e:
                            print("Error :",e)
                            continue
                        confirm=input(f"Change name  from {student.name} to {new_name} ? (Y/N) :")
                        if not confirm.lower() == 'y':
                            logger.info("Student Name not changed .")
                            return

                        student.name=new_name
                        logger.info(Fore.GREEN+"Student Name update succesfully .")
                        self.save_to_file()
                        found=True
                        return

            if not found:
                logger.info(Fore.GREEN+f"Student not found on Roll No {roll_no} .")
                return

            ##### ------: Update Roll No :----------####
##### ------: Update Roll No :----------####
    def update_roll_no(self):
        while True :
            try:
                roll_no=input("Enter Roll No of student  :")
                self.validate_roll_no_for_update_student(roll_no)
            except ValueError as e:
                print("Error :",e)
                continue
            found=False
            for student in students:
                if roll_no == student.roll_no:
                    logger.info(Fore.GREEN+f"Student found on Roll No {roll_no} His Name is {student.name} .")
                    while True:
                        try:
                            new_roll_no=input("Enter new Roll No :")
                            self.validate_roll_no(new_roll_no)
                        except ValueError as e:
                            print("Error :",e)
                            continue
                        confirm=input(f"Change name  from {student.roll_no} to {new_roll_no} ? (Y/N) :")
                        if not confirm.lower() == 'y':
                            logger.info("Student roll no not changed .")
                            return
                        student.roll_no=new_roll_no
                        logger.info(Fore.GREEN+"Student Roll No update succesfully .")
                        self.save_to_file()
                        found=True
                        return

            if not found:
                logger.warning(Fore.RED+"Student not found on Roll No ",roll_no)
                return
            ##### ------: Update Age :----------####
    def update_age(self):
        while True:
           try:
              roll_no=input("Enter Roll No of student :")
              self.validate_roll_no_for_update_student(roll_no)
           except ValueError as e:
               print("Error :",e)
               continue
           found=False
           for student in students:
               if roll_no == student.roll_no:
                   logger.info(Fore.GREEN+f"Student found on Roll No {roll_no} His Name is {student.name} and age is {student.age}.")
            
                   while True:
                       try:
                           new_age=int(input("Enter new age for student :"))
                           validate_age(new_age)
                       except ValueError as e:
                           print("Error :",e)
                           continue
                       
                       confirm=input(f"Change name  from {student.age} to {new_age} ? (Y/N) :")
                       if not confirm.lower() == 'y':
                            logger.info(Fore.GREEN+"Student Age no changed .")
                            return
                       student.age=new_age
                       logger.info(Fore.GREEN+"Student age update succesfully .")
                       self.save_to_file()
                       found=True
                       return
           if not found:
               logger.warning(Fore.RED+"Student not found on Roll No ",roll_no)
               return

 
##### ------: Update Semester :----------####
    def update_semester(self):
        while True:
           try:
              roll_no=input("Enter Roll No of student :")
              self.validate_roll_no_for_update_student(roll_no)
           except ValueError as e:
               print("Error :",e)
               continue
           found=False
           for student in students:
               if roll_no == student.roll_no:
                   logger.info(Fore.GREEN+f"Student found on Roll No {roll_no} His Name is {student.name} and semester is {student.semester}.")
            
                   while True:
                       try:
                           new_semester=int(input("Enter new semester for student :"))
                           validate_semester(new_semester)
                       except ValueError as e:
                           print("Error :",e)
                           continue
                       confirm=input(f"Change name  from {student.semester} to {new_semester} ? (Y/N) :")
                       if not confirm.lower() == 'y':
                            logger.info(Fore.GREEN+"Student Semester not changed .")
                            return
                       student.semester=new_semester
                       logger.info(Fore.GREEN+"Student semester update succesfully .")
                       self.save_to_file()
                       found=True
                       return

           if not found:
               logger.warning(Fore.RED+"Student not found on Roll No ",roll_no)
               return

##### ------: Update Department :----------####
    def update_department(self):

        while True:
           try:
              roll_no=input("Enter Roll No of student :")
              self.validate_roll_no_for_update_student(roll_no)
           except ValueError as e:
               print("Error :",e)
               continue
           found=False
           for student in students:
               if roll_no == student.roll_no:
                   logger.info(Fore.GREEN+f"Student found on Roll No {roll_no} His Name is {student.name} and Department is {student.department} .")
            
                   while True:
                       try:
                           new_department=input("Enter new Department for student :").strip().title()
                           validate_department(new_department)
                       except ValueError as e:
                           print("Error :",e)
                           continue
                       confirm=input(f"Change name  from {student.department} to {new_department} ? (Y/N) :")
                       if not confirm.lower() == 'y':
                            logger.info("Student Department not changed .")
                            return
                       student.department=new_department
                       logger.info(Fore.GREEN+"Student department update succesfully .")
                       self.save_to_file()
                       found=True
                       return

           if not found:
               logger.warning(Fore.RED+"Student not found on Roll No ",roll_no)
               return 

##### ------: Update Student Marks  :----------####
    def update_student_marks(self):
        while True :
            try:
                roll_no=input("Enter Roll No of student  :")
                self.validate_roll_no_for_update_student(roll_no)
            except ValueError as e:
                print("Error :",e)
                continue
            found=False
            for student in students:
                if student.roll_no == roll_no:
                    logger.info(Fore.GREEN+f"Student found on Roll No {roll_no} His Name is {student.name} .")
                    print("All Subjects :",student.subjects.keys())
                    while True:
                        subject=input("Enter subject name to update marks :")
                        found1=False
                        for subject_name in student.subjects:
                            if subject.lower() == subject_name.lower():
                                try:
                                    new_marks = float(
                                        input(f"Enter {subject_name} new marks: ")
                                    )
                                    validate_marks(new_marks)

                                except ValueError as e:
                                    print("Error:", e)
                                    continue

                                confirm = input(
                                    f"Change marks from "
                                    f"{student.subjects[subject_name]} "
                                    f"to {new_marks}? (Y/N): "
                                )

                                if confirm.lower() != "y":
                                    logger.info("Marks not changed.")
                                    return

                                student.subjects[subject_name] = new_marks
                                self.save_to_file()

                                found1 = True
                                logger.info(Fore.GREEN+"Subject marks updated successfully.")
                                return

                        if not found1:
                            logger.warning(Fore.RED+f"Subject not found: {subject}")
                            return
            else:
                logger.warning(f"Student not found on roll no {roll_no}")
                return


###### ---------------- : Main Menu For Updating Studnt ------------- : #######

    def update_student(self):
        
        if not students:
            logging.info(Fore.GREEN+"No Student in student List .\n Student List is Empty .")
            return
        logger.info("--: Welcome to Student Updation  Menu :-----")
        while True:
            print("------------ : Update Student Menu : -------------")
            print("1. Update Name ")
            print("2. Update Roll No ")
            print("3. Update Age ")
            print("5. Update Marks ")
            print("6. Update Semester ")
            print("7. Update Department ")  
            print("8. Exit")
            print("-------------------------------------------------:")
            choice=input("Enter your choice :")
            if choice == '1':
                self.update_name()
            elif choice == '2':
                self.update_roll_no()
            elif choice == '3':
                self.update_age()
            elif choice == '5':
                self.update_student_marks()
            elif choice == '6':
                self.update_semester()
            elif choice == '7':
                self.update_department()
            elif choice == '8':
                logger.info("Student Updation exited")
                break
            else:
                print("Invalid choice : try again !")



#     ####################### ------: Student Statestic :------###############
    #Total Students

###### ------- : Total Students : ------- ###### 
    def total_students(self) -> int:
       return len(students)


#### ------ : Highest Marks :------- #####
    def highest_marks(self):
        highest_student = None
        highest_subject = None
        highest_marks = float("-inf")

        for student in students:
            for subject, marks in student.subjects.items():
                if marks > highest_marks:
                    highest_marks = marks
                    highest_student = student
                    highest_subject = subject

        print(f"Student : {highest_student.name}")
        print(f"Subject : {highest_subject}")
        print(f"Marks   : {highest_marks}")


###### ------- : Lowest Marks  : ------- ###### 

    def lowest_marks(self):
        lowest_student=None
        lowest_subject=None
        lowest_marks=float("inf")
        for student in students:
            for subject ,marks in student.subjects.items():
                if marks < lowest_marks:
                    lowest_marks=marks
                    lowest_subject=subject
                    lowest_student=student

        print("Student : ",lowest_student.name)
        print("Subject : ",lowest_subject)
        print("Marks   : ",lowest_marks)


###### ------- : Average Marks  : ------- ###### 
    def average_marks(self):
        for student in students:
            total = 0
            count = 0

            for marks in student.subjects.values():
                total += marks
                count += 1

            average = total / count

            print(f"Name : {student.name} :  average marks: {average:.2f}\n")


###### ------- : Student Gpa Calculation -------- : ######

    def student_gpa(self):
        while True:
            try:
                roll_no=input("Enter student roll no :")
                self.validate_roll_no_for_update_student(roll_no)
            except ValueError as e:
                print("Error :",e)
                continue
            found=False
            for student in students:
                if roll_no == student.roll_no:
                    name=student.name
                    gpa=student.calculate_gpa()
                    found=True
            if not found:
                logger.warning(Fore.RED+"Student not found .")
                print("Student not found.  on roll no ",roll_no)
                return
            
            print("Student Name :",name)
            print("Student GPA  :",gpa)

            again=input("Are you want to calculate another student gpa (Y/N) ? ").lower()
            if not again=='y':
                logger.info("User GPA calculation exit . ")
                break
            


####### --------- : Statistics :--------- ########

    def statistics(self):
        if not students:
            logging.info(Fore.GREEN+"No Student in student List .\n Student List is Empty .")
            return
        
        while True:
            print("-----------: Statistics Main Menu :-----------")
            print("1. Total Students ")
            print("2. Largest Marks Student ")
            print("3. Lowest Marks Student ")
            print("4. Average Marks of students ")
            print("5. Student GPA ")
            print("6. Exit ")
            print("-----------------------------------------")
            choice=input("Enter your choice :")
            if choice == '1':
                total=self.total_students()
                print("Total Students :",total)
            elif choice == '2':
                self.highest_marks()
            elif choice == '3':
                self.lowest_marks()
            elif choice == '4':
                self.average_marks()
            elif choice == '5':
                self.student_gpa()
            elif choice == '6':
                logger.info("Student Statistics exited.")
                break
            else:
                print("Invalid input . try again !")





      






    






    


            
                







        

            