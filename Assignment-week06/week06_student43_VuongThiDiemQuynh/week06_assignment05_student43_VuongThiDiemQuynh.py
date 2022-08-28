'''
Bài tập 5. (iterating a directory)
Viết một hàm liệt kê tất cả những tệp tin và thư mục là con trực tiếp của một thư mục cho trước, đồng thời trả lời xem mỗi đối tượng là tệp tin hay là thư mục. Học viên tự quyết định kiểu dữ liệu trả về phù hợp.

Ví dụ với cây thư mục như sau

foo/
  bar/
    fileA.txt
    fileB.png
  ham/
  egg/
    fileC.pdf
  fileD.svg
  fileE.tif
chương trình sẽ có input/output dưới đây

Input: /path/to/folder/foo
Output:
- object bar, type folder
- object ham, type folder
- object egg, type folder
- object fileD.svg, type file
- object fileE.tif, type file
'''
# os.listdir() returns everything inside a directory -- including both files and directories.

# os.path's isfile() can be used to only list files.

from os import listdir
from os.path import isfile, isdir

def iterating_a_directory(path):
  for item in listdir(path):
    if isfile(item):
      print(item, "type file\n")
    if isdir(item):
      print(item, "type folder\n")


if __name__ == '__main__':
    path = '/Users/macbook/Desktop/MIM Python'
    iterating_a_directory(path)
# Output: 
'''
week04_student43_VuongThiDiemQuynh 2 type folder

week04_student43_VuongThiDiemQuynh type folder

week01_student43_VuongThiDiemQuynh type folder

.DS_Store type file

week05_student43_VuongThiDiemQuynh type folder

week04_student43_VuongThiDiemQuynh.zip type file

README.md type file

week06_student43_VuongThiDiemQuynh type folder

week05_student43_VuongThiDiemQuynh.zip type file

week03_student43_VuongThiDiemQuynh type folder

.git type folder

week03_student43_VuongThiDiemQuynh.zip type file

week02_student43_VuongThiDiemQuynh type folder
'''