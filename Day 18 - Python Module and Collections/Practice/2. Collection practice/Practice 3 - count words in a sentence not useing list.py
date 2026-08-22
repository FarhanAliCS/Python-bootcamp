import collections

sentence=input("Enter sentence :")

words=sentence.lower().split()

count=collections.Counter(words)

print(count)

print("Top 3 :",count.most_common(3))