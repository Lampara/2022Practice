import datetime

now = datetime.datetime.now()
print("Current data and time : ")
print(now)
print("Other")
print(now.strftime("%Y-%m-%d %H:%M:%S"))