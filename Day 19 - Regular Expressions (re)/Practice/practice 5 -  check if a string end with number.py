import re
text=input("Enter your text :")
result=re.search(r"\d+$",text)
if result:
    print("End is number .")
else:
    print("End is word .")