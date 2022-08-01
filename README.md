# MIMPython2022-Assignment

Repo chứa bài tập hàng tuần của học viên

Thư mục `selectedSolutions/` chứa những bài làm nổi bật của học viên. Mỗi bài làm đều có những khía cạnh được thể hiện tốt hơn so với mặt bằng chung của các học viên trong khóa học. Tuy nhiên MIMPython **không đưa ra bất cứ khẳng định nào** về tính chính xác và độ tin cậy của những bài làm này.


Bổ sung ngày 01/08/2022 \
Để bổ sung bài làm của những tuần học trước, học viên tạo một pull request tới nhánh `main` của repository này.


## Valid Code

Chương trình nhận biết những file không đúng quy tắc nộp bài. Để sử dụng thay đổi giá trị các biến sau.

```py
zipAssignmentFolderPath = Path('path/to/week03_student01_TranThanhTung.zip')
week = 3
numberOfAssignments = 13
studentID = 1
nameWithoutAccent = 'TranThanhTung'
```

Trong đó:
`zipzipAssignmentFolderPath`: đường dẫn đến file zip chứa bài tập
`week`: tuần muốn kiểm tra
`numberOfAssignments`: số lượng bài tập tối đa của tuần
`nameWithoutAccent`: họ tên viết liên không dấu của sinh viên

Cài đặt thư viện cần thiết
`pip install -r requirements.txt`
