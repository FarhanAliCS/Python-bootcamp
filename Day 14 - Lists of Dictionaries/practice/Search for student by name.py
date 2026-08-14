students=[
    {
     "Name" : "Farhan Ali", "Marks" : 85 , "gpa"  : 3.5
     },{
         "Name"  : "Abbas Ahmed", "Marks"  : 80, "gpa"  : 3.6   
     },{
         "Name"  : "Ashraf Ali", "Marks"  : 90, "gpa"   : 3.1
     },{
         "Name" : "Ahmed" , "Marks" : 70 , "gpa"  : 3.21
     }
]
name=input("Enter student name :").lower()
found=False
for student in students:
     if name in student["Name"].lower():
        print("======== Student info =======")
        print(f"Name      :   {student["Name"]}")
        print(f"Marks     :   {student["Marks"]}")
        print(f"gpa       :   {student["gpa"]}")
        print()
        found=True
if not found:
    print("Not found .")
        
        
