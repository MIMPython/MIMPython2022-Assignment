A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

def a():
    B = A.copy()
    B[2] = B[2]**2
    print(B)

def b1():
    B = A.copy()
    B.pop(2)
    print(B)
def b2():
    B = A.copy()
    B.remove(B[2])
    print(B)
def c():
    B=A.copy()
    B.append(A[-1]**2)
    print(B)
def d():
    print(len(A))

def e():
    print(sum(A))

def f():
    print(A[1]+A[2]+ A[3]+A[5])

def g1():
    B = A.copy()
    B.reverse()
    print(B)
def g2():
    B=[]
    for i in range(len(A),0,-1):
        B.append(A[i-1])
    print(B)

def h():
    odd =[]
    even = []
    for i in A:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    print("Odd list: ", end=" ")
    print(odd)
    print("Even list: ", end=" ")
    print(even)

def sortList(listnum):
    sortList=listnum.copy()
    for i in range(0,len(sortList)-1):
        maxIndex = i
        for j in range(i+1,len(sortList)):
            if sortList[j]>sortList[maxIndex]:
                maxIndex = j

        temp = sortList[i]
        sortList[i] = sortList[maxIndex]
        sortList[maxIndex] = temp
    return sortList

def i():
    sortArray=sortList(A)
    print(sortArray)

def j():
    B=sortList(A)
    print("Length of List A before and after sort are: "+str(len(A) == len(B) and "Equal" or "Different"))

def k():
    C=A.copy()
    B=sortList(C)
    C.extend(B)
    print(C)

if __name__ == '__main__':
    pass
    print("a)\n->Answer:")
    a()
    print()

    print("b1)\n->Answer:")
    b1()
    print()
    
    print("b2)\n->Answer:")
    b2()
    print()

    print("c)\n->Answer:")
    c()
    print()
    
    print("d)\n->Answer:")
    d()
    print()
    
    print("e)\n->Answer:")
    e()
    print()
    
    print("f)\n->Answer:")
    f()
    print()
        
    print("g1)\n->Answer:")
    g1()
    print()
        
    print("g2)\n->Answer:")
    g2()
    print()

            
    print("h)\n->Answer:")
    h()
    print()

                
    print("i)\n->Answer:")
    i()
    print()
                    
    print("j)\n->Answer:")
    j()
    print()
                    
    print("k)\n->Answer:")
    k()
    print()
    

    
    