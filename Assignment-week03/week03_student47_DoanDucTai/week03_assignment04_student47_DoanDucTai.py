#bài 4.Fibonacci numbers
# cách 1: vòng lặp
numberFibo = int(input("nhập n: "))
fibo_1 = 0
fibo_2 = 1
if ( numberFibo == 0 or numberFibo == 1):
    print("fibonacci thứ ", numberFibo," là: ", numberFibo, sep = "" )
else:
    i=2
    while ( i <= numberFibo ):
        fibo = fibo_1+ fibo_2
        fibo_1 = fibo_2
        fibo_2 = fibo
        i += 1
    print("C1: fibonacci thứ ", numberFibo," là: ", fibo, sep = "" )

# cách 2: đệ quy
def fibonacci(n):
    if (n == 0 or n == 1):
        return n;
    else:
        return fibonacci(n - 1) + fibonacci(n - 2);
 
print("c2: fibonacci thứ ", numberFibo," là: ", fibonacci(numberFibo), sep = "");