#For loop
num=int(input("Enter the number :"))
count=0
for digit in str(num):
    num=num//10
    count+=1
print(count)

print("In for while loop")
#using while loop
digit=''
while num>0:
    num=num//10
    count+=1
print(count)