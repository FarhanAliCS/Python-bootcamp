
#For Adding contact 
def add_contact(names, numbers):

    while True:

        name = input("Enter name or 'stop' to exit: ")

        if name.lower() == "stop":
            break

        if name in names:
            print("Name already exists.")
            continue

        while True:

            number = input("Enter phone number: ")

            if number.isdigit() and len(number) == 11 and number.startswith("03"):
                break

            print("Invalid mobile number. Try again.")

        names.append(name)
        numbers.append(number)

        print("Contact added successfully.")

#For searching contact
def search_contact (names,numbers):
    name=input("Enter name of contact to seaech :")
    if  not  names:
        print("Contact list is empty .")
    for i in range(len(names)):
        if names[i]==name:
            print(names[i] ,":",numbers[i])
            return


#For printing all contacts
def display_contacts(names,numbers):
    print("\n====== contact list ========\n")
    if len(names)==0:
        print("List is empty .")
        return
    for i in range(len(names)):
             print("   ",names[i],":",numbers[i])



#For Deleting contacts
def delete_contact(names,numbers):
    name=input("Enter the name to delete :")
    if len(names)==0:
        print("contact list is empty .")
    for i in range(len(names)):
        if names[i]==name.lower():
            check=input("are you you sure you want to delte y/n:")
            if check.lower()=='y':
              names.pop(i)
              numbers.pop(i)
              print("Delete succesfully.")
              return
            elif check.lower()=='n':
                return
        

    
#============================ Main Minu ============================
names=[]
numbers=[]
while True:
    print("==========================================================")
    print("==================Main Menue========================")
    print("1. Add contact ")
    print("2. Search contact")
    print("3. Display contacts")
    print("4. Delete contact ")
    print("5. Exit")
    print("============================================================")
    choice=input("Enter your choice :")

#For Adding contact 
    if choice == '1':
        add_contact(names,numbers)

#For searching contact 
    elif choice == '2':
        search_contact(names,numbers)

#For printing all contacts
    elif choice == '3':
        display_contacts(names,numbers)

#For Deleting contacts
    elif choice == '4':
        delete_contact(names,numbers)

#For exiting 
    elif choice == '5':
        print("Program end ..")
        break

    else:
        print('Invalid choice :please enter menue options ')

   
       
   

   