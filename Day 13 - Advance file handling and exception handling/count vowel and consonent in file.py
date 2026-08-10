values="notes.txt"
try:
    note=input("Enter notes :")
    if note == "":
        raise ValueError("Notes must not be empty .")
    if len(note) < 6:
        raise ValueError("Length must be atleast 6 character .")
except ValueError as e:
    print("Error :",e)
else:
    try:
        with open(values,'a+')as file:
            file.write(note + "\n")
            print("Data write succesfully .")
            file.seek(0)
            data=file.read()
            data=data.replace(" ","").replace("\n","")
            vowel="aeiou"
    except FileNotFoundError :
        print("file not found .")

    else:
        vowel_count=0
        consonant_count=0
        for i in range(len(data)):
            if data[i].lower() in vowel:
                vowel_count+=1
            elif data[i].isalpha():
                consonant_count+=1
        print("vowel count :",vowel_count)
        print("Consonant count :",consonant_count)
               
                
        

