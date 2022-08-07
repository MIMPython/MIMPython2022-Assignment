def solve(n):
    if n==0:
        return 1
    if n<0:
        return 0
    muti = n
    count = 0
    for i in range(2,n):
        muti*=i
        while muti%10==0:
            muti//=10
            count +=1
    return muti,count

if __name__ == "__main__":
    n = int(input())
    ans = list(solve(n))
    ans_a = ans[1]
    ans_b = ans[0]
    print("Factorial of {} is: {}".format(n,str(ans_b)+str("0"*ans_a)))
    print("Number last right zero digit is:", ans_a)
    print("Last digit of new number is:",str(ans_b)[-1])
