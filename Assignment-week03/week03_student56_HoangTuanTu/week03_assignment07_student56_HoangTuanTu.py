def primeFactors(n):
    n = abs(n)
    if n==0:
        return []
    elif n<2:
        return [n]
    i=2
    divisor = set()
    while n>0 and i<=n:
        while n%i==0:
            n//=i
            divisor.add(i)
        i+=1
    ans = list(divisor)
    ans.sort()
    return ans

if __name__ == "__main__":
    n = int(input())
    print(primeFactors(n)[-1])
