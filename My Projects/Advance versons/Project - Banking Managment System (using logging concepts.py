import logging
import json

file=logging.FileHandler("Bank.log")

terminal=logging.StreamHandler()

file_formatter=logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

file.setFormatter(file_formatter)

file.setLevel(logging.DEBUG)

terminal.setLevel(logging.INFO)

logging.basicConfig(handlers=[file,terminal], level= logging.DEBUG)

logger=logging.getLogger(__name__)
class Bank:
    def __init__(self):
        self.account="Bankdetails.json"

        self.account_number = 0

        self.holder_name = ""

        self.balance = 0

        self.bank_account=[]

        try:
            with open(self.account,'r') as file:

                self.bank_account=json.load(file)

        except FileNotFoundError:
            logger.warning("Bankaccount.jsonfile not found so continuing with empty bankaccount .")
            self.bank_account=[]

        except json.JSONDecodeError:
            logger.warning("bankdetails .json contain invlid details .")

            self.bank_account=[]

    def save_to_file(self):
        try:
          with open (self.account,'w') as file:
             json.dump(self.bank_account,file,indent=4)

             logger.info("Save data succesflly .")

        except OSError:

            logger.exception("Fail to save bank data .")
        

    def create_account(self):
        logger.info("Creating Acccount ....")
        while True:
            self.account_number=input("Enter holder account  number : or enter stop to exist :")

            if self.account_number == 'stop':
                break
               
            if not self.account_number.isdigit():
                logger.warning("Account number must be digit .")
                continue
                   
            if not len(self.account_number) == 4 :
                logger.warning("Length of account number must be 4 ")
                continue

            found=False

            for num in self.bank_account:
                if num["AccountNumber"] == self.account_number:
                    found=True

            if found:
                logger.warning("Account number already exists .")
                continue  

            while True:
                
                self.holder_name=input("Enter account holder name :").strip().title()

                if not self.holder_name.replace(" ","").isalpha():

                    logger.warning("Holder name must contain only alphabets  ")
                    continue

                break


            while True:
                try:
                    self.balance=input("Enter balance :")

                    if self.balance == "":
                        logger.warning(" empty input not allowed .")
                        continue

                    self.balance = float(self.balance)
                    break

                except ValueError:

                    logger.warning("Invalid input for float() ")
                    continue

            self.bank_account.append(
                {
                "AccountNumber" : self.account_number,
                "AccountHolder" : self.holder_name,
                "Balance"      : self.balance
            }
            )

            logger.info(
                        f"Account {self.account_number} created successfully."
                       )
            
            self.save_to_file()

    def deposite(self):
        logger.info("Depositing Request ....")

        while True:

            number=input("Enter accout number :")

            if not number.isdigit() or len(number) != 4 :
                logger.warning("Account number must be  4 digit .")
                continue

            found=False

            for num in self.bank_account:
                if num["AccountNumber"] == number:
                   found=True
                   break

            if not found:
                logger.warning("Account number not found .")
                return
            
            while True:
                try:
                    amount=input("Enter amount to deposite :")

                    if amount == "":
                        logger.warning("amount must not be empty ")
                        continue

                    amount=float(amount)

                    if amount <= 0:
                        logger.warning("Amount must not be negitive .")
                        continue   

                except ValueError:
                    logger.warning("Invalid input for float() ")
                    continue

                
                num["Balance"]+=amount

                logger.info("Amount deposite succesfully .")

                print("New balance is :",num["Balance"])

                self.save_to_file()
                break
            break

    def withdraw(self):
        logger.info("Widrawel Request ......")

        while True:
            number=input("Enter account number :")

            if not number.isdigit() or len(number) !=4 :
                logger.warning("Account number must be 4 digit .")
                continue

            found=False
            for account in self.bank_account:

                if account["AccountNumber"] == number:
                    found=True
                    break

            if not found:
                logger.warning("Account number not found .")
                return
            
            while True:
                try:
                    amount=input("Enter amount to withdraw :")

                    if amount == "":
                        logger.warning("Amount must not be empty .")
                        continue

                    amount=float(amount)

                    if  amount < 0 or amount == 0:
                        logger.warning("Amount must not be negitive or zero.")
                        continue
                    
                    if amount > account["Balance"]:
                        logger.warning("not anough funds in account .")
                        continue

                except ValueError:
                    logger.exception("Invalid input for float() .")
                    continue

                account["Balance"]-=amount

                logger.info("Amount withdraw succesfully .")

                print("Now balance is :",account["Balance"])

                self.save_to_file()
                break
            break

    def check_balance(self):
        logger.info("Cheking Balance ....")

        while True:
            number=input("Enter account number :")

            if not number.isdigit() or len(number) !=4 :
                logger.warning("Account number must be 4 digit .")
                continue

            found=False

            for account in self.bank_account:
                if number == account["AccountNumber"]:
                    found=True
                    break

            if found:
                logger.info("Acount found .")
                print("Account Balance is :",account["Balance"])
                break

            logger.warning("Account number not found.")
            return

    def serach_account(self):
        logger.info("Searching for account ....")

        while True:
            number=input("Enter account number :")

            if not number.isdigit() or len(number) !=4 :
                logger.warning("Account number must be 4 digit .")
                continue

            found=False

            for account in self.bank_account:

                if number == account["AccountNumber"]:
                    found=True
                    print("--------------- Account Details ---------------")
                    print(f"AccountNumber      :     {account["AccountNumber"]}")
                    print(f"HolderName         :     {account["AccountHolder"]} ")
                    print(f"Blance             :     {account["Balance"]}\n")
                    
            if not found:
               logger.warning("Account number not found.")
               return
                    

        

                         

bank=Bank()
while True:
    print("--------------- Bank Account ------------------")
    print("1. Create Account")
    print("2. Deposite ")
    print("3. Withdraw ")
    print("4. Check balance ")
    print("5. Search Account")
    print("6. Exit")
    print("----------------------------------")
    choice=input("Enter your choice :")
    if choice == '1':
        bank.create_account()

    elif choice == '2':
        bank.deposite()

    elif choice == '3':
        bank.withdraw()

    elif choice == '4':
        bank.check_balance()

    elif choice == '5':
        bank.serach_account()

    elif choice == '6':
        logger.info("Program ended .")
        break

    else:
        logger.warning("Invalid inpur . try again ! ..")
        