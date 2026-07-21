age=int(input("Enter your age :"))

if age<=12:
    print("Child .")
elif age>12 and age<18:
    print("Teenager .")
elif age>=18 and age<60:
    print("adult .")
else:
    print("Senior .")