
def StudentEntry():
        Name=input("Enter student name :")
        Age=int(input("Enter Age of student :"))
        Roll_No=input("Enter Roll No of student :")
        return Name, Age,Roll_No
def Showresult(Name,Age,Roll_No):
    print("Student Name is :",Name)
    print("Age of student is :",Age)
    print("Roll no of student is :",Roll_No)

#Main Menue
Name=''
Age=0
Roll_No=0
print(" \n          (:Student Management System :)    ")
while True:
      print("\n 1. Data Entry  \n 2. Show Result \n 3. Enter 3 for exit .\n")
      choice=input("Enter your choice :")
      if choice=='1':
           Name,Age ,Roll_No=StudentEntry()
      elif choice=='2':
          if Name=='':
            print(" \n No Data Found .")
          else:
            print("\n (: Student Record :)")
            Showresult(Name,Age,Roll_No)
      elif choice=='3':
            break
      else:
            print("Envalid input .")


            
        

