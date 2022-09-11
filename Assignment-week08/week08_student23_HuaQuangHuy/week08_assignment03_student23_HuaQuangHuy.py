# tao data frame
from time import strftime
import pandas as pd
import datetime
from random_timestamp import random_timestamp


dateTime = []
dates = []
for i in range(0, 1000):
    randomDay = random_timestamp(2022)
    dateTime.append(randomDay)
    dates.append(f"{randomDay.year}-{randomDay.month}-{randomDay.day}")
data = pd.DataFrame({
    'timestamp': dateTime,
    'date': dates
})
print(data)
