students = {
    "Ali": 85,
    "Ahmed": 42,
    "Sara": 73,
    "Usman": 35,
    "Ayesha": 91,
    "Hamza": 58
}
pass_students_name= [name for name , marks in students.items() if marks >=50 ]

fail_students_name=[name for name,marks in students.items() if marks < 50]

bonus_marks={name: marks+5 for name , marks  in students.items()  }

pass_students={name: marks for name,marks in students.items() if marks >= 50}

grades = {
    name: "A" if marks >= 90
    else "B" if marks >= 80
    else "C" if marks >= 70
    else "D" if marks >= 60
    else "F"
    for name, marks in students.items()
}

print("=========== Student Marks Analyzer using comprehensions ================")
print("Pass student name           :",pass_students_name)
print("Fail student name           :",fail_students_name)
print("Student Marks after bonus   :",bonus_marks)
print("Pass students               :",bonus_marks)
print("Student with grades         :",grades)
