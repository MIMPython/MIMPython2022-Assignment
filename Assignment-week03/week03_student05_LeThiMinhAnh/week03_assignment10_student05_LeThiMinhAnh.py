# a) So sánh vòng lặp do-while trong C++ với vòng lặp while trong Python.
'''
- Vòng lặp do-while trong C++ cũng tương tự như vòng lặp while,
cả 2 vòng lặp đều lặp lại một đoạn code nào đó khi điều kiện đúng.
- Vòng lặp do-while thực hiện đoạn code bên trong vòng lặp rồi mới kiểm tra điều kiện, 
vì vậy đoạn code bên trong vòng lặp do-while được thực hiện ít nhất 1 lần, 
còn đoạn code bên trong vòng lặp while có thể không được thực hiện lần nào.
'''
# b) Có thể biến đổi tương đương đoạn code sử dụng do-while trong C++ sang đoạn code sử dụng while trong Python hay không?
'''
Có thể biến đổi tương đương đoạn code sử dụng do-while sang đoạn code sử dụng while bằng cách sử dụng cấu trúc sau:
while True:
   # execute code
   if not condition:
       break
Ví dụ: Đoạn code C++ sử dụng do-while sau:
  int i = 10;
  do {
    cout << i << "\n"; # 10
    i++;
  }
  while (i < 10);
sẽ tương đương với:
'''
i = 10
while True:
    print(i)  # 10
    i += 1
    if not i < 10:
        break
