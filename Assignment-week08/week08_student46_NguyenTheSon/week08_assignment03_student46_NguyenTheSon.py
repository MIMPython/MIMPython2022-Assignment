# Bài 3:
from calendar import week
import pandas as pd 
import numpy as np 
import datetime
import random

# random_time_year_2022 = 
# data_frame = pd.DataFrame()
list_timestamp = []
list_date = []
for i in range(1000):
    week = random.randrange(1, 13)
    day =  random.randrange(1,29)
    hour = random.randrange(24)
    minute = random.randrange(60)
    second = random.randrange(60)

    random_time = datetime.datetime(2022, week, day, hour, minute, second)
    list_timestamp.append(random_time)
    
    date =  datetime.datetime(2022, week, day)
    list_date.append(date)

data_time = pd.DataFrame({'timestamp': list_timestamp})
data_time['date'] = list_date
print(data_time)
