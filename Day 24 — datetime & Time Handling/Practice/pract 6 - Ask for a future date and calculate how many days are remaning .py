import datetime as dt
today= dt.datetime.now()
future_date=input("Enter future date :")
future_date=dt.datetime.strptime(future_date, "%d-%m-%Y")
difference=future_date - today
print("Days remaning :" ,difference.days)