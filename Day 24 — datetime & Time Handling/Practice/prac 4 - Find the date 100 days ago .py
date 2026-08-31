import datetime as dt
today=dt.date.today()

future=today - dt.timedelta(days=100)

print( "100 Day ago date :", future)