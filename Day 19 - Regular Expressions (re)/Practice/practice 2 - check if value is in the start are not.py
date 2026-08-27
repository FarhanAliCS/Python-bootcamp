import re
text="My name is farhan ali"
value=input("Enter value to search if it is in start are not :")
result=re.match(value,text)
if result:
    print("value is in start .")
else:
    print(" not in start .")