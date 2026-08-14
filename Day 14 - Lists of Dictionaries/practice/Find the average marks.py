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
total=0
count=0
for student in students:
    total+=student["Marks"]
    count+=1
average=total/len(students)
print("Average Marks is :",average)