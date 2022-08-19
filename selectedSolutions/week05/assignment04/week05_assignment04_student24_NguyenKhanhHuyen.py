import datetime

gia = 7.24
count =0 

#phan a:
while gia < 58.69:
    gia = gia *1.07
    count +=1

dt = datetime.datetime(2022, 8, 7)
dt_new = dt + datetime.timedelta(days=count)
print(f"Thời điểm sớm nhất mà giá của cổ phiếu này chạm mốc 58.69 nghìn đồng là {dt_new}") # 7/9/2022

#phan b:
while gia < 58.69:
    gia = round(gia *1.07, 2)
    count +=1

dt = datetime.datetime(2022, 8, 7)
dt_new = dt + datetime.timedelta(days=count)
print(f"Thời điểm sớm nhất mà giá của cổ phiếu này chạm mốc 58.69 nghìn đồng là {dt_new}") #7/9/2022