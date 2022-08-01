def getScore(name, order): #Hàm tính điểm
    sum = 0
    for char in name:
        sum = sum + ord(char) - 64
    return sum * order

def main():
    path = "D:/temp/names.txt"
    with open (path, "r") as file: #đọc file tên
        data = file.read().split(",")
    data = [name.strip('"') for name in data] #loại bỏ nốt dấu ngoặc kép còn thừa lại
    data.sort() #sắp xếp lại list theo thứ tự tăng dần bảng chữ cái
    count = 1
    for name in data:
        data[count - 1] = getScore(name, count)
        count += 1
    totalscores = sum(data)
    print (f"Tổng điểm của tất cả các tên trong file là: {totalscores}") #Tổng điểm của tất cả các tên trong file là: 871198282
    
if __name__ == "__main__":
    main()