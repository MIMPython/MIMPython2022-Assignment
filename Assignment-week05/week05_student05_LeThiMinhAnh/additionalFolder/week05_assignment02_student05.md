# **Bài 12. Github và markdown**

## **GitHub**

### **1. GitHub là gì?**

GitHub là một dịch vụ nổi tiếng cung cấp kho lưu trữ mã nguồn Git cho các dự án phần mềm. **Github có đầy đủ những tính năng của Git**, ngoài ra nó còn bổ sung những tính năng về social để các developer tương tác với nhau.

Vài thông tin về GIT:

- Là công cụ giúp quản lý source code tổ chức theo dạng dữ liệu phân tán.

- Giúp đồng bộ source code của team lên một server.

- Hỗ trợ các thao tác kiểm tra source code trong quá trình làm việc (diff, check modifications, show history, merge source, …)

### **2. GitHub cơ bản**

#### **Tạo GitHub Repository**

Repository (gọi tắt là repo) là một không gian để lưu trữ dự án của bạn. Do tính chất phân tán của Git, nên có thể hiểu repo là nơi lưu trữ mã nguồn ở cả local và server.

Bạn có thể lưu trữ file code, text, hình ảnh hoặc bất kỳ loại tệp nào trong repo.

Để tạo một repo trên GitHub bạn làm như sau:

- Vào Github, đăng ký một tài khoản bằng cách click vào “Sign up for Github”.

- Sau khi đăng ký và kích hoạt thành công. Ấn dấu + trên thanh status bar chọn `New repository`.

![github-1.png](https://mimpython.github.io/assets/images/courses/05-01-github-markdown/github-1.png)

Nhập tên Repositoty và nhấn nút “Create Repository”. Ngoài ra, bạn cũng có thể thêm mô tả cho repo.

![github-2.png](https://mimpython.github.io/assets/images/courses/05-01-github-markdown/github-2.png)

Trong đó, bạn lưu ý 2 options sau:

- Theo mặc định thì repository để là public. Tức là ai cũng có thể xem được repo này của bạn. Nếu dự án của bạn chưa muốn công khai mà chỉ muốn quản lý nội bộ thì chọn Private.

- Bạn có thêm một README file để giới thiệu repo kèm với một file [.gitignore.](https://github.com/github/gitignore) Github đã có sẵn template .gitignore cho bạn, cứ chọn một template phù hợp với mã nguồn dự án là được.

Khi tạo xong, repo sẽ như sau:

![github-3.png](https://mimpython.github.io/assets/images/courses/05-01-github-markdown/github-3.png)

Khi đã có repository, bạn có thể clone, pull, push… source code của mình lên đó.

> Các lệnh thực hiện để làm việc với GitHub tương tự như với Git xem tại [đây](https://mimpython.github.io/pythonSummerCourse/week-03-git/)
