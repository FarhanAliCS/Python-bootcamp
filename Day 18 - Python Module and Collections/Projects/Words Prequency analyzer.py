import collections

sentence=input("Enter yor sentence :")
words=sentence.lower().split()
counts=collections.Counter(words)
print("--------- Words and count --------")
for word , count in counts.most_common():
    print(word,":",count)
    print(counts.most_common(3))



