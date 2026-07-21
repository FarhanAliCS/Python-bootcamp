Num=int(input("Enter the number :"))
reverse=0
for digit in str(Num):
    digit=Num%10
    reverse=reverse*10+digit
    Num=Num//10
    print(reverse)
