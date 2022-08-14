# importing necessary libraries
import math
from datetime import date,timedelta

#Some initial values
F = 7.24
B = []
date_1 = date(2022,8,7)

print(f'On {date_1}, the stock price is {F}')

#Using while loop
while F < 58.69*(100/107):
    F = F * (107/100)
    B.append(F)

#Concluding the ending date
date_2 = date_1 + timedelta(days = len(B))

print(f'The stock price would get to {round(F,2)} on {date_2}')