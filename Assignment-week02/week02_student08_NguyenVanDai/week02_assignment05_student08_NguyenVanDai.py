from hashlib import new
from pickle import TRUE
from re import T


A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
# a
A[3]=3**2
# b
A.pop(3)
del A[3:4]
# c
A.append(A[-1]**2)
#d
length= len(A)
#e
sum = 0
for i in range (len(A)):
    sum += A[i]
print (sum)
# f
C = [A[1],A[2],A[3],A[5]]
print(sum(C))
# g
new_list1 = list(reversed(A))
print(new_list1)
#h 
def splitevenodd(): 
   evenlist = [] 
   oddlist = [] 
   for i in A: 
      if (i % 2 == 0): 
         evenlist.append(i) 
      else: 
         oddlist.append(i) 
   print("Even lists:", evenlist) 
   print("Odd lists:", oddlist)      
splitevenodd()

#i 
B = sorted(A,reverse=T)
print(B)
#j
if len(A)> len(B):
     print('list A dài hơn list B')
if len (A) < len (B) :
     print('list A ngắn hơn list B ')
else :
     print('list A bằng list B ')
#k 
C = A+ B
print(C)

      
       



 


