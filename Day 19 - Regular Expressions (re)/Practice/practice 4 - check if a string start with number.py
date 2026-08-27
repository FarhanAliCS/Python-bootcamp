import re
text=input("Enter text :")
result=re.match(r"\d+",text)
if result:
    print("First one is number .")
else:
    print("first word is text")
