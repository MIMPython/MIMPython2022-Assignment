import datetime
import math
# a)
Date1=datetime.date(2022,8,7)
i=0
F=7.24
while F<58.69 :
    F=F*107/100
    i+=1
Date2=Date1+datetime.timedelta(days=i)
print(Date2)
# b)
Date1=datetime.date(2022,8,7)
i=0
F=7.24
while F<58.69 :
    F=int((F*107/100)*(100))/(100)
    i+=1
Date2=Date1+datetime.timedelta(days=i)
print(Date2)