from random import randint

def maxDayInMonth(month: int):
    if month == 2:
        return 28
    lessDay = [4,6,9,11]
    for i in lessDay:
        if month == i:
            return 3
    return 30
# f = open("additionalFolder\dataFame.txt","r+")
# a = f.read()
# # f.write(a)
f = open("additionalFolder\dataFame.txt","w")
f.write("{:>23}  {:>10}".format("timestamp","date"))
for line in range(1000):
    hh = randint(0,23)
    mm = randint(0,59)
    ss = randint(0,59)
    month = randint(1,12)
    day = randint(1,maxDayInMonth(month))
    date = "{:4}-{:02}-{:02}".format(2022,month,day)
    time = "{:02}:{:02}:{:02}".format(hh,mm,ss)
    data = "\n{:<3} {date:^} {time:^}  {date:^}"
    f.write(data.format(line, date = date, time = time))