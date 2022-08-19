# # a)
# a=1
# while a>0:
#     a+=1
# # b)
# A=[0]
# for i in A:
#     A.append(i+1)
# print(A)
# c)
def infiniteLoop():
    for i in iter(int,1) :
        print(i)

infiniteLoop()