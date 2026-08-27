def generator():
    text=input("Enter text :")
    with open("text.txt",'a') as file:
        file.write(text + "\n")

    with open("text.txt", 'r') as file:
        data=file.read()
        data=data.split()
    for d in data:
        if d.lower() == "python":
            yield d

text=generator()
for word in text:
    print(word)