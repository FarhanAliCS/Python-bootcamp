from functools import reduce
words = ["python", "java", "programming", "ai", "developer", "code", "machine"]

#Using filter(), map(), and reduce():
#Keep words having more than 4 characters.
#Convert them to uppercase.
#Combine them into one string separated by " - ".

final_words=filter(lambda x:len(x) >4 ,words)
result=map(lambda x:x.upper(),final_words)
final=reduce(lambda a,b:a+" - "+b,result)
print(final)
