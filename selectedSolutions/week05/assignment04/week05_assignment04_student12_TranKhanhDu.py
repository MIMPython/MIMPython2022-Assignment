#to reach the value 58.69 from value 7.24 in the fastest way, absolutely, the stock must increase 
#so fast as possible, it means that the stock must increase 107 percent per day 
import datetime
beginDay = datetime.datetime(2022, 8, 7)
increaseRate = 56.89/7.24
print(increaseRate)
daysToReach = 0
while(increaseRate  > 1):
    increaseRate = increaseRate / 1.07
    daysToReach += 1

reachedDay = beginDay + datetime.timedelta(days = daysToReach)
print("the soonest day from " + str((beginDay.strftime('%d/%m/%Y'))) + " for the stock to reach 58.69 is " + str((reachedDay.strftime('%d/%m/%Y'))))
