# create a dictionary to store value in each letter
dictionary = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7,
             "H":8, "I":9, "K":10, "J":11, "L":12, "M":13, "N":14,
             "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21,
             "V":22, "W":23, "X":24, "Y":25, "Z":26}
#read file
file_path = "D:\\VisualCode\\Python\\MIM2022Python\\p022_names.txt"
with open(file_path) as file_object:
    reader = file_object.read()
# creat a string list
temporary_list = reader.split(',')
string_list = []
# remove quotes:
for ele in temporary_list:
    variable = ele.strip('"')
    string_list.append(variable)
#sorting list
sorted_list = sorted(string_list)
print(sorted_list)

#calculate sum of all ele in list
sum_of_all_eles = 0
for ele in sorted_list:
    sum_of_each_ele = 0
    multify_of_each_ele = 1
    for letter in ele:
       sum_of_each_ele += dictionary[letter]
    multify_of_each_ele = sum_of_each_ele*sorted_list.index(ele)
    sum_of_all_eles += multify_of_each_ele
print("sum of all eles is: " + str(sum_of_all_eles))
