import pandas as pd
from datetime import datetime
import random as rd

temp = range(1641000000, 1662877730)
# 1641000000 ứng với: 2022-01-01 08:20:00
# 1662877730 ứng với: 2022-09-11 13:28:50
timestamp = rd.choices(temp, k=1000)
date_time = [datetime.fromtimestamp(i) for i in timestamp]
data = pd.DataFrame(date_time, columns=['Timestamp'])
date = [i.strftime('%Y-%m-%d') for i in date_time]
data['Date'] = date
print(data)
print(data.dtypes)

# # Output:
#               Timestamp        Date
# 0   2022-04-26 23:45:48  2022-04-26
# 1   2022-08-02 01:19:40  2022-08-02
# 2   2022-04-16 20:45:05  2022-04-16
# 3   2022-03-04 09:05:09  2022-03-04
# 4   2022-03-05 12:46:22  2022-03-05
# ..                  ...         ...
# 995 2022-01-05 23:44:22  2022-01-05
# 996 2022-03-26 19:57:49  2022-03-26
# 997 2022-03-18 05:51:28  2022-03-18
# 998 2022-09-07 11:51:24  2022-09-07
# 999 2022-05-05 02:37:27  2022-05-05

# [1000 rows x 2 columns]
# Timestamp    datetime64[ns]
# Date                 object
# dtype: object