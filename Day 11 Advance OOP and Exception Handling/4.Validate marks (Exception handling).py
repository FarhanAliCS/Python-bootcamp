def marks_validation():
    try :
        marks=int(input("Enter marks :"))
        if not (0 <=marks <=100):
            raise ValueError("Invalid marks .Enter marks between 1 - 100")

    except ValueError as e:
            print("Error :",e)
    else:
        print("Marks is :",marks)
    finally:
        print("Program ended .")


marks_validation()
    