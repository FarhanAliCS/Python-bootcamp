import logging

# Terminal = WARNING - Low balance

# file = 2026-09-01 18:45:20 - WARNING - Low balance

file=logging.FileHandler("bank.log")
consol=logging.StreamHandler()
formatter_for_file=logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file.setFormatter(formatter_for_file)
logging.basicConfig(handlers=[file,consol],level=logging.INFO)
logger=logging.getLogger(__name__)

def withdraw():
    balance=1000
    logger.info("Bank operation start .")

    try: 
        amount= int(input("Enter amount to deposite :"))

    except ValueError:
        logger.exception("invalid input for int()")
        return
    
    if amount > balance:

        logger.warning("low balance ")

    balance-=amount

    logger.info("Balance withdraw succesfully .")
    print("New balance :",balance)

withdraw()
        

