""" CMD Window:
Chuyển đường dẫn tới một thư mục rỗng X đã được tạo thủ công từ trước.
    cd .\Assignment\week05_student33_HoangNhatMinh\additionalFolder\x
Tạo một thư mục mới với tên foo trong đó.
    mkdir .\foo
Chuyển đường dẫn vào thư mục foo.
    cd .\foo
Tạo một file với tên data.txt trong thư mục foo và ghi Hello World! vào trong file này.
    echo 'Hello World!' > data.txt
Tạo một bản sao của file data.txt với tên newData.txt (cùng trong thư mục foo).
    copy .\data.txt .\newData.txt
Tạo một bản sao của file data.txt với tên newData_2.txt (cùng trong thư mục foo).
    copy .\data.txt .\newData_2.txt
Chuyển đường dẫn lên thư mục X.
    cd ..
Tạo một thư mục mới với tên bar trong đó.
    mkdir .\bar
Chuyển file newData.txt từ thư mục foo sang thư mục bar.
    move .\foo\newData.txt .\bar
Xóa file newData_2.txt trong thư mục foo.
    del .\foo\newData_2.txt
"""

