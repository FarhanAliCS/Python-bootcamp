password=input("Enter the password :")
digit=0
uppercase=0
lowercase=0
special=0
specialchar='@!#$%^&~'
for ch in password:
    if ch.isupper():
        uppercase+=1
    elif ch.islower():
        lowercase+=1
    elif ch in specialchar:
        special+=1
    elif ch.isdigit():
        digit+=1

print ("\n  Checking password ..........")

if len(password) < 8:
    print("\nLength must be 8 character .")
if len(password)>20:
    print("\nlenth must be between 8 and 20 character .")
if uppercase==0:
    print("\npassword must contanin upper case character .")
if lowercase==0:
    print("\npassword must contain lower case character .")
if digit==0:
    print("\npassword must contain digit .")
if special ==0:
    print("\npassword must contain atlease one special character .")
if len(password)>8 and len(password)<20 and uppercase !=0 and lowercase!=0 and digit!=0 and special!=0:
    print("\nStrong password .")
else:
    print("\n  Weak Password .")