import re
class Text_Analyzer:
    def __init__(self):
        self.text=""

    def input_text(self):
        self.text=input("Enter text .")


    def all_numbers(self):
        if not self.text:
            print("First enter text :")
            return
        result=re.findall(r"\d+",self.text)
        print(result)

    def all_words(self):
        if not self.text:
            print("First enter text :")
            return
        result=re.findall(r"\w+",self.text)
        print(result)

    def total_words(self):
        if not self.text:
            print("First enter text :")
            return
        result=re.findall(r"\w+",self.text)
        total_words=len(result)
        print("Total words :",total_words)

    def total_numbers(self):
        if not self.text:
            print("First enter text :")
            return
        result=re.findall(r"\d+",self.text)
        print("total numbers :",len(result))

    def reflace_seleted_word(self):
        if not self.text:
            print("First enter text :")
            return
        print(self.text)
        word=input("Enter word from text to replace :")
        new_word=input("Enter new word to change to it :")
        result=re.sub(word,new_word,self.text)
        if result:
            print("Update succesfully .")
            print("New text is :",result)
        else:
            print("Plese enter correct word .")

    def phone_number_exists(self):
        if not self.text:
            print("First enter text :")
            return
        phone=r"03\d{9}"
        result=re.findall(phone,self.text)
        if result:
            print("Phone number found .")
            print(result[0])
        else:
            print("Phone number not found .")


text_analyzer=Text_Analyzer()
while True:
        print("---------------------- Text Analyzer ----------------------")
        print("1. Input text")
        print("2. Print  Numbers in text")
        print("3. Print Words in text")
        print("4. Count of total words")
        print("5. Count of total numbers")
        print("6. Replace selected word ")
        print("7. Check whether a phone number exists ")
        print("8. Exit ")
        print("-----------------------------------------------------------")
        choice=input("Enter your choice :")
        if choice == '1':
            text_analyzer.input_text()
        elif choice == '2':
            text_analyzer.all_numbers()
        elif choice == '3':
            text_analyzer.all_words()

        elif choice == '4':
            text_analyzer.total_words()

        elif choice == '5':
            text_analyzer.total_numbers()

        elif choice == '6':
            text_analyzer.reflace_seleted_word()

        elif choice == '7':
            text_analyzer.phone_number_exists()

        elif choice == '8':
            print("Program ended .")
            break
        else:
            print("Invalid input")


    
