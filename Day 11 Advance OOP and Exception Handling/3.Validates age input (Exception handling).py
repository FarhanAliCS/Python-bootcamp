def Age_Validation():
    try:
        age=int(input("Enter Your age :")) 
        if age <=0:
            raise ValueError("Invalid age .")
    except ValueError:
        print("Invalid input .")
    except Exception as e:
        print("Errot :",e)
    else:
        print(age)
    finally:
        print("Program end .")

Age_Validation()
            
                
    