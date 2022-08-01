bigNumbers = 'week03_assignment02_student38_NguyenVietNgoc_data.txt'
with open(bigNumbers, 'r') as myFile:
    data = myFile.read().splitlines()
data = [int(x) for x in data]
sumBigNumbers = sum(data)
print ("The first ten digits of the sum of the following one hundred 50 digit numbers: " 
        + str(sumBigNumbers)[:10])  # 5537376230

