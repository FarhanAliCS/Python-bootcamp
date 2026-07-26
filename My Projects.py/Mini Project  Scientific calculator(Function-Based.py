#scientific calculator
#addition
def addition(num1 , num2):
    return num1+num2

#subtraction
def subtraction(num1 , num2):
    return num1-num2

#Multiplication
def multiplication(num1,num2):
    return num1*num2

#Division
def division(num1,num2):
    if num2 == 0:
       print("Not divisble by zero .")
    return num1/num2

#Power
def power(num1 , num2 ):
    return num1**num2

#squre Root
def squre_Root(num1 ):
    return num1**0.5

#Display Main tab

while True:
    while True:
        print("\n(     -:======Calculator=======:-     )\n")
        print(" 1. Addition")
        print(" 2. Subtraction")
        print(" 3. Multiplication")
        print(" 4. Division")
        print(" 5. power")
        print(" 6. squre root")
        choice=input("Enter you choice :")

   #check for addition
        if choice=='1':
           num1=int(input("Enter num 1 :"))
           num2=int(input("Enter num 2 :"))
           print(addition(num1,num2))
           break

#check for subtraction
        elif choice=='2':
           num1=int(input("Enter num 1 :"))
           num2=int(input("Enter num 2 :"))
           print(subtraction(num1,num2))
           break

#check for multiplication
        elif choice=='3':
           num1=int(input("Enter num 1 :"))
           num2=int(input("Enter num 2 :"))
           print(multiplication(num1,num2))
           break

#check for division
        elif choice=='4':
           num1=int(input("Enter num 1 :"))
           num2=int(input("Enter num 2 :"))
           print(division(num1,num2))
           break

#check for power
        elif  choice=='5':
           num1=int(input("Enter num 1 :"))
           num2=int(input("Enter num 2 :"))
           print(power(num1,num2))
           break

#check for squre root
        elif choice=='6':
           num1=int(input("Enter num  :"))
           print(squre_Root(num1))
           break
        else:
          print("Invalid choice .")

#Outer while loop
    again=input("\n You want to perform another calculation? Yes/No :")
    if again.lower() !='yes':
       print("\n Thanks for using caluclator")
       break
       
       

    


    

    
    

    
