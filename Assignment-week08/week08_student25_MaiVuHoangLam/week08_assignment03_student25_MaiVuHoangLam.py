import datetime
import pandas as pd
import random as rd

df = pd.DataFrame({
    'timestamp': []
})

first_date = datetime.datetime(2022, 1, 1, 0, 0, 0)

for index in range(1000):
    df.loc[index] = first_date + datetime.timedelta(days=rd.randint(0, 364), seconds=rd.randint(0, 86400))

date = []
for index in range(1000):
    date.append(df['timestamp'][index].date())
df['date'] = date



