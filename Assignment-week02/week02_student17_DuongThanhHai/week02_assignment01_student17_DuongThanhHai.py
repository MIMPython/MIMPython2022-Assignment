
from gettext import ngettext
from statistics import harmonic_mean
from tkinter import N
from unicodedata import name


a)
    những ký tự không được phép xuất hiện trong tên biến: khoảng trắng, những ký tự đắc biệt (vdu: @, *, %, ...), 

b) 
    tên biến hợp lệ:        'half_pyramid'  'student_1'        
    tên biến không hợp lệ:  'half pyramid'  '1_student'

c)
    ví dụ về cách đặt tên biến tốt: 'A_height' , thay vì 'heigth_of_A' dài hơn và 'heigth' chưa bao quát được hết nội dung của biến 

d)
    - cách 1: viết liền, các chữ cái đều viết thường
    - cách 2: viết liền, các chữ cái đều viết hoa 
    - cách 3: viết liền, các từ đều viết hoa trừ từ đầu tiên 
    - cách 4: viết liền, các từ đều viết hoa 
    - cách 5: các từ viết thường,  nối với nhau bằng dấu gạch dưới


e)
    - Camel Case: viết liền, viết hoa tất cả các từ trừ từ đầu tên ('sumOfList')
    - Pascal Case: viết liền, viết hoa tát cả các từ ('SumOfList')
    - Snake Case: các khoảng trắng được thay bằng gạch dưới ('sum_of_list') 

f)
    em chọn phong cách Snake Case vì các từ được tách riêng biệt nên sẽ dễ hiểu hơn.