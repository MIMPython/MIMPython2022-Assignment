#Bài 8

def full_pyramid():
    matrix = [[' ' for x in range(11)] for y in range(6)] 
    left, right = 0, 10
    for i in range(6):
        for i_1 in range(11):
            if(i%2==0):
                for i_2 in range(left,right+1):
                    if(i_2%2==0):
                        matrix[i][i_2] = "*"
            if(i%2!=0):
                for i_2 in range(left,right+1):
                    if(i_2%2!=0):
                        matrix[i][i_2] = "*"
        left += 1
        right -= 1

    #Inverted full paramid
    for i in range(6):
        for j in range(11):
            print(matrix[i][j], end=" ")
        print(end='\n')

    print('=========================')
    #Full paramid
    for i in range(5,-1, -1):
        for j in range(11):
            print(matrix[i][j], end=" ")
        print(end='\n')

def hollow_full_pyramid():
    m = [[' ' for x in range(11)] for y in range(6)] 
    left, right = 0, 10
    for i in range(6):
        if(i==0):
            for j in range(11):
                if(j%2==0):
                    m[i][j] = '*'
        else: 
            for i_1 in range(11):
                m[i][left] = '*'
                m[i][right] = '*'
        left += 1
        right -= 1

    for i in range(6):
        for j in range(11):
            print(m[i][j], end=" ")
        print(end='\n')

def half_pyramid():
    for i in range(7):
        print('*'*i)

def inverted_half_pyramid():
    for i in range(6,0,-1):
        print('*'*i)

def hollow_inverted_half_pyramid():
    x, y = 3, 1
    for i in range(0,6):
        if(i==0):
            print("*"*6)
        elif(i==5):
            print('*')
        else:
            print('*' + ' '*x + '*' +' '*y)
            x -= 1
            y += 1

