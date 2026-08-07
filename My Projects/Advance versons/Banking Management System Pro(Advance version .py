import json
class Bank:
    def __init__(self):
        
        try:
            self.data="Bank Management system.json"
            with open(self.data,'r') as file:
                self.accounts=json.load(file)
        except (FileNotFoundError,json.JSONDecodeError ):
            self.accounts={}

    def save_to_file(self):
        with open(self.data,'w') as file:
            json.dump(self.accounts,file,indent=4)

    def display_info(self,number,details):
            print(f"\nAccount Number    :    {number}")
            print(f"UserName          :    {details["UserName"]}")
            print(f"Balance           :    {details["Balance"]}")
            print(f"Transactions      :     {details["Transactions"]}")

    def validate_number(self,account_no):
                if not account_no.isdigit():
                    raise ValueError("Account number must contain digits .")
                if len(account_no) != 4:
                    raise ValueError ("Account number length must be 4 digit .")

    def validate_amount(self,amount):
                  if amount <= 0 :
                      raise ValueError("Amount must be greater them zero .")
                  
    def add_account(self):
        while True:
            try:
                account_no=input("Enter account number : or enter (stop) to exit :")
                if account_no.lower() == 'stop':
                    break
                self.validate_number(account_no)
                if account_no in self.accounts:
                   print("Accounts already exists .")
                   continue
            except ValueError as e :
                print("Error :",e)
                continue
            while True:
                try:
                    pin=input("Enter account pin :")
                    if not pin.isdigit():
                        raise ValueError("Pin must be digit .")
                    if not len(pin) == 4 :
                        raise ValueError("length of pin must be equal to 4")
                except ValueError as e:
                    print("Error :",e)
                    continue
                else:
                    break

            while True:
                try:
                    name=input("Enter user name :").strip().title()
                    
                    if not name.replace(" ","").isalpha():
                        raise ValueError ("Integer and special character not accepted in name .")
                    if not len(name) >= 4:
                        raise ValueError("length must be atlest 4 character .")
                except ValueError as e:
                    print("Error :",e)
                    continue
                else:
                    break

            while True:
                try:
                    balance=int(input("Enter balance :"))
                    if balance < 0:
                        raise ValueError ("Balance must be greater then zero .")
                    else:
                        break
                except ValueError as e:
                    print("Error :",e)
                    continue
            transactions=[]

            self.accounts[account_no]={
                "UserName"  :  name,
                "Pin"  : pin,
                "Balance" : balance,
                "Transactions" : transactions
            }
            self.save_to_file()
            print("Account add succesfully .\n")
    def show_accounts(self):
        if not self.accounts:
            print("Empty accounts dictionary .")
            return
        count=0
        for number,details in self.accounts.items():
            count+=1
            print("==== Account :",count," =====")
            print(f"Account Number    :    {number}")
            print(f"UserName          :    {details["UserName"]}")
            print(f"Balance           :    {details["Balance"]}")
            print(f"Transactions      :    {details["Transactions"]}")


    def search_account(self):
        if not self.accounts:
            print("Empty accounts dictionary .")
            return
        while True:
            try:
                search=input("Enter account number :")
                self.validate_number(search)
            except ValueError as e:
                print("Error :",e)
            else:
                if search not in self.accounts:
                    print("Not found .")
                    break
                details=self.accounts[search]
                self.display_info(search,details)
                break

    def delete_account(self):
        if not self.accounts:
            print("Empty accounts dictionary .")
        while True:
            try:
                number=input("Enter account number to delete your account .")
                self.validate_number(number)
            except ValueError as e:
                print("Error :",e)
                continue
            else:
                if not number in self.accounts:
                    print("Account not found .")
                    break
    
                while True:
                    try:
                        sure=input("Are you sure you want to delete account yes/no :")
                        if sure.lower() == 'yes':
                            del self.accounts[number]
                            self.save_to_file()
                            print("Account delete succesfully .")
                        print("Account not deleted")
                        break
                    except ValueError as e:
                        print("Error .",e)
                        break
                break

    def login_account(self):
        if not self.accounts:
            print("Empty accounts dictionary .")
            return
        while True:
            try:
                number=input("Enter account number :")
                self.validate_number(number)
                if number not in self.accounts:
                    raise ValueError("Number not in accounts .")
            except ValueError as e:
                print("Error :",e)
                continue
            while True:
                try:
                    pin=input("Enter account pin :")
                    if pin == self.accounts[number]["Pin"]:
                        print(f"========== Welcome {self.accounts[number]["UserName"]} ===========")
                        self.current_account=number
                        self.dashboard()
                        return
                    raise ValueError("Incorrect pin .")
                except ValueError as e:
                    print("Error :",e)
                    continue
    def wihdraw(self):
        while True:
            try:
                amount=int(input("Enter amount to wihdraw :"))
                self.validate_amount(amount)
                details=self.accounts[self.current_account]
                balance=details["Balance"]
                if amount > balance:
                    raise ValueError("Insaficiant balance .")
            except ValueError as e:
                print("Error :",e)
                continue
            else:
                balance-=amount
                details["Balance"]=balance
                details["Transactions"].append(f"Withdraw : Rs {amount}")
                print("Now current balance is :",details["Balance"])
                self.save_to_file()
                print("Withdraw succesfully .")
                break

    def deposite(self):
          
          while True:
            try:
                amount=int(input("Enter amount to deposite :"))
                self.validate_amount(amount)
                details=self.accounts[self.current_account]
                balance=details["Balance"]
            except ValueError as e:
                print("Error :",e)
                continue
            else:
                balance+=amount
                details["Balance"]=balance
                details["Transactions"].append(f"Deposite : Rs {amount}")
                print("Now current balance is :",details["Balance"])
                self.save_to_file()
                print("Deposite succesfully .")
                break
    def transfer_money (self):
        while True:
            try:
                recever=input("Enter recever account no :")
                self.validate_number(recever)
                if recever not in self.accounts:
                    raise ValueError("recever account not found  .")
                if recever == self.current_account:
                    raise ValueError("Accounts must be different .")
            except ValueError as e:
                print("Error :",e)
                continue

            while True:
                try:
                    amount=int(input("Enter amount to transfer :"))
                    self.validate_amount(amount)
                    sender_details=self.accounts[self.current_account]
                    balance=sender_details["Balance"]
                    if amount > balance:
                        raise ValueError("Insaficiant balance .")
                except ValueError as e:
                    print("Error :",e)
                    continue
                else:
                    balance -= amount
                    sender_details["Balance"]=balance
                    recever_details=self.accounts[recever]
                    recever_details["Balance"]+=amount
                    sender_details["Transactions"].append(f"send Rs {amount} to account {recever} .")
                    recever_details["Transactions"].append(f"Receive Rs {amount} from account {self.current_account} .")
                    self.save_to_file()
                    print("Transaction perform succesfully .")
                    return
    def transactions(self):
        print("======= Transactions ========")
        for t in self.accounts[self.current_account]["Transactions"]:
            print(t)
                

    def show_details(self):
        if not self.accounts:
            print("Empty accounts dictionary .")
            return
        details=self.accounts[self.current_account]
        self.display_info(self.current_account,details)


                    
    def dashboard(self):
        while True:
            print("== Account Menu ==")
            print("1. Withdraw ")
            print("2. Deposite")
            print("3. Tranafar money ")
            print("4. Show details ")
            print("5. Transactions")
            print("6. Exit ")
            choice =input("Enter your choice :")
            if choice == '1':
                self.wihdraw()
            elif choice == '2':
                self.deposite()
            elif choice == '3':
                self.transfer_money()
            elif choice == '4':
                self.show_details()
            elif choice == '5':
                self.transactions()
            elif choice == '6':
                print("Program ended .\n")
                break
            else:
                print("Invalid choice . Try again! ")
        
                





# =====================#
#     Account          #
#======================#

account_info=Bank()
while True:
    print("=============== Banking Management System ===================")
    print("1. Create Account ")
    print("2. Delete Account ")
    print("3. Search Account ")
    print("4. Login Account ")
    print("5. Show all accounts")
    print("6. Exit ")
    print("===========================================================")
    choice =input("Enter your choice :")
    if choice == '1':
        account_info.add_account()
    elif choice == '2':
        account_info.delete_account()
    elif choice == '3':
        account_info.search_account()
    elif choice == '4':
        account_info.login_account()
    elif choice == '5':
        account_info.show_accounts()
    elif choice == '6':
        print("program ended .")
        break
    else:
        print("Invalid choice .")

            
                    



                    





            

            

