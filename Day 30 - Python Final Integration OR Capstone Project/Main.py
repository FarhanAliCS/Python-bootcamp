import Manage 

from colorama import Fore,Style,init
init(autoreset=True)

student_manager=Manage.StudentManager()

while True:
    print(Fore.CYAN+Style.BRIGHT+"\n=========== Student Management System ============")
    print("1. Add Students ")
    print("2. Search Students ")
    print("3. Show All Students  ")
    print("4. Update Students ")
    print("5. Delete Student ")
    print("6. Statistics")
    print("7. Exit ")
    print(Fore.CYAN+"=================================================")
    choice=input("Enter your choice :").strip()
    if choice == '1':
        student_manager.add_student()
    elif choice == '2':
        student_manager.search_student()
    elif choice == '3':
        student_manager.show_students()
    elif choice == '4':
        student_manager.update_student()
    elif choice == '5':
        student_manager.delete_student()
    elif choice == '6':
        student_manager.statistics()
    elif choice == '7':
        print(Fore.GREEN+"Thank You for using our system .")
        break
    else:
        print(Fore.RED+"Invalid choice : try again !")
