print('*')
print('**')
print('***')
print('****')
print('*****')
print('******')
print('\n')

print('******')
print('*****')
print('****')
print('***')
print('**')
print('*')
print('\n')

print('******')
print('*   *')
print('*  *')
print('* *')
print('**')
print('*')
print('\n')

k = 5
for i in range(0, 6):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i+1):
        print("* ", end="")
    print('\r')
print('\n')

k = 5
for i in range(0, 6):
    for j in range(0, k+1):
        print("* ", end="")
    print('\r')
    k = k - 1
    for j in range(0, i+1):
        print(end=" ")
print('\n')