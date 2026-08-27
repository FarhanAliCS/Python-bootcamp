def generator():
    with open("text.txt","r") as file:
        for line in file:
            if "python" in line.lower():
                yield line

            

            

lines=generator()
for i in lines:
    print(i)


        