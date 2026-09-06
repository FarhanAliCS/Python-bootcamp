from colorama import Fore, Style,init

init(autoreset=True)


def calculate_grade(percentage):

    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"
    
def message(grade):
    if grade == 'A+':
        return "Outstanding"
    elif grade == "A":
        return "Excellent"
    elif grade == "B":
        return "Very Very Good "
    
    elif grade == "C":
        return "Good"

    elif grade == 'D':
        return "Not Bad !"
    
    else:
        return "Better luck next time "
    
while True:
    print(Fore.CYAN + Style.BRIGHT + "===== STUDENT RESULT CALCULATOR =====")

    while True:
        try:
            name = input("Enter student name: ")
            if not name.replace(" ","").isalpha():
                raise ValueError("Only alphabet allowed in name ")
            break
        except ValueError as e:
            print("Error :",e)
            continue
    while True:
        try:
            math = float(input("Enter Math marks: "))
            if math < 0 or math >= 100:
                raise ValueError("Marks must be between 0 - 100 .")
            python = float(input("Enter Python marks: "))
            if math < 0 or math >= 100:
                raise ValueError("Marks must be between 0 - 100 .")
            english = float(input("Enter English marks: "))
            if math < 0 or math >= 100:
                raise ValueError("Marks must be between 0 - 100 .")
            
            computer=float(input("Enter computer science marks :"))

            if math < 0 or math >= 100:
                raise ValueError("Marks must be between 0 - 100 .")
            break

        except ValueError as e:
            print("Error :",e)
            continue

        
    total = math + python + english + computer
    percentage = total / 400 * 100
    highest_marks = max(math,python,english,computer)
    lowest_marks=min(math,python,english,computer)
    grade = calculate_grade(percentage)
    messege=message(grade)

    print("\n" + Fore.YELLOW + "===== RESULT =====")
    print(f"Name: {name}")
    print(f"Total Marks: {total}/400")
    print(f"Percentage: {percentage:.2f}%")
    print("Highest Marks :",highest_marks)
    print("Lowest Marks  :",lowest_marks)
    print(f"Grade: {grade}")
    print("Appreciation :",messege)
    
        
    if percentage >= 50:
        print(Fore.GREEN + Style.BRIGHT + "Status: PASS")
    else:
            print(Fore.RED + Style.BRIGHT + "Status: FAIL")

    again=input("\nYou want to calculate another student  (Y/N) :")
    if not again.lower()=="y":
       print("Thanks for using over system .")
       break













