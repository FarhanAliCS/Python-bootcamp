import logging
logging.basicConfig(filename="division.log", level=logging.INFO , format="%(asctime)s - %(levelname)s - %(message)s")

def division(num1,num2):
    try:
        num1=float(input("Enter num 1 :"))
    except ValueError:
        logging.exception("invild input for float()")
        return
    try:
        num2=float(input("Enter num 2 :"))
    
    except ValueError:
        logging.exception("invild input for float()")
        return

    logging.info("Calculation started succesfully .")
    if num2 == 0:
        logging.error("Zero divison error occur .")
        return

    if abs(num2) < 1 :
        logging.warning("Domenator is very small number .")

    result = num1 / num2

    logging.info("Calculation complete succesfully .")

    print("Result :",result)




division(12,0)
    

    
        