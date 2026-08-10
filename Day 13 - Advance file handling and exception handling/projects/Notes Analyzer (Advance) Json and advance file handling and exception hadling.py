import json
class Notes:
    def __init__(self):
        self.NOTES='Notes.txt'

    def save_to_file(self,data):
            with open(self.NOTES, 'a') as file:
                file.write(data + "\n")

#Helper validate_notes
    def validate_notes(self,notes):
        if notes.lower() == "stop":
            return "stop"
        
        if notes == "":
            raise ValueError("Notes must not be empty .")

        if len(notes) < 6 :
            raise ValueError("Length of notes must not be less then 6 .")
        return notes

            

    def show_notes(self):
        try:
            with open(self.NOTES,'r') as file:
                data=file.readlines()
            if data == []:
                raise ValueError("No data found .")
            
        except FileNotFoundError:
            print("File not found .")

        except ValueError as e:
            print("Error :",e)

        else:
           for note in data:
              print( note, end="")

    def add_notes(self):
        while True:
            try:
                notes= input("Enter notes : or enter stop to exit .")
                notes=self.validate_notes(notes)
                if notes == "stop":
                    break                            
                self.save_to_file(notes)
            except ValueError as e:
                print("Error :",e)
                continue

    def count_notes(self):
        try:
            with open(self.NOTES,'r') as file:
                data=file.readlines()

            print("Total notes :",len(data))

        except FileNotFoundError:
            print("File not found .")
            

    def search_notes(self):
        while True:
          try:
            search=input("Enter whole note or search by words :")
            if search == "":
                raise ValueError("Search must not be empty .")
          except ValueError as e:
              print("Error :",e)
              continue
          else:
              try:
                  with open(self.NOTES,'r') as file:
                      data=file.readlines()
                  
                  if not data:
                      raise ValueError("No data found .")
                  found=False
                  for index,value in enumerate(data):
                      if search.lower() in value.lower():
                          print(f"{index+1}: {value}",end="")
                          found=True
                  if not found:
                      print("Not found .")
              except FileNotFoundError:
                  print("File not found .")
              except ValueError as e:
                  print("Error :",e)


    def delete_notes(self):
        while True:
            try:
                delete=input("Enter notes or enter one word of notes to delete :")
                if delete == "":
                    raise ValueError("Notes must not be empty .")
            except ValueError as e:
                print("Error :",e)
                continue
            else:
                try:
                    with open(self.NOTES,'r') as file:
                        data=file.readlines()
                    found=False
                    for i in range (len(data)):
                        if delete.lower() in data[i].lower():
                           found = True
                           data.pop(i)
                           with open(self.NOTES,'w') as r :
                                r.writelines(data)
                           print("Delete successfully .")
                           return
                    if not found:
                        print("Not found .")
                        break
                except FileNotFoundError:
                    print("File not found .")


    def update_notes(self):
        while True:
            try:
                update=input("Enter note which you want to update :").strip()
                if not update:
                    raise ValueError("update is empty .")
            except ValueError as e:
                print("Error:",e)
                continue
            else:
                try:
                    with open(self.NOTES,'r') as file:
                        data=file.readlines()
                    found=False
                    for i in range(len(data)):
                        if update.lower() in data[i].lower():
                            new_note=(input("Enter new note to add :"))
                            self.validate_notes(new_note)
                            data[i]=new_note + "\n"
                            found= True
                            break
                    if not found:
                           print("Not found .")
                           break
                    with open(self.NOTES,'w') as file:
                          file.writelines(data)
                          print("Update successfully .")
                          return
                except FileNotFoundError:
                    print("File not found .")

                except ValueError as e:
                    print("Error :",e)
                    continue

    def count_words(self):
        try:
            with open(self.NOTES,'r') as file:
                data=file.read()

            print("\n Total words in data :",len(data.split()))
        except FileNotFoundError:
            print("File not found .")



    def count_of_vowel_and_consonant(self):
        try:
            with open(self.NOTES,'r') as file:
                data=file.read().lower()
            count_vowel=0
            count_consonant=0
            vowel="aeiou"
            for char in data:
               if char.isalpha():
                   if char in vowel:
                       count_vowel+=1
                   else:
                       count_consonant+=1

            print("\nCount of vowel are :",count_vowel)
            print("Total consonant are :",count_consonant)

        except FileNotFoundError:
            print("File not found .")





                        
        

    
notes=Notes()
while True:
    print("================== NOTES MANAGER =================")
    print("1. Add Notes ")
    print("2. Show All Notes ")
    print("3. Count Notes")
    print("4. Count Words ")
    print("5. Count Vowel and Consonant ")
    print("6. Search Notes ")
    print("7. Delete Notes ")
    print("8. Update Notes ")
    print("9. Exit ")
    print("==================================================")

    choice = input ("Enter your choice :")

    if choice == '1':
        notes.add_notes()

    elif choice == '2':
        notes.Show_notes()

    elif choice == '3':
        notes.count_notes()

    elif choice == '4':
        notes.count_words()

    elif choice == '5':
        notes.count_of_vowel_and_consonant()

    elif choice == '6':
        notes.search_notes()

    elif choice == '7':
        notes.delete_notes()

    elif choice == '8':
        notes.update_notes()

    elif choice == '9':
        print("Program ended .")
        break

    else:
        print("Invalid input . try again !")

                
                