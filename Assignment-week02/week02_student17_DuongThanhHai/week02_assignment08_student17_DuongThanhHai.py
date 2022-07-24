
def half_prm (n):
    for i in range (1,n+1):
        for j in range (1, i+1):
            print ('* ' , end='')
        print()

half_prm(6)  
print()

def inverted_half_prm (n):
    for i in range (1, n+1):
        for j in range (1, n+2-i):
            print('* ', end = '')
        print()

inverted_half_prm(6)
print()

def full_prm (n):
    for i in range (1, n+1):
        for k in range (1, n+1-i):
            print (" ", end ='')
        for j in range (1, i+1):
            print ('* ', end='')
        print()

full_prm(6)
print()

def inverted_full_prm(n):
    for i in range (1, n+2):
        for j in range (1, i):
            print ( " ", end = '')
        for k in range (1, n-i+2):
            print ( '* ', end = '')
        print ()

inverted_full_prm(6)
    
