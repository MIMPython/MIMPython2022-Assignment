
"""
(a) So sánh vòng lặp do-while trong C++ với vòng lặp while trong Python.
-> Trả lời:
While trong python sẽ kiểm tra điều kiện trước rồi mới chạy còn do-while sẽ chạy ít nhất 1 lần 
trước rồi mới kiểm tra điều kiện. Điều này có nghĩa là do-while sẽ chạy ít nhất 1 lần (với while là
0 lần chạy tối thiểu).

_________________________________________________________

(b) Có thể biến đổi tương đương đoạn code sử dụng do-while trong C++ sang đoạn code sử dụng while
trong Python hay không?
-> Trả lời:
Có thể biến đổi đoạn code sử dụng do-while trong C++ sang code sử dụng while trong python

"""
#C++
"""
int i = 0;
do {
    cout << i << "\n";
    i++;
}
while (i < 5);
"""
# python
def insideLoop(i):
    print(i)
    i+=1
    return i

def loop():
    i = insideLoop(0)
    while i<5:
        i=insideLoop(i)
loop()
