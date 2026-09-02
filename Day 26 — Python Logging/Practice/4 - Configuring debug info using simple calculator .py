import logging

logging.basicConfig(level=logging.DEBUG)

def division(a,b):
    logging.info("Calculation Started .")

    if b == 0 :
        logging.error("Cannot divide by zero .")
        return

    if abs(b) < 1:

        logging.warning("Domenator is very small number .")

    result=a/b
    logging.info("Calculation completed .")

    print("Result :",result)



a=float(input("Enter num 1 :"))
b=float(input("Enter num 2 :"))
division(a,b)

    