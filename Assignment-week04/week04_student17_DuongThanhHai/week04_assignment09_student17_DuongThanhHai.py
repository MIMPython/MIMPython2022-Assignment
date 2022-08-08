
def factorial_number (n):
    result = 1
    for i in range (1, n+1):
        result *= i
    
    count = 0
    while result % 10 == 0:
        count +=1
        result /=10
    
    return count

    

print (factorial_number(10)) #2

