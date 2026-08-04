#Add new contact 
def add_contact(book):
    while True :
        name=input("Enter your name : or enter 'stop' to exit :")
        if name.isdigit():
            print("digit not allowed in name")
            continue
        if name.lower()== 'stop':
            break
        found=False
        try:
            with open(book,'r') as file:
                data=file.readlines()
                for line in data:
                    line=line.strip()
                    if line == "":
                        continue
                    if ": " not in line:
                        continue
                    temp_name,temp_number=line.split(": ")
                    if temp_name.lower()==name.lower():
                        found=True
                        break
        except FileNotFoundError:
            pass        
        if found:
            print("contact already exists .")
            continue
        while True:
               number=input("Enter contact number :")
               if number.isdigit() and len(number) == 11 and number.startswith("03"):
                break
               print("Invalid mobile number. Try again.")
        print("contact add succesfully .")
          

        try:
          with open(book,'a') as file:
               file.write(name + ": ")
               file.write(number+ "\n")
        except FileNotFoundError:
            print("File does not exist .")
            continue


#Show all contact     
def display_contact(book):
    try:
        with open(book,'r') as file:
            data=file.readlines()
            for line in data:
                print(line,end="")
    except FileNotFoundError:
        print("File not found")


#Search for a specific contact and display its number 
def searching_for_contact(book):
    search=input("Enter contact to search :")
    found=False
    try:
        with open(book,'r') as file:
            data=file.readlines()
            for line in data:
                line=line.strip()
                if line =="":
                    continue
                if ": " not in line:
                    continue
                if search.lower() in line.lower():
                    print(line,end="")
                    found=True
    except FileNotFoundError:
        print("File not found .")
    if not found:
        print("contact not found .")


#Update a specific contact 
def update_contact(book):
    search=input("Enter name :")
    try:
        with open(book,'r') as file:               
            data=file.readlines()
            found=False
            for i in range(len(data)):
               name,number=data[i].strip().split(": ")
               if name.lower()==search.lower():
                  while True:
                        new_number=input("Enter new number :")
                        if new_number.isdigit() and len(new_number)==11 and new_number.startswith('03'):
                            break
                        print("invalid mobile number.try again !")
                        continue
               
                  data[i]=name+": "+new_number+"\n" 
                  found=True 
                  break
            if found:
               with open(book,'w') as file:
                file.writelines(data) 
                print("data update succesfully .")
            else:
                print("not found .")            
    except FileNotFoundError:
        print("File not found .")

#Delete a specific contact 
def delete_contact(book):
    delete=input("Enter value to delete :")
    found=False
    try:
        with open(book,'r') as file:
            data=file.readlines()
            for i in range (len(data)):
                data[i]=data[i].strip()
                if data[i]=="":
                    continue
                if ": " in data[i]:
                    continue
                name,number=data[i].strip().split(": ")
                if name.lower()==delete.lower():
                    del data[i]
                    found=True
                    print("delete succesfully .")
                    break
            if found:
                with open(book,'w') as file:
                    file.writelines(data)
            else:
                print("contact not found")
    except FileNotFoundError:
        print("file not found .")


#Total numbers of contact 
def total_contact(book):
    try:
        with open(book,'r') as file:
            data=file.readlines()
            print("Total contact :",len(data))
    except FileNotFoundError:
        print("file not found .")


#=================
#   MENU
#=================
book='contact_book.txt'
while True:
        print("===============================")
        print("1. Add contact ")
        print("2. Display contact ")
        print("3. Search for contact ")
        print("4. Update contact ")
        print("5. Delete contact ")
        print("6. Total number of contact ")
        print("7. Exit ")
        print("===============================")
        choice=input("Enter your choice :")

#Add new contact 
        if choice == '1':
            add_contact(book)

#Display contact
        elif choice == '2':
            display_contact(book)

#Search contact
        elif choice == '3':
            searching_for_contact(book)

#Update contact
        elif choice == '4':
            update_contact(book)

#Delete contact
        elif choice == '5':
            delete_contact(book)

#Total contacts
        elif choice == '6':
            total_contact(book)

#Exit
        elif choice == '7':
            print("Program ended .")
            break

#Else
        else:
            print("Invalid input .")



    

            
