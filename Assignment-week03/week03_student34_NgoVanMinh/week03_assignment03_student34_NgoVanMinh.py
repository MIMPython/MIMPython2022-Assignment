if __name__ == '__main__':
    with open("names.txt", 'r') as f:
        num_dict = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
                         "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23,
                         "X": 24, "Y": 25, "Z": 26}
        names = sorted(f.read().replace('"', '').split(','))    #Sắp xếp lại các từ theo thứ tự và thay thế "" để dễ thao tác và tách các chuỗi có , đi
        sum = 0
        for id, val in enumerate(names):        #Duyệt toàn bộ value(các kí tự đã tách) của names và id (chạy từ 0)
            temp = 0
            for i in val:
                temp += num_dict[i]             #cộng dồn toàn bộ các chỉ số đi với val đó
            sum += temp * (id+1)                # tính tổng của toàn bộ name (id chạy từ 0)
        print(sum)