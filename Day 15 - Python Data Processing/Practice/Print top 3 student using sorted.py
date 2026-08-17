students = [
    {"Name": "Farhan", "Marks": 85,"gpa" : 3.2},
    {"Name": "Ahmed", "Marks": 70,"gpa" : 3.6},
    {"Name": "Ashraf", "Marks": 90,"gpa" : 3.1},
    {"Name": "Ali", "Marks": 60,"gpa" : 2.2}
]
result=sorted(
    students,
              key=lambda student : student["Marks"] ,
              reverse=True)
for position,student in enumerate(result,start=1):
    if position == 4:
        break
    print(f'position {position} {student}')