'''
Bài tập 4. (về bờ không khó)
Giả sử giá của một cổ phiếu trong một ngày là cố định và phải nằm trong khung từ 93% đến 107% so với giá của ngày liền trước. Biết rằng vào ngày 07/08/2022, giá của cổ phiếu F là 7.24 (đơn vị nghìn đồng). Hỏi thời điểm sớm nhất mà giá của cổ phiếu này chạm mốc 58.69 nghìn đồng là khi nào?
Giải Quyết bài tập này trong hai trường hợp sau đây:
a) Giá cổ phiếu nhận giá trị là một số thực.
b) Giá cổ phiếu (đơn vị nghìn đồng) là một số có hai chữ số sau dấu chấm thập phân, ví dụ 32.40.
'''
import math
from datetime import datetime, timedelta 

# a)
def getDateA(begin_value, finish_value, percent_value):
    # begin_value la gia tri co phieu ngay dau tien
    # finish_value la gia tri co phieu muon cham moc

    # finish_value = begin_value * (percent_value)**(theNearestDate)
    
    theNearestDate = math.log(finish_value/begin_value, percent_value)
    sumOfDays = round(theNearestDate, 0)
    return sumOfDays


# b)
def getDateB(begin_value, finish_value, percent_value):
    # begin_value la gia tri co phieu ngay dau tien
    # finish_value la gia tri co phieu muon cham moc

    # finish_value = begin_value * (percent_value)**(theNearestDate)

    theNearestDate = math.log(round(finish_value/begin_value,2), percent_value)
    sumOfDays = round(theNearestDate, 0)
    return sumOfDays

# Function convert the date after n days from 07/08/2022

def dateNDaysAfter(sumOfDays):

    begin_date_str = '07/08/22'
    begin_date = datetime.strptime(begin_date_str, '%d/%m/%y') # https://www.educative.io/answers/how-to-convert-a-string-to-a-date-in-python
    date_N_days_after = begin_date + timedelta(days=sumOfDays)
    return date_N_days_after


if __name__ == "__main__":
    sumOfDaysA = getDateA(7.24, 58.69, 107/100) 
    print(sumOfDaysA) # 31.0 

    sumOfDaysB = getDateB(7.24, 58.69, 107/100) 
    print(sumOfDaysB) # 31.0

    resultA = dateNDaysAfter(sumOfDays=sumOfDaysA)
    print("Thời điểm sớm nhất mà giá của cổ phiếu F chạm mốc 58.69 nghìn đồng là", resultA) # Thời điểm sớm nhất mà giá của cổ phiếu F chạm mốc 58.69 nghìn đồng là 2022-09-07 00:00:00
    
    resultB = dateNDaysAfter(sumOfDays=sumOfDaysB)
    print("Thời điểm sớm nhất mà giá của cổ phiếu F chạm mốc 58.69 nghìn đồng là", resultB) # Thời điểm sớm nhất mà giá của cổ phiếu F chạm mốc 58.69 nghìn đồng là 2022-09-07 00:00:00
    