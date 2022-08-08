
import pandas as pd

class Datetime:
    
    # in ra ngay/thang/nam/gio... mong muon 
    a = pd.Timestamp(day = 5, month = 8, year = 2022) # 2022-08-05 00:00:00

    # return day of year/month/week
    b1 = a.day_of_year  #217
    b2 = a.day_of_week  #4
    
    # leap year
    a.is_leap_year  #False
    
    # end/start month/year
    a.is_month_end   #False
    a.is_year_start     #False

    # now
    now = pd.Timestamp.now()



    
