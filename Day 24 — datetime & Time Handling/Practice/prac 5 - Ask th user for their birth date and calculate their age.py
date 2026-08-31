import datetime as dt
today=dt.datetime.now()

birth_date=input("Enter your birth date :")

birth=dt.datetime.strptime(birth_date,"%d - %m - %Y")

difference= today.year - birth.year

if (birth.month > today.month) or ( birth.month == today.month and birth.day > today.day):
    difference-=1
    
print(difference)

