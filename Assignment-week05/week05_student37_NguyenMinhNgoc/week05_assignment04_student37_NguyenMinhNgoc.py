import math
import datetime
days = int(math.log(58.69/7.25,1.07)) + 1
begin = datetime.date(2022, 8, 7)
print(begin +  datetime.timedelta(days = days))