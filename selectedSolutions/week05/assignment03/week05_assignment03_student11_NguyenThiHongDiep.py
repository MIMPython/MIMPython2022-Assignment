"""
* Hệ điều hành Windows
* Tất cả những câu lệnh đã thực thi
    Windows + X  
1. Chuyển đường dẫn tới một thư mục rỗng X đã được tạo thủ công từ trước.
    cd D:\Downloads\x
2. Tạo một thư mục mới với tên foo trong đó.
    mkdir foo 
3. Chuyển đường dẫn vào thư mục foo.
    cd foo 
4. Tạo một file với tên data.txt trong thư mục foo.
    type nul > data.txt 
5. Ghi Hello World! vào trong file này.
    echo "Hello World!" > data.txt
6. Tạo một bản sao của file data.txt với tên newData.txt (cùng trong thư mục foo).
    copy data.txt newData.txt 
7. Tạo một bản sao của file data.txt với tên newData_2.txt (cùng trong thư mục foo).
    copy data.txt newData_2.txt
8. Chuyển đường dẫn lên thư mục x.
    cd .. 
9. Tạo một thư mục mới với tên bar trong đó.
    mkdir bar
10. Chuyển file newData.txt từ thư mục foo sang thư mục bar.  
    cd foo
    mv newData.txt D:\Downloads\x\bar
11. Xóa file newData_2.txt trong thư mục foo.
    rm newData_2.txt 
12. Sử dụng lệnh code data.txt để tạo mới file data.txt đồng thời ghi nội dung file bằng VS Code.
    code data.txt # Hello World! HIHI.
"""
