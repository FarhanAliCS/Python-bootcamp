students = [
    {"Name": "Farhan", "Marks": 85},
    {"Name": "Ahmed", "Marks": 70},
    {"Name": "Ashraf", "Marks": 90},
    {"Name": "Ali", "Marks": 60}
]

result=sorted(
    students,
    key=lambda student:student["Marks"]
)
print(result)