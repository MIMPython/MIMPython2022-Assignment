"""Sắp xếp A theo tiêu chí của đề"""
A = [[1,2], [3,0,4], [2], [4,5]] 

B = sorted(A, key = lambda x: sum(x))
print(B) #[[2], [1, 2], [3, 0, 4], [4, 5]]

"""
Tiêu chí để sắp xếp hai list ổn bất kỳ:
Ta sẽ sắp xếp các list theo số lượng yếu tố của list tăng dần.
Đối với các list mà có cùng số lượng yếu tố, ta sẽ sắp xếp theo lối từ điển.
Cụ thể hơn, nếu hai list A, B khác nhau thì sẽ có chỉ số i nhỏ nhất sao cho A[i] != B[i]
Khi đó nếu A[i] < B[i] thì list A sẽ được sắp xếp trước list B và ngược lại.
"""

"""
Ta xây dựng một hàm với hai biến đầu vào: 
+)list: một list ổn bất kỳ 
và 
+)list_of_list: một list gồm các list ổn bất kỳ, 
rồi sử dụng quy tắc vừa nêu trên để xem liệu trong list_of_list
 có bao nhiêu list mà đứngtrước list đầu vào của ta
"""

def sorting_function(list, list_of_list):
    position_of_list = 0
    for well_list in list_of_list:
        if len(well_list) < len(list):  #độ dài của well_list ngắn hơn list thì position_of_list tăng 1
            position_of_list += 1
        elif len(well_list) > len(list):#độ dài của well_list dài hơn list thì position_of_list không đổi
            position_of_list += 0
        elif well_list == list:         #well_list bằng list thì position_of_list không đổi
            position_of_list += 0
        else:                           # bây giờ well_list sẽ khác list và có độ dài bằng list
            list_subtract = [list[i] - well_list[i] for i in range(0, len(list))] # trừ list cho well_list
            i = 0                       #bắt đầu so sánh từng phần tử một của list_subtract
            while i < len(list):        
                if list_subtract[i] < 0: #nếu i nhỏ nhất để listsubtract[i] khác không mà âm thì well_list sẽ đứng sau list
                    position_of_list += 0
                    break
                elif list_subtract[i] > 0:# ngược lại thì well_list đứng trước list nên position_of_list tăng 1
                    position_of_list += 1
                    break
                else:
                    i += 1
                    
    return(position_of_list)

"""Sắp xếp A theo cách mới"""
A = [[1,2], [3,0,4], [2], [4,5]]
A = sorted(A , key = lambda list: sorting_function(list, A))
print(A) #[[2], [1, 2], [4, 5], [3, 0, 4]]


