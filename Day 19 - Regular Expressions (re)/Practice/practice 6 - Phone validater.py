import re
number=input("Enter number :")
pattern=r"^03\d{9}$"
result=re.search(pattern,number)
if result:
    print("Valid number .")
else:
    print("Not")