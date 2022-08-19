"""
Bài tập 3. (scripting)

Hệ điều hành: Windows 10 Pro

"""

# Chuyển đường dẫn tới một thư mục rỗng X
"""
cd C:\Users\ScyllA\Desktop\x
"""
# Tạo một thư mục mới với tên foo trong đó.
"""
mkdir foo
"""
# Chuyển đường dẫn vào thư mục foo.
"""
cd foo
"""
# Tạo một file với tên data.txt trong thư mục foo và ghi Hello World! vào trong file này.
"""
cat > data.txt
"""
# Tạo một bản sao của file data.txt với tên newData_2.txt (cùng trong thư mục foo).
"""
cp ~Desktop\x\foo\data.txt ~Desktop\x\foo\newData_2.txt
"""
# Chuyển đường dẫn lên thư mục X.
"""
cd x
"""
# Tạo một thư mục mới với tên bar trong đó.
"""
mkdir bar
"""
# Chuyển file newData.txt từ thư mục foo sang thư mục bar.
"""
cp ~Desktop\x\foo\newData_2.txt ~Desktop\x\bar
"""
# Xóa file newData_2.txt trong thư mục foo.
"""
rm ~Desktop\x\foo\newData_2.txt
"""

