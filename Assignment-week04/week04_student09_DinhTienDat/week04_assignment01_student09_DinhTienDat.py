import math

A = [[2,3],[3,5,8],[1],[0]]
B = [[1,2],[0,4,7],[5],[3,5,7]]

print("A =",A)
print("B =",B)

#The stability function
def sorted(C):
    C_1 = [sum(c) for c in C]
    C_1.sort()
    return C_1

print("List A after being sorted is",sorted(A))
print("List B after being sorted is",sorted(B))

#Comparing lists
def stability(C):
    return max(sorted(C))

if stability(A) > stability(B):
    print("List A is more stable than list B")
elif stability(A) < stability(B):
    print("List B is more stable than list A")
else:
    print("List A and list B have the same stability")

