class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Student(Person):
    def __init__(self,name,age,roll_no):
        super().__init__(name,age)
        self.roll_no=roll_no


    def display(self):
        print("\n=== student info ===\n")
        print("student name    :",self.name)
        print("student age     :",self.age)
        print("student roll no :",self.roll_no)

    def study(self):
        print(self.name," is studing")

class Teacher(Person):
    def __init__(self, name, age,id):
        super().__init__(name, age)
        self.id=id
    def display(self):
         print("\n=== Teacher info ===\n")
         print("Teacher name    :",self.name)
         print("Teacher age     :",self.age)
         print("Teacher id      :",self.id)
    def teaching(self):
         print(self.name,"is teaching .")


#================  MAIN =======
#
# =============================


#First Object
s1=Student("farhan",20,101)
s1.display()
s1.study()

#2nd Object
s2=Student("abbas",21,102)
s2.display()
s2.study()

#Teacher object
t1=Teacher("ahmad",30,11)
t1.display()
t1.teaching()


