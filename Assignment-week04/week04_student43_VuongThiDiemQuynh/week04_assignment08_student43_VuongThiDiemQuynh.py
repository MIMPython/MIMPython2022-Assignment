'''
Xây dựng class Datetime cho phép thực hiện các tác vụ liên quan đến thời gian. Tham khảo pandas.Timestamp để nắm được những thuộc tính/phương thức cơ bản của class cần cài đặt.
'''

from operator import truediv


class Datetime:
    def __init__(self, timezone, year, month, day, hour, minute, second):
        self.timezone = timezone
        self.year = year
        self.month = month 
        self.day = day 
        self.hour = hour 
        self.minute = minute 
        self.second = second

    # Return the number of days in the month:
    def daysInMonth(self): 
        full_month = ['january', 'march', 'may', 'july', 'august', 'october', 'december']
        other_month = ['april', 'june', 'september', 'november']

        totalDays = 0

        if self.year % 4 == 0: 
            # Leap year
            for i in full_month:
                if self.month.lower() == i:
                    totalDays = 31
            for m in other_month: 
                if self.month.lower() == m:
                    totalDays = 30
            if self.month.lower() == 'february':
                    totalDays = 29
        if self.year % 4 != 0:
            # Common year
            for i in full_month:
                if (self.month).lower() == i:
                    totalDays = 31
            for m in other_month:
                if (self.month).lower() == m:
                    totalDays = 30
            if (self.month).lower() == 'february':
                totalDays = 28
        
        return totalDays


    # Check leap year:
    def isLeapYear(self):

        if self.month % 4 != 0:
            return False
        else:
            return True


    # Return the quarter of the year:
    def quarter(self):

        '''
        January, February, and March (Q1)
        April, May, and June (Q2)
        July, August, and September (Q3)
        October, November, and December (Q4)
        '''
        quarter = str

        if (self.month).lower() == 'january' or (self.month).lower() == 'february' or (self.month).lower() == 'march':
            quarter == 'Q1'
        if (self.month).lower() == 'april' or (self.month).lower() == 'may' or (self.month).lower() == 'june':
            quarter == 'Q2'
        if (self.month).lower() == 'july' or (self.month).lower() == 'august' or (self.month).lower() == 'september':
            quarter == 'Q3'
        if (self.month).lower() == 'october' or (self.month).lower() == 'november' or (self.month).lower() == 'december':
            quarter == 'Q4'
        return quarter
    
    # Convert timezone to another timezone:
    def asTimezone(tz):
        return None # Chua kip viet se bo sung sau a!!!
