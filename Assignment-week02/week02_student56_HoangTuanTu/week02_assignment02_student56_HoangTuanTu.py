def foo(number):
    return number**2

if __name__ == '__main__':
    print(foo(-2)) # 4
    print(foo(5)) # 25
    print(foo(0)) # 0
    number = int(input("Input a number: "))
    print("Square of {} is: {}".format(number,foo(number)) )
