Current_balance=int(input("Enter balance :"))
withdrawl_amount=int(input("Enter amount to withdraw :"))

if withdrawl_amount<=Current_balance:
    Current_balance=Current_balance-withdrawl_amount
    print("Amount withdraw :",withdrawl_amount,'\n\nNow balance is :',Current_balance)
else:
    print("Not enough fund .") 