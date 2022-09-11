from time import sleep

def collatz(number: int):
    step = 0
    while number > 1:
        number = number % 2 == 0 and int(number / 2) or float(3 * number + 1)
        step +=1
    return step

def startNumber():
    mostStep = 1
    num = 1
    for i in range(1,10**6):  
        step = collatz(i)
        if step == 524:
            mostStep =  step
            num = i
    return mostStep, num

if __name__ == "__main__":
    mostStep, number = startNumber()
    print("Starting at {} produces the longest chain with: {} step".format(number, mostStep))
    # 837799 with 524 step

"""
Bài này còn có cách khác nhanh hơn tuy nhiên hiện tại thì mình vẫn đang thử nghiệm và chưa
được thành công cho lắm. Cụ thể hơn thì cách mình đang thử đó là sử dụng thuật toán DFS tìm
kiếm theo chiều sâu. Các con số theo "Quy tắc" Collazt khi được vẽ trên đồ thị sẽ đều hướng
về số 1, cho nên ta có thể chọn 1 là gốc của cây sau đó đi và rẽ nhánh. Các nhành sẽ kết 
thúc tại giá trị lớn nhất đầu tiền nếu như số hiện tại là số chẵn và >= 10^6. Khi đó độ phức tạp
sẽ giảm đáng kể và chỉ còn khoảng O(n^2) ( tương đương Độ phức tạp của thuật toán DFS).
Tuy nhiên vì còn 1 vài vấn đề trong việc ứng dụng giải thuật DFS vào bài toán nên  mình chưa
thể đưa ra được cách  làm chính xác và chưa đưa ra được kết quả.
"""