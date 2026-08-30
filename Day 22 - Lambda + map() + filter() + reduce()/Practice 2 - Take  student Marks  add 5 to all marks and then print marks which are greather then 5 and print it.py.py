from functools import reduce
marks=[78,34,52,49,67,90,34]

result=map(lambda x : x+5 ,marks)
passed_students=filter(lambda x:x >= 50 ,result)

print("Passed students ;",list(passed_students))




