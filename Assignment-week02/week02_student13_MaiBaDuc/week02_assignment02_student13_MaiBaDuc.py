'''
Bài tập 2. Viết một hàm tính bình phương của một số nguyên.
Ghi chú: Đối với tất cả bài tập yêu cầu cài đặt chương trình (implementation), nội dung được trình bày trong một file .py cần có đủ những ví dụ minh họa. Khi đó, chỉ cần thực thi chương trình để kiểm chứng nội dung của chương trình.
Dưới đây là một lời giải tham khảo cho bài tập này.
def foo(x):
    return x**2

if __name__ == '__main__':
    print(foo(-2)) # 4
    print(foo(5)) # 25
    print(foo(0)) # 0

'''
x = input()
def squared(x):
    if(isinstance(x,int)==True): 
        return x**2

if __name__ == '__main__':
    print(squared(-2))
    print(squared(0)) 