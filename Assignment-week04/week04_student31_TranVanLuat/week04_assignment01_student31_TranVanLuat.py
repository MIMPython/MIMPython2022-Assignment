
A = [[2,3],[1,2,3],[4,0],[3,0,0,3]] #input

#Cách 1
A.sort(key = sum)
#Cách 2
result = sorted(A, key = lambda x: sum(x))
print(list(result)) #Kết quả: [[4, 0], [2, 3], [1, 2, 3], [3, 0, 0, 3]]


#Tiêu chí so sánh giữa 2 list ổn bất kỳ: Nếu phần tử đầu tiên của A lớn hơn B thì A > B
A = [[2,3],[1,2,3],[4,0],[3,0,0,3]] 
result = sorted(A, key = lambda x: x[0])
print(list(result)) #[[1, 2, 3], [2, 3], [3, 0, 0, 3], [4, 0]]





