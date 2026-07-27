def add_notes(NOTES):
       while True:
          notes=input("Enter your notes : or enter 'stop' to exit :")
          if notes.lower()== 'stop':
               break
          with open(NOTES,'a') as file:
               file.write(notes +"\n")
def read_notes(NOTES):
     try:
          with open(NOTES,'r') as file:
               data=file.read()
               if data=="":
                   print("No data avalible .")
               print(data)
     except FileNotFoundError:
          print("file not found .")
def clear_notes(NOTES):
     conform=input("Are you sure you want to clear notes . yes/no .")
     if conform.lower() == 'yes':
        with open(NOTES,'w') as file:
          file.write("")
          print("Notes clear succesfully .")
     else:
         print("Operation cancelled .")

NOTES='notes.txt'
while True :
    print("======= Main Menu ==========")
    print("1. Add notes")
    print("2. Read notes ")
    print("3. clear notes ")
    print("4. Eixt")
    print("============================")
    choice=input("Enter your choice :")
    if choice == '1':
        add_notes(NOTES)
    elif choice== '2':
        read_notes(NOTES)
    elif choice == '3':
        clear_notes(NOTES)
    elif choice == '4':
        print("program ended .")
        break
    else:
        print("Invlaid chocie .try again !")

