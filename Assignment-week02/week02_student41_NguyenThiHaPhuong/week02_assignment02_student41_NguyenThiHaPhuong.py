from unicodedata import name


def foo(x):
    return x**2

if __name__ == '__main__':
    print(foo(-2))
    print(foo(5))
    print(foo(0)) 
    
    