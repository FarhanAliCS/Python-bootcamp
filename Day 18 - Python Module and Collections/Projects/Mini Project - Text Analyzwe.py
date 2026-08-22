import collections
class Text_analyzer:
    def __init__(self):
        self.sentence=""
        
    def get_sentence(self):
        while True:
            self.sentence=input("Enter sentence :")
            if  self.sentence == "":
                print("Empty sentence no allowed .")
                continue
            return self.sentence
            

    def words_in_sentence(self):
    
        if not self.sentence:
            print("First enter sentence .")
            return
        sentence=self.sentence.replace(".","")

        words=sentence.lower().split()

        counts=collections.Counter(words)
        print("------ Count of words ------")
        for word , count in counts.most_common():
            print(word ,":", count)

    def char_in_sentence(self):
         if not self.sentence:
             print("First enter sentence .")
             return
         sentence=self.sentence.replace(".","").replace(" ","")
         print("------ Count of characters  ------")
         count=collections.Counter(sentence)
         for word , count in count.most_common():
            print(word ,":", count)

    def common_words(self):

        if not self.sentence:
            print("First enter sentence .")
            return
        sentence=self.sentence.replace(".","")

        words=sentence.lower().split()

        counts=collections.Counter(words)
        print("------ Top 3 most common words ------")
        for word , count in counts.most_common(3):
            print(word ,":", count)
    
    def count_of_vowel(self):
        if not self.sentence:
            print("First enter sentence .")
            return

        vowel="aeiou"
        sentence=self.sentence.lower().replace(" ","")
        characters=collections.Counter(sentence)
        characters=characters.most_common()
        print("---------------- Vowel and their counts in sentence ---------------")
        for char ,count in characters:
          if char in vowel:
            print(char, ":" ,count)

    def count_conconant(self):
        if not self.sentence:
            print("First enter sentence .")
            return
        vowel="aeiou"
        sentence=self.sentence.lower().replace(" ","")
        characters=collections.Counter(sentence)
        characters=characters.most_common()
        print("---------------- consonant and their counts in sentence ---------------")
        for char ,count in characters:
          if char.isalpha() and char not in vowel:
            print(char, ":" ,count)

    def total_vowel(self):
        if not self.sentence:
            print("First enter sentence .")
            return
        sentence=self.sentence.lower().replace(" ","")
        characters=collections.Counter(sentence)
        characters=characters.most_common()
        print("---------------- Count of vowel in sentence ---------------")
        total=0
        for char ,count in characters:
          if char in "aeiou":
              total+=count
        print("Total vowel :",total)

    def total_consonants(self):
            if not self.sentence:
                print("First enter sentence .")
                return
            sentence=self.sentence.lower().replace(" ","")
            characters=collections.Counter(sentence)
            characters=characters.most_common()
            print("---------------- Count of consonant in sentence ---------------")
            total=0
            for char ,count in characters:
                if  char.isalpha() and char not in "aeiou":
                    total+=count
            print("Total consonant :",total)
                
    
              
        

    def total_words(self):
        if not self.sentence:
            print("first enter sentence .")
            return
        words=self.sentence.replace(".","").split()
        print("Total words :",len(words))

    def  largest_word(self):
        if not self.sentence:
            print("first enter sentence .")
            return
        words=self.sentence.replace(".","").split()
        largest_word=float("-inf")
        for i in words:
            if len(i) > largest_word:
                largest_word=len(i)
                word=i
        print("largest word :",word)
        print("length is  :",largest_word)
            









        




        

        

    


text_analyzer=Text_analyzer()
while True:
    print("---------- TEXT ANALYZER ------------")
    print("1. Input Sentence ")
    print("2. Counts words")
    print("3. Counts characters ")
    print("4. Moste common words")
    print("5. Total words")
    print("6. Count of vowel and consonant")
    print("7. Consonant count .")
    print("8. Total vowels")
    print("9. Total consonant")
    print("10. Largest word in sentence .")
    print("11. Exit ")
    print("-------------------------------------")
    choice=input("Enter your choice :")
    
    if choice == '1':
      text_analyzer.get_sentence()

    elif choice == '2':
        text_analyzer.words_in_sentence()

    elif choice == '3':
        text_analyzer.char_in_sentence()

    elif choice == '4':
        text_analyzer.common_words()

    elif choice == '5':
        text_analyzer.total_words()

    elif choice == '6':
        text_analyzer.count_of_vowel()

    elif choice == '7':
        text_analyzer.count_conconant()

    elif choice == '8':
        text_analyzer.total_vowel()

    elif choice == '9':
        text_analyzer.total_consonants()

    elif choice == '10':
         text_analyzer.largest_word()

    elif choice == '11':
        print("program ended .")
        break
    else:
        print("Invalid input .")



    








