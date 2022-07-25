#This is the program used to calculate the square of x, which is entered from the user

#Method for calculating the square value
def Square(x): 
    return x*x 


#input 1: 2
#output 1: The square of  2  is  4

#input 2: 3
#output 2: The square of  3  is  9

#input 3: 100
#output 3: The square of 100  is  10000

#Test 
xValue = int(input('Input the value of x: '))
print('The square of ', xValue, ' is ', Square(xValue))

