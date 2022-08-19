# Bai tap 5
# a, infinity while loop


# while 1:
#     print("Hello")

# b, infinity for loop
# list = [2, 2]
# for i in list:
#     print("Hello 1")
#     list.append(i)

# c, infinity for loop with out list, tuple, dictionary, set
beginStr = 'abc'
for i in beginStr:
    for j in beginStr:
        print("Hello 2")

    beginStr = beginStr + 'he'
