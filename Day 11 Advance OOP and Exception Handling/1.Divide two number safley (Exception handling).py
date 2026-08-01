def divide():
    while True:
        try:
            num1=int(input("Enter num1 :"))
            num2=int(input("Enter num2 :"))
            result=num1/num2

        except ValueError:
           print("invild input")
           continue
        except ZeroDivisionError:
            print("zero not divisible .")
            continue

        else:
           print("result :",result)
        
        finally:
           print("Program end .")

divide()
       
    

