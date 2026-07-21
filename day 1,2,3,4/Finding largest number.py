num1=int(input("Enter the number :"))
num2=int(input("Enter the number :"))
num3=int(input("Enter the number :"))

if (num1>num2 and num1>num3):
    print("Num1 is greater.")
elif num2>num1 and num2>num3:
    print("num2 is greater .")
elif num3>num1 and num3>num2:
    print("Num 3 is greater .")
else:
    print("Invilid input .")