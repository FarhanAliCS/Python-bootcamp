name =input("Enter your character :")
vowel='aeiouAEIOU'
vowel_count=0
consonant_count=0
for ch in name:
    if ch.isalpha():
        if ch in vowel:
            vowel_count+=1
        else:
            consonant_count+=1
print("count of vowel is :",vowel_count)
print("consonanat count is :",consonant_count)

#Print char that are vowel
vowel='aeiouAEIOU'
for ch in name:
    if ch.isalpha():
        if ch in vowel:
            print(ch,'char is vowel .')
        else:
            print(ch,'char is consonant .')