import random
import time
import datetime
import numpy as np
import pandas as pd

startTime = time.time()
timeData = pd.DataFrame({'timestamp':[], 'date':[]})
for i in range(0, 1000):
    list = []
    randomDatetime = datetime.datetime(2022, random.randint(1, 12), random.randint(1, 28), random.randint(0, 23), random.randint(0, 59), random.randint(0, 59))
    randomDate = datetime.date(randomDatetime.year, randomDatetime.month, randomDatetime.day)
    list.append(randomDatetime)
    list.append(randomDate)
    timeData.loc[len(timeData)] = list
endTime = time.time()
processingTime = endTime - startTime
print(timeData)

print('processingTime: ' + str(processingTime))

