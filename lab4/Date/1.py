import datetime
today = datetime.datetime.now()
five_days_ago = today - datetime.timedelta(days=5)
print(five_days_ago.strftime("%Y-%m-%d"))
