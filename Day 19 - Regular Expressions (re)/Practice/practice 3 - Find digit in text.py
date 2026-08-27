import re
text="I am 18 year old . And I studey in class 12 ."

# "\d" for finding single digit in text
result=re.findall(r"\d",text)
print("Single digits :",result)

# "\d+" for finding  full digits  in text 

result=re.findall(r"\d+",text)
print("Full digits ",result)

# "\w" for printing char wise in character

result=re.findall(r"\w",text)
print("Single characters :",result)

# "\w+" for whole word in text

result=re.findall(r"\w+",text)
print("words :",result)

# For spaces
result=re.findall(r"\s+",text)
count=0
for i in result:
    count+=1
print(count)



