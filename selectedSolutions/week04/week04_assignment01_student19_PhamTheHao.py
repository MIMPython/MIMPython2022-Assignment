"""
Bài tập 1. (sort a list)
Một list được gọi là ổn nếu nó chỉ chứa các số thực và có ít nhất một phần tử. Cho một 
list gồm các list con ổn. Viết một chương trình sắp xếp list này theo thứ tự tăng dẫn 
của tổng các số trong mỗi list con.
"""
A = [[1,2], [3,0,4], [2], [4,5], [11], [1, 0, 6]]

A.sort(key = sum)

print(A)

"""
Yêu cầu bổ sung: đặt ra thêm tiêu chí để so sánh hai list ổn bất kỳ và áp dụng tiêu chí 
này để sắp xếp list đầu vào.
"""
A.sort(key = lambda x:x[0])