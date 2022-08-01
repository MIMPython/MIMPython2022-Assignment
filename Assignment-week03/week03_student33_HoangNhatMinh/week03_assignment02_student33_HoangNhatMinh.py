with open('week03_assignment01_data.txt') as data:
    datas = data.readlines()

result = 0
for data in datas:
    result = result + int(data.rstrip())

print(result)
