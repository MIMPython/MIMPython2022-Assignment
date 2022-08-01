numbers = []
with open("numbers.txt",'r')as data:
     for number in data :
        numbers.append(int(number))
print(str(sum(numbers))[:10])