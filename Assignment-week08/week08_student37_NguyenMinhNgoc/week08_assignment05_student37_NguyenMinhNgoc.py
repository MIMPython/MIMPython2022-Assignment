arr = [0] * 9
used = [False] * 10
cnt = 0
def permutation(pos):
    if pos == 9:
        if arr[0] + arr[1]/arr[2] + arr[3] + arr[4]/arr[5] == arr[6] + arr[7]/arr[8]:
            for i in range(9):
                print(arr[i], end = ' ')
            print()
        return
    for i in range (1, 10):
        if not used[i]:
            arr[pos] = i
            used[i] = True
            permutation(pos + 1)
            used[i] = False
print('A B C D E F G H I')
print('-----------------')
permutation(0)