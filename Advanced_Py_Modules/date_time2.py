from datetime import datetime
from datetime import date


mydatetime = datetime(2021,10,3,14,20,1)
print (mydatetime)

mydatetime = mydatetime.replace(year=2020)
print (mydatetime)


date1 = date(2021,11,3)
date2 = date(2020,11,3)
print(date1)
print(date2)
date_diff = date1 - date2
print(date_diff)
print(date_diff.days)
print(type(date_diff))