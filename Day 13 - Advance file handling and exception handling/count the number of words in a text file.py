notes="notes.txt"
try:
        note=input("Enter notes :")
        if note == "":
                raise ValueError("Notes cannot be empty .")
        if len(note) < 5 :
                raise ValueError("Length of notes must be atleast 4 character .")
except ValueError as e:
        print("Error :",e)
        
else:
        try:
           with open(notes,'a+') as file :

                file.write(note + "\n")

                print("Write data to file succesfully .")

                file.seek(0)

                data=file.read()

        except FileNotFoundError as e:
               
               print("Error :",e)

        else:
             
             print("===== Data =====")

             print(data)
             
             print(len(data.replace(" ","").replace("\n","")))




    