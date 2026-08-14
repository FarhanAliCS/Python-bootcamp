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

highest_marks=students[0]["Marks"]
name=""
for student in students:
    if student["Marks"] > highest_marks:
        highest_marks=student["Marks"]
        name=student["Name"]

print("Highest Marks are :",highest_marks)
print("Student name is :",name)

