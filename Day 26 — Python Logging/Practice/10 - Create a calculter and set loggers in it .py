import logging

file=logging.FileHandler("cal.log")
consol=logging.StreamHandler()

formatter=logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
logging.basicConfig(handlers=[file,consol],level=logging.INFO)

def addition():
    try:
        num1=int(input("Enter num 1 :"))
    except ValueError:
        logging.exception("Invalid input for int()")
        return

    try:
        num2=int(input("Enter num 2 :"))
    except ValueError:
        logging.exception("Invalid input for int() ")
        return

    logging.info("Calculation started ....")

    result=num1+num2

    logging.info("Calculation ended ....")

    print(" Result : ",result)

def subtraction():

    try:
        num1=int(input("Enter num 1 :"))

    except ValueError:
        logging.exception("Invalid input for int()")
        return

    try:
        num2=int(input("Enter num 2 :"))
    except ValueError:
        logging.exception("Invalid input for int() ")
        return
    
    logging.info("Calculation started ....")

    result=num1+num2

    logging.info("Calculation ended ....")

    print(" Result : ",result)

def divison():
    try:
        num1=float(input("Enter num 1 :"))
    except ValueError:
        logging.exception("Invalid input for int()")
        return

    try:
        num2=float(input("Enter num 2 :"))
    except ZeroDivisionError:
        logging.exception("Zero divison error occur .")
        return
    except ValueError:
        logging.exception("Invalid input for int() ")
        return

    if abs(num2) < 1 :

        logging.warning("domenator is too small .")

    logging.info("Calculation started ....")

    result=num1/num2

    logging.info("Calculation ended ....")

    print(" Result : ",result)

while True:
    print(" ----------------- Calculator -------------")
    print("1. Addition ")
    print("2. Subtraction ")
    print("3. Divison ")
    print("4. exit")
    print("-------------------------------------------")
    choice=input("Enter your choice :")
    if choice == '1':
        addition()

    elif choice == '2':
        subtraction()

    elif choice == '3':
        divison()

    elif choice == '4':
        break

    else:
        logging.warning("Invalid inpur . try again ")     