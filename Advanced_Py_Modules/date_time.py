import datetime

mytime  = datetime.datetime.now()
print("\ncurrent time = ",mytime)
print("current month = ",mytime.month)

myt = datetime.time(2,20) # 2 hours and 20 mins
print("\nmyt = ",myt)

print("myt.minute = ",myt.minute)
print("myt.hour = ",myt.hour)
print("myt.second = ",myt.second)

myt = datetime.time(2,20,11,22)
print("\nnew myt = ",myt)
print("myt.microsecond = ",myt.microsecond)

today  = datetime.date.today()
print("\ntoday = ", today)
print("today.year = ", today.year)
print("today.month = ", today.month)
print("today.day = ", today.day)
print("today.ctime() = ", today.ctime())