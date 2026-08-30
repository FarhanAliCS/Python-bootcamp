from functools import reduce
marks=[56,23,34,45,32,65,76,87]
passsed_marks=filter(lambda x : x > 40 ,marks)
after_bonus=map(lambda x:x+5 ,passsed_marks)
now_marks=list(after_bonus)
total=reduce(lambda a,b:a+b ,now_marks)
print(total)
highest_marks=reduce(lambda a,b:max(a,b) ,now_marks )
print(highest_marks)
