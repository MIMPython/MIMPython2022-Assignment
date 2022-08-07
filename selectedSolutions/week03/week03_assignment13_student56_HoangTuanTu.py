def pow(n,pow):
    return str(n**pow)

def toString(f,l):
    return f+l
if __name__ == "__main__":
    n = int(input())
    a = 2
    b = 5
    number = toString(pow(a,n),pow(b,n))
    print("After Pairing Number Have lenght:" , len(number))
