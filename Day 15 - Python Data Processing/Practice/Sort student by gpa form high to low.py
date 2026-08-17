students = [
    {"Name": "Farhan", "Marks": 85,"gpa" : 3.2},
    {"Name": "Ahmed", "Marks": 70,"gpa" : 3.6},
    {"Name": "Ashraf", "Marks": 90,"gpa" : 3.1},
    {"Name": "Ali", "Marks": 60,"gpa" : 2.2}
]
result=sorted(
    students,key=lambda student : student["gpa"] 
    ,reverse=True
)
print(list(result))