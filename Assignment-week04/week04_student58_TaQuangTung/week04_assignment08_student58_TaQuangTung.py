print("Bài 8: Class Datetime")
print()

import pandas as pd

class Datetime:
    def __init__(self, hour, day, month, year):
        self.hour = hour
        self.day = day
        self.month = month
        self.year = year
        
    def thoigian(self):
        kq = pd.Timestamp(hour = self.hour, day = self.day, month = self.month, year = self.year)
        print("Thời gian cần tìm là:",kq)

day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))
hour = int(input("Nhập giờ: "))
d = Datetime(hour, day, month, year).thoigian()  
