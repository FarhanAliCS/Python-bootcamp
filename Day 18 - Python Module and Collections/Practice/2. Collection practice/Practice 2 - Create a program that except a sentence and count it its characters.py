import collections
sentence=input("Enter your input :")
result=collections.Counter(sentence)
print(result)
print(result.most_common(3))


