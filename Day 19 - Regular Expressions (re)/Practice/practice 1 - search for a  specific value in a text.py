import re 
text="My name is Farhan ALi Khan . And I am from Damlai Swat ."
value=input("Enter value to search in text :")
result=re.search(value,text)
print(result)
if result:
    print("Found ")
else:
    print("Not found .")