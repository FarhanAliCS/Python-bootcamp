Math=int(input ("Enter the numbers of  subject 1:"))
Science=int(input("Enter the numbers of subject 2"))
English=int(input("Enter the numbers of subject 3"))
Urdu=int(input("Enter the numbers of subject 4"))
Total=Math+Science+English+Urdu
average=Total/4
percentage=(Total/400)*100
print(average)
print(percentage)
if percentage >=90:
    print("A")
elif percentage >=80 and percentage<90:
    print("B")
elif percentage >=70 and percentage < 80:
    print("C")
elif percentage >=60 and percentage<70:
    print("D")
else :
    print("Fail")