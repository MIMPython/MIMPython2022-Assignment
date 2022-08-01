
nums = []
with open('bignumber.txt', 'r') as f:
    for num in f:
        nums.append(int(num))
total = sum(nums)
answer = str(total)[:10]
print(answer)


