from random import randrange
from datetime import timedelta
from datetime import datetime
import pandas as pd
import numpy as np

# Get random timestamp 
def getRandomDate(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

date1 = datetime.strptime('1/1/2022 1:00 AM', '%m/%d/%Y %I:%M %p')
date2 = datetime.strptime('12/30/2022 1:00 AM', '%m/%d/%Y %I:%M %p')

# Create timestamp list
timestamp = [None]*1000
for i in range(1000):
    timestamp[i] = getRandomDate(date1, date2)

# Create the dataframe
df = pd.DataFrame(timestamp, columns=['timestamp'])

# Create only date column
date = []

for i in df['timestamp']:
    date.append(i.date())

# Add date column to df
df['date'] = date

print(df)

'''
              timestamp        date
0   2022-03-17 22:40:40  2022-03-17
1   2022-10-13 09:03:28  2022-10-13
2   2022-09-19 20:53:15  2022-09-19
3   2022-04-29 04:28:41  2022-04-29
4   2022-12-04 00:24:36  2022-12-04
..                  ...         ...
995 2022-05-14 19:53:39  2022-05-14
996 2022-04-01 04:46:56  2022-04-01
997 2022-04-12 09:07:04  2022-04-12
998 2022-05-26 06:19:26  2022-05-26
999 2022-10-26 00:42:30  2022-10-26     
'''




