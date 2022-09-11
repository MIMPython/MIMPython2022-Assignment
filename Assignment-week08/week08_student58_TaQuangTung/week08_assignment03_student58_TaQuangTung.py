print("Bài 3: DataFrame Datetime Tricks")

from datetime import *
from random import randint
import pandas as pd

timestamp = []
dated = []
for i in range(1000):
    thang = randint(1, 12)
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        ngay = randint(1, 31)
    elif thang in [4, 6, 9, 11]:
        ngay = randint(1, 30)
    else:
        ngay = randint(1, 28)
    gio = randint(0, 23)
    phut = randint(0, 59)
    giay = randint(0, 59)
    dl = datetime(year = 2022, month = thang, day = ngay, hour = gio, minute = phut, second = giay)
    dy = date(year = 2022, month = thang, day = ngay)
    timestamp.append(dl)
    dated.append(dy)
# print(timestamp)
# print(dated)

df = pd.DataFrame({'timestamp': timestamp, 'date': dated})
print(df)
