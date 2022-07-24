A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

if __name__ == '__main__':
    #a
    A[2] = A[2]**2
    print("Phần a "+str(A))
    #[70, 43, 49, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

    #b
    A.pop(2)    #C1
    del A[2]    #C2
    print("Phần b "+str(A))

    #[70, 43, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
    #c
    A.append(A[-1]**2)
    print("Phần c"+str(A))
    #[70, 43, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53, 2809]

    #d
    print("Tổng phần tử trong list là "+str(sum(A)))
    #Tổng phần tử trong list là 3315

    #e
    print("Tổng số phần tử trong list là "+str(len(A)))
    #Tổng số phần tử trong list là 14

    #f
    sum = A[1] + A[2]+ A[3]+ A[5]
    print("Tổng các phần tử có index 1, 2,3,5 "+str(sum))

    #g

    #C1
    B = list(reversed(A))
    print("B là list đảo ngược của B " + str(B))
    #B là list đảo ngược của B [2809, 53, 3, 53, 5, 1, 3, 49, 35, 80, 77, 34, 43, 70]

    #C2

    C = A[::-1]
    print("C là list đảo ngược của A "+str(C))
    #C là list đảo ngược của A [2809, 53, 3, 53, 5, 1, 3, 49, 35, 80, 77, 34, 43, 70]

    #h
    D =[]
    E=[]
    for i in A:
        if i %2==0 :
            D.append(i)     #Tập hợp phần tử chẵn
        else:
            E.append(i)     #Tập hợp phần tử lẻ
    print("Phần tử chẵn là "+str(D))                #[70, 34, 80]
    print("Phần tử lẻ là "+str(E))                #[43, 77, 35, 49, 3, 1, 5, 53, 3, 53, 2809]


    #i
    B = sorted(A, reverse=True)
    print("Các phần tử sau khi được sắp xếp là "+str(B))
    #Các phần tử sau khi được sắp xếp là [2809, 80, 77, 70, 53, 53, 49, 43, 35, 34, 5, 3, 3, 1]

    #j
    print(len(A) == len(B))
    #Sau khi so sánh ta thấy số lượng phần tử sau khi sắp xếp là không thay đổi

    #k
    C = A + B
    print("List C là list ghép của list A và list B :"+str(C))
    #[70, 43, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53, 2809, 2809, 80, 77, 70, 53, 53, 49, 43, 35, 34, 5, 3, 3, 1]
    
