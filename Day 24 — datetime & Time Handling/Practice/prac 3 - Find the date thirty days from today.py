import datetime as dt

today=dt.date.today()

future=today + dt.timedelta(days=10)

print("Date after 10 days :",future)