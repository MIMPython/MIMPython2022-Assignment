import datetime
from math import *

str = "22/08/07"
d1 = datetime.datetime.strptime(str,"%y/%m/%d") #get str in class datetime

#Function take prices as a real number
def getTimeByFloatPrice():
    stockPrice = 7.24 #stock price in 07/08/2022
    day = 0
    while stockPrice < 58.69:
        stockPrice = stockPrice *1.07 #the real number 
        day += 1
    return(d1 + datetime.timedelta(days=day)) #add the numbers of days by using the variable day

#Function take prices as a number with two digits after decimal point
def getTimeByRoundPrice():
    stockPrice = 7.24 #stock price in 07/08/2022
    day = 0
    while stockPrice < 58.69:
        stockPrice = round(stockPrice*1.07,2) #the rounded real number with two digits after decimal point
        day += 1
    return(d1 + datetime.timedelta(days=day)) #add the numbers of days by using the variable day

if __name__ == '__main__':
    print(getTimeByFloatPrice())
    print(getTimeByRoundPrice())