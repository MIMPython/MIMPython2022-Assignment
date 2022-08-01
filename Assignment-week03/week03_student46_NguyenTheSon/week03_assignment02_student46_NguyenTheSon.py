file_path = 'D:\pi_digits.txt'
sum = 0
with open(file_path) as file_object:
	lines = file_object.readlines()
sum_lines = 0
for line in lines:
	sum_lines += int(line)
print(str(sum_lines)[:10])