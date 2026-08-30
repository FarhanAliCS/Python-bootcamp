numbers=[1,2,3,4,5,6,7,8,9]
result=[]
for num in numbers:
    if num % 2 == 0:
        num*=2
        result.append(num)
print(result)

#Using Lambda and filtter fun
result=filter(lambda x: x % 2 == 0,numbers)
result1=map(lambda x : x*2,result)
print(list(result1))
