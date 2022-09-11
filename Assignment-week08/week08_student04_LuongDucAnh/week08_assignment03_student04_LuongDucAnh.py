from randomtimestamp import randomtimestamp
import pandas as pd

datatimeList = []
for _ in range(1000):
    datatimeList.append(randomtimestamp(start_year=2022, end_year=2022))
    
data = pd.DataFrame({"timestamp": datatimeList})

dateList = []
for dt in datatimeList:
    dateList.append(dt.date())
    
data["date"] = dateList

print(data)
print(data.dtypes)