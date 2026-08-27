import re
email=input("Enter email :")
validate=r"^\w+@\w+\.com$"
result=re.findall(validate,email)
print(result)
print(validate)