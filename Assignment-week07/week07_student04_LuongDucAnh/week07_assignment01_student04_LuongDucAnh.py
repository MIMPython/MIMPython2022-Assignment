import math

def getMean(numbers):
    try:
        return sum(numbers)/len(numbers)
    except ZeroDivisionError:
        print ("List is empty")
    except TypeError:
        print ("List must contain only numbers")
        
print (getMean([1, 2.0, 3.0, 4, 5])) #3.0

print (getMean([1, 2, "str", 4, 5])) #List must contain only numbers

print (getMean([])) #List is empty