class Date:
    __day = 1
    __month = 1
    __year = 1

    def __init__(this,day=1,month=1,year=1):
        day,month,year = map(int,Date.correctDate(day,month,year))
        this.__day = day  
        this.__month = month   
        this.__year = year  

    def getDay(this):
        return this.__day

    def getMonth(this):
        return this.__month

    def getYear(this):
        return this.__year

    def setYear(this,year):
        this.__year = year
    
    def setMonth(this,month):
        this.__month = month

    def setDay(this,day):
        this.__day = day

    def setDate(this,day,month,year):
        this.__day = day  
        this.__month = month   
        this.__year = year  

    def getDate(this):
        return this.__day, this.__month  ,this.__year 

    def toString(this):
        day = (this.__day<10) and "0"+ str(this.__day) or str(this.__day)
        month = (this.__month<10) and "0"+ str(this.__month) or str(this.__month)
        if this.__year ==0:
            year = str(1)
        elif (this.__year)<0 :
            year =  str(abs(this.__year)) +"BC" 
        else: 
            year = str(this.__year)
        return "{}/{}/{}".format(day,month,year)

    @staticmethod
    def checkLeapYear(year):
        isLeapYear = year % 4 == 0
        isLeapYear = isLeapYear and (year % 100 != 0)
        isLeapYear = isLeapYear or (year % 400 == 0)
        return isLeapYear

    @staticmethod
    def maxDayMonth(month,year):
        leapYear = Date.checkLeapYear(year)
        dayInMonth = [4, 6, 9, 11 ]
        month,year = map(int,Date.corectMonthYear(month,year))
        if month == 2:
            if leapYear:
                return 29
            return 28
        elif month in dayInMonth:
            return 30
        return 31

    def maxDayYear(month,year):
        leapYear = Date.checkLeapYear(year)
        if leapYear:
            return 366
        return 365

    @staticmethod
    def correctDay(day,month,year):
        maxDay = Date.maxDayMonth(month,year)
        month,year = map(int,Date.corectMonthYear(month,year))
        if day>maxDay:
            day-=maxDay
            month,year = map(int,Date.corectMonthYear(month+1,year))
            maxDay = Date.maxDayMonth(month,year)
        if day <= 0:
            maxDay = Date.maxDayMonth(month-1,year)
            day+=maxDay
            month,year = map(int , Date.corectMonthYear(month-1,year))
        Date.setDate(Date,day,month,year)
        return day,month,year,maxDay

    @staticmethod
    def corectMonthYear(month,year):
        while month>12:
            year+=1
            month-=12
        while month <0:
            year-=1
            month+=12
        if month == 0:
            month =12
        return month,year
    
    @staticmethod
    def correctDate(day,month,year):
        month,year = Date.corectMonthYear(month,year)
        maxDay = Date.maxDayMonth(month,year)
        while day>maxDay:
            day,month,year,maxDay = map(int,Date.correctDay(day,month,year))
        while day<=0:
            day,month,year,maxDay = map(int,Date.correctDay(day,month,year))
        return day,month,year
    
    def changeDay(this,n=1,cal = "+"):
        if cal == "*":
            this.__day*=n
        elif cal == "/":
            this.__day//=n
        elif cal == "-":
            this.__day-=n
        else:
            this.__day+=n
        day,month,year = map(int,Date.correctDate(this.__day,this.__month,this.__year))
        this.setDate(day,month,year)
        return this

    def compareDay(this,date):
        fDay = this.__day
        fMonth = this.__month
        fYear = this.__year
        sDay,sMonth,sYear = map(int,Date.getDate(date))
        if sYear != fYear:
            return fYear>sYear and 1 or -1 
        elif sMonth != fMonth:
            return fMonth>sMonth and 1 or -1 
        elif sDay != fDay:
            return fDay>sDay and 1 or -1 
        return(0)

    def smaller(this,day):
        return this.compareDay(day)== -1 and this or day
    
    def bigger(this,sDay):
        return this.compareDay(sDay)== 1 and this or sDay
        
    def numberDay(this,date):
        this,date  = Date.smaller(this,date),Date.bigger(this,date)
        dayf,monthf,yearf =Date.getDate(this)
        days,months,years =Date.getDate(date)
        day,month,year = days - dayf,months - monthf,years - yearf

        while (year > 0):
            if this.getMonth() > 2:
                day += Date(date.getDay(), date.getMonth(), yearf + 1).maxDayYear(yearf)
            else:
                day += this.maxDayYear(yearf)
            yearf+=1
            year-= 1
        
        while (month > 0):
            if this.getMonth() > 2:
                day += Date(date.getDay(), date.getMonth(), monthf + 1).maxDayMonth(monthf,yearf)
            else:
                day += this.maxDayMonth(monthf,yearf)
            monthf+=1
            month-= 1

        return day

class DateTime(Date):
    __date = Date(1,1,1)
    __hour = 0
    __minute = 0
    __second = 0

    def __init__(this,hour=0,minute=0,second = 0,date = Date()):
        hour,minute,second,date = DateTime.correctTime(hour,minute,second,date)
        this.setTime(hour,minute,second,date)
    
    def getHour(this):
        return this.__hour

    def getMinute(this):
        return this.__minute

    def getSecond(this):
        return this.__second

    def setSecond(this,second):
        this.__second = second
    
    def setMinute(this,minute):
        this.__minute = minute

    def setHour(this,hour):
        this.__hour = hour

    def setTime(this,hour=0,minute=0,second=0,date=Date()):
        this.__hour = hour  
        this.__minute = minute   
        this.__second = second 
        this.__date = date

    def getTime(this):
        return this.__hour, this.__minute, this.__second 

    def getDate(this):
        return this.__date

    @staticmethod
    def correctTime(hour,minute,second,date):        
        while second <0: 
            second = 60 - abs(second)
            minute-=1

        while minute<0:
            minute = 60 - minute
            hour -= 1

        while hour < 0:
            hour = 24 - hour 

        minute+= second//60
        hour+=minute//60
        Date.setDay(date,Date.getDay(date)+hour//24)
        day,month,year = Date.getDate(date)
        day,month,year =Date.correctDate(day,month,year)
        second%=60
        minute%=60
        hour%=24
        Date.setDate(date,day,month,year)
        return hour,minute,second,date

    def nextTime(this,hour=1,minute=1,second=1,cal ="+"):
        if cal == "*":
            this.__hour *= hour
            this.__minute *= minute
            this.__second *= second
        elif cal == "/":
            this.__hour //= hour
            this.__minute //= minute
            this.__second //= second
        elif cal == "-":
            this.__hour -= hour
            this.__minute -= minute
            this.__second -= second
        this.__hour += hour
        this.__minute += minute
        this.__second += second
        return this

    def compareTime(this,time):

        if this.__date.compareDay(DateTime.getDate(time))!=0:
            return this.__date.compareDay(DateTime.getDate(time))

        hour,minute,second = DateTime.getTime(time)
        
        if this.__hour != hour:
            return this.__hour > hour and 1 or -1
        
        elif this.__minute != minute:
            return this.__minute > minute and 1 or -1

        elif this.__second != second:
            return this.__second > second and 1 or -1

        return 0

    def biggerTime(this, time):
        return this.compareTime(time)>0 and this or time

    def smallerTime(this, time):
        return this.compareTime(time)<0 and this or time

    def toString(this):
        second = (this.__second<10) and "0"+ str(this.__second) or str(this.__second)
        minute = (this.__minute<10) and "0"+ str(this.__minute) or str(this.__minute)
        hour = (this.__hour<10) and "0"+ str(this.__hour) or str(this.__hour)
        return "{}:{}:{} day {}".format(hour,minute,second,this.__date.toString())

if __name__ == "__main__":
    date = Date(26,10,2003)
    date2 = Date (26,10,2003)
    time = DateTime(14,35,0,date)
    dateTime  = DateTime(15,36,00,date2)
    print(date.toString())
    print(date2.toString())
    print(time.toString())
    print(dateTime.toString())
    print(time.compareTime(dateTime))