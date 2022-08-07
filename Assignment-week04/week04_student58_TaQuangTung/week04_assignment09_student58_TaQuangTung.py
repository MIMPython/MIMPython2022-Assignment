print("Bài 9: Factorial Number")

class Factorials:
    def __init__(self, n):
        self.n = n
    def number(self):
        k = self.n
        tich = 1
        for i in range(1, k+1):
            tich *= i 
        print(f"{self.n}! = {tich}")

        #Đếm số 0 tận cùng bên phải
        tich = str(tich)
        lst = []        #Mảng gồm các phần tử của n! được tách ra
        for j in tich:
            lst.append(j)
            
        length = len(lst)           #Độ dài mảng lst
        d = 0
        for x in range(length-1, -1, -1):
            if lst[x] == "0":
                d += 1
            else:
                break 
        print(f"=> {self.n}! có {d} chữ số 0 tận cùng bên phải")
        print()

        #Số mới sau khi bỏ các chữ số 0 tận cùng bên phải
        i = length - 1
        while lst[i] == '0':
            lst.pop(i)
            i -= 1
        st = ""
        for element in lst:
            st += element
        print("Số mới là:",int(st))
        print(f"Chữ số tận cùng bên phải là: {lst[-1]}")
n = int(input("Nhập n = "))
Factorials(n).number()
