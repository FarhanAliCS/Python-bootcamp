import logging
logging.basicConfig(filename="info.log", level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

def addition(a,b):

    logging.info("Calculatin start .")

    print("Result =",a+b)

    logging.info("Calculation ended .")


addition(12,34)


