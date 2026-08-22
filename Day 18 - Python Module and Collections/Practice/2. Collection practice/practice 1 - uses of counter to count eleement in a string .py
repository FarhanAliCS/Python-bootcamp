import collections
name="Farhan Ali khan"
count=collections.Counter(name)
print("Count of every word :",count)
print("Top 2 highes count :",count.most_common(2))
