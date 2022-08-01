import numpy as np
def FibonacciUseLoop(n):
    f1 = 1
    f2 = 1
    if(n == 1 or n == 2):
        return 1
    elif(n == 0):
        return 0
    count = 3
    fn = 0
    while (count <= n):
        fn = f1 + f2
        f1 = f2
        f2 = fn
        count += 1
    return fn

def FibonacciUseNumpy(n):
    F = np.array([n+1])
    count = 3
    while(count <= n):
        F[count] = F[count - 1] + F[count - 2]
        count+=1
    return F(n)

    
        
    
if __name__ == '__main__':
    n = int(input('Input of n: '))
    ans1 = 'The fibonacci '+ str(n) + ' use loop is: ' + str(FibonacciUseLoop(n))
    print(ans1)
    ans2 = 'The fibonacci '+ str(n) + ' use Numpy is: ' + str(FibonacciUseLoop(n))
    print(ans2)
    
    
    
    