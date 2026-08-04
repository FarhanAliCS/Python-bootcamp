class Calculator:
    def __init__(self):
        self.FILE='History.txt'
        
    def show_histry(self):  
        try:
          with open(self.FILE,'r') as file:
            data =file.readlines()
            if not data:
                  print("No histry found .")
                  return
            print("==== HISTORY ===")
            for indix,i in enumerate(data,start=1):
                print(f"{indix}. {i}")
        except FileNotFoundError as e:
           print("Error :",e)

            

    def addition(self):
      try:
              num1=int(input("Enter num1 :"))
              num2=int(input("Enter num2:"))
              add= num1+num2
      except ValueError as e:
              print("Error :",e)
      else:
            with open(self.FILE,'a') as file:
               file.write(f"{num1} + {num2 } = {add}")
      return add

#subtraction
    def subtraction(self):
      try:
         num1=int(input("Enter num1 :"))
         num2=int(input("Enter num2:"))
         subtract= num1-num2
      except ValueError as e:
         print("Error :",e)
      else:
        with open(self.FILE,'a') as file:
               file.write(f"{num1} - {num2 } = {subtract}")
      return subtract

#Multiplication
    def multiplication(self):
      try:
                  num1=int(input("Enter num1 :"))
                  num2=int(input("Enter num2:"))
                  multiply= num1*num2
      except ValueError as e:
                  print("Error :",e)
      else:
          with open(self.FILE,'a') as file:
               file.write(f"{num1} x {num2 } = {multiply}")
      return multiply

#Division
    def division(self):
      try:
         num1=int(input("Enter num1 :"))
         num2=int(input("Enter num2:"))
         if num2 ==0:
                print("0 are not divisible .")
         div= num1/num2
      except ValueError as e:
                  print("Error :",e)
      else:
          with open(self.FILE,'a') as file:
               file.write(f"{num1} / {num2 } = {div}")
      return div
    def clear_history(self):
      open(self.FILE,'w').close()
      print("Histoty clear succesfully")

calculator=Calculator()
while True:
     print("\n========== Calculator MENU =============\n")
     print("1. Addition")
     print("2. Subtraction")
     print("3. Multiplication")
     print("4. Division")
     print("5. Show history")
     print("6. Claear hitory")
     print("7. Exit")
     print("=============================")
     choice =input("Enter your choice :")
     if choice == '1':
          print("result :",calculator.addition())
     elif choice == '2':
          print("result :",calculator.subtraction())
     elif choice == '3':
          print("result :",calculator.multiplication())
     elif choice == '4':
          print("result :",calculator.division())
     elif choice == '5':
          calculator.show_histry()
     elif choice == '6':
          calculator.clear_history()
     elif choice == '7':
          print("program ended .")
     else:
          print("Invalid input .")
          continue
     try:
            again=input('you want to perform another operation ? yes/no :')
            if again.lower() == 'yes':
                 continue
            else:
                 if again.lower()=='no':
                   print("Thanks for using calculator.")
                   break
     except ValueError as e:
            print("Error :",e)
            continue
     
  
            
    