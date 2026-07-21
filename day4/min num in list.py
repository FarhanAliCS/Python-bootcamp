num=[1,2,3,4,5,6,7,8]
MinNum=num[0]
#loop
for i in num:
    if i < MinNum:
        MinNum = i
print(MinNum)