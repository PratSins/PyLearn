from datetime import datetime

datetime1 = datetime(2021,11,3,22,0)
datetime2 = datetime(2020,11,3,12,0)

date_diff = datetime1 - datetime2
print(date_diff)
print(type(date_diff))

print()
print(date_diff.seconds)
print(date_diff.total_seconds())