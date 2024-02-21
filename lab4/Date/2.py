import datetime 

today = datetime.datetime.now() 

yesterday = today - datetime.timedelta(days=1) 

tomorrow = today + datetime.timedelta(days=1) 

print(today ,end='\n') 
print(yesterday, end ='\n') 
print(tomorrow, end = '\n')