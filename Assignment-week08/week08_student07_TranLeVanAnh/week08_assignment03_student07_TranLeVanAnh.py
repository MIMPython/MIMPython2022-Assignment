#Bài 3
from random import randrange
from datetime import datetime,date
import pandas as pd
table = []
table1 = []
for i in range (1000):
    months = randrange(1,13)
    if months in [1,3,5,7,8,10,12]:
        days = randrange(1,32)
    elif months in [2]:
        days = randrange(1,29)
    elif months in [4,6,9,11]:
        days = randrange(1,31)
    hours = randrange(0,24)
    minutes = randrange(0,60)
    seconds = randrange(0,60)
    col1 = datetime(year = 2022, month = months, day = days, hour = hours, minute = minutes, second = seconds)
    col2 = date(year = 2022, month = months, day = days)
    table.append(col1)
    table1.append(col2)
print(table)
print(table1)

data = pd.DataFrame({'timestamp': table, 'date': table1})
print(data)