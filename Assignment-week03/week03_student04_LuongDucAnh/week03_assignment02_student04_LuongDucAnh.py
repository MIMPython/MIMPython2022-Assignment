path = "D:/temp/100numbers.txt" #Đường dẫn đến file chứ 100 chữ số dài 50
with open (path, "r") as file:
    data = file.read().splitlines()
data = [int(i) for i in data]
sum = str(sum(data))
print (f"10 chữ số đầu tiên của tổng 100 số dài 50 đã cho là: {sum[:10]}")