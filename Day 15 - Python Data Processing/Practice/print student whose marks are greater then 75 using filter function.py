students = [
    {"Name": "Farhan", "Marks": 85},
    {"Name": "Ahmed", "Marks": 70},
    {"Name": "Ashraf", "Marks": 90},
    {"Name": "Ali", "Marks": 60}
]
data=sorted(
    students
    ,key=lambda student:student["Marks"],
    reverse=True
)
result=filter(
    lambda student:student["Marks"] > 75 ,
    data
)


print(list(result))