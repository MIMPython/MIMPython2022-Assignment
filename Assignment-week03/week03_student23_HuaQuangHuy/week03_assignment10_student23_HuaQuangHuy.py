# Bài tập 10:
"""
Sự khác nhau giữa vòng lặp do-while trong C++ và while trong Python:
Trong do-while, các câu lệnh trong mệnh đề do được thực hiện trước tiên, sau đó mới thực hiện kiểm tra điều kiện lặp và thực hiện các câu lệnh trong vòng lặp
Trong while, điều kiện được kiểm tra trước, nếu thỏa mãn thì mới thực hiện các câu lệnh tiếp theo trong vòng lặp
Có thể nói: do-while ít nhất sẽ thực hiện lần lặp, dù điều kiện có thỏa mãn hay không, 
còn while thì tùy thuộc vào điều kiện có thỏa mãn hay không thì mới thực hiện.

Biến đổi vòng while trong python để thực hiện do while: 
Ví dụ về đoạn code in số thỏa mãn điều kiện là số đó > 10
ví dụ đoạn code trong C++:
int i = 10
do {
    printf("%d", i)
}
while(i > 10)
Kết quả: i = 10 vẫn được in ra

Thực hiện điều này trong Python
"""
i = 10
print(i)
while (i > 10):
    print(i)
