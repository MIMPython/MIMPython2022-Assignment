# a)

def arrange(list_numbers):
        sum_numbers = []
        for list_number in list_numbers: 
            sum_numbers.append(sum(list_number)) 
            sum_numbers.sort()
        new_list_numbers = []
        for i in sum_numbers:
            for list_number in list_numbers: 
                if sum(list_number) == i:
                    new_list_numbers.append(list_number)
        print(new_list_numbers) 

A = [[1, 2], [3, 0, 4], [2], [4, 5]]

# arrange(A)
#b)
'''Tiêu chí để so sánh 2 list là ổn: Nếu tổng các list con lần 
lượt theo thứ tự của 2 list bằng nhau. 
'''





