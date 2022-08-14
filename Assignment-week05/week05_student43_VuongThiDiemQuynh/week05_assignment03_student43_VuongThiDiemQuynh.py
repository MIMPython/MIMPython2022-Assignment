# # Bài tập 3. (scripting)
# # Mở một terminal và thực hiện những yêu cầu dưới đây. Ghi lại tất cả những câu lệnh đã thực thi (kể từ thời điểm mở terminal) vào phần bài làm của bài tập này, đồng thời đặt thư mục X vào trong thư mục bổ sung additionalFolder/ trong phần bài nộp.

# # Danh sách yêu cầu:

'''
Chuyển đường dẫn tới một thư mục rỗng X đã được tạo thủ công từ trước.
'''
    # macbooks-MacBook-Pro:~ macbook$ cd Downloads
    # macbooks-MacBook-Pro:Downloads macbook$ cd X

'''
Tạo một thư mục mới với tên foo trong đó.
'''
    # macbooks-MacBook-Pro:X macbook$ mkdir foo 

'''
Chuyển đường dẫn vào thư mục foo.
'''
    # macbooks-MacBook-Pro:X macbook$ cd foo

'''
Tạo một file với tên data.txt trong thư mục foo và ghi Hello World! vào trong file này.
'''
    # macbooks-MacBook-Pro:foo macbook$ touch data.txt
    # macbooks-MacBook-Pro:foo macbook$ echo "Hello World" >> data.txt
    # macbooks-MacBook-Pro:foo macbook$ cat data.txt
    # Hello World
'''
Tạo một bản sao của file data.txt với tên newData.txt (cùng trong thư mục foo).
'''
    # macbooks-MacBook-Pro:foo macbook$ cp data.txt newData.txt
    # macbooks-MacBook-Pro:foo macbook$ cat newData.txt
    # Hello World
'''
 Tạo một bản sao của file data.txt với tên newData_2.txt (cùng trong thư mục foo).
'''
    # macbooks-MacBook-Pro:foo macbook$ cp data.txt newData_2.txt
'''
Chuyển đường dẫn lên thư mục X.
'''
    # macbooks-MacBook-Pro:foo macbook$ cd\
    # > 
    # macbooks-MacBook-Pro:~ macbook$ cd Downloads
    # macbooks-MacBook-Pro:Downloads macbook$ cd X

'''
Tạo một thư mục mới với tên bar trong đó.
'''
    # macbooks-MacBook-Pro:X macbook$ mkdir bar

'''
Chuyển file newData.txt từ thư mục foo sang thư mục bar.
'''
    # macbooks-MacBook-Pro:X macbook$ cd\
    # > 
    # macbooks-MacBook-Pro:Downloads macbook$ cd X
    # macbooks-MacBook-Pro:X macbook$ cd foo
    # macbooks-MacBook-Pro:foo macbook$ mv newData.txt /Users/macbook/Downloads/X/bar

'''
Xóa file newData_2.txt trong thư mục foo.
'''
    # macbooks-MacBook-Pro:foo macbook$ rm newData_2.txt
    # macbooks-MacBook-Pro:foo macbook$ ls
    # data.txt
    # macbooks-MacBook-Pro:foo macbook$ 

