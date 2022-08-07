A = [[1,2], [3,0,4], [2], [4,5]]
dictionary = {}
sum_list = []
for element in A:
    sum = 0
    for number in element:
        sum += number
    #store value in dictionary
    dictionary[sum] = element
    # calculate and store sum of each element in new list
    sum_list.append(sum)
# sort sum 
sorted_sum_list = sorted(sum_list)
answer = []
for number in sorted_sum_list:
    answer.append(dictionary[number])
print(dictionary)
print(answer)
    