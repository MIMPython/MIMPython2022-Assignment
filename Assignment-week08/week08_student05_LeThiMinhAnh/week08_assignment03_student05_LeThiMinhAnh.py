import pandas as pd
import radar

startDate = "01-01-2022 00:00:00"
stopDate = "12-31-2022 23:59:59"

data = {"timestamp": []}
for i in range(1000):
    data["timestamp"].append(radar.random_datetime(
        startDate, stopDate).strftime("%m-%d-%Y %H:%M:%S"))
data["date"] = [data["timestamp"][i].split(" ")[0] for i in range(1000)]

df = pd.DataFrame(data)
print(df)
'''
               timestamp        date
0    06-13-2022 10:53:33  06-13-2022
1    08-31-2022 02:05:58  08-31-2022
2    03-16-2022 23:21:46  03-16-2022
3    03-09-2022 12:05:34  03-09-2022
4    04-16-2022 15:44:37  04-16-2022
..                   ...         ...
995  09-13-2022 00:31:42  09-13-2022
996  08-23-2022 19:05:24  08-23-2022
997  12-26-2022 15:18:44  12-26-2022
998  04-02-2022 20:24:54  04-02-2022
999  02-11-2022 23:32:53  02-11-2022

[1000 rows x 2 columns]
'''

df.to_csv("DatetimeData.csv", index=False)
