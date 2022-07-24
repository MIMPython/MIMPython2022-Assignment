import string
A = list(string.ascii_lowercase)

def encode(A,characters, number):
    k = 0
    for i in range(0,len(A)):  
        if(characters == A[i]):
            k = i
            continue
    k+= number
    if(k <= 25):
        return A[k]
    if(k>=26): 
        k-=26
        return A[k]

B = 'python'
print(B,'encode to: ',end='')      
for i in B:
    print(encode(A,i,13),end='')
# print : "python encode to: clguba"