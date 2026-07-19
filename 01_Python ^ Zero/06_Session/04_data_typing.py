from datetime import datetime

datetime_1 = "2026-05-08 10:00"
datetime_2 = "2026-05-08 11:30"

print(type(datetime_1), type(datetime_2)) # str, str
try:
    print(datetime_2 - datetime_1) # Error
except TypeError as error:
    print(error)

datetime_1 = datetime.strptime(datetime_1, '%Y-%m-%d %H:%M')
datetime_2 = datetime.strptime(datetime_2, '%Y-%m-%d %H:%M')

print(type(datetime_1), type(datetime_2)) # datetime, datetime
print(datetime_2 - datetime_1) # Not Error