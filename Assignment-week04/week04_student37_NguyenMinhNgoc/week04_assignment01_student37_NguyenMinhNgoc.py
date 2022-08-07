from pyparsing import nums

def select_sort():
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
    nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
        
A = [[1,2], [3,0,4], [2], [4,5]] 
select_sort(A)
print(A)