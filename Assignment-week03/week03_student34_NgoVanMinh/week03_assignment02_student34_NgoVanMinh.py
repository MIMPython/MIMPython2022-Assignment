path = "data1.txt"
if __name__ == '__main__':
    with open(path, 'r') as f:
        allLines = f.read().split("\n") # ['MIM\n', 'Python\n', '2022\n']

    sum =0
    for i in allLines:
        sum += int(i)
    temp = str(sum)
    print(temp[0:10])
    #result : 5537376230
