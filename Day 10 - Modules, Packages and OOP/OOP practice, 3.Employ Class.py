class Employ:
    def __init__(self,name,department,salary):
        self.name=name
        self.department=department
        self.salary=salary

    def display(self):
        print("name       :",self.name)
        print("department :",self.department)
        print("salary     :",self.salary)



employ1=Employ("Farhan","development",1000010)
employ2=Employ("Ahmad","sales",50000)

print()
print("\n=== Employ 1 ===\n")
employ1.display()
print("\n=== Employ 2 ===\n")
employ2.display()
    