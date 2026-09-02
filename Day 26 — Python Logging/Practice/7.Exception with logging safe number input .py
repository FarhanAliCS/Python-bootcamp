import logging
import random
logging.basicConfig(filename=("number.log"),level=logging.DEBUG,format="%(asctime)s - %(levelname)s - %(message)s ")

def guess(number):
    try:
        num=int(input("Enter number :"))

    except ValueError:

        logging.exception("Invalid input for int() ")

        return

    if num == number:
        logging.info("Your guess is right .")

        print("You guess it .")
    else:
        logging.warning("You guess is not right")

        print("wrong guess .")

        print("Secreat number is ",number)

secreat=random.randint(1,20)
guess(secreat)