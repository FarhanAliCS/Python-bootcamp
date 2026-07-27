class Student:
    def __init__(self):
        name=input("Enter student name :")
        age=int(input("Enter studen age :"))
        department=input("Enter student department :")
        self.name=name
        self.age=age
        self.department=department

    def Show_details(self):
        print("name       :",self.name)
        print("age        :",self.age)
        print("department :",self.department)


#Main Menu========================================================================================

#=================================================================================================


Student1=Student()
Student2=Student()
print("\n====== Student 1 =======\n")
Student1.Show_details()
print()

print("\n====== Student 2 =======\n")
Student2.Show_details()        