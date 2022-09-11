print("Bài 1: Documentation/Docstrings")

# Google Docstrings
def sumofvalue(a, b, c):
    """
    Đây là hàm được sử dụng để tính tổng ba số
    
    Arguments
        a (float): number1
        b (float): number2
        c (float): number3
    
    Return:
        sum: the result of a + b + c
    """
    sum = a + b + c
    return sum
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = ")) 
print(f"sum = {sumofvalue(a, b, c)}")
